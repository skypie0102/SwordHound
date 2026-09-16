# Project State

**Checkpoint:** 2026-09-16  
**Target edition:** 500 chapters  
**Accepted:** 13  
**Staged:** 0  
**Next chapter:** 14

## Current accepted checkpoint

Four complete title families have passed the restarted Chinese-semantic/Fandom-canonical workflow:

- **Chapters 1–3 — Hellhound (1)–(3)**
- **Chapters 4–7 — The Baskerville Dog (1)–(4)**
- **Chapters 8–11 — Hounds of Hell (1)–(4)**
- **Chapters 12–13 — The Gluttonous Flies (1)–(2)**

Family QA:

- `qa/families/hellhound-0001-0003.md` — **PASS**
- `qa/families/baskerville-dog-0004-0007.md` — **PASS**
- `qa/families/hounds-of-hell-0008-0011.md` — **PASS**
- `qa/families/gluttonous-flies-0012-0013.md` — **PASS**

Every accepted chapter has a Chinese-first draft, chapter QA, provenance, and hash-bound acceptance record. Recovered English MTL/XHTML is used only after title/content alignment and never overrides Chinese narrative meaning.

## Chapter 11 canonical terminology correction

After the Hounds of Hell merge, stronger current Fandom evidence established that the numbered Baskerville sword techniques are canonically **Fangs**, not the earlier project fallback **Forms**.

Chapter 11 was reopened for terminology only and rebound through draft, chapter QA, family QA, provenance, acceptance, and tracker evidence. Source semantics and fight mechanics were unchanged.

Use **Baskerville Fang Sword Style** / **1st Fang, 2nd Fang, 3rd Fang...** going forward.

## Newly accepted Chapters 12–13

The Gluttonous Flies family revalidated/promoted:

- **Cain Baskerville**
- **Abel Baskerville**
- **Red Fang Mountain** in the dungeon geography
- **Beelzebub**
- **The Fly of Gluttony**
- **Seven Calamities**
- **Hemorrhage — Hellhound (B+)**
- **Incinerate — Cerberus (A+)**
- **Rapid Regeneration — Brown Rat Norvegicus (F)**
- canonical **Baskerville Fangs** through the 9th/10th-Fang discussion

Key editorial decisions:

- Chapter 12 corrects the recovered English from **two skeletons** to the Chinese source’s **one skeleton**. Cain is the surviving note writer; Abel is the dead younger twin.
- The dungeon riddle resolves through **shadow**: one in darkness → body + shadow under ruby light → one again after the ruby is destroyed.
- Chapter 12 intentionally stops at the relic-name recognition point; Chapter 13 repeats/completes the Beelzebub inscription as the source does.
- Chapter 13 excludes a large recovered-English-only block about Beelzebub’s custody by the family, later theft by demons, battlefield ownership, and explicit fusion into Vikir’s hand because that exposition is **absent from Chinese Chapter 13**.
- Beelzebub’s two ability windows use the canonical slot names **Hemorrhage / Incinerate / Rapid Regeneration**.
- Vikir’s Chapter 13 self-assessment is normalized to roughly Fourth-Circle mana quantity while practical sword output remains around **High Sword Expert**, perhaps nearing **Low Sword Graduator**.
- Chapter 13 ends before the practical-exam result/report sequence; Chinese Chapter 14 begins after the examination has ended.

## Next title family

Chapter 14 begins Chinese `独食 (1)` / recovered English **Solitary (1)**.

The full contiguous Solitary-family boundary must be verified before acceptance. Do not assume how many parts it contains from numbering alone.

## Mandatory continuation record

`HANDOFF.md` is the operational handoff file for every work session. Read and reconcile it with this file, `PROGRESS.md`, `editorial/chapter-tracker.json`, `editorial/reconstruction-status.json`, and accepted QA/provenance evidence before editing.

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

The English *Revenge of the Iron-Blooded Sword Hound* Fandom wiki is the canonical English reference for identified names, terms, locations, ranks, skills, monsters, organizations, titles, and other proper nouns where applicable. It does not override Chinese narrative meaning or reveal chronology.

Direct Fandom pages may be intermittently blocked by robots rules. Current indexed Fandom search results may be used as canonical evidence when clearly identified as indexed retrieval; do not falsely claim a blocked direct-page refresh succeeded.

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

Determine the complete contiguous **Solitary** title family beginning at Chapter 14, verify target↔MTL mappings and canonical terminology, reconstruct the whole family, QA/accept it if clean, then continue onward. A successful PR merge is a checkpoint, not a stopping condition.
