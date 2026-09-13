"""Render an explicit paragraph edit set and its provenance; originals stay untouched."""
from pathlib import Path
import argparse
import hashlib
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = {'h': 'http://www.w3.org/1999/xhtml'}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canonical_sha(value):
    return sha(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode())


def evidence_sha(path):
    return sha(path.read_bytes() if path.suffix == '.png' else path.read_text(encoding='utf-8').encode())


def acceptance_context(chapter, spec, qa, text, alignment):
    evidence = sorted({p for issue in qa['issues'] for p in issue.get('evidence', [])} | set(qa.get('final_review_evidence', [])))
    return {'chapter': chapter, 'scope': 'editorial_only', 'review_basis': qa['review_basis'],
            'draft_sha256': sha(text.encode()), 'mtl_sha256': spec['source_sha256'],
            'korean_sha256': alignment['korean_sha256'] if alignment else None,
            'edit_set_sha256': canonical_sha(spec), 'decisions_sha256': canonical_sha(qa['issues']),
            'alignment_sha256': canonical_sha(alignment),
            'evidence_sha256': {p: evidence_sha(ROOT / p) for p in evidence}}


def render(chapter, *, validate_acceptance=True):
    spec = json.loads((ROOT / f'editorial/edits/chapter-{chapter:04d}.json').read_text(encoding='utf-8'))
    source = (ROOT / spec['source']).read_bytes()
    if spec['chapter'] != chapter or sha(source) != spec['source_sha256']:
        raise ValueError('Edit set does not match the original source')
    doc = ET.fromstring(source)
    title = ''.join(doc.find('.//h:h1', NS).itertext())
    body = doc.find('.//h:div[@class="chapter-content"]', NS)
    paragraphs = [''.join(p.itertext()) for p in body.findall('.//h:p', NS)]
    if len(paragraphs) != spec['expected_paragraphs']:
        raise ValueError('Source paragraph count changed')
    alignment = None
    korean_by_paragraph = {}
    if spec.get('korean_alignment'):
        alignment = json.loads((ROOT / spec['korean_alignment']).read_text(encoding='utf-8'))
        korean = (ROOT / alignment['korean_source']).read_bytes()
        lines = korean.decode('utf-8-sig').splitlines()
        if alignment['chapter'] != chapter or alignment['mtl_source'] != spec['source'] or alignment['mtl_sha256'] != sha(source) or alignment['korean_sha256'] != sha(korean):
            raise ValueError('Korean alignment source mismatch')
        if len(lines) != alignment['line_count']:
            raise ValueError('Korean line count mismatch')
        if [p['mtl_paragraph'] for p in alignment['paragraphs']] != list(range(1, len(paragraphs)+1)):
            raise ValueError('Korean alignment omits or duplicates an MTL paragraph')
        accounted = [entry['line'] for entry in alignment['non_body_lines']]
        for entry in alignment['paragraphs']:
            numbers = entry['korean_lines']
            if not numbers or any(not 1 <= n <= len(lines) for n in numbers):
                raise ValueError('Invalid Korean line reference')
            if entry['line_text_sha256'] != [sha(lines[n-1].encode()) for n in numbers]:
                raise ValueError('Korean quoted-line hash mismatch')
            accounted.extend(numbers)
            korean_by_paragraph[entry['mtl_paragraph']] = numbers
        if sorted(accounted) != list(range(1, len(lines)+1)):
            raise ValueError('Korean coverage omits or duplicates a line')
    scene_breaks = spec.get('scene_breaks_after', [])
    if len(set(scene_breaks)) != len(scene_breaks) or any(not 1 <= n < len(paragraphs) for n in scene_breaks):
        raise ValueError('Invalid scene-break placement')
    edits = {}
    for number, replacement, reason in spec['edits']:
        if number in edits or not 1 <= number <= len(paragraphs):
            raise ValueError(f'Duplicate or invalid paragraph: {number}')
        if not replacement.strip() or '\n' in replacement or not reason.strip():
            raise ValueError(f'Invalid replacement or missing rationale: {number}')
        if replacement == paragraphs[number - 1]:
            raise ValueError(f'Edit changes nothing: {number}')
        edits[number] = (replacement, reason)
    qa = json.loads((ROOT / f'qa/chapter-{chapter:04d}.json').read_text(encoding='utf-8'))
    if qa['chapter'] != chapter or qa['source_sha256'] != spec['source_sha256']:
        raise ValueError('QA report source mismatch')
    issues = qa['issues']
    if len({issue['id'] for issue in issues}) != len(issues):
        raise ValueError('Duplicate QA issue identifier')
    for issue in issues:
        if issue['status'] not in ('open', 'resolved') or not issue['paragraphs']:
            raise ValueError('Invalid issue state or missing location')
        if any(not 1 <= n <= len(paragraphs) for n in issue['paragraphs']):
            raise ValueError('QA issue points outside source')
        if issue['status'] == 'resolved':
            if not issue.get('resolution') or not issue.get('evidence'):
                raise ValueError('Resolved QA issue requires a decision and evidence')
            for evidence in issue['evidence']:
                if not (ROOT / evidence).is_file():
                    raise ValueError(f'Missing QA resolution evidence: {evidence}')
    if qa['accepted'] and (any(i['status'] == 'open' for i in issues) or not qa.get('acceptance_evidence')):
        raise ValueError('QA acceptance requires closed issues and acceptance evidence')
    state = json.loads((ROOT / 'editorial/reconstruction-status.json').read_text(encoding='utf-8'))[str(chapter)]
    if state['open_issues'] != [i['id'] for i in issues if i['status'] == 'open']:
        raise ValueError('Tracker overlay disagrees with QA issues')
    if not qa['accepted'] and state['status'] == 'qa_accepted':
        raise ValueError('Tracker incorrectly claims QA acceptance')
    if qa['accepted'] and state['status'] != 'qa_accepted':
        raise ValueError('Tracker does not reflect QA acceptance')
    draft_path = f'manuscript/drafts/chapter-{chapter:04d}.md'
    qa_path = f'qa/chapter-{chapter:04d}.md'
    if state['draft'] != draft_path or state['qa_report'] != qa_path:
        raise ValueError('Tracker links disagree with generated chapter paths')
    rows, draft = [], []
    for number, original in enumerate(paragraphs, 1):
        replacement, reason = edits.get(number, (original, None))
        draft.append(f'<!-- source-p:{number:03d} -->\n{replacement}')
        if number in scene_breaks:
            draft.append('◆◆◆')
        rows.append({'paragraph': number, 'source_text_sha256': sha(original.encode()),
                     'draft_text_sha256': sha(replacement.encode()), 'source_text': original,
                     'draft_text': replacement, 'changed': original != replacement, 'rationale': reason,
                     'open_issues': [i['id'] for i in issues if i['status'] == 'open' and number in i['paragraphs']]})
        if alignment:
            rows[-1]['korean_lines'] = korean_by_paragraph[number]
    status = 'Editorially accepted reconstruction — EPUB release pending.' if qa['accepted'] else 'Reconstruction draft — QA not accepted.'
    text = f'# Chapter {chapter}: {title}\n\n> {status} See [review](../../{qa_path}). Paragraph markers refer to the unchanged source.\n\n' + '\n\n'.join(draft) + '\n'
    if qa['accepted'] and validate_acceptance:
        if qa['review_basis'] not in ('korean_plus_mtl', 'mtl_with_supporting_references'):
            raise ValueError('Invalid accepted review basis')
        if (qa['review_basis'] == 'korean_plus_mtl') != bool(alignment):
            raise ValueError('Accepted review basis disagrees with available alignment')
        record = json.loads((ROOT / qa['acceptance_evidence']).read_text(encoding='utf-8'))
        expected = acceptance_context(chapter, spec, qa, text, alignment)
        if any(record.get(key) != value for key, value in expected.items()):
            raise ValueError('Acceptance evidence is stale or does not match the final chapter')
        if not record.get('reviewer') or not record.get('review_date') or not qa.get('final_review_evidence'):
            raise ValueError('Acceptance lacks final review evidence')
    provenance = {'chapter': chapter, 'source': spec['source'], 'source_sha256': sha(source),
                  'draft': draft_path, 'draft_sha256': sha(text.encode()), 'paragraph_count': len(rows),
                  'changed_paragraphs': len(edits), 'paragraphs': rows}
    provenance['scene_breaks_after'] = scene_breaks
    provenance['editorial_accepted'] = qa['accepted']
    provenance['acceptance_evidence'] = qa.get('acceptance_evidence')
    if alignment:
        provenance.update(korean_source=alignment['korean_source'], korean_sha256=alignment['korean_sha256'], korean_alignment=spec['korean_alignment'])
    return {draft_path: text, f'editorial/provenance/chapter-{chapter:04d}.json': json.dumps(provenance, ensure_ascii=False, indent=2) + '\n'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('chapter', type=int)
    parser.add_argument('--check', action='store_true', help='Fail if generated files are stale; write nothing')
    args = parser.parse_args()
    outputs = render(args.chapter)
    for name, text in outputs.items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_bytes() != text.encode('utf-8'):
                raise ValueError(f'Missing or stale draft output: {name}')
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(text.encode('utf-8'))
    print(f'Chapter {args.chapter}: {"verified" if args.check else "generated"} draft and paragraph provenance; editorial acceptance is separate.')


if __name__ == '__main__':
    main()
