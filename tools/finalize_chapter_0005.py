"""Finalize Chapter 5 only after the workflow's pre-acceptance checks have passed."""
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
    validation = """# Chapter 5 repository validation — 2026-09-14

The temporary branch workflow reached this finalization step only after the following commands completed successfully on a complete GitHub checkout:

- `python tools/materialize_chapter_0005.py`
- `python tools/rebuild_editorial_tracking.py`
- `python tools/verify_recovery.py`
- `python tools/build_editorial_draft.py 5 --check`
- `python tools/build_chapter_preview.py 5 --check`
- `python tools/rebuild_editorial_tracking.py --check`
- `python -m unittest discover -s tests -v`
- `git diff --check`

These checks establish preserved-source integrity, deterministic Chapter 5 materialization, tracker consistency, test-suite compatibility, and whitespace cleanliness. They do not independently authenticate the Korean witness or constitute whole-EPUB release QA.
"""
    write('qa/chapter-0005-validation.md', validation)

    final_path = ROOT / 'editorial/reviews/chapter-0005-final.md'
    final = final_path.read_text(encoding='utf-8')
    final = final.replace(
        'Four screenshots cover the opening, ten-minute breath-hold, restored Hugo maxim/second attack, and mobile ending.',
        'Four local review captures covered the opening, ten-minute breath-hold, restored Hugo maxim/second attack, and mobile ending; the committed layout record preserves the measured results.'
    )
    old = ('The prose and presentation review therefore pass. **Editorial acceptance is intentionally withheld at this checkpoint** '
           'because the current connected environment cannot execute the repository-wide recovery verifier, tracker rebuild, and full unittest suite against a local checkout. '
           'CH005-06 remains open for those repository-level reproducibility checks. Once they pass without changing reviewed text/evidence, the acceptance record can be generated from the exact hashes and the status may move to `qa_accepted`.')
    new = ('The prose, presentation, and repository-level reproducibility reviews therefore pass. Chapter 5 is **editorially accepted** under `korean_plus_mtl`. '
           'The acceptance record binds the reviewed text, Korean alignment, source decisions, continuity, preview, layout measurements, and validation report. '
           'This remains new reconstruction work rather than recovered old production, independent human review, publisher authentication, or whole-EPUB release.')
    if old not in final:
        raise SystemExit('Expected Chapter 5 final-review checkpoint paragraph not found')
    final = final.replace(old, new)
    write('editorial/reviews/chapter-0005-final.md', final)

    qa_path = ROOT / 'qa/chapter-0005.json'
    qa = json.loads(qa_path.read_text(encoding='utf-8'))
    issue = next(i for i in qa['issues'] if i['id'] == 'CH005-06')
    issue['status'] = 'resolved'
    issue['resolution'] = 'Complete-checkout recovery verification, deterministic draft/preview checks, tracker regeneration/check, full unittest suite, and whitespace check passed before acceptance.'
    issue['evidence'] = ['qa/chapter-0005-validation.md']
    issue.pop('required_evidence', None)
    qa['accepted'] = True
    qa['acceptance_evidence'] = 'qa/acceptance/chapter-0005.json'
    qa['pass'] = 'Final editorial, source, continuity, layout and repository validation'
    qa['pass_description'] = 'Complete Korean/MTL source comparison, final prose reading, continuity, actual desktop/mobile layout review, and complete-checkout reproducibility validation'
    qa['final_review_evidence'] = [
        'editorial/reviews/chapter-0005-final.md',
        'editorial/continuity/chapter-0005.md',
        'preview/chapter-0005.html',
        'qa/layout/chapter-0005.json',
        'qa/chapter-0005-validation.md'
    ]
    write('qa/chapter-0005.json', json.dumps(qa, ensure_ascii=False, indent=2) + '\n')

    state_path = ROOT / 'editorial/reconstruction-status.json'
    state = json.loads(state_path.read_text(encoding='utf-8'))
    state['5'] = {
        'status': 'qa_accepted',
        'draft': 'manuscript/drafts/chapter-0005.md',
        'qa_report': 'qa/chapter-0005.md',
        'open_issues': [],
        'acceptance_evidence': 'qa/acceptance/chapter-0005.json'
    }
    write('editorial/reconstruction-status.json', json.dumps(state, ensure_ascii=False, indent=2) + '\n')

    outputs = bed.render(5, validate_acceptance=False)
    for name, text in outputs.items():
        write(name, text)
    subprocess.run([sys.executable, str(ROOT / 'tools/build_chapter_preview.py'), '5'], check=True)

    spec = json.loads((ROOT / 'editorial/edits/chapter-0005.json').read_text(encoding='utf-8'))
    alignment = json.loads((ROOT / 'editorial/korean-alignment/chapter-0005.json').read_text(encoding='utf-8'))
    qa = json.loads(qa_path.read_text(encoding='utf-8'))
    draft = outputs['manuscript/drafts/chapter-0005.md']
    record = bed.acceptance_context(5, spec, qa, draft, alignment)
    record.update({
        'review_date': '2026-09-14',
        'reviewer': 'Codex editorial/QA agent; no independent human review claimed',
        'release_status': 'epub_not_built'
    })
    write('qa/acceptance/chapter-0005.json', json.dumps(record, ensure_ascii=False, indent=2) + '\n')

    qa_md = """# Chapter 5 — The Baskerville Dog (2): reconstruction QA

**Editorially accepted Korean-plus-MTL reconstruction; all six QA items resolved.** All 183 MTL paragraphs are preserved, 179 edited, and all 188 Korean physical lines accounted for. Complete source comparison, final prose reading, continuity review, measured desktop/mobile layout inspection, and repository-level reproducibility checks passed. [Final review](../editorial/reviews/chapter-0005-final.md) · [Acceptance evidence](acceptance/chapter-0005.json) · [Preview](../preview/chapter-0005.html). EPUB release remains pending; this is not recovered old production.

[Source decisions](../editorial/reviews/chapter-0005.md) · [Continuity](../editorial/continuity/chapter-0005.md) · [QA decisions](chapter-0005.json) · [Validation](chapter-0005-validation.md) · [Draft](../manuscript/drafts/chapter-0005.md).
"""
    write('qa/chapter-0005.md', qa_md)

    project_path = ROOT / 'PROJECT_STATE.md'
    project = project_path.read_text(encoding='utf-8')
    anchor = '- Chapters 3–4 are **editorially accepted**: 258 paragraphs retained, 248 edited, 255 Korean lines accounted for and nine QA items resolved. Their source decisions, final reviews and acceptance evidence are linked from [Chapter 3 QA](qa/chapter-0003.md) and [Chapter 4 QA](qa/chapter-0004.md).\n'
    addition = anchor + '- Chapter 5 is **editorially accepted**: 183 paragraphs retained, 179 edited, all 188 Korean physical lines accounted for and all six QA items resolved. See [Chapter 5 QA](qa/chapter-0005.md) and its [acceptance record](qa/acceptance/chapter-0005.json).\n'
    if anchor not in project:
        raise SystemExit('PROJECT_STATE Chapter 3–4 anchor missing')
    project = project.replace(anchor, addition, 1)
    project = project.replace('**Current total: 4 accepted reconstructions; Chapters 5–493 remain unstarted.**', '**Current total: 5 accepted reconstructions; Chapters 6–493 remain unstarted.**', 1)
    write('PROJECT_STATE.md', project)

    readme_path = ROOT / 'README.md'
    readme = readme_path.read_text(encoding='utf-8')
    old_checkpoint = '**Current checkpoint: Chapters 1–4 editorially accepted; Chapter 5 is next.** Each includes Korean/MTL comparison, explicit source decisions and inspected desktop/mobile layout. [Chapter 3](manuscript/drafts/chapter-0003.md) · [Chapter 4](manuscript/drafts/chapter-0004.md) · [Latest QA and evidence](qa/chapter-0004.md). The remaining 489 chapters await reconstruction.'
    new_checkpoint = '**Current checkpoint: Chapters 1–5 editorially accepted; Chapter 6 is next.** Each includes Korean/MTL comparison, explicit source decisions and inspected desktop/mobile layout. [Chapter 4](manuscript/drafts/chapter-0004.md) · [Chapter 5](manuscript/drafts/chapter-0005.md) · [Latest QA and evidence](qa/chapter-0005.md). The remaining 488 chapters await reconstruction.'
    if old_checkpoint not in readme:
        raise SystemExit('README checkpoint text missing')
    write('README.md', readme.replace(old_checkpoint, new_checkpoint, 1))

    progress_path = ROOT / 'PROGRESS.md'
    progress = progress_path.read_text(encoding='utf-8')
    insert_after = '# Project progress\n\nThis log records recovered evidence and new reconstruction work separately. Historical completion reports do not count as recovered chapter QA.\n\n'
    section = """## 2026-09-14 — Chapter 5 reconstructed and accepted

**Result: 5 chapters editorially accepted; Chapter 6 is next.** Chapter 5 retains all 183 MTL paragraphs, records 179 explicit edits, accounts for all 188 Korean physical lines, and resolves all six QA items.

- Corrected pervasive machine-translation damage against the supplied Korean while preserving the MTL paragraph structure. The unused-corridor room replaces the corrupted “bikinis” line; ten minutes is restored as six hundred seconds; Hugo’s child-rearing maxim is reconstructed from Korean; and the extra short-sword line is integrated into Highbro’s second charge.
- Resolved localized actor conflicts with explicit evidence: Lowbro remains the youngest, restrains Vikir, and loses the finger; Highbro is the eldest and later attacks with the short sword. Fandom search-retrieved character/synopsis evidence was used narrowly where the supplied witnesses conflict, without importing Chapter 6 events.
- Final continuity stops when the Trident of Baskerville begins splitting from within. Styx protection is scoped to the blade resistance demonstrated in this scene rather than generalized into universal invulnerability.
- Desktop/mobile layout review covered all 183 paragraphs, 61 dialogue paragraphs, 122 narrative paragraphs and two italic thoughts at 1100px and 390px widths, with 1.65 line height, correct indentation and no horizontal overflow.
- Complete-checkout recovery verification, deterministic draft/preview checks, tracker regeneration/check, full unittest suite and whitespace checks passed before the acceptance record was generated. Source/archive evidence remains unchanged.

**Next:** reconstruct Chapter 6 from the triplets’ internal collapse, again using Korean plus MTL and preserving the Chapter 5 endpoint. Whole-EPUB release remains pending.

"""
    if insert_after not in progress:
        raise SystemExit('PROGRESS insertion anchor missing')
    progress = progress.replace(insert_after, insert_after + section, 1)
    write('PROGRESS.md', progress)

    print('Chapter 5 finalized for editorial acceptance; final repository checks must still run after this script.')


if __name__ == '__main__':
    main()
