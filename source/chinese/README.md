# Chinese Raw Corpus

This directory is the primary semantic source corpus for the 500-target reconstruction.

## Coverage audit

- Target chapters: **1–500**
- Physical `.txt` files: **492**
- Target chapters with at least partial Chinese text: **500**
- Standalone `055.txt`: **absent**
- Chapter 55 status: **partial overlap inside `054.txt`, not English-only**
- Multi-target/overlap physical containers currently documented: **8**

The authoritative exception table is `chapter-exceptions.tsv`.

### Chapter 54 / 55 overlap

A later boundary audit superseded the original assumption that Chapter 55 was completely missing.

Physical `054.txt` contains:
- target 54 body, with a short target-54 closing exchange missing from Chinese and restored from aligned E54;
- then most of target 55 appended without a Chapter-55 heading.

For target 55:
- E55 supplies the missing opening/title boundary;
- Chinese `054.txt` controls semantics for the overlapping body.

Do not treat Chapter 55 as an MTL-only chapter.

## Multi-target / overlapping containers

| File | Covers | Notes |
| --- | --- | --- |
| `054.txt` | 54 + most of 55 | overlap/splice; E54/E55 repair only documented missing boundaries |
| `075.txt` | 75 + 76 | shared container |
| `267.txt` | 267 + 268 | shared container with localized gap |
| `284.txt` | 284 + 285 | shared container with localized gap |
| `351.txt` | 351 + 352 | shared container |
| `353.txt` | 353 + 354 | embedded Chapter-354 boundary |
| `385.txt` | 385 + 386 | embedded Chapter-386 boundary plus localized closing gap |
| `495.txt` | 495 + 496 | main ending plus Side Story 1 |

Do not physically split a source file merely to make filenames sequential. Use the exact boundary evidence documented in `chapter-exceptions.tsv`, chapter QA, and provenance. Reconstructed English still emits one file per target chapter with no gap or overlap.

## Localized source gaps

Known localized Chinese omissions/splices include targets 49, 54/55, 170, 267, 284, and 385, plus any later entries recorded in `chapter-exceptions.tsv`. Use aligned English only for the explicitly missing material; Chinese remains primary elsewhere.

## English reference warning

The recovered English MTL has 493 chapters and numbering diverges from the 500-target edition. Do not use same-number lookup as a general rule. Align by title, opening/closing events, entities, and scene sequence. See `chapter-exceptions.tsv` and `editorial/SOURCES.md`.
