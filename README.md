# Revenge of the Iron-Blooded Sword Hound

Recovered source, reference, and reconstruction material for the English EPUB project.

## Current source policy

As of **2026-09-16**, the project uses the user-supplied Chinese raws as the primary source of truth. The previously used Korean raws were themselves translated from the Chinese material and are no longer part of the active repository or workflow.

**Current checkpoint: 1 / 500 accepted; next Chapter 2.** Chapter 1 (*Hellhound (1)*) has been rebuilt and QA'd under the Chinese-first workflow.

- `source/chinese/chapters/` — primary text source for the 500-chapter target edition.
- `source/chapters/` — recovered 493-chapter English MTL/XHTML corpus. It is a secondary reference, and the sole text source only when a Chinese raw is unavailable.
- `source/chinese/chapter-exceptions.tsv` — missing/combined raw exceptions and verified nontrivial English-MTL alignments.
- `editorial/SOURCES.md` and `editorial/WORKFLOW.md` — authoritative source and editorial procedures.
- `editorial/chapter-tracker.json` — current 500-chapter tracker.
- `PROJECT_STATE.md` / `PROGRESS.md` — current checkpoint and work log.
- `manuscript/drafts/chapter-0001.md` — accepted Chinese-first Chapter 1 draft.
- `qa/chapter-0001.md` — Chapter 1 source comparison and QA record.

The Chinese corpus contains **492 physical files covering 499 of 500 target chapters**. Chapter **55** is the only confirmed missing Chinese raw and therefore uses the English MTL as its source. Seven physical files contain two target chapters each; they are intentionally retained intact because the raw files do not expose a reliable second-chapter boundary on their own. The English output must nevertheless remain one translated chapter per target chapter.

## Critical numbering rule

Do **not** assume that Chinese target chapter `N` maps to English MTL chapter `N`. The numbering diverges later in the novel. Align English references by title and content before using them. Chapter 55 is explicitly verified as MTL Chapter 55; additional verified exceptions are recorded in `source/chinese/chapter-exceptions.tsv`.

## Editorial quality bar

Every chapter is edited and QA'd individually for semantic fidelity to the Chinese primary source, omissions/additions, names and terminology, title-family continuity, grammar and natural English, paragraph/scene integrity, and project formatting. MTL-only fallback chapters receive the same full editorial pass plus explicit uncertainty review.

Formatting decisions preserved from the prior project include dialogue indentation, no narrative indentation, 1.65 line height, single-quote handling, styled information windows, `◆◆◆` scene breaks, Highbro/Middlebro/Lowbro, and separate side stories. See `editorial/Recovered-Editorial-Decisions.md`.

Historical reconstruction work based on the superseded source policy remains available in Git history but is not accepted production state.
