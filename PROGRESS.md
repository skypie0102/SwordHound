# Reconstruction Progress

## 2026-09-16 — Hellhound (1)–(3) accepted under restarted workflow

**Current state:** 3 / 500 accepted; 0 staged; next Chapter 4.

Completed the first full contiguous title-family batch after the deliberate restart:

- Chapter 1 — *Hellhound (1)*
- Chapter 2 — *Hellhound (2)*
- Chapter 3 — *Hellhound (3)*

The family boundary was verified from Chinese headings before acceptance; Chapter 4 changes base title. English MTL Chapters 1–3 were independently verified by title, opening, scene order, distinctive content, and endpoint rather than same-number assumption.

Current canonical-reference checks established/scoped:

- Vikir Van Baskerville
- Hugo Le Baskerville
- Marquis, with Chinese Chapter 1’s `伯爵` conflict documented
- Baskerville Clan / Iron-Blooded Sword Clan
- Le/La/Van naming distinction
- Cradle of Swords
- River Styx
- Seven Great Families in Chapter 2 context
- 1 Circle terminology in Chapter 3 retrospective
- Bloody Mamba retained only as a documented recovered-English fallback because current Fandom retrieval has no dedicated formal species entry

Important corrections include restoration of Chapter 1’s execution placard and “live again” wish, source-faithful Hugo dialogue, Chapter 2’s rabbit/hound proverb and full Styx mechanics, and Chapter 3’s nursing favoritism, explicit snake-death details, and removal of MTL-only Le Rogue/Fang Castle assertions not supported by the Chinese/current Fandom evidence.

Family QA: `qa/families/hellhound-0001-0003.md` — PASS.

The next family boundary has already been verified:

- **Chapters 4–7 — The Baskerville Dog (1)–(4)**
- Chapter 8 changes to **Hounds of Hell (1)**.

Per the continuous-processing rule, work proceeds directly into Chapters 4–7 rather than stopping at this checkpoint.

## 2026-09-16 — Full restart from Chapter 1 with mandatory handoff

The project was restarted from the beginning again after recovering established workflow rules that had been unintentionally dropped during the Chinese-source migration.

Restored rules:

- Chinese raws are the semantic/narrative authority.
- The English Fandom wiki is the canonical English reference for established names, terms, locations, ranks, skills, monsters, organizations, titles, and other proper nouns.
- Chapters are processed as complete contiguous title-family batches.
- Finishing a chapter, title family, or PR is a checkpoint, **not** a reason to stop; work continues across subsequent title families until the user pauses it, the corpus ends, or a genuine blocker prevents safe progress.
- Source explicitness is not sanitized.
- Editorial/source QA comes before final EPUB presentation QA.
- GitHub-hosted runners remain a last resort.

The previous pre-restart Chapter 1 acceptance was invalidated. Its old work remains in Git history only and may be consulted as a non-authoritative lead.

A root-level `HANDOFF.md` is the mandatory cross-session operational record. Every session must read it first and update it before ending or handing off work.

## 2026-09-16 — Chinese-source migration

The active reconstruction was originally reset to Chapter 1 after the user supplied the Chinese raws from which the previously used Korean raws had been translated.

Corpus audit retained from that migration:

- 492 physical Chinese chapter files cover 499 target chapters.
- Chapter 55 is the only confirmed missing Chinese raw and uses recovered English MTL Chapter 55 as fallback text source.
- Seven Chinese files are combined two-chapter containers: 075→75–76, 267→267–268, 284→284–285, 351→351–352, 353→353–354, 385→385–386, and 495→495–496.
- Those seven combined raws remain intact because no defensible second-chapter marker was found in the raw alone; translated output must still be split by target chapter.
- English MTL numbering is not globally aligned with the Chinese 500-chapter target. Every secondary-source lookup must be aligned by title/content rather than chapter number alone.

See `HANDOFF.md`, `PROJECT_STATE.md`, `AGENTS.md`, `editorial/SOURCES.md`, `editorial/WORKFLOW.md`, and `source/chinese/chapter-exceptions.tsv`.
