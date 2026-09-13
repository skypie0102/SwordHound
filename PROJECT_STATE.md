# Recovery and reconstruction checkpoint — 2026-09-14

Recovery has preserved the available source corpus, local EPUB, historical audit, and production context. Reconstruction has begun. Distinguish recovered source bytes from the former repository's edited production state.

## Current reconstruction checkpoint

- **Current source policy:** Korean plus MTL for Chapters 1–54; MTL with supporting-reference QA for 55–493. The user supplied all 54 Korean files and designated Fandom and Namu Wiki for terminology/context checks; further web research is allowed. See [SOURCES.md](editorial/SOURCES.md).

- All 493 chapters have a [new tracker](editorial/chapter-tracker.json); original edited and QA files remain marked not recovered.
- All 2,151 historical audit findings are indexed: 266 have a unique text-and-title match, 40 are ambiguous, and 1,845 are unmatched. Matching does not approve a suggested change.
- Chapter 1 is **editorially accepted**: 106 paragraphs retained, 91 edited, all 116 Korean lines accounted for, and all nine QA items resolved. The [acceptance record](qa/acceptance/chapter-0001.json) binds the exact reviewed text and evidence.
- Final source decisions, explicit age harmonization and source limitations are documented in the [final review](editorial/reviews/chapter-0001-final.md). Desktop/mobile chapter layout was checked and visually inspected. Whole-EPUB packaging and release QA remain pending.
- Chapter 2 is **editorially accepted**: 143 paragraphs retained, 140 edited, all 149 Korean lines accounted for, and all five QA items resolved. See its [final review](editorial/reviews/chapter-0002-final.md) and [acceptance record](qa/acceptance/chapter-0002.json).
- Chapters 3–4 are **editorially accepted**: 258 paragraphs retained, 248 edited, 255 Korean lines accounted for and nine QA items resolved. Their source decisions, final reviews and acceptance evidence are linked from [Chapter 3 QA](qa/chapter-0003.md) and [Chapter 4 QA](qa/chapter-0004.md).
- **Current total: 4 accepted reconstructions; Chapters 5–493 remain unstarted.** No recovered or newly reconstructed chapter is certified as the former finished production version.
- Read [PROGRESS.md](PROGRESS.md) for work completed, validation, and next actions; use [the workflow](editorial/WORKFLOW.md) for future batches.

## Verified recovery

- User-supplied Korean archive `001-054.zip`: all 54 files preserved unchanged, numbered headings checked, archive and member checksums verified. This establishes source availability and byte integrity, not editorial acceptance.

- Original September source corpus: Chapters 001–493, all embedded SHA-256 checksums verified.
- Local July 29 EPUB snapshot: 493 chapters plus cover, CSS, navigation, and front matter, preserved unchanged and extracted under `epub/local-2026-07-29/`.
- Original editorial audit: 2,151 findings concerning a separate, older 500-chapter corrected EPUB. These findings are historical suggestions, not completed edits or a QA pass for the recovered 493-chapter corpus.
- Prior production status reports, including commit identifiers and continuity notes, preserved in `recovery/prior-production-records.json`.

## Last reported production checkpoint (historical; edited files not recovered)

The latest report in **Continue Chapter 54** says `shadowmonarchbooks-cloud/SwordHound` had merged PR #57 and completed translation and QA through Chapter 372. Chapters 373–374, *Poseidon*, were reported complete and validated on `production/chapters-0373-plus`, but PR creation/merge was blocked by account suspension. Chapter 375, *The Hounds of Nouvelle Vague (1)*, was next.

Do not label the recovered MTL XHTML as those finished translations. The old `chapter-XXXX.md` production files, per-chapter QA, continuity YAML, glossaries, source mappings, and validator workflows have not yet been recovered as original files. Do not resume at Chapter 54: that earlier status was explicitly corrected in the conversation.

## Continuity leads from the last reports

- Kirko: Ensign through Chapter 372; Lieutenant promotion pending. This supersedes an earlier report calling her Lieutenant in 367–368.
- Flauros = Second Corpse; Andrealphus = Third; Cimeries = Fourth.
- The 373–374 report describes roughly two years in Nouvelle Vague, the Rainy Season of Fear lasting 150 days/five months, and 98% mortality among living humanity.
- Poseidon: approximately five-meter blue egg-like sphere with underground aura roots; disturbing roots causes explosions, while impacts to the central body feed its growth/brightness.
- Treat these as recovered context to compare against source, not a substitute for the lost edited chapter files.

See `recovery/RECOVERY_REPORT.md` for provenance, limitations, and remaining recovery leads.
