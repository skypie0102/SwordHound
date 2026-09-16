"""Rebuild source/audit indexes without applying editorial suggestions."""
from collections import Counter, defaultdict
from pathlib import Path
import csv
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from build_editorial_draft import render as validate_editorial_chapter
from import_korean_raws import check_korean_raws
from korean_mtl_witness_map import mtl_gaps, verify_mapping_files, witnesses_for_mtl

ROOT = Path(__file__).resolve().parents[1]
NS = {'h': 'http://www.w3.org/1999/xhtml'}


def normalize(text):
    return ' '.join(text.split())


def save(path, data):
    target = ROOT / path
    rendered = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
    if '--check' in sys.argv:
        if not target.exists() or target.read_text(encoding='utf-8') != rendered:
            raise ValueError(f'Stale generated index: {path}')
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(rendered, encoding='utf-8')


def main():
    with (ROOT / 'source/chapter-sha256.tsv').open(encoding='utf-8') as f:
        source_rows = list(csv.DictReader(f, delimiter='\t'))
    chapter_data = {}
    titles = defaultdict(list)
    for row in source_rows:
        number = int(row['chapter'])
        path = ROOT / 'source/chapters' / row['repo_file']
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != row['sha256']:
            raise ValueError(f'Source checksum mismatch: {number}')
        doc = ET.fromstring(data)
        title = ''.join(doc.find('.//h:h1', NS).itertext())
        body = doc.find('.//h:div[@class="chapter-content"]', NS)
        paragraphs = [''.join(p.itertext()) for p in body.findall('.//h:p', NS)]
        chapter_data[number] = {'title': title, 'paragraphs': paragraphs, 'source': path.relative_to(ROOT).as_posix(), 'sha256': row['sha256']}
        titles[normalize(title).casefold()].append(number)

    audit = (ROOT / 'editorial/Editorial-Audit.md').read_text(encoding='utf-8')
    findings = []
    historical_title = None
    for block in re.split(r'(?=^### Chapter |^#### ED-)', audit, flags=re.M):
        title_match = re.match(r'### Chapter (\d+): (.+)', block)
        if title_match:
            historical_title = title_match.group(2)
        head = re.match(r'#### (ED-\d+) — (.+)', block)
        if not head:
            continue
        loc = re.search(r'^- \*\*Location:\*\* Chapter (\d+), paragraph (\d+)', block, re.M)
        quoted = re.search(r'^- \*\*Current text:\*\* “(.*)”\s*$', block, re.M)
        if not loc or not quoted:
            raise ValueError(f'Unrecognized audit structure: {head.group(1)}')
        old_chapter, old_paragraph = map(int, loc.groups())
        text = normalize(quoted.group(1))
        candidates = titles.get(normalize(historical_title).casefold(), [])
        hits = [(n, i+1) for n in candidates for i, p in enumerate(chapter_data[n]['paragraphs']) if normalize(p) == text]
        status = 'unmatched'
        match = None
        if len(hits) == 1:
            match = {'chapter': hits[0][0], 'paragraph': hits[0][1]}
            status = 'exact_text_and_title'
        elif len(hits) > 1:
            status = 'ambiguous_text'
        findings.append({
            'id': head.group(1), 'historical_chapter': old_chapter, 'historical_paragraph': old_paragraph,
            'historical_title': historical_title, 'category_and_severity': head.group(2),
            'match_status': status, 'source_match': match,
            'candidate_matches': [{'chapter': n, 'paragraph': p} for n, p in hits],
            'disposition': 'not_reviewed',
        })
    if len(findings) != 2151:
        raise ValueError(f'Expected 2151 original findings, got {len(findings)}')
    aligned = defaultdict(list)
    for item in findings:
        if item['source_match']:
            aligned[item['source_match']['chapter']].append(item['id'])
    overlay_path = ROOT / 'editorial/reconstruction-status.json'
    overlay = json.loads(overlay_path.read_text(encoding='utf-8')) if overlay_path.exists() else {}

    supplemental_manifest = check_korean_raws(ROOT)
    original_manifest = json.loads((ROOT / 'recovery/korean-raws-manifest.json').read_text(encoding='utf-8'))
    path_meta = {
        item['path']: item
        for item in original_manifest['members'] + supplemental_manifest['members']
    }
    verify_mapping_files(ROOT, 125)
    if mtl_gaps(125) != [55, 125]:
        raise ValueError(f'Unexpected edition-aligned MTL Korean gaps: {mtl_gaps(125)}')

    chapters = []
    for number, item in sorted(chapter_data.items()):
        state = overlay.get(str(number), {})
        if state.get('status') == 'qa_accepted':
            validate_editorial_chapter(number)
        row = {
            'chapter': number,
            'title': item['title'],
            'source': item['source'],
            'source_sha256': item['sha256'],
            'source_integrity': 'verified',
            'source_paragraphs': len(item['paragraphs']),
            'original_edited_file': 'not_recovered',
            'original_qa_file': 'not_recovered',
            'historical_reported_state': 'merged_through_372' if number <= 372 else ('validated_unmerged_373_374' if number <= 374 else 'not_reported_complete'),
            'reconstruction_status': state.get('status', 'not_started'),
            'draft': state.get('draft'),
            'qa_report': state.get('qa_report'),
            'open_issues': state.get('open_issues', []),
            'audit_findings_with_exact_unique_match': aligned[number],
        }
        mapped = witnesses_for_mtl(number) if number <= 125 else []
        witnesses = []
        for mapping in mapped:
            meta = path_meta[mapping['path']]
            witnesses.append({
                **mapping,
                'sha256': meta['sha256'],
                'alignment': meta['alignment'],
            })
        row.update({
            'review_basis': 'korean_plus_mtl' if witnesses else 'mtl_with_supporting_references',
            'korean_source': {
                'path': witnesses[0]['path'],
                'sha256': witnesses[0]['sha256'],
                'alignment': witnesses[0]['alignment'],
            } if len(witnesses) == 1 else None,
            'korean_witnesses': witnesses,
            'source_policy': 'editorial/SOURCES.md',
            'editorial_accepted': state.get('status') == 'qa_accepted',
            'acceptance_evidence': state.get('acceptance_evidence'),
        })
        chapters.append(row)

    save('editorial/audit-alignment.json', {
        'notice': 'Exact quoted text plus chapter title matching after whitespace normalization only. A match locates an old suggestion; it does not approve or apply it. Unmatched findings may involve changed text, numbering, or titles. Duplicate suggestions remain separate.',
        'counts': dict(Counter(x['match_status'] for x in findings)),
        'findings': findings,
    })
    save('editorial/chapter-tracker.json', {
        'notice': 'Reconstructed tracker. Historical completion reports and current QA acceptance are separate. Only original source integrity is verified for every chapter. Korean witness mapping through MTL 125 is edition-aware and may be composite or bundled.',
        'chapter_count': len(chapters),
        'chapters': chapters,
    })
    print(json.dumps({
        'chapters': len(chapters),
        'audit_findings': len(findings),
        'alignment_counts': dict(Counter(x['match_status'] for x in findings)),
        'supplemental_korean_files': supplemental_manifest['file_count'],
        'mtl_korean_gaps_1_125': [55, 125],
    }))


if __name__ == '__main__':
    main()
