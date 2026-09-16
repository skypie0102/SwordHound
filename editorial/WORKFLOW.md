# Reconstruction workflow

Canonical chapter identity follows the original Korean/source chapter number. The recovered 493-chapter English MTL corpus is a working translation witness, not the authority for chapter numbering. Its Chapter 59 merges canonical source Chapters 59 and 60, so recovered MTL numbering runs one chapter behind the source from canonical Chapter 61 onward in the currently mapped range. Korean source Chapter 125 is present in `source/korean/chapters/125.txt` and aligns to recovered MTL Chapter 124. Use `editorial/reprocessing/source-inventory-001-125.json` for the source-to-MTL map. The user reports possessing a Chapter 55 Korean raw, but no `055.txt` is currently committed in the accessible repository tree; use MTL fallback only while that raw is unavailable. Use the Fandom and Namu Wiki references for QA, with additional web research as needed. Follow [SOURCES.md](SOURCES.md) for evidence rules and review modes.

The older audit concerns 500 chapters, and historical reports describe lost edited production through 374. Preserve the identities of each source and do not equate historical reports with recovered finished chapters.

## Current files and ownership

- `source/`, `archives/`, `artifacts/`, `epub/`, and `editorial/Editorial-Audit.md` preserve recovered originals. Do not edit them to incorporate new corrections.
- `editorial/edits/chapter-NNNN.json` contains explicit, reviewable paragraph replacements anchored to a source file hash.
- `qa/chapter-NNNN.json` records source questions, review scope, and acceptance. The companion Markdown report explains the review to readers.
- `editorial/reconstruction-status.json` is the manually maintained status overlay. The tracker is generated from this file and original source records.
- `manuscript/drafts/` and `editorial/provenance/` are generated. Change the edit set, then regenerate; do not silently hand-edit the output.
- `editorial/korean-alignment/` accounts for supplied Korean lines against MTL paragraphs, including headings and scene breaks. `editorial/reviews/` records source decisions and web evidence. Resolved QA items must link to their written decision and evidence files.
- When one Korean physical line spans several MTL paragraphs, repeat its reference only with an explicit `shared_lines` declaration containing the line number, all owning MTL paragraphs in order, and the reason. The validator requires exact coverage and rejects undeclared duplicates or incorrect owners.
- When a recovered MTL paragraph genuinely has no counterpart in the supplied Korean witness, declare it explicitly through `mtl_only_paragraphs` with a reason. Do not fabricate Korean coverage. Korean physical-line coverage must still remain exact.
- `editorial/audit-alignment.json` locates historical findings using exact quoted text and title after whitespace normalization. Its `not_reviewed` disposition belongs to the immutable locator index; chapter QA reports hold actual manual triage. Unmatched and ambiguous findings remain available for review.

## Continuous title-family processing

Reconstruct chapters as contiguous title families. Determine the complete family boundary from `editorial/chapter-tracker.json` before starting. A family such as `Solitary (1)` through `Solitary (4)` is one editorial batch for continuity and QA purposes.

Finishing one title family is a checkpoint, **not a stopping condition**. After integrating a completed family, immediately identify the next base-title family and continue editorial work. Continue across title families until the user explicitly asks to stop/pause, the corpus ends, or a genuine editorial blocker prevents safe progress.

Do not introduce runner/browser work between ordinary title families. Preserve a short continuity handoff at each boundary so the next family begins from the exact preceding endpoint.

## Editorial-first per-chapter procedure

1. Confirm source hash and corresponding reference editions. Check chapter title and actual text rather than trusting old chapter numbers.
2. Read the entire chapter. Make explicit English edits and record the reason for each. Prioritize translation fidelity, grammar, awkward wording, mistranslations, names/terms, speaker attribution, chronology, information-window content/structure, scene-break meaning, and natural prose.
   - Preserve the source's actual intensity and specificity. Do not sanitize violence, gore, profanity, anatomical language, degradation, sexual material, or other harsh content; do not euphemize or omit it for palatability, and do not intensify beyond what the evidence supports.
3. Work by canonical Korean/source chapter number. For every canonical chapter with a Korean witness in the inventory, compare that Korean material against its mapped recovered-MTL passage(s) line by line. Treat the MTL Chapter 59 merge as a boundary defect to repair: canonical Chapters 59 and 60 remain separate chapters. Physical bundles such as Korean `075.txt` likewise do not collapse canonical Chapters 75 and 76. If a canonical Korean raw is genuinely unavailable in the repository, use the recovered MTL plus context, continuity, and supporting references under an explicit `mtl_with_supporting_references` limitation. Consult the designated wikis where relevant, record evidence and conflicts, and never describe MTL-only fallback as bilingual verification.
4. Check continuity against the chapter's current knowledge and reveal timeline. Recovered later summaries are leads, not permission to introduce later knowledge early.
5. Generate/review the draft and paragraph provenance, regenerate the tracker, and review the resulting draft as prose, including every unchanged paragraph. Run deterministic text/source/alignment/tracker checks that do not require a browser or hosted runner.
6. Accept editorially only after all reviews required by the source mode and all actual open editorial issues are resolved, with evidence linked to the final text hash. MTL-only passages or chapters may receive editorial acceptance under an explicitly recorded limitation; do not call them bilingually verified.
7. Record scope, unresolved issues, validation, continuity handoff, and the next title-family checkpoint in `PROGRESS.md`, then continue directly into the next family.

## Checks during editorial reconstruction

Use deterministic text/integrity checks only during chapter processing. Typical checks include:

```text
python tools/build_editorial_draft.py N
python tools/rebuild_editorial_tracking.py
python tools/verify_recovery.py
python tools/build_editorial_draft.py N --check
python tools/rebuild_editorial_tracking.py --check
python -m unittest discover -s tests -v
```

These checks protect recovered evidence, alignment/provenance conservation, deterministic draft generation, tracker consistency, acceptance hashes, and failure handling. They do **not** certify the translation by themselves.

Do not require `build_chapter_preview.py`, Playwright, browser screenshots, CSS measurements, viewport checks, or GitHub Actions for ordinary title-family editorial acceptance. Existing preview/layout evidence from earlier accepted chapters may remain in history, but future editorial batches should not spend time or runner capacity producing equivalent evidence.

## Complete-EPUB presentation/release phase

Defer presentation work until a complete EPUB is assembled. At that stage, apply and verify the recovered formatting requirements, including dialogue indentation, unindented narration, 1.65 line height, single-quote handling, information-window presentation, `◆◆◆` scene breaks, typography, CSS behavior, device/viewport rendering, and any other visual polish.

Browser rendering, screenshots, Playwright-based layout inspection, overflow measurements, final CSS tuning, EPUB packaging, and EPUBCheck belong to this complete-EPUB/release phase unless the user explicitly requests an earlier visual check. Batch these expensive checks together rather than repeating them per chapter or title family.

## Acceptance records

Before changing accepted chapter material, set `accepted` to false in its QA record and reopen the corresponding overlay state and issues. Keep prior decisions in Git history. Complete the editorial review again before setting `qa_accepted`.

The reviewing agent records closed issues, review basis, final-review evidence paths, date and reviewer identity. The acceptance record binds `acceptance_context` from `tools/build_editorial_draft.py`: final Markdown, source hashes, edit-set and decision digests, alignment and evidence hashes. Text evidence is normalized for checkout line endings. Existing older records may also bind PNG layout evidence; new editorial-first records do not require browser/layout evidence.

When preparing a record after actual review, the agent may use `render(chapter, validate_acceptance=False)` solely to compute the proposed final bytes before the record exists. Ordinary generation, checks, and tracker integration must use validation. Never refresh hashes automatically to hide a change from review. A valid record must pass the normal deterministic builder and tracker checks before publishing.

## Working style

Use past-tense narration with intentional exceptions for general descriptions, direct thoughts, dialogue, and system text. Preserve rhetorical fragments when useful. Keep curly quotation marks; repair accidental point-of-view shifts. Normalize ellipses where editing has been reviewed, without treating all sounds or pauses as scene breaks. Apply the recovered formatting requirements in [Recovered-Editorial-Decisions.md](Recovered-Editorial-Decisions.md) when building the complete EPUB rather than interrupting chapter-by-chapter editorial work for presentation tuning.

Keep source-dependent terminology provisional in [GLOSSARY.md](GLOSSARY.md). Do not globally flatten family/clan/house, sword ranks, threat labels, or ritual names merely because variants exist. Do not treat a grammar repair as evidence of correct meaning.
