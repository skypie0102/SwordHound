# Source Policy

## Authority order

Effective **2026-09-16**, the reconstruction uses this authority order:

1. `source/chinese/chapters/` — **primary source** for the 500-chapter target edition.
2. `source/chapters/` plus `source/chapter-index.tsv` — recovered 493-chapter English MTL/XHTML corpus; **secondary reference** only.
3. `editorial/GLOSSARY.md`, recovered editorial decisions, and accepted neighboring chapters — consistency/style references.

The previously used Korean raw corpus is retired and must not be used in active translation, editorial decisions, title resolution, QA, or alignment.

## Why Chinese is primary

The Korean files previously present in the repository were translations made from the Chinese raws. Using the Chinese layer removes an intermediate translation and therefore provides the closer available text for source-faithful reconstruction.

## Chinese corpus coverage

The target is Chapters 1–500. There are 492 physical Chinese files, covering 499 target chapters because seven files each contain two chapters.

See `source/chinese/chapter-exceptions.tsv` for machine-readable exceptions and `source/chinese/README.md` for the audit.

### Missing source

Chapter 55 has no Chinese raw. For that chapter only, the recovered English MTL Chapter 55 is the sole text source. It requires full editorial QA and explicit uncertainty review.

### Combined source files

The following source containers are combined and currently remain intact: `075.txt` → 75–76; `267.txt` → 267–268; `284.txt` → 284–285; `351.txt` → 351–352; `353.txt` → 353–354; `385.txt` → 385–386; `495.txt` → 495–496.

An audit found no reliable explicit second-chapter marker in those files. Do not introduce an arbitrary raw split. Establish the translation boundary with source sequence plus verified English title/content alignment; then emit two separate translated chapters.

## English MTL alignment

The English corpus has 493 chapters while the target Chinese edition has 500. Numbering therefore diverges.

- Never assume target Chapter N equals English MTL Chapter N.
- Match by title family, opening/closing events, named entities, and scene sequence.
- A mapping is not considered verified merely because numbers happen to match.
- Record verified exceptional/nontrivial mappings in `source/chinese/chapter-exceptions.tsv`.
- Chapter 55 → MTL 55 is verified.
- Target 75 → MTL 74 and target 76 → MTL 75 are verified by title/content.
- Target 267 → MTL 265 and target 268 → MTL 266 are verified by title/content.

## Archived/reference material

The recovered original English source archive and local EPUB snapshots remain reference/recovery artifacts. They do not outrank the Chinese primary source and do not certify translation quality. Historical editorial-audit material may help identify English prose issues, but it was produced against an older/different edition and must never be auto-applied to the new Chinese-first reconstruction.
