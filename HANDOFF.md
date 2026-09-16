# SwordHound Session Handoff

> **Mandatory:** Read this file before beginning editorial work. Update it after meaningful checkpoints and always before ending a session or handing work to another agent. `AGENTS.md` and `editorial/WORKFLOW.md` define the required protocol.

## Handoff metadata

- **Last updated:** 2026-09-17
- **Updated by:** ChatGPT — Solitary acceptance checkpoint
- **Working branch:** `editorial/restart-solitary-family`
- **Base main checkpoint:** `6b357f39fcaec5c1ce9185dbbc7342c66a172333` (after PR #10)
- **Current PR:** pending creation
- **Blocking issue:** none

## Authoritative current checkpoint

- **Target edition:** 500 chapters
- **Accepted:** **17**
- **Staged:** **0**
- **Next chapter:** **18**
- **Latest accepted family:** **Chapters 14–17 — Solitary (1)–(4)**
- **Latest family QA:** `qa/families/solitary-0014-0017.md` — **PASS** — `506806e1fa1da7aac61b9d54d202e3e727d14308`
- **Next family:** **Chapters 18–19 — Bared Teeth (1)–(2)**
- **Next-family boundary:** **VERIFIED** from Chinese + recovered-English headings; Chapter 20 changes to **Camus Morgue (1)**.

Accepted families so far:

1. Chapters 1–3 — *Hellhound (1)–(3)*
2. Chapters 4–7 — *The Baskerville Dog (1)–(4)*
3. Chapters 8–11 — *Hounds of Hell (1)–(4)*
4. Chapters 12–13 — *The Gluttonous Flies (1)–(2)*
5. Chapters 14–17 — *Solitary (1)–(4)*

## Rules that must not be lost

- Chinese raw = semantic/narrative authority.
- English Fandom wiki = canonical English authority for identified names, terminology, locations, ranks, skills, monsters, organizations, titles, and other proper nouns where applicable.
- English MTL/XHTML = secondary alignment/phrasing witness only except Chapter 55.
- Do not sanitize or soften source content.
- Do not import MTL/wiki narrative exposition absent from Chinese.
- Process complete contiguous title families; a chapter/family/PR completion is a checkpoint, not a stopping condition.
- Never assume target N == MTL N without title/content verification.
- Protect reveal chronology.
- Keep information windows atomic.
- Numbered Baskerville techniques are **Fangs**, not Forms.

## Accepted family — Chapters 14–17: Solitary

### Boundary and verified MTL mapping

Chinese:
- `014.txt` — `独食 (1)` — `6985275ffc44d7d6cb13674567aeb7b4eb2abe57`
- `015.txt` — `独食 (2)` — `d2ed35aa2f110b51c245d860dbf151c9db7f2a9f`
- `016.txt` — `独食 (3)` — `66d7a6dc326cd1118d5c4c06660429db0812d0f6`
- `017.txt` — `独食 (4)` — `a06435731264acf695a613b6bffc28270bd8d3fe`
- boundary witness `018.txt` — `显露的獠牙 (1)` — `7c313862e83ae30acfd9270ae5e0972d82eecf65`

Recovered English mappings verified by full content:
- target 14 → MTL 14 — `1f9904992e6d0354590d923fcab450f7ab60fa14`
- target 15 → MTL 15 — `b081799012eb00f8ae21fc555cff817ce586cddf`
- target 16 → MTL 16 — `a585d0e5d5df242bb52e478550ab651be2d93558`
- target 17 → MTL 17 — `186f5ce33d50b654427866f735e8f223e3786b3f`

Alignment evidence includes title sequence, post-exam report/library-access scene, Sixth-Fang manual, discovery of *Lurking Embedded Teeth*, torn-page retrieval recollection, Fifth-Fang breakthrough, book burning, and Chapter 18 Hugo summons.

### Final drafts

- `manuscript/drafts/chapter-0014.md` — `556a0e1ff32eb251b35b71f4222b208e04b1f1ae`
- `manuscript/drafts/chapter-0015.md` — `6c79f7db01d40e4eb5ee823ce1007e969aca55f1`
- `manuscript/drafts/chapter-0016.md` — `a26bedbdddac060808091e7aeef8b090e504f9e9`
- `manuscript/drafts/chapter-0017.md` — `217b62806c86b7d4d641276fc925a0e0723823a1`

### Chapter QA

- `qa/chapter-0014.md` — PASS — `2f8a11af61456f1a3439c0642712efae662c988e`
- `qa/chapter-0015.md` — PASS — `f3a72f7b55976588f2eb6004fabc189f19691bf6`
- `qa/chapter-0016.md` — PASS — `7d804fb8770669f172787116730242f54d07c214`
- `qa/chapter-0017.md` — PASS — `1ca241417fbc048ce4745ef71c47b4c9ab86dbe6`

### Provenance

- `editorial/provenance/chapter-0014.json` — `5687c5f3bb044762efbcc4d5314e8c36ca571dc9`
- `editorial/provenance/chapter-0015.json` — `3fa2a186c325647d1e200f13694a5bc4dc531cba`
- `editorial/provenance/chapter-0016.json` — `9fcef3f48729ad8e41e6b348ebcf63a3d7126702`
- `editorial/provenance/chapter-0017.json` — `4e4d7953c27785e5aa347148ac777644622db2d8`

### Acceptance records

- `qa/acceptance/chapter-0014.json` — `4ae5d314e18ab5964285a21cf317cf8cce1e1bf3`
- `qa/acceptance/chapter-0015.json` — `42d06e19ce46861428d6098e64dd692d2f2a73e0`
- `qa/acceptance/chapter-0016.json` — `bb9b9039523c1e5c90c94ccb35efcebf8b778c3f`
- `qa/acceptance/chapter-0017.json` — `cb8cca9d3e4c39094624d3bb97dce255cd0d6328`

### Accepted canonical terminology / decisions

- **10,000 Book Library**
- **Lurking Embedded Teeth**
- **Baskerville Fang Sword Style** / numbered Fangs
- **Sixth Fang** material offered by Hugo
- **Low Sword Graduator** for Vikir after the Chapter 17 breakthrough
- Vikir can stably show four Fangs and unstably produce a fifth at this point.

Material source repairs:

- Chapter 16 Chinese describes first-life Vikir as a **one-eyed black hound**; recovered English `right-handed black dog` is rejected.
- The first-life torn-page campaign preserves lost fingers/toes, both ears, severe burns/scars, dead siblings/comrades, and Hugo's single `Well done` reward without sanitization.
- Chapter 16 source timing for the later library fire is about **10 hours 50 minutes**; recovered English's duplicated `11 hours 50 minutes` block is rejected.
- Chapter 17 preserves the book-burning concealment and the servants' decision not to report it.

## Next family — Chapters 18–19: Bared Teeth

### Verified boundary

Chinese headings:
- Ch. 18 — `显露的獠牙 (1)` — `7c313862e83ae30acfd9270ae5e0972d82eecf65`
- Ch. 19 — `显露獠牙 (2)` — `bc88dc2708487354d9ff29ca8978252e8001d572`
- Ch. 20 changes to `米尔格·卡米耶 (1)` — `b4b2011e2c0ab569f7ee420c05608498970d2dd8`

Recovered English headings:
- Ch. 18 — *Bared Teeth (1)* — `5d58111d3a188ea82343910782f38dc22da8caea`
- Ch. 19 — *Bared Teeth (2)* — `bdaa1abc7dfe521570a9998c43099c576da16d37`
- Ch. 20 — *Camus Morgue (1)* — `5706f9f22b35d53b4e58208c3e24c04f59e40632`

**Important:** only the title-family boundary is verified at this checkpoint. Full 18→18 and 19→19 content alignment still must be established before the English witnesses are used editorially.

### Exact next actions

1. Open and merge the clean Solitary PR after verifying mergeability.
2. Create a fresh branch from merged main for **Bared Teeth Chapters 18–19**.
3. Read complete Chinese Chapters 18 and 19; use Chinese 20 opening as boundary/continuity witness.
4. Read complete recovered English Chapters 18 and 19 and verify target↔MTL alignment by opening, events, distinctive entities/techniques, and endpoints.
5. Canonicalize newly introduced proper nouns/terms against current English Fandom evidence; do not backfill later reveals.
6. Reconstruct Chapters 18–19 from Chinese.
7. Run chapter QA + 18–19 family QA, including the 17→18 Hugo-summons handoff and the 19→20 Camus Morgue boundary.
8. Create hash-bound provenance/acceptance, update glossary/tracker/status/project/progress/handoff, merge if clean.
9. Immediately determine and begin the Chapter 20 **Camus Morgue** title family.

## Persistent exceptions

- Chapter 55 Chinese raw missing; verified MTL 55 fallback.
- Combined raw containers retained intact: `075.txt`→75–76, `267.txt`→267–268, `284.txt`→284–285, `351.txt`→351–352, `353.txt`→353–354, `385.txt`→385–386, `495.txt`→495–496.
- Verified nontrivial mappings already recorded: target 75→MTL 74, 76→75, 267→265, 268→266.
