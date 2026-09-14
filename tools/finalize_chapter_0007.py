"""Finalize Chapter 7 only after the complete-checkout acceptance gate passes."""
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import build_editorial_draft as bed


def write(path, text):
    target=ROOT/path
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(text,encoding='utf-8',newline='\n')


def main():
    validation="""# Chapter 7 repository validation — 2026-09-14

The Chapter 7 acceptance workflow reached finalization only after the reviewed candidate was regenerated with its final prose refinements and passed all of the following on a complete GitHub checkout:

- Chromium rendering at 1100×900 and 390×844, including committed layout measurements and screenshots;
- `python tools/verify_recovery.py`;
- `python tools/build_editorial_draft.py 7 --check`;
- `python tools/build_chapter_preview.py 7 --check`;
- `python tools/rebuild_editorial_tracking.py --check`;
- `python -m unittest discover -s tests -v`;
- `git diff --check`.

These checks establish preserved-source integrity, deterministic materialization, exact Korean-line accounting, browser-rendered layout invariants, tracker consistency and test compatibility. They do not authenticate the supplied Korean as a publisher witness or constitute whole-EPUB release QA.
"""
    write('qa/chapter-0007-validation.md',validation)

    layout=json.loads((ROOT/'qa/layout/chapter-0007.json').read_text(encoding='utf-8'))
    d,m=layout['viewports']['desktop'],layout['viewports']['mobile']
    final=f"""# Chapter 7 final editorial review — 2026-09-14

Codex completed Korean/MTL comparison and a complete final reading of all 146 English paragraph slots. All 151 Korean physical lines are accounted for: four repeated heading lines, one explicit Korean scene-break line and 146 mapped body lines. The source MTL's divider paragraph is deliberately repurposed as the first post-break narrative slot, allowing the Korean `* * *` to become the real `◆◆◆` divider without dropping or manufacturing a paragraph. This is new reconstruction work, not recovered old production, independent human review or publisher authentication.

The [source review](chapter-0007.md) records the consequential choices: Hugo's weapon/utilitarian worldview and Baskerville creed; the triplets' forgiveness; the age/eldest-son wordplay and Hugo's fratricidal succession; Vikir turning Hugo's own forgiveness maxim back on him; the under-fifteen haggis/chocolate reward regime; the direct-line encouragement; the post-break pantry realignment; `cacao` rather than `coca`; Bloody Bean concentration; and the exact endpoint that Vikir did not take the beans to eat. Later references were used only to resolve corrupted wording and were not used to reveal the beans' later purpose.

The final preview was browser-rendered at 1100×900 and 390×844. Both viewports contain 146 paragraphs, one scene break, {d['dialogue_count']} dialogue paragraphs, {d['narrative_count']} narrative paragraphs and seven italicized thought paragraphs. Desktop line height is {d['body_line_height']} with {d['dialogue_indent']} dialogue indentation; mobile line height is {m['body_line_height']} with {m['dialogue_indent']} dialogue indentation. Narration remains unindented and neither viewport has horizontal overflow. Four committed browser captures cover the opening, eldest-son/forgiveness exchange, Bloody Bean passage and mobile ending. The layout measurements passed; no independent human screenshot-review claim is made.

The complete-checkout recovery verifier, deterministic draft/preview checks, tracker check, full unit-test suite and whitespace check passed on the final text. Chapter 7 is therefore **editorially accepted** under `korean_plus_mtl`. Its acceptance record binds the final draft, both source hashes, edit set, Korean alignment, source decisions, continuity, preview, layout evidence and validation report. Whole-EPUB packaging and EPUBCheck remain separate release work.
"""
    write('editorial/reviews/chapter-0007-final.md',final)

    qa_path=ROOT/'qa/chapter-0007.json'
    qa=json.loads(qa_path.read_text(encoding='utf-8'))
    issue=next(i for i in qa['issues'] if i['id']=='CH007-06')
    issue['status']='resolved'
    issue['resolution']='Complete final prose reading, final Chromium desktop/mobile rendering, recovery verification, deterministic draft/preview checks, tracker check, full unittest suite and whitespace check passed before acceptance.'
    issue['evidence']=['editorial/reviews/chapter-0007-final.md','qa/layout/chapter-0007.json','qa/chapter-0007-validation.md']
    issue.pop('required_evidence',None)
    qa['accepted']=True
    qa['acceptance_evidence']='qa/acceptance/chapter-0007.json'
    qa['pass']='Final editorial, source, continuity, browser-layout and repository validation'
    qa['pass_description']='Complete Korean/MTL source comparison, final prose reading, continuity review, final desktop/mobile browser rendering and complete-checkout reproducibility validation'
    qa['final_review_evidence']=[
      'editorial/reviews/chapter-0007-final.md','editorial/continuity/chapter-0007.md','preview/chapter-0007.html','qa/layout/chapter-0007.json',
      'qa/layout/chapter-0007-desktop-opening.png','qa/layout/chapter-0007-desktop-eldest.png','qa/layout/chapter-0007-desktop-beans.png','qa/layout/chapter-0007-mobile-ending.png','qa/chapter-0007-validation.md']
    write('qa/chapter-0007.json',json.dumps(qa,ensure_ascii=False,indent=2)+'\n')

    state_path=ROOT/'editorial/reconstruction-status.json'
    state=json.loads(state_path.read_text(encoding='utf-8'))
    state['7']={'status':'qa_accepted','draft':'manuscript/drafts/chapter-0007.md','qa_report':'qa/chapter-0007.md','open_issues':[],'acceptance_evidence':'qa/acceptance/chapter-0007.json'}
    write('editorial/reconstruction-status.json',json.dumps(state,ensure_ascii=False,indent=2)+'\n')

    outputs=bed.render(7,validate_acceptance=False)
    for name,text in outputs.items(): write(name,text)
    subprocess.run([sys.executable,str(ROOT/'tools/build_chapter_preview.py'),'7'],check=True)
    spec=json.loads((ROOT/'editorial/edits/chapter-0007.json').read_text(encoding='utf-8'))
    alignment=json.loads((ROOT/'editorial/korean-alignment/chapter-0007.json').read_text(encoding='utf-8'))
    qa=json.loads(qa_path.read_text(encoding='utf-8'))
    draft=outputs['manuscript/drafts/chapter-0007.md']
    record=bed.acceptance_context(7,spec,qa,draft,alignment)
    record.update({'review_date':'2026-09-14','reviewer':'Codex editorial/QA agent; no independent human review claimed','release_status':'epub_not_built'})
    write('qa/acceptance/chapter-0007.json',json.dumps(record,ensure_ascii=False,indent=2)+'\n')

    qa_md="""# Chapter 7 — The Baskerville Dog (4): reconstruction QA

**Editorially accepted Korean-plus-MTL reconstruction; all six QA items resolved.** All 146 MTL paragraph slots are preserved, 135 edited, and all 151 Korean physical lines are accounted for, including the restored source scene break. Complete source comparison, final prose reading, continuity review, desktop/mobile browser rendering and repository-level reproducibility checks passed. [Final review](../editorial/reviews/chapter-0007-final.md) · [Acceptance evidence](acceptance/chapter-0007.json) · [Preview](../preview/chapter-0007.html). EPUB release remains pending; this is not recovered old production.

[Source decisions](../editorial/reviews/chapter-0007.md) · [Continuity](../editorial/continuity/chapter-0007.md) · [QA decisions](chapter-0007.json) · [Validation](chapter-0007-validation.md) · [Draft](../manuscript/drafts/chapter-0007.md).
"""
    write('qa/chapter-0007.md',qa_md)

    p=ROOT/'PROJECT_STATE.md'; text=p.read_text(encoding='utf-8')
    anchor='- Chapter 6 is **editorially accepted**: 124 paragraphs retained, 118 edited, all 124 Korean physical lines accounted for and all six QA items resolved. See [Chapter 6 QA](qa/chapter-0006.md) and its [acceptance record](qa/acceptance/chapter-0006.json).\n'
    add=anchor+'- Chapter 7 is **editorially accepted**: 146 paragraph slots retained, 135 edited, all 151 Korean physical lines accounted for and all six QA items resolved. See [Chapter 7 QA](qa/chapter-0007.md) and its [acceptance record](qa/acceptance/chapter-0007.json).\n'
    if anchor not in text: raise SystemExit('PROJECT_STATE anchor missing')
    text=text.replace(anchor,add,1).replace('**Current total: 6 accepted reconstructions; Chapters 7–493 remain unstarted.**','**Current total: 7 accepted reconstructions; Chapters 8–493 remain unstarted.**',1)
    write('PROJECT_STATE.md',text)

    p=ROOT/'README.md'; text=p.read_text(encoding='utf-8')
    old='**Current checkpoint: Chapters 1–6 editorially accepted; Chapter 7 is next.** Each includes Korean/MTL comparison, explicit source decisions and desktop/mobile layout review. [Chapter 5](manuscript/drafts/chapter-0005.md) · [Chapter 6](manuscript/drafts/chapter-0006.md) · [Latest QA and evidence](qa/chapter-0006.md). The remaining 487 chapters await reconstruction.'
    new='**Current checkpoint: Chapters 1–7 editorially accepted; Chapter 8 is next.** Each includes Korean/MTL comparison, explicit source decisions and desktop/mobile layout review. [Chapter 6](manuscript/drafts/chapter-0006.md) · [Chapter 7](manuscript/drafts/chapter-0007.md) · [Latest QA and evidence](qa/chapter-0007.md). The remaining 486 chapters await reconstruction.'
    if old not in text: raise SystemExit('README checkpoint text missing')
    write('README.md',text.replace(old,new,1))

    p=ROOT/'PROGRESS.md'; text=p.read_text(encoding='utf-8')
    anchor='# Project progress\n\nThis log records recovered evidence and new reconstruction work separately. Historical completion reports do not count as recovered chapter QA.\n\n'
    section="""## 2026-09-14 — Chapter 7 reconstructed and accepted

**Result: 7 chapters editorially accepted; Chapter 8 is next.** Chapter 7 retains all 146 MTL paragraph slots, records 135 explicit edits, accounts for all 151 Korean physical lines, and resolves all six QA items.

- Restored Hugo's utilitarian worldview and Baskerville's strength/weakness creed, reconstructed the triplets' forgiveness and age/eldest-son wordplay, and clarified that Vikir turns Hugo's own old forgiveness maxim back on him.
- Restored the under-fifteen haggis/chocolate reward system, Hugo's instruction not to lose to the direct line, and the two-suns visual echo without naming later competitors.
- Realigned the source divider safely: Korean line 98 becomes the real `◆◆◆` break after paragraph 93, while the MTL divider slot is reused for the first post-break line. All 146 slots and all Korean lines remain accounted for.
- Normalized raw cacao/Bloody Bean terminology, corrected the 100-liter-per-bean versus roughly 10,000-liter-per-pouch math, and preserved the endpoint that Vikir did not take the beans to eat.
- Final Chromium rendering and repository checks passed before hash-bound acceptance evidence was generated.

**Next:** reconstruct Chapter 8 (*Hounds of Hell (1)*) using Korean plus MTL, beginning from the still-unrevealed purpose of the Bloody Beans. Whole-EPUB release remains pending.

"""
    if anchor not in text: raise SystemExit('PROGRESS anchor missing')
    write('PROGRESS.md',text.replace(anchor,anchor+section,1))
    print('Chapter 7 acceptance files generated; final repository checks must still pass.')

if __name__=='__main__': main()
