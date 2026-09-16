# SwordHound Session Handoff

> **Mandatory:** Read this file before beginning editorial work. Update it after meaningful checkpoints and always before ending a session or handing work to another agent.

## Handoff metadata

- **Last updated:** 2026-09-17
- **Updated by:** ChatGPT — Bared Teeth source/alignment checkpoint
- **Working branch:** `editorial/restart-bared-teeth-family`
- **Base main checkpoint:** `fc4620c6134c9230eb6fe1047949021fa3c98b9b` (PR #11 merged)
- **Current PR:** not yet created
- **Blocking issue:** none

## Authoritative current checkpoint

- **Target edition:** 500 chapters
- **Accepted:** **17**
- **Staged:** **0**
- **Next chapter:** **18**
- **Active family:** **Chapters 18–19 — Bared Teeth (1)–(2)**
- **Family boundary:** **VERIFIED**. Chapter 20 changes to **Camus Morgue (1)**.
- **Latest accepted family:** Chapters 14–17 — *Solitary (1)–(4)* — family QA PASS.

## Rules that must not be lost

- Chinese raw = semantic/narrative authority.
- English Fandom wiki = canonical English authority for identified names/terms/locations/ranks/skills/monsters/organizations/titles where applicable.
- English MTL/XHTML = secondary alignment/phrasing witness only except Chapter 55.
- Do not sanitize or soften source content.
- Do not import MTL/wiki narrative exposition absent from Chinese.
- Process complete contiguous title families; chapter/family/PR completion is a checkpoint, not a stopping condition.
- Never assume target N == MTL N without title/content verification.
- Protect reveal chronology.
- Keep information windows atomic.
- Numbered Baskerville techniques are **Fangs**, not Forms.

## Current family — Chapters 18–19: Bared Teeth

### Boundary and source SHAs

Chinese:
- `018.txt` — `显露的獠牙 (1)` — `7c313862e83ae30acfd9270ae5e0972d82eecf65`
- `019.txt` — `显露獠牙 (2)` — `bc88dc2708487354d9ff29ca8978252e8001d572`
- boundary witness `020.txt` — `米尔格·卡米耶 (1)` — `b4b2011e2c0ab569f7ee420c05608498970d2dd8`

Recovered English:
- target 18 → MTL 18 — `5d58111d3a188ea82343910782f38dc22da8caea` — **verified by full content**
- target 19 → MTL 19 — `bdaa1abc7dfe521570a9998c43099c576da16d37` — **verified by full content**
- Chapter 20 title witness — `5706f9f22b35d53b4e58208c3e24c04f59e40632`

Alignment evidence:
- 17→18: Vikir leaves the burned scripture/library and is immediately summoned by Hugo.
- Ch. 18: Hugo asks what Vikir learned; training-ground test; C-rank Orc; Vikir reveals gaseous aura/1st Fang; asks for a larger opponent.
- Ch. 19: C+ Troll; Vikir first uses 1st Fang, then deliberately reveals 2nd Fang / Mid Sword Expert to sever the neck.
- 19→20: Chapter 20 explicitly records the public state as **2nd Fang / Mid Sword Expert** and the real hidden state as **Low Sword Graduator / 4th Fang**, then begins the Camus Morgue family.

### Current canonical evidence

Current indexed Fandom evidence establishes:
- **Orc** — Danger Rating **C**, **2 m**, humanoid demonic creature; **High-Speed Regeneration**.
- **Troll** — Danger Rating **C+**; canonical skill **Superspeed Regeneration**.
- **Le Rouge et Le Noir Mountain** remains the canonical mountain name.
- Dedicated `Baskerville Clan/Swordsmanship` page maps **1st Fang = Stabbing Fang = Low Sword Expert** and **2nd Fang = Mid Sword Expert**.
- A separate Fandom `Martial Skills` page gives conflicting descriptive names for early Fang material. For this family, use the dedicated clan swordsmanship progression and document the page conflict rather than pretending the wiki is uniform.
- Existing accepted Beelzebub slot terms remain **Incinerate / Hemorrhage / Rapid Regeneration**.

### Source-specific issues / repairs to preserve

Chapter 18:
- Chinese repeatedly establishes Vikir as **eight**, but one late sentence literally calls him a `15-year-old youth`. Chapter 20 immediately explains that **Low Sword Expert / 1st Fang is the typical fifteen-year-old Baskerville milestone**. Treat the isolated Ch. 18 age phrase as a source/translation inconsistency and render the intended comparison rather than changing Vikir's actual age.
- Chinese rumor says Vikir stayed in River Styx for **seven minutes**; recovered English incorrectly says eight.
- Opening question means Hugo asks what Vikir **gained/realized**, not MTL `Did you have a bad day?`.
- Orc location should follow the Chinese lowlands/foothills of the Le Rouge et Le Noir range, not MTL `Enemies and the Black Mountains Valley`.
- Keep the Orc information block complete.
- Beelzebub's Hemorrhage suppresses the Orc's High-Speed Regeneration.
- Vikir is really Low Sword Graduator after Ch. 17 but intentionally displays only **Low Sword Expert / 1st Fang** here.

Chapter 19:
- Troll window is **Danger Rating C+**, not MTL C.
- Troll location is the **2nd Ridge of Le Rouge et Le Noir Mountain**.
- Troll's regeneration is the reason nonfatal attacks are wasted.
- Vikir deliberately waits for the Troll's charge to supply counterforce.
- Final disclosed power is **2nd Fang / Mid Sword Expert**, still far below his actual Low Sword Graduator / stable 4th Fang state.
- Chapter 20, not Chapter 19, reveals Beelzebub's third slot changing to the Troll's **Superspeed Regeneration**; do not import that update early.

## Exact next actions

1. Draft fresh Chinese-first Chapters 18–19.
2. QA Chapter 18 with special attention to the age inconsistency, seven-minute Styx rumor, Orc window, Beelzebub window, and deliberate low-rank disclosure.
3. QA Chapter 19 with complete Troll window and deliberate Mid Sword Expert / 2nd Fang disclosure.
4. Run 18–19 family QA including 17→18 and 19→20 continuity.
5. Create hash-bound provenance/acceptance; update tracker/status/project/progress/glossary/handoff.
6. Merge the Bared Teeth family if clean.
7. Immediately determine and begin the complete **Camus Morgue** family starting at Chapter 20.

## Persistent exceptions

- Chapter 55 Chinese raw missing; verified MTL 55 fallback.
- Combined raw containers retained intact: `075.txt`→75–76, `267.txt`→267–268, `284.txt`→284–285, `351.txt`→351–352, `353.txt`→353–354, `385.txt`→385–386, `495.txt`→495–496.
- Verified nontrivial mappings already recorded: target 75→MTL 74, 76→75, 267→265, 268→266.
