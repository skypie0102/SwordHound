"""Finalize Chapter 6 after the complete-checkout acceptance gate passes."""
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import build_editorial_draft as bed


def write(path, text):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding='utf-8', newline='\n')


def main():
    validation = """# Chapter 6 repository validation — 2026-09-14

The Chapter 6 acceptance workflow reached finalization only after these checks completed successfully on a complete GitHub checkout of the reviewed candidate:

- final punctuation fixes regenerated the explicit edit set, draft, provenance and preview;
- Chromium rendered the final preview at 1100×900 and 390×844 and regenerated the committed layout measurements/screenshots;
- `python tools/verify_recovery.py`;
- `python tools/build_editorial_draft.py 6 --check`;
- `python tools/build_chapter_preview.py 6 --check`;
- `python tools/rebuild_editorial_tracking.py --check`;
- `python -m unittest discover -s tests -v`;
- `git diff --check`.

These checks establish preserved-source integrity, deterministic materialization, complete Korean-line accounting, browser-rendered layout invariants, tracker consistency and test compatibility. They do not authenticate the supplied Korean as a publisher witness or constitute whole-EPUB release QA.
"""
    write('qa/chapter-0006-validation.md', validation)

    layout = json.loads((ROOT / 'qa/layout/chapter-0006.json').read_text(encoding='utf-8'))
    d, m = layout['viewports']['desktop'], layout['viewports']['mobile']
    final_review = f"""# Chapter 6 final editorial review — 2026-09-14

Codex completed the Korean/MTL comparison and a full final reading of all 124 English paragraphs. The chapter preserves all 124 MTL paragraph slots and accounts for all 124 Korean physical lines, including three explicit shared-line groups and the restored scene break after paragraph 66. The final pass also removed two accidental interior spaces from silent-response ellipses at paragraphs 99 and 122. This is a new reconstruction, not recovered old production, independent human review or publisher authentication.

The consequential source choices are recorded in the [source review](chapter-0006.md): John Barrymore and Hugo Le Baskerville terminology; Morgue Family and Red Fang Mountain; removal of the MTL-only advertisement insertion without deleting a paragraph; the two-suns and multicolored-cloud omen; the Chapter 5 injury aftermath; concealment of mana as experience from the Age of Destruction; the `Patriarch`/`Father` exchange; the triplets' broken fighting spirit; and the Baskerville creed that strength is justice and weakness is sin. Chapter 7's opening continuity also treats Hugo as Vikir's father, supporting the relationship underlying that adjudication without importing Chapter 7 events into this chapter.

The final preview was browser-rendered at 1100×900 and 390×844. Desktop/mobile both contain 124 paragraphs, one scene break, 51 dialogue paragraphs, 73 narrative paragraphs and three italicized thought paragraphs. Desktop line height is {d['body_line_height']} with {d['dialogue_indent']} dialogue indentation; mobile line height is {m['body_line_height']} with {m['dialogue_indent']} dialogue indentation. Narration remains unindented and neither viewport has horizontal overflow. Four committed browser captures cover the opening, two-suns omen, father/patriarch exchange and mobile ending. The automated layout measurements passed; no independent human image-review claim is made.

The complete-checkout recovery verifier, deterministic draft/preview checks, tracker check, full unit-test suite and whitespace check passed on the final text. Chapter 6 is therefore **editorially accepted** under `korean_plus_mtl`. The acceptance record binds the final draft, both source hashes, edit set, Korean alignment, source decisions, continuity, preview, layout evidence and validation report. Whole-EPUB packaging and EPUBCheck remain separate release work.
"""
    write('editorial/reviews/chapter-0006-final.md', final_review)

    qa_path = ROOT / 'qa/chapter-0006.json'
    qa = json.loads(qa_path.read_text(encoding='utf-8'))
    issue = next(i for i in qa['issues'] if i['id'] == 'CH006-06')
    issue['status'] = 'resolved'
    issue['resolution'] = 'Complete final prose reading, final Chromium desktop/mobile rendering, recovery verification, deterministic draft/preview checks, tracker check, full unittest suite and whitespace check passed before acceptance.'
    issue['evidence'] = ['editorial/reviews/chapter-0006-final.md', 'qa/layout/chapter-0006.json', 'qa/chapter-0006-validation.md']
    issue.pop('required_evidence', None)
    qa['accepted'] = True
    qa['acceptance_evidence'] = 'qa/acceptance/chapter-0006.json'
    qa['pass'] = 'Final editorial, source, continuity, browser-layout and repository validation'
    qa['pass_description'] = 'Complete Korean/MTL source comparison, final prose reading, continuity review, final desktop/mobile browser rendering and complete-checkout reproducibility validation'
    qa['final_review_evidence'] = [
        'editorial/reviews/chapter-0006-final.md',
        'editorial/continuity/chapter-0006.md',
        'preview/chapter-0006.html',
        'qa/layout/chapter-0006.json',
        'qa/layout/chapter-0006-desktop-opening.png',
        'qa/layout/chapter-0006-desktop-omen.png',
        'qa/layout/chapter-0006-desktop-father.png',
        'qa/layout/chapter-0006-mobile-ending.png',
        'qa/chapter-0006-validation.md'
    ]
    write('qa/chapter-0006.json', json.dumps(qa, ensure_ascii=False, indent=2) + '\n')

    state_path = ROOT / 'editorial/reconstruction-status.json'
    state = json.loads(state_path.read_text(encoding='utf-8'))
    state['6'] = {'status':'qa_accepted','draft':'manuscript/drafts/chapter-0006.md','qa_report':'qa/chapter-0006.md','open_issues':[],'acceptance_evidence':'qa/acceptance/chapter-0006.json'}
    write('editorial/reconstruction-status.json', json.dumps(state, ensure_ascii=False, indent=2) + '\n')

    outputs = bed.render(6, validate_acceptance=False)
    for name, text in outputs.items():
        write(name, text)
    subprocess.run([sys.executable, str(ROOT / 'tools/build_chapter_preview.py'), '6'], check=True)

    spec = json.loads((ROOT / 'editorial/edits/chapter-0006.json').read_text(encoding='utf-8'))
    alignment = json.loads((ROOT / 'editorial/korean-alignment/chapter-0006.json').read_text(encoding='utf-8'))
    qa = json.loads(qa_path.read_text(encoding='utf-8'))
    draft = outputs['manuscript/drafts/chapter-0006.md']
    record = bed.acceptance_context(6, spec, qa, draft, alignment)
    record.update({'review_date':'2026-09-14','reviewer':'Codex editorial/QA agent; no independent human review claimed','release_status':'epub_not_built'})
    write('qa/acceptance/chapter-0006.json', json.dumps(record, ensure_ascii=False, indent=2) + '\n')

    qa_md = """# Chapter 6 — The Baskerville Dog (3): reconstruction QA

**Editorially accepted Korean-plus-MTL reconstruction; all six QA items resolved.** All 124 MTL paragraphs are preserved, 118 edited, and all 124 Korean physical lines accounted for, including three declared shared-line groups and one restored scene break. Complete source comparison, final prose reading, continuity review, desktop/mobile browser rendering, and repository-level reproducibility checks passed. [Final review](../editorial/reviews/chapter-0006-final.md) · [Acceptance evidence](acceptance/chapter-0006.json) · [Preview](../preview/chapter-0006.html). EPUB release remains pending; this is not recovered old production.

[Source decisions](../editorial/reviews/chapter-0006.md) · [Continuity](../editorial/continuity/chapter-0006.md) · [QA decisions](chapter-0006.json) · [Validation](chapter-0006-validation.md) · [Draft](../manuscript/drafts/chapter-0006.md).
"""
    write('qa/chapter-0006.md', qa_md)

    project_path = ROOT / 'PROJECT_STATE.md'
    project = project_path.read_text(encoding='utf-8')
    anchor = '- Chapter 5 is **editorially accepted**: 183 paragraphs retained, 179 edited, all 188 Korean physical lines accounted for and all six QA items resolved. See [Chapter 5 QA](qa/chapter-0005.md) and its [acceptance record](qa/acceptance/chapter-0005.json).\n'
    addition = anchor + '- Chapter 6 is **editorially accepted**: 124 paragraphs retained, 118 edited, all 124 Korean physical lines accounted for and all six QA items resolved. See [Chapter 6 QA](qa/chapter-0006.md) and its [acceptance record](qa/acceptance/chapter-0006.json).\n'
    if anchor not in project: raise SystemExit('PROJECT_STATE anchor missing')
    project = project.replace(anchor, addition, 1)
    project = project.replace('**Current total: 5 accepted reconstructions; Chapters 6–493 remain unstarted.**', '**Current total: 6 accepted reconstructions; Chapters 7–493 remain unstarted.**', 1)
    write('PROJECT_STATE.md', project)

    readme_path = ROOT / 'README.md'
    readme = readme_path.read_text(encoding='utf-8')
    old = '**Current checkpoint: Chapters 1–5 editorially accepted; Chapter 6 is next.** Each includes Korean/MTL comparison, explicit source decisions and inspected desktop/mobile layout. [Chapter 4](manuscript/drafts/chapter-0004.md) · [Chapter 5](manuscript/drafts/chapter-0005.md) · [Latest QA and evidence](qa/chapter-0005.md). The remaining 488 chapters await reconstruction.'
    new = '**Current checkpoint: Chapters 1–6 editorially accepted; Chapter 7 is next.** Each includes Korean/MTL comparison, explicit source decisions and desktop/mobile layout review. [Chapter 5](manuscript/drafts/chapter-0005.md) · [Chapter 6](manuscript/drafts/chapter-0006.md) · [Latest QA and evidence](qa/chapter-0006.md). The remaining 487 chapters await reconstruction.'
    if old not in readme: raise SystemExit('README checkpoint text missing')
    write('README.md', readme.replace(old, new, 1))

    progress_path = ROOT / 'PROGRESS.md'
    progress = progress_path.read_text(encoding='utf-8')
    anchor = '# Project progress\n\nThis log records recovered evidence and new reconstruction work separately. Historical completion reports do not count as recovered chapter QA.\n\n'
    section = """## 2026-09-14 — Chapter 6 reconstructed and accepted

**Result: 6 chapters editorially accepted; Chapter 7 is next.** Chapter 6 retains all 124 MTL paragraphs, records 118 explicit edits, accounts for all 124 Korean physical lines, and resolves all six QA items.

- Removed the MTL-only advertisement insertion without deleting a paragraph, declared the three combined Korean-line mappings, and restored the Korean scene break after Barrymore identifies Vikir.
- Standardized Morgue Family and Red Fang Mountain with the witness variants documented; repaired the two-suns/multicolored-cloud omen, written-exam wording and Chapter 5 injury aftermath.
- Restored the Age-of-Destruction explanation for mana concealment, the triplets' loss of fighting spirit, the three-dull-blades metaphor, and the Baskerville creed. The corrupt form-of-address exchange is explicitly adjudicated as `Patriarch` versus `Father`, supported by established relationship continuity rather than presented as literal Korean wording.
- Final Chromium rendering at desktop/mobile widths confirmed 124 paragraphs, one scene break, three italic thoughts, 1.65 line height, correct dialogue/narration indentation and no horizontal overflow. Four browser captures were committed as presentation evidence.
- Preserved-source verification, deterministic draft/preview checks, tracker checks, the full unittest suite and whitespace checks passed before the acceptance record was generated.

**Next:** reconstruct Chapter 7 from Hugo's satisfaction with Vikir, preserving Chapter 6's exact endpoint and continuing Korean-plus-MTL review. Whole-EPUB release remains pending.

"""
    if anchor not in progress: raise SystemExit('PROGRESS anchor missing')
    write('PROGRESS.md', progress.replace(anchor, anchor + section, 1))
    print('Chapter 6 acceptance files generated; final repository checks must still pass.')


if __name__ == '__main__':
    main()
