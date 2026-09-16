# Project State

**Checkpoint:** 2026-09-16  
**Target edition:** 500 chapters  
**Accepted:** 7  
**Staged:** 0  
**Next chapter:** 8

## Current accepted checkpoint

Two complete title families have now passed the restarted Chinese-semantic/Fandom-canonical workflow:

- **Chapters 1–3 — Hellhound (1)–(3)**
- **Chapters 4–7 — The Baskerville Dog (1)–(4)**

Family QA:

- `qa/families/hellhound-0001-0003.md` — **PASS**
- `qa/families/baskerville-dog-0004-0007.md` — **PASS**

Each accepted chapter has a fresh Chinese-first draft, chapter QA, provenance record, and hash-bound acceptance record. Recovered English MTL chapters are used only after title/content alignment and never override Chinese narrative meaning.

The older pre-restart Chapter 1 acceptance remains superseded in Git history and is not current evidence.

## Next title family

Chapter 8 begins **Hounds of Hell (1)**.

The **start** of the next family is verified, but its full contiguous end boundary has **not yet been established**. The next session must inspect Chinese headings from Chapter 8 onward until the base title changes, then verify the corresponding English-reference sequence before accepting any chapter in that family.

## Mandatory continuation record

`HANDOFF.md` is the operational handoff file for every work session. Read and reconcile it with this file, `PROGRESS.md`, `editorial/chapter-tracker.json`, and accepted QA/provenance evidence before editing.

Update `HANDOFF.md` after meaningful progress and always before ending or handing off a session. If the handoff conflicts with hash-bound accepted evidence, the accepted evidence wins and the handoff must be corrected.

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

## Newly accepted Chapters 4–7 terminology

The Baskerville Dog family revalidated and accepted:

- **Sword Beginner**
- **Sword Expert**
- **Sword Graduator**
- **Sword Master**
- **Low / Mid / High** rank substages where source-supported
- **Highbro Le Baskerville**
- **Middlebro Le Baskerville**
- **Lowbro Le Baskerville**
- **John Barrymore** — Head Butler
- **Morgue Clan**
- **Red Fang Mountain**
- **Rok Empire** / Seven Great Clans context
- **Bloody Beans**

The child-rearing/nursery castle remains descriptively rendered. Current canonical evidence does not justify treating the recovered MTL label **Fang Castle** as an established proper name.

## Key Chapters 4–7 editorial decisions

- Chinese Chapter 4 defines the sword-rank system; previous-life Vikir reached High Sword Expert at **sixteen**, correcting the MTL’s corrupted age-ten line.
- Chapter 5 retains the full ten-minute suffocation attempt, severed finger, broken teeth/nose/jaw, urine, blood, and death-game threat without sanitization.
- Chapter 6 removes recovered-English `Advertisement` contamination, canonicalizes Morgue Clan and Red Fang Mountain, and preserves Hugo asking **how many died** after hearing of the children’s fight.
- Chapter 7 preserves Hugo’s implied fratricide, the destroyed-family survivor/nun forgiveness anecdote, the under-fifteen haggis/offal diet, and the concentrated Bloody Beans sequence.

See `editorial/GLOSSARY.md`, `qa/chapter-0004.md` through `qa/chapter-0007.md`, and the corresponding provenance records for scope and evidence.

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

Determine the complete contiguous **Hounds of Hell** family beginning at Chapter 8, verify its target↔MTL mappings and canonical terminology, then reconstruct the whole family before continuing onward. A successful family merge is a checkpoint, not a stopping condition.
