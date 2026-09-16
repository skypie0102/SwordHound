"""Build a review queue for possible source softening in MTL Chapters 14-54.

This is diagnostic only. Keyword hits are not editorial findings. The report deliberately
includes nearby Korean and English context so a reviewer can decide whether source force,
anatomy, degradation, sexual wording, bodily detail, or violence was softened/omitted.
"""
from __future__ import annotations

from pathlib import Path
import html
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / 'editorial' / 'reprocessing'
NS = {'h': 'http://www.w3.org/1999/xhtml'}

RULES = [
    ('gore_blood', re.compile(r'피투성이|피범벅|출혈|선혈|혈액|피를|피가|피로|핏빛'), ('blood', 'bleed')),
    ('organs_entrails', re.compile(r'내장|장기|창자|내부 장기|장기액|내장액'), ('organ', 'entrail', 'intestin', 'gut')),
    ('corpse_death', re.compile(r'시체|사체|주검|죽음|죽었다|죽였다|살해|목숨'), ('corpse', 'dead', 'death', 'kill', 'life')),
    ('mutilation', re.compile(r'절단|잘라|베어|찢어|찢겨|뜯어|꿰뚫|관통|짓이기|으깨|터뜨|파열'), ('sever', 'cut', 'slice', 'tear', 'rip', 'pierc', 'crush', 'burst')),
    ('bones_brain_eyes', re.compile(r'뼈|골수|두개골|뇌|안구|눈알|눈구멍'), ('bone', 'marrow', 'skull', 'brain', 'eye')),
    ('pain_torture', re.compile(r'고문|학대|고통|비명|신음|절규'), ('tortur', 'abuse', 'pain', 'scream', 'groan', 'shriek')),
    ('sexual_direct', re.compile(r'강간|겁탈|성폭행|성관계|교미|짝짓기|욕정|음욕|정액|성기|처녀막'), ('rape', 'sex', 'mate', 'mating', 'lust', 'semen', 'genital', 'hymen')),
    ('nudity_body', re.compile(r'알몸|나체|벗은|유방|가슴|사타구니'), ('naked', 'nude', 'breast', 'chest', 'groin')),
    ('degradation_slavery', re.compile(r'창녀|매춘|노예|성노예|불구|장애인|벌레 취급|짐승 취급'), ('prostitut', 'whore', 'slave', 'disabled', 'cripple', 'vermin', 'beast')),
    ('bodily_functions', re.compile(r'오줌|소변|똥|대변|배설|설사|구토|토사물|침|타액|점액|방광'), ('piss', 'urine', 'shit', 'fec', 'stool', 'excret', 'diarr', 'vomit', 'saliva', 'mucus', 'bladder')),
    ('profanity_insult', re.compile(r'개새끼|씨발|병신|좆|썅|빌어먹을'), ('bastard', 'fuck', 'shit', 'damn', 'asshole', 'dick')),
]


def clean_text(text: str) -> str:
    return ' '.join(html.unescape(text).split())


def mtl_paragraphs(chapter: int) -> list[str]:
    path = ROOT / f'source/chapters/chapter-{chapter:03d}.xhtml'
    root = ET.fromstring(path.read_bytes())
    body = root.find('.//h:div[@class="chapter-content"]', NS)
    return [clean_text(''.join(p.itertext())) for p in body.findall('.//h:p', NS)]


def korean_lines(chapter: int) -> list[str]:
    path = ROOT / f'source/korean/chapters/{chapter:03d}.txt'
    lines = [line.strip() for line in path.read_text(encoding='utf-8-sig').splitlines() if line.strip()]
    while lines and (re.match(r'^#?\d+', lines[0]) or re.match(r'^제\s*\d+\s*(?:장|화)', lines[0])):
        lines.pop(0)
    return lines


def prior_review(chapter: int) -> str:
    path = OUT_DIR / 'prior-reviews' / f'chapter-{chapter:04d}.md'
    return path.read_text(encoding='utf-8') if path.is_file() else ''


def around(items: list[str], center: int, radius: int) -> list[dict]:
    start = max(0, center - radius)
    end = min(len(items), center + radius + 1)
    return [{'index': i + 1, 'text': items[i]} for i in range(start, end)]


def candidate_rows(chapter: int) -> list[dict]:
    ko = korean_lines(chapter)
    en = mtl_paragraphs(chapter)
    review = prior_review(chapter)
    rows = []
    for i, line in enumerate(ko):
        for category, pattern, expected in RULES:
            if not pattern.search(line):
                continue
            if len(ko) <= 1:
                estimated = 0
            else:
                estimated = round(i * (len(en) - 1) / (len(ko) - 1))
            en_window = around(en, estimated, 3)
            joined = ' '.join(x['text'].casefold() for x in en_window)
            expected_present = any(term.casefold() in joined for term in expected)
            review_lower = review.casefold()
            review_mentions = [
                term for term in expected
                if term.casefold() in review_lower
            ]
            # Rank likely omissions/softenings ahead of straightforward matches.
            score = 2 if not expected_present else 0
            if category in {'sexual_direct', 'organs_entrails', 'degradation_slavery', 'bodily_functions', 'profanity_insult'}:
                score += 2
            elif category in {'gore_blood', 'mutilation', 'bones_brain_eyes', 'pain_torture'}:
                score += 1
            rows.append({
                'chapter': chapter,
                'category': category,
                'score': score,
                'korean_line': i + 1,
                'korean_context': around(ko, i, 1),
                'estimated_english_paragraph': estimated + 1,
                'english_context': en_window,
                'expected_english_stems': list(expected),
                'expected_stem_seen_near_estimate': expected_present,
                'prior_review_mentions': review_mentions,
                'diagnostic_only': True,
            })
    # Exact duplicate hits from overlapping Korean terms are intentionally collapsed.
    unique = {}
    for row in rows:
        key = (row['chapter'], row['category'], row['korean_line'])
        unique[key] = row
    return sorted(unique.values(), key=lambda r: (-r['score'], r['korean_line'], r['category']))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    all_rows = []
    chapter_summary = []
    for chapter in range(14, 55):
        rows = candidate_rows(chapter)
        all_rows.extend(rows)
        chapter_summary.append({
            'chapter': chapter,
            'candidate_count': len(rows),
            'high_priority_count': sum(r['score'] >= 3 for r in rows),
            'prior_review_present': bool(prior_review(chapter)),
        })
    doc = {
        'range': [14, 54],
        'notice': 'Diagnostic candidate queue only. A keyword hit or missing English stem is not a finding. Every candidate requires source-context editorial judgment before any correction is recorded.',
        'candidate_count': len(all_rows),
        'high_priority_count': sum(r['score'] >= 3 for r in all_rows),
        'chapters': chapter_summary,
        'candidates': all_rows,
    }
    (OUT_DIR / 'sanitization-candidates-0014-0054.json').write_text(
        json.dumps(doc, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    md = [
        '# Sanitization candidate queue — Chapters 14–54', '',
        'This is a **diagnostic queue, not a findings report**. Korean keyword hits and rough positional alignment only prioritize human/model review.', '',
        f"Candidates: **{doc['candidate_count']}**; high-priority diagnostics: **{doc['high_priority_count']}**", '',
        '| Ch. | Candidates | High priority | Prior production review |',
        '|---:|---:|---:|:---:|',
    ]
    for row in chapter_summary:
        md.append(f"| {row['chapter']} | {row['candidate_count']} | {row['high_priority_count']} | {'yes' if row['prior_review_present'] else 'no'} |")
    (OUT_DIR / 'SANITIZATION-CANDIDATES-0014-0054.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print(json.dumps({'candidates': doc['candidate_count'], 'high_priority': doc['high_priority_count']}))


if __name__ == '__main__':
    main()
