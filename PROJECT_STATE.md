# Project State

**Checkpoint:** 2026-09-16  
**Target edition:** 500 chapters  
**Accepted:** 3  
**Staged:** 0  
**Next chapter:** 4

## Current accepted checkpoint

The first restarted title-family batch has completed under the full restored workflow:

- **Chapter 1 — Hellhound (1)**
- **Chapter 2 — Hellhound (2)**
- **Chapter 3 — Hellhound (3)**

Family QA: `qa/families/hellhound-0001-0003.md` — **PASS**.

These chapters were rebuilt from the Chinese raws as semantic/narrative authority, independently aligned to recovered English references by content, checked against the designated English Fandom wiki for applicable canonical English names/terms, reviewed individually, and then reviewed as one contiguous title family.

The older pre-restart Chapter 1 acceptance remains superseded in Git history and is not current evidence.

## Next verified title family

The next batch boundary has already been determined so the following session does not need to rediscover it:

- **Chapters 4–7 — The Baskerville Dog (1)–(4)**
- Chinese Chapters 4–7 remain the same title family despite small wording variation between “dog” and “hounds.”
- Recovered English Chapters 4–7 consistently title the family *The Baskerville Dog (1)–(4)*.
- **Chapter 8 changes to Hounds of Hell (1)**, proving the boundary.

The next target is therefore **Chapter 4**, with Chapters **4–7** to be processed as one editorial/QA batch.

## Mandatory continuation record

`HANDOFF.md` is the operational handoff file for every work session.

Every agent/session must:

- read `HANDOFF.md` before beginning editorial work;
- reconcile it with this file, `PROGRESS.md`, `editorial/chapter-tracker.json`, and accepted QA/provenance evidence;
- update it after meaningful progress and **always before ending a session or handing work to another agent**;
- record the exact next chapter/title-family action, in-progress work, source alignment, canonical-wiki checks, decisions, blockers, branch/PR state, and files created or changed.

If `HANDOFF.md` disagrees with accepted tracker/provenance evidence, accepted evidence wins and the handoff must be corrected immediately.

## Source authority

### Semantic / narrative authority

Chinese is primary for the 500-chapter target edition.

- Physical Chinese files: **492**
- Target chapters covered by Chinese: **499 / 500**
- Confirmed missing Chinese chapter: **55**
- Combined two-chapter source containers: **7**
- Recovered English MTL/XHTML corpus: **493 chapters**, secondary/reference source only except Chapter 55

### Canonical English terminology authority

The English *Revenge of the Iron-Blooded Sword Hound* Fandom wiki is the canonical English reference for identified names, terms, locations, ranks, skills, monsters, organizations, titles, and other proper nouns where an applicable entry exists. It does not override Chinese narrative meaning or reveal chronology.

## Accepted early terminology decisions

Current accepted scope from Chapters 1–3 includes:

- **Vikir Van Baskerville**
- **Hugo Le Baskerville**
- **Marquis** for Hugo, with Chinese Chapter 1’s `伯爵` conflict documented
- **Baskerville Clan** / **Iron-Blooded Sword Clan**
- **Le/La/Van** naming distinction
- **Cradle of Swords**
- **River Styx**
- **Seven Great Families** in Chapter 2 context
- **1 Circle** wording for Vikir’s age-15 retrospective in Chapter 3
- **Bloody Mamba** only as a scoped recovered-English fallback; current Fandom retrieval does not expose a dedicated formal species entry

See `editorial/GLOSSARY.md` and the chapter provenance/QA records for evidence and limits.

## Combined-source exceptions

| Raw file | Target chapters |
| --- | --- |
| `075.txt` | 75–76 |
| `267.txt` | 267–268 |
| `284.txt` | 284–285 |
| `351.txt` | 351–352 |
| `353.txt` | 353–354 |
| `385.txt` | 385–386 |
| `495.txt` | 495–496 |

The combined raws remain intact because none exposes a sufficiently reliable second heading/boundary to justify destructive splitting from the raw alone. Translation outputs must still be split into individual target chapters.

## Missing Chapter 55

`055.txt` is genuinely absent. Recovered English MTL Chapter 55 is the verified fallback source and still requires full editing, canonical terminology verification, neighboring-continuity review, uncertainty review, and normal QA.

## Numbering warning

The Chinese target numbering and 493-chapter English MTL numbering diverge later. Same-number lookup is prohibited unless verified by title/content. Known nontrivial mappings are documented in `source/chinese/chapter-exceptions.tsv`.

## Immediate next action

Continue with **The Baskerville Dog (1)–(4), Chapters 4–7** under `editorial/WORKFLOW.md` and `HANDOFF.md`. Do not stop after that family merely because it is merged; immediately determine and begin the Chapter-8 family unless an explicit stopping condition applies.
