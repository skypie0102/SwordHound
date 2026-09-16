"""Reduce the Chapters 14-54 diagnostic queue to likely source-softening mismatches."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'editorial/reprocessing/sanitization-candidates-0014-0054.json'
OUT = ROOT / 'editorial/reprocessing/SANITIZATION-SHORTLIST-0014-0054.md'
OUT_JSON = ROOT / 'editorial/reprocessing/sanitization-shortlist-0014-0054.json'

SENSITIVE = {
    'sexual_direct', 'organs_entrails', 'degradation_slavery',
    'bodily_functions', 'profanity_insult',
}


def main() -> None:
    doc = json.loads(SRC.read_text(encoding='utf-8'))
    rows = [
        r for r in doc['candidates']
        if r['category'] in SENSITIVE
        and not r['expected_stem_seen_near_estimate']
        and not r['prior_review_mentions']
    ]
    # Keep all candidates in JSON. Markdown remains compact by showing at most
    # three per chapter/category; the rest are still available for review.
    OUT_JSON.write_text(json.dumps({
        'notice': 'Shortlist remains diagnostic. These rows have a sensitive Korean keyword, no expected English stem in the rough positional window, and no obvious prior-review mention. They require manual context/alignment judgment.',
        'count': len(rows),
        'by_category': dict(Counter(r['category'] for r in rows)),
        'by_chapter': dict(Counter(str(r['chapter']) for r in rows)),
        'candidates': rows,
    }, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    md = [
        '# Sanitization manual-review shortlist — Chapters 14–54', '',
        '**Diagnostic only. Nothing in this file is automatically a finding.**', '',
        f'Candidates requiring manual context judgment: **{len(rows)}**', '',
        'Category counts: ' + ', '.join(f'`{k}`={v}' for k, v in sorted(Counter(r['category'] for r in rows).items())), '',
    ]
    seen = Counter()
    for r in rows:
        key = (r['chapter'], r['category'])
        if seen[key] >= 3:
            continue
        seen[key] += 1
        md += [
            f"## Chapter {r['chapter']} — {r['category']} — Korean line {r['korean_line']}", '',
            '**Korean context**', '',
        ]
        for x in r['korean_context']:
            marker = '→' if x['index'] == r['korean_line'] else ' '
            md.append(f"- {marker} L{x['index']}: {x['text']}")
        md += ['', f"**Rough English position:** paragraph {r['estimated_english_paragraph']}", '']
        for x in r['english_context']:
            md.append(f"- P{x['index']}: {x['text']}")
        md += ['', '---', '']
    OUT.write_text('\n'.join(md).rstrip() + '\n', encoding='utf-8')
    print(json.dumps({'shortlist': len(rows), 'by_category': dict(Counter(r['category'] for r in rows))}))


if __name__ == '__main__':
    main()
