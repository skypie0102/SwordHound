"""Build a diagnostic sanitation scan against staged reconstructed text for canonical Chapters 14-54."""
from __future__ import annotations

from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'editorial' / 'reprocessing' / 'STAGED-SANITIZATION-SCAN-0014-0054.md'

RULES = [
    ('organs_entrails', re.compile(r'내장|장기|창자|내부 장기|장기액|내장액'), ('organ', 'entrail', 'intestin', 'gut')),
    ('pain_torture', re.compile(r'고문|학대|고통|비명|신음|절규'), ('tortur', 'abuse', 'pain', 'scream', 'groan', 'shriek')),
    ('sexual_direct', re.compile(r'강간|겁탈|성폭행|성관계|교미|짝짓기|욕정|음욕|정액|성기|처녀막|번식 도구|번식도구'), ('rape', 'sex', 'mate', 'mating', 'lust', 'semen', 'genital', 'hymen', 'breed', 'breeding')),
    ('nudity_body', re.compile(r'알몸|나체|벗은|유방|가슴|사타구니|다리를 벌|치마를.*올'), ('naked', 'nude', 'breast', 'chest', 'groin', 'legs', 'skirt')),
    ('degradation_slavery', re.compile(r'창녀|매춘|노예|성노예|불구|장애인|벌레 취급|짐승 취급'), ('prostitut', 'whore', 'slave', 'disabled', 'cripple', 'vermin', 'beast')),
    ('bodily_functions', re.compile(r'오줌|소변|똥|대변|배설|설사|구토|토사물|침|타액|점액|방광'), ('piss', 'pee', 'urine', 'shit', 'fec', 'stool', 'excret', 'diarr', 'vomit', 'saliva', 'mucus', 'bladder')),
    ('profanity_insult', re.compile(r'개새끼|씨발|병신|좆|썅|빌어먹을'), ('bastard', 'fuck', 'shit', 'damn', 'asshole', 'dick')),
]

BRANCHES = [
    (14,17,'production/batch-solitary-0014-0017'),
    (18,19,'production/batch-bared-teeth-0018-0019'),
    (20,25,'production/batch-camus-morgue-0020-0025'),
    (26,27,'production/batch-the-graduate-0026-0027'),
    (28,31,'production/batch-special-laws-of-vikir-0028-0031'),
    (32,34,'production/batch-the-social-club-0032-0034'),
    (35,37,'production/batch-slave-auction-0035-0037'),
    (38,39,'production/batch-sponsored-0038-0039'),
    (40,42,'production/batch-morgues-united-front-0040-0042'),
    (43,45,'production/batch-the-fiancee-0043-0045'),
    (46,51,'production/batch-the-husband-hunt-0046-0051'),
    (52,54,'production/batch-slaves-of-the-barbarian-tribe-0052-0054'),
]

def branch_for(ch: int) -> str:
    for lo, hi, branch in BRANCHES:
        if lo <= ch <= hi:
            return branch
    raise ValueError(ch)

def korean_lines(ch: int) -> list[str]:
    lines = [x.strip() for x in (ROOT / f'source/korean/chapters/{ch:03d}.txt').read_text(encoding='utf-8-sig').splitlines() if x.strip()]
    while lines and (re.match(r'^#?\d+', lines[0]) or re.match(r'^제\s*\d+\s*(?:장|화)', lines[0])):
        lines.pop(0)
    return lines

def staging_lines(ch: int) -> list[str]:
    branch = branch_for(ch)
    path = f'editorial/staging/chapter-{ch:04d}-final-text.txt'
    result = subprocess.run(['git','show',f'origin/{branch}:{path}'], cwd=ROOT, text=True, capture_output=True)
    if result.returncode:
        return []
    return result.stdout.splitlines()

def context(lines: list[str], center: int, radius: int = 2) -> list[tuple[int,str]]:
    return [(i + 1, lines[i]) for i in range(max(0, center-radius), min(len(lines), center+radius+1))]

def main() -> None:
    rows = []
    for ch in range(14, 55):
        ko = korean_lines(ch)
        st = staging_lines(ch)
        if not st:
            continue
        for i, line in enumerate(ko):
            for category, pattern, expected in RULES:
                if not pattern.search(line):
                    continue
                est = 0 if len(ko) <= 1 else round(i * (len(st)-1)/(len(ko)-1))
                stage_ctx = context(st, est, 4)
                joined = ' '.join(x.casefold() for _, x in stage_ctx)
                seen = any(term in joined for term in expected)
                rows.append((not seen, ch, category, i, line, est, ko, st, expected))
    rows.sort(key=lambda r: (not r[0], r[1], r[3], r[2]))
    md = ['# Staging-aware sanitation scan — canonical Chapters 14–54','',
          '**Diagnostic only.** This compares Korean sensitive-language hits against the actual staged reconstruction on the relevant production branch. Missing English stems are review priorities, not automatic findings.','',
          f'Total sensitive hits: **{len(rows)}**; missing expected English stems near estimated slot: **{sum(r[0] for r in rows)}**.','']
    for missing, ch, category, i, line, est, ko, st, expected in rows:
        md += [f'## Chapter {ch} — {category} — Korean line {i+1} — {"REVIEW" if missing else "stem nearby"}','',
               f'Expected English stems: `{", ".join(expected)}`','', '**Korean context**','']
        for n, text in context(ko, i, 1):
            md.append(f'- {"→" if n == i+1 else " "} L{n}: {text}')
        md += ['', f'**Staged context near slot {est+1}**','']
        for n, text in context(st, est, 4):
            md.append(f'- {"→" if n == est+1 else " "} S{n}: {text}')
        md += ['','---','']
    OUT.write_text('\n'.join(md) + '\n', encoding='utf-8')
    print({'hits': len(rows), 'review': sum(r[0] for r in rows)})

if __name__ == '__main__':
    main()
