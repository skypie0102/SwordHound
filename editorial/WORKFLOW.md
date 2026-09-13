# Reconstruction workflow

The recovered 493-chapter English MTL corpus is the working narrative base. User-supplied Korean raws are available for Chapters 1–54; from Chapter 55 onward the user has no Korean raws and authorizes MTL-based reconstruction. Use the Fandom and Namu Wiki references for QA, with additional web research as needed. Follow [SOURCES.md](SOURCES.md) for exact paths, links, evidence rules, and review modes.

The older audit concerns 500 chapters, and historical reports describe lost edited production through 374. Preserve the identities of each source and do not equate historical reports with recovered finished chapters.

## Current files and ownership

- `source/`, `archives/`, `artifacts/`, `epub/`, and `editorial/Editorial-Audit.md` preserve recovered originals. Do not edit them to incorporate new corrections.
- `editorial/edits/chapter-NNNN.json` contains explicit, reviewable paragraph replacements anchored to a source file hash.
- `qa/chapter-NNNN.json` records source questions, review scope, and acceptance. The companion Markdown report explains the review to readers.
- `editorial/reconstruction-status.json` is the manually maintained status overlay. The tracker is generated from this file and original source records.
- `manuscript/drafts/` and `editorial/provenance/` are generated. Change the edit set, then regenerate; do not silently hand-edit the output.
- `editorial/korean-alignment/` accounts for supplied Korean lines against MTL paragraphs, including headings and scene breaks. `editorial/reviews/` records source decisions and web evidence. Resolved QA items must link to their written decision and evidence files.
- `editorial/audit-alignment.json` locates historical findings using exact quoted text and title after whitespace normalization. Its `not_reviewed` disposition belongs to the immutable locator index; chapter QA reports hold actual manual triage. Unmatched and ambiguous findings remain available for review.

## Per-chapter procedure

1. Confirm source hash and identify corresponding reference editions. Check chapter title and actual text rather than trusting old chapter numbers.
2. Read the entire chapter. Make explicit English edits and record the reason for each. Keep unresolved meaning, chronology, names, ranks, and speaker attribution in the QA record.
3. For Chapters 1–54, compare the supplied Korean and MTL passages. For Chapters 55–493, review the MTL against context, continuity, and supporting references; Korean availability is not a prerequisite. Consult the two designated wikis for applicable names, terms, and locations, and seek other web support when needed. Record specific evidence, access dates, decisions, and conflicts. Label the review basis as `korean_plus_mtl` or `mtl_with_supporting_references`.
4. Check continuity against the chapter's current knowledge and reveal timeline. Recovered later summaries are leads, not permission to introduce later knowledge early.
5. Render the draft and paragraph provenance, regenerate the tracker, and run the checks below. Review the resulting draft as prose, including every unchanged paragraph.
6. Accept only after all reviews required by the chapter's source mode and its actual open issues are resolved, with evidence linked to the final text hash. MTL-only chapters can receive editorial acceptance under that explicitly recorded limitation; do not call them bilingually verified. Chapter 1 now demonstrates the acceptance format in `qa/acceptance/`. The renderer and tracker reject stale acceptance records. Whole-EPUB release validation remains separate.
7. Record the scope, unresolved issues, validation, and next checkpoint in `PROGRESS.md`, then commit and push without rewriting existing history.

## Checks for the current batch

```text
python tools/build_editorial_draft.py 1
python tools/rebuild_editorial_tracking.py
python tools/verify_recovery.py
python tools/build_editorial_draft.py 1 --check
python tools/build_chapter_preview.py 1 --check
python tools/rebuild_editorial_tracking.py --check
python -m unittest discover -s tests -v
```

The first two commands regenerate outputs. The remaining commands check preserved evidence, draft reproducibility, tracker consistency, and failure handling. They do not certify a translation. EPUB building, presentation verification, and EPUBCheck remain release work after editorial acceptance.

For an edited chapter preview, run `python tools/build_chapter_preview.py 1` after generating the draft, then inspect its layout and record the actual results. Chapter 1's standalone layout has been inspected; final EPUB rendering still needs its own review.

## Acceptance records

Before changing accepted chapter material, set `accepted` to false in its QA record and reopen the corresponding overlay state and issues. Keep prior decisions in Git history. Complete the review again before setting `qa_accepted`.

The reviewing agent records closed issues, review basis, final-review evidence paths, date and reviewer identity. The acceptance record binds `acceptance_context` from `tools/build_editorial_draft.py`: final Markdown, source hashes, edit-set and decision digests, alignment and evidence hashes. Text evidence is normalized for checkout line endings; PNG evidence is byte-exact. This is an integrity mechanism, not proof of reviewer identity.

When preparing a record after actual review, the agent may use `render(chapter, validate_acceptance=False)` solely to compute the proposed final bytes before the record exists. Ordinary generation, checks, and tracker integration must use validation. Never refresh hashes automatically to hide a change from review. A valid record must pass the normal builder and tracker checks before publishing.

## Working style

Use past-tense narration with intentional exceptions for general descriptions, direct thoughts, dialogue, and system text. Preserve rhetorical fragments when useful. Keep curly quotation marks; repair accidental point-of-view shifts. Normalize ellipses where editing has been reviewed, without treating all sounds or pauses as scene breaks. Apply the recovered formatting requirements in [Recovered-Editorial-Decisions.md](Recovered-Editorial-Decisions.md) when building a new EPUB.

Keep source-dependent terminology provisional in [GLOSSARY.md](GLOSSARY.md). Do not globally flatten family/clan/house, sword ranks, threat labels, or ritual names merely because variants exist. Do not treat a grammar repair as evidence of correct meaning.
