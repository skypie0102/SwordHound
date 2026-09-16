# SwordHound Session Handoff

> **Mandatory:** Read this file before beginning editorial work. Update it after meaningful checkpoints and always before ending a session or handing work to another agent. `AGENTS.md` and `editorial/WORKFLOW.md` define the required handoff protocol.

## Handoff metadata

- **Last updated:** 2026-09-16
- **Updated by:** ChatGPT — Baskerville Dog family acceptance checkpoint
- **Working branch:** `editorial/restart-baskerville-dog-family`
- **Previous merged PR:** #7 — Hellhound Chapters 1–3
- **Base main commit for this branch:** `786cbd96627a86fca550ee684001b7ba2cc94665`
- **Open PR for current branch:** pending creation

## Authoritative current checkpoint

- **Target edition:** 500 chapters
- **Accepted:** **7**
- **Staged:** **0**
- **Next chapter:** **8**
- **Accepted title families:**
  - Chapters 1–3 — *Hellhound (1)–(3)*
  - Chapters 4–7 — *The Baskerville Dog (1)–(4)*
- **Next family start:** Chapter 8 — *Hounds of Hell (1)*
- **Next-family full boundary:** **NOT YET VERIFIED**. Determine the complete contiguous run from Chapter 8 before accepting any chapter in it.
- **Blocking issue:** none

## Rules that must not be lost

- Chinese raw = semantic/narrative authority.
- English Fandom wiki = canonical English authority for identified proper nouns/terms where an applicable entry exists.
- English MTL = secondary alignment/phrasing reference only except Chapter 55.
- Do not sanitize source content.
- Process complete contiguous title families; chapter/family/PR completion is a checkpoint, not a stopping condition.
- Do not assume target N == MTL N without content verification.
- Final EPUB visual/layout QA remains deferred until complete-EPUB assembly.

## Accepted production evidence — Chapters 4–7

### Family

- `qa/families/baskerville-dog-0004-0007.md` — PASS
- Family range: **4–7**
- Chapter 8 changes title to *Hounds of Hell (1)*, establishing the boundary.

### Chapter 4 — The Baskerville Dog (1)

- Chinese: `source/chinese/chapters/004.txt` — `a72d0371ccf0b3da0ad5a4cdb660ac7223753379`
- MTL: `source/chapters/chapter-004.xhtml` — `42ad39ef16ea789978c405e5c80038df6edf3a08`
- Draft: `manuscript/drafts/chapter-0004.md` — `ff0997d2b046a92f88d077094281ecd01f106e31`
- QA: `qa/chapter-0004.md` — `fcd9d715a72245b301b53f14e74780f50a3bf515`
- Provenance: `editorial/provenance/chapter-0004.json` — `b962e5787a5e19f9b357f31f3e9f789adda7cb9e`
- Acceptance: `qa/acceptance/chapter-0004.json` — `d0d02a010f82d87420f0268d6b4288e2e69ada43`

### Chapter 5 — The Baskerville Dog (2)

- Chinese: `005.txt` — `2c2540ed32360a8010ff2083fdb6151d1b758971`
- MTL 5 — `e8d0886160b5d4ec02db37cb7f939e77eb87631f`
- Draft — `4ab417641b7f81ccf0f406a13a2e861df2e8fe06`
- QA — `c653369290a599555598e5c58f1568273cde2b17`
- Provenance — `f29379417da8e5bb9e7003867a3b5b0eeb3eb3f9`
- Acceptance — `233d3763b1d9fe81e9945e20447a9fc9bcc18b1c`

### Chapter 6 — The Baskerville Dog (3)

- Chinese: `006.txt` — `66ddbad71c43a90215fa1f56f4336071033c4e3a`
- MTL 6 — `4827e0019e9a6e707c4e75debed26a974e9e4a33`
- Draft — `561828cb5d4298d6e5a4649d45d293ce867da308`
- QA — `4d0ba3155211857a9922a6463d97a18d75cc2814`
- Provenance — `8a4749898e74371e6b69fd1e1fa3fc0f5c1d5d5d`
- Acceptance — `76e0f558223ad1997b319e70b5b6f216be08e62b`

### Chapter 7 — The Baskerville Dog (4)

- Chinese: `007.txt` — `f1a4dcf06a722c6d14b38d8beb08a425d471eb4d`
- MTL 7 — `9d5414b25ad77e975bfb326666cc868be161953b`
- Draft — `5a1d8c21aff248d7b8fe667dac47c06505116d11`
- QA — `d4fcb71ffce885d0cc1ebda06e0e539f94db0f0c`
- Provenance — `9f517b4492f81b13f378133e55dd42eb4405c97b`
- Acceptance — `67a63daf7754fc38e1dd860a096120ff08301672`

## Accepted terminology/decisions from Chapters 4–7

- **Sword Beginner → Sword Expert → Sword Graduator → Sword Master**
- **Low / Mid / High** substages when source-supported
- Vikir at age eight: **High Sword Expert**
- Previous-life High Sword Expert age: **sixteen**; MTL age-ten line rejected
- **Highbro / Middlebro / Lowbro Le Baskerville**
- contextual **Baskerville Trident / Hugo’s Trident** image
- **John Barrymore**, Head Butler
- **Morgue Clan**
- **Red Fang Mountain** for the ruby-mine dispute; MTL Red Cane Mountain rejected
- **Rok Empire** / Seven Great Clans context
- **Bloody Beans**
- child-rearing/nursery castle remains descriptive; MTL **Fang Castle** is not treated as canonically verified

## Important source/editorial findings preserved

### Chapter 4

- complete Chinese sword-rank mechanics restored;
- Hugo’s Seventh-Circle-equivalent mana + Sword Master standing retained;
- Vikir’s previous-life age corrected to sixteen;
- two-suns ending preserved as a distant guard’s observation of Vikir’s enormous mana manifestation.

### Chapter 5

- ten-minute suffocation attempt preserved;
- Lowbro’s severed finger, Highbro’s broken nose/teeth, Middlebro’s jaw injury, blood/saliva/urine retained;
- Styx protection stops Highbro’s dagger;
- Vikir’s one-survivor threat and forced internal fracture of the Trident retained.

### Chapter 6

- John Barrymore introduction restored;
- Morgue/Red Fang ruby dispute canonicalized;
- MTL `Advertisement` debris removed;
- Hugo’s “How many died?” reaction retained;
- physical healing versus psychological destruction of the triplets kept distinct;
- ends on Vikir’s “How can the strong be wrong?” doctrine.

### Chapter 7

- direct continuation of Chapter 6 interview preserved;
- Hugo’s implied fratricide retained;
- destroyed-family survivor/nun forgiveness anecdote retained;
- under-fifteen water + haggis/offal diet and sweets-as-reward system restored;
- concentrated **Bloody Beans** sequence retained with source quantities;
- Vikir refuses bean processing, leading into the next family’s practical-exam arc.

## Canonical-reference access note

Current-family Fandom evidence was gathered during the active source-review phase. During final QA, fresh direct Fandom retrieval was blocked by robots.txt. This is recorded as an access limitation; no new canonical claim was fabricated after the block. Chinese remains narrative authority throughout.

## Global state files synchronized

- `editorial/chapter-tracker.json` — 7 accepted, next 8
- `editorial/reconstruction-status.json` — 7 accepted, next 8
- `PROJECT_STATE.md` — 7 accepted, next 8
- `PROGRESS.md` — Chapters 4–7 acceptance logged
- `editorial/GLOSSARY.md` — Chapters 4–7 terms promoted/scoped
- `README.md` — current checkpoint updated

## Exact next actions

1. Open the Chapters 4–7 PR from `editorial/restart-baskerville-dog-family` to `main`, verify mergeability, and squash merge.
2. Create a fresh branch from merged `main` for the Chapter 8 family.
3. Inspect Chinese headings starting at `008.txt` until the base title changes; determine the complete **Hounds of Hell** family boundary.
4. Verify the corresponding target↔MTL mappings by title/content, not number alone.
5. Read every Chinese raw in the family completely and inspect the next chapter for boundary continuity.
6. Revalidate applicable Fandom canonical terms, especially **Le Rouge et Le Noir Mountain**, Guide Hounds, monster names/ranks, exam terminology, Bloody Beans usage, and any sword ranks/skills that recur.
7. Draft and QA the full family, create hash-bound provenance/acceptance evidence, update tracker/status/glossary/progress/handoff, merge, and continue to the next family.

## Persistent source exceptions

- Chapter 55 Chinese raw missing; MTL 55 fallback.
- Combined raw containers retained intact: 075→75–76, 267→267–268, 284→284–285, 351→351–352, 353→353–354, 385→385–386, 495→495–496.
- Verified nontrivial mappings already recorded: target 75→MTL 74, 76→75, 267→265, 268→266.
