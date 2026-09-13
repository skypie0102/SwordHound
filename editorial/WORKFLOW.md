# Reconstruction workflow

The recovered 493-chapter English MTL corpus is the working narrative base. User-supplied Korean raws are available for Chapters 1–54; from Chapter 55 onward the user has no Korean raws and authorizes MTL-based reconstruction. Use the Fandom and Namu Wiki references for QA, with additional web research as needed. Follow [SOURCES.md](SOURCES.md) for exact paths, links, evidence rules, and review modes.

The older audit concerns 500 chapters, and historical reports describe lost edited production through 374. Preserve the identities of each source and do not equate historical reports with recovered finished chapters.

## Current files and ownership

- `source/`, `archives/`, `artifacts/`, `epub/`, and `editorial/Editorial-Audit.md` preserve recovered originals. Do not edit them to incorporate new corrections.
- `editorial/edits/chapter-NNNN.json` contains explicit, reviewable paragraph replacements anchored to a source file hash.
- `qa/chapter-NNNN.json` records source questions, review scope, and acceptance. The companion Markdown report explains the review to readers.
- `editorial/reconstruction-status.json` is the manually maintained status overlay. The tracker is generated from this file and original source records.
- `manuscript/drafts/` and `editorial/provenance/` are generated. Change the edit set, then regenerate; do not silently hand-edit the output.
- `editorial/audit-alignment.json` locates historical findings using exact quoted text and title after whitespace normalization. Its `not_reviewed` disposition belongs to the immutable locator index; chapter QA reports hold actual manual triage. Unmatched and ambiguous findings remain available for review.

## Per-chapter procedure

1. Confirm source hash and identify corresponding reference editions. Check chapter title and actual text rather than trusting old chapter numbers.
2. Read the entire chapter. Make explicit English edits and record the reason for each. Keep unresolved meaning, chronology, names, ranks, and speaker attribution in the QA record.
3. For Chapters 1–54, compare the supplied Korean and MTL passages. For Chapters 55–493, review the MTL against context, continuity, and supporting references; Korean availability is not a prerequisite. Consult the two designated wikis for applicable names, terms, and locations, and seek other web support when needed. Record specific evidence, access dates, decisions, and conflicts. Label the review basis as `korean_plus_mtl` or `mtl_with_supporting_references`.
4. Check continuity against the chapter's current knowledge and reveal timeline. Recovered later summaries are leads, not permission to introduce later knowledge early.
5. Render the draft and paragraph provenance, regenerate the tracker, and run the checks below. Review the resulting draft as prose, including every unchanged paragraph.
6. Accept only after all reviews required by the chapter's source mode and its actual open issues are resolved, with evidence linked to the final draft hash. MTL-only chapters can receive editorial acceptance under that explicitly recorded limitation; do not call them bilingually verified. Current Chapter 1 has not reached acceptance. Extend the draft-only tooling and acceptance validation before using it for an accepted release.
7. Record the scope, unresolved issues, validation, and next checkpoint in `PROGRESS.md`, then commit and push without rewriting existing history.

## Checks for the current batch

```text
python tools/build_editorial_draft.py 1
python tools/rebuild_editorial_tracking.py
python tools/verify_recovery.py
python tools/build_editorial_draft.py 1 --check
python tools/rebuild_editorial_tracking.py --check
python -m unittest discover -s tests -v
```

The first two commands regenerate outputs. The remaining commands check preserved evidence, draft reproducibility, tracker consistency, and failure handling. They do not certify a translation. EPUB building, presentation verification, and EPUBCheck remain release work after editorial acceptance.

## Working style

Use past-tense narration with intentional exceptions for general descriptions, direct thoughts, dialogue, and system text. Preserve rhetorical fragments when useful. Keep curly quotation marks; repair accidental point-of-view shifts. Normalize ellipses where editing has been reviewed, without treating all sounds or pauses as scene breaks. Apply the recovered formatting requirements in [Recovered-Editorial-Decisions.md](Recovered-Editorial-Decisions.md) when building a new EPUB.

Keep source-dependent terminology provisional in [GLOSSARY.md](GLOSSARY.md). Do not globally flatten family/clan/house, sword ranks, threat labels, or ritual names merely because variants exist. Do not treat a grammar repair as evidence of correct meaning.
