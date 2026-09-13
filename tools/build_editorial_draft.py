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


def render(chapter):
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
    if qa['accepted'] and (any(i['status'] == 'open' for i in issues) or not qa.get('acceptance_evidence')):
        raise ValueError('QA acceptance requires closed issues and acceptance evidence')
    state = json.loads((ROOT / 'editorial/reconstruction-status.json').read_text(encoding='utf-8'))[str(chapter)]
    if state['open_issues'] != [i['id'] for i in issues if i['status'] == 'open']:
        raise ValueError('Tracker overlay disagrees with QA issues')
    if not qa['accepted'] and state['status'] == 'qa_accepted':
        raise ValueError('Tracker incorrectly claims QA acceptance')
    draft_path = f'manuscript/drafts/chapter-{chapter:04d}.md'
    qa_path = f'qa/chapter-{chapter:04d}.md'
    if state['draft'] != draft_path or state['qa_report'] != qa_path:
        raise ValueError('Tracker links disagree with generated chapter paths')
    rows, draft = [], []
    for number, original in enumerate(paragraphs, 1):
        replacement, reason = edits.get(number, (original, None))
        draft.append(f'<!-- source-p:{number:03d} -->\n{replacement}')
        rows.append({'paragraph': number, 'source_text_sha256': sha(original.encode()),
                     'draft_text_sha256': sha(replacement.encode()), 'source_text': original,
                     'draft_text': replacement, 'changed': original != replacement, 'rationale': reason,
                     'open_issues': [i['id'] for i in issues if i['status'] == 'open' and number in i['paragraphs']]})
    text = f'# Chapter {chapter}: {title}\n\n> Reconstruction draft — QA not accepted. See [review](../../{qa_path}). Paragraph markers refer to the unchanged source.\n\n' + '\n\n'.join(draft) + '\n'
    provenance = {'chapter': chapter, 'source': spec['source'], 'source_sha256': sha(source),
                  'draft': draft_path, 'draft_sha256': sha(text.encode()), 'paragraph_count': len(rows),
                  'changed_paragraphs': len(edits), 'paragraphs': rows}
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
