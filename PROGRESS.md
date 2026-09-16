# Reconstruction Progress

## 2026-09-16 — Chinese-source reset

The active reconstruction has been reset to **Chapter 1**.

**Current state:** 0 / 500 accepted; 0 staged; next Chapter 1.

Reason: the user supplied the Chinese raws from which the previously used Korean raws had been translated. Chinese is therefore now the primary source of truth and the Korean source path has been retired from the repository and workflow.

Corpus audit:

- 492 physical Chinese chapter files cover 499 target chapters.
- Chapter 55 is the only confirmed missing Chinese raw and will use the recovered English MTL Chapter 55 as its sole text source.
- Seven Chinese files are combined two-chapter containers: 075→75–76, 267→267–268, 284→284–285, 351→351–352, 353→353–354, 385→385–386, and 495→495–496.
- Those seven combined raws do not expose a reliable second-chapter heading/boundary, so they remain intact. Their translated output must still be divided into two independently edited and QA'd chapters.
- English MTL numbering is not globally aligned with the Chinese 500-chapter target. Every secondary-source lookup must be aligned by title/content rather than chapter number alone.

All prior generated drafts, QA acceptances, staging/provenance records, and Korean alignment artifacts are superseded by this reset. They remain available in Git history for audit only.

See `PROJECT_STATE.md`, `editorial/SOURCES.md`, `editorial/WORKFLOW.md`, and `source/chinese/chapter-exceptions.tsv`.
