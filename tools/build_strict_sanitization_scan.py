"""Build a compact strict sanitation review queue for canonical Chapters 14-54.

Unlike the broad diagnostic, this only targets Korean wording whose removal would
materially soften sexual/reproductive content, nudity, bodily functions, torture,
degradation, or disability. It remains diagnostic: every row needs editorial judgment.
"""
from __future__ import annotations

from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'editorial' / 'reprocessing' / 'STRICT-SANITIZATION-SCAN-0014-0054.md'

RULES = [
    ('sexual_reproductive', re.compile(r'강간|겁탈|성폭행|성관계|교미|짝짓기|욕정|음욕|정액|성기|처녀막|번식|임신|아이를\s*낳|미인계|글래머러스한\s*몸매|음탕한|침대에서\s*시중'),
     ('rape','sexual','sex','intercourse','mate','breeding','breed','pregnan','child','seduc','volupt','glamorous','lewd','bed')),
    ('nudity_exposure', re.compile(r'알몸|나체|발가벗|벌거벗|옷을\s*벗|다리를\s*벌|치마.*(?:올리|들어)|노출'),
     ('naked','nude','bare','strip','undress','expos','legs spread','skirt')),
    ('bodily_functions', re.compile(r'오줌|소변|똥|대변|배설|설사|구토|토사물|토해|토했'),
     ('piss','pee','urine','shit','fec','stool','excret','diarr','vomit','throw up')),
    ('torture_abuse', re.compile(r'고문|학대'), ('tortur','abuse')),
    ('degradation_disability', re.compile(r'창녀|매춘|성노예|불구|장애인|벌레\s*취급|짐승\s*취급'),
     ('prostitut','whore','sex slave','cripple','disabled','vermin','beast')),
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

def branch_for(ch):
    return next(branch for lo, hi, branch in BRANCHES if lo <= ch <= hi)

def korean(ch):
    p = ROOT / f'source/korean/chapters/{ch:03d}.txt'
    lines=[x.strip() for x in p.read_text(encoding='utf-8-sig').splitlines() if x.strip()]
    while lines and (re.match(r'^#?\d+', lines[0]) or re.match(r'^제\s*\d+\s*(?:장|화)', lines[0])):
        lines.pop(0)
    return lines

def staged(ch):
    path=f'editorial/staging/chapter-{ch:04d}-final-text.txt'
    r=subprocess.run(['git','show',f'origin/{branch_for(ch)}:{path}'],cwd=ROOT,text=True,capture_output=True)
    return r.stdout.splitlines() if r.returncode == 0 else []

def main():
    rows=[]
    for ch in range(14,55):
        ko, en = korean(ch), staged(ch)
        if not en: continue
        for i,line in enumerate(ko):
            for cat,pat,expected in RULES:
                if not pat.search(line): continue
                est=0 if len(ko)<=1 else round(i*(len(en)-1)/(len(ko)-1))
                lo=max(0,est-4); hi=min(len(en),est+5)
                ctx=' '.join(en[lo:hi]).casefold()
                seen=any(x in ctx for x in expected)
                rows.append((ch,i+1,cat,not seen,line,est+1,en[lo:hi],expected))
    rows.sort(key=lambda x:(x[0],x[1],x[2]))
    md=['# Strict sanitation scan — canonical Chapters 14–54','',
        '**Diagnostic only.** Exact source-sensitive terms only; editorial judgment is still required.','',
        f'Rows: **{len(rows)}**; rows without an expected direct English term nearby: **{sum(r[3] for r in rows)}**.','']
    for ch,ln,cat,review,src,slot,ctx,expected in rows:
        md += [f'## Ch {ch} L{ln} — {cat} — {"REVIEW" if review else "DIRECT TERM PRESENT"}', '',
               f'Korean: {src}', f'Expected: `{", ".join(expected)}`', f'Estimated staging slot: {slot}',
               'Staging context:']
        md.extend(f'- {x}' for x in ctx)
        md += ['','---','']
    OUT.write_text('\n'.join(md)+'\n',encoding='utf-8')
    print({'rows':len(rows),'review':sum(r[3] for r in rows)})
if __name__=='__main__': main()
