# Project State

**Checkpoint:** 2026-09-17  
**Target edition:** 500 chapters  
**Accepted:** 19  
**Staged:** 0  
**Next chapter:** 20

## Current accepted checkpoint

Six complete title families have passed the restarted Chinese-semantic/Fandom-canonical workflow:

- **Chapters 1–3 — Hellhound (1)–(3)**
- **Chapters 4–7 — The Baskerville Dog (1)–(4)**
- **Chapters 8–11 — Hounds of Hell (1)–(4)**
- **Chapters 12–13 — The Gluttonous Flies (1)–(2)**
- **Chapters 14–17 — Solitary (1)–(4)**
- **Chapters 18–19 — Bared Teeth (1)–(2)**

Latest family QA: `qa/families/bared-teeth-0018-0019.md` — **PASS**.

Every accepted chapter has a Chinese-first draft, chapter QA, provenance, and hash-bound acceptance record. Recovered English MTL/XHTML is used only after title/content alignment and never overrides Chinese narrative meaning.

## Bared Teeth family decisions

- Target 18→MTL 18 and 19→MTL 19 are verified by complete content, not numbering alone.
- Chapter 18 rebuilds the **Orc** window as Danger Rating **C**, 2 m, Le Rouge et Le Noir Mountain lowlands, with canonical **High-Speed Regeneration**.
- Chapter 19 rebuilds the **Troll** window as Danger Rating **C+**, 4 m, Le Rouge et Le Noir Mountain 2nd Ridge, with canonical **Superspeed Regeneration**.
- Chapter 18's isolated Chinese phrase calling Vikir a fifteen-year-old conflicts with the repeated age-eight chronology. It is documented and resolved as comparison with the normal age-fifteen **Low Sword Expert / 1st Fang** milestone.
- Vikir deliberately reveals only **Low Sword Expert / 1st Fang** in Chapter 18 and **Mid Sword Expert / 2nd Fang** in Chapter 19. His accepted hidden state remains **Low Sword Graduator** from Chapter 17.
- Chapter 19 does **not** import the Troll-derived Beelzebub Slot 3 replacement early; Chinese Chapter 20 is where that update is actually revealed.
- Fandom pages conflict on some early Fang descriptive names. The dedicated `Baskerville Clan/Swordsmanship` progression is used for Fang/rank mapping and the conflict is documented.

## Next verified title family

- **Chapters 20–25 — Camus Morgue (1)–(6)**
- Chinese Chapter 26 changes to `毕业生 (graduater) (1)`.
- Recovered English Chapter 26 changes to **The Graduate (1)**.

The six-part 20–25 boundary is verified from both corpora. Full target↔MTL content alignment and canonical checks must still be completed before acceptance.

## Mandatory continuation record

`HANDOFF.md` is the operational handoff file for every work session. Read and reconcile it with this file, `PROGRESS.md`, `editorial/chapter-tracker.json`, `editorial/reconstruction-status.json`, and accepted QA/provenance evidence before editing.

Update `HANDOFF.md` after meaningful progress and always before ending or handing off a session. If the handoff conflicts with hash-bound accepted evidence, accepted evidence wins and the handoff must be corrected.

## Source authority

Chinese is primary for narrative/semantic content. The English *Revenge of the Iron-Blooded Sword Hound* Fandom wiki is the canonical English reference for identified names, terms, locations, ranks, skills, monsters, organizations, titles, and other proper nouns where applicable. It does not override Chinese narrative meaning or reveal chronology.

Corpus constants:

- Physical Chinese files: **492**
- Target chapters covered by Chinese: **499 / 500**
- Confirmed missing Chinese chapter: **55**
- Combined two-chapter source containers: **7**
- Recovered English MTL/XHTML corpus: **493 chapters**, secondary/reference source only except Chapter 55

Direct Fandom pages can be intermittently blocked by robots rules. Clearly identified indexed Fandom retrieval may be used as canonical evidence; never claim a blocked direct refresh succeeded.

## Persistent exceptions

Combined raw containers remain intact: `075.txt`→75–76, `267.txt`→267–268, `284.txt`→284–285, `351.txt`→351–352, `353.txt`→353–354, `385.txt`→385–386, `495.txt`→495–496.

Chapter 55 Chinese raw is genuinely missing; verified recovered English MTL 55 is the fallback source and still requires full editorial/QA treatment.

## Immediate next action

Merge the clean **Bared Teeth (1)–(2), Chapters 18–19** checkpoint, then process **Camus Morgue (1)–(6), Chapters 20–25** as one title-family batch. Read Chinese 20–25 completely, use Chapter 26 as the boundary witness, independently align English references 20–25 by content, canonicalize applicable terms, reconstruct and QA the full family, accept/merge if clean, then continue onward without stopping at the PR.
