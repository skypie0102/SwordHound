# Reconstruction Progress

## 2026-09-16 — Chapter 1 accepted under Chinese-first workflow

**Current state:** 1 / 500 accepted; 0 staged; next Chapter 2.

Chapter 1, **Hellhound (1)**, was rebuilt from `source/chinese/chapters/001.txt`. Recovered English MTL Chapter 1 was independently aligned by title, opening/closing events, named entities, and scene sequence and used only as a secondary reference.

QA restored or corrected several items that the English MTL had lost or materially altered, including:

- the execution placard naming Vikir and charging him with colluding with demons;
- humanity’s victory being carved into stone;
- Vikir’s explicit wish to **live again**;
- the broken birth-celebration sentence;
- the Cradle/Styx mechanics and mother’s-milk comparison;
- Hugo asking when the children will be strong enough to fight the Demon Realm and watch his back;
- the final “young master is drinking the water” line; and
- Hugo’s open-mouthed shock rather than the MTL’s grin.

Chapter 2 was checked for boundary continuity. Its replay of the nursery and Cradle sequence is intentional in the Chinese source because it shifts into Vikir’s internal perspective; it must not be deduplicated.

Evidence: `manuscript/drafts/chapter-0001.md`, `qa/chapter-0001.md`, `qa/acceptance/chapter-0001.json`, and `editorial/provenance/chapter-0001.json`.

## 2026-09-16 — Chinese-source reset

The active reconstruction was reset to **Chapter 1**.

Reason: the user supplied the Chinese raws from which the previously used Korean raws had been translated. Chinese is therefore now the primary source of truth and the Korean source path has been retired from the repository and workflow.

Corpus audit:

- 492 physical Chinese chapter files cover 499 target chapters.
- Chapter 55 is the only confirmed missing Chinese raw and will use the recovered English MTL Chapter 55 as its sole text source.
- Seven Chinese files are combined two-chapter containers: 075→75–76, 267→267–268, 284→284–285, 351→351–352, 353→353–354, 385→385–386, and 495→495–496.
- Those seven combined raws do not expose a reliable second-chapter heading/boundary, so they remain intact. Their translated output must still be divided into two independently edited and QA’d chapters.
- English MTL numbering is not globally aligned with the Chinese 500-chapter target. Every secondary-source lookup must be aligned by title/content rather than chapter number alone.

All prior generated drafts, QA acceptances, staging/provenance records, and Korean alignment artifacts are superseded by this reset. They remain available in Git history for audit only.

See `PROJECT_STATE.md`, `editorial/SOURCES.md`, `editorial/WORKFLOW.md`, and `source/chinese/chapter-exceptions.tsv`.
