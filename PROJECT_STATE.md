# Project State

**Checkpoint:** 2026-09-16  
**Target edition:** 500 chapters  
**Accepted:** 11  
**Staged:** 0  
**Next chapter:** 12

## Current accepted checkpoint

Three complete title families have passed the restarted Chinese-semantic/Fandom-canonical workflow:

- **Chapters 1–3 — Hellhound (1)–(3)**
- **Chapters 4–7 — The Baskerville Dog (1)–(4)**
- **Chapters 8–11 — Hounds of Hell (1)–(4)**

Family QA:

- `qa/families/hellhound-0001-0003.md` — **PASS**
- `qa/families/baskerville-dog-0004-0007.md` — **PASS**
- `qa/families/hounds-of-hell-0008-0011.md` — **PASS**

Every accepted chapter has a fresh Chinese-first draft, chapter QA, provenance record, and hash-bound acceptance record. Recovered English MTL/XHTML is used only after title/content alignment and never overrides Chinese narrative meaning.

## Next verified title family

The next batch is already bounded:

- **Chapter 12 — The Gluttonous Flies (1)**
- **Chapter 13 — The Gluttonous Flies (2)**
- **Chapter 14 changes to `独食 (1)`**, proving the 12–13 boundary.

Recovered English Chapters 12 and 13 also carry *The Gluttonous Flies (1)–(2)* titles. Their content alignment still needs the normal full-source verification during the next batch; same-number mapping is not accepted merely from numbering.

## Mandatory continuation record

`HANDOFF.md` is the operational handoff file for every session. Read and reconcile it with this file, `PROGRESS.md`, `editorial/chapter-tracker.json`, `editorial/reconstruction-status.json`, and accepted QA/provenance evidence before editing.

Update `HANDOFF.md` after meaningful progress and always before ending or handing off a session. If the handoff conflicts with hash-bound accepted evidence, accepted evidence wins and the handoff must be corrected.

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

During the Hounds of Hell family, principal applicable Fandom evidence was retrieved earlier in the research pass. A later refresh attempt was blocked by Fandom robots rules; that limitation is recorded in chapter QA/provenance, and no fresh canonical claim was invented from the failed refresh.

## Accepted terminology through Chapter 11

In addition to previously accepted terms, Chapters 8–11 revalidate/promote:

- **Le Rouge et Le Noir Mountain**
- **Guide Dog**
- **Pavlov Van Baskerville**
- **Brown Rat ‘Norvegicus’**
- **Hellhound** — Danger Rating B+, 3 m, 2nd Ridge
- **Cerberus** — Danger Rating A+, 7 m, 7th Ridge
- **Hell’s Watchdog**
- **Camus Morgue** / **Ironblood Empress** within the source’s future-war retrospective
- **Baskerville 1st / 2nd / 3rd Form**, with first-life mastery through the 4th Form
- Sword/mage equivalence: Low/Mid/High Sword Expert = 1st/2nd/3rd Circle; Low/Mid/High Sword Graduator = 4th/5th/6th Circle; Sword Master = 7th Circle

**Bloody Mamba** remains a scoped recovered-English fallback rather than a newly claimed direct Fandom canonicalization.

## Key Chapters 8–11 editorial decisions

- Chapter 8 restores the full practical-exam scoring rubric, Guide Dog supervision, and the complete **Le Rouge et Le Noir Mountain** setting.
- Chapter 9 keeps the Brown Rat and Hellhound information windows complete and atomic; the Hellhound entry includes B+, 3 m, **2nd Ridge**, its descriptive epithet, fatal-bite warning, and sulfuric-fire description.
- Chapter 10 corrects the MTL’s `height` error to **kidneys**, preserves the full chocolate-poison symptoms, keeps post-kill strengthening non-numerical, and ends on the complete Cerberus window.
- Chapter 11 normalizes the sword/mage rank table and Baskerville Forms, preserves Vikir’s broken ribs and shattered shortsword, restores the **Cradle of Needles**, and ends with Cerberus collapsing after exactly seven steps from the Bloody Mamba venom.
- Cerberus is rendered as the **pinnacle of underworld-type monsters**, following Chinese rather than the MTL’s generic canine-classification drift.

See `editorial/GLOSSARY.md`, `qa/chapter-0008.md` through `qa/chapter-0011.md`, and the corresponding provenance records for evidence and limits.

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

The combined raws remain intact unless new evidence establishes a defensible source boundary. English output must still be split into individual target chapters with no gap or duplicated overlap.

## Missing Chapter 55

`055.txt` is genuinely absent. Recovered English MTL Chapter 55 is the verified fallback source and still requires full editing, canonical terminology verification, neighboring-continuity review, uncertainty review, and normal QA.

## Numbering warning

Chinese target numbering and the 493-chapter English MTL sequence diverge later. Never assume target `N` maps to MTL `N` unless verified by title/content. Known nontrivial mappings are recorded in `source/chinese/chapter-exceptions.tsv`.

## Immediate next action

Process **The Gluttonous Flies (1)–(2), Chapters 12–13** as one title-family batch. Read both Chinese raws completely, verify MTL alignment by content, re-check canonical terminology, run chapter + family QA, accept/merge if clean, then immediately determine and begin the Chapter 14 family. A successful family merge is a checkpoint, not a stopping condition.
