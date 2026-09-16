# SwordHound Session Handoff

> **Mandatory:** Read this file before beginning editorial work. Update it after meaningful checkpoints and always before ending a session or handing work to another agent. `AGENTS.md` and `editorial/WORKFLOW.md` define the required handoff protocol.

## Handoff metadata

- **Last updated:** 2026-09-16
- **Updated by:** ChatGPT — Hellhound-family acceptance checkpoint
- **Working branch:** `editorial/restart-hellhound-family`
- **Open PR:** pending creation
- **Base:** `main`
- **Base main commit:** `6186004e6e095401e457b1b258a6545bb07b7640`
- **Reason for current state:** Chapters 1–3 were fully rebuilt and accepted under the restarted Chinese-semantic/Fandom-canonical workflow. The next family boundary has already been verified.

## Authoritative current checkpoint

- **Target edition:** 500 chapters
- **Accepted:** **3**
- **Staged:** **0**
- **Next chapter:** **4**
- **Latest accepted family:** **Chapters 1–3 — Hellhound (1)–(3)**
- **Next active title family:** **Chapters 4–7 — The Baskerville Dog (1)–(4)**
- **Next-family boundary:** **VERIFIED**. Chinese Chapters 4–7 are parts (1)–(4) of the Baskerville-dog/hounds title family; Chinese Chapter 8 changes to `地狱的猎犬 (1)` and the aligned English reference calls it *Hounds of Hell (1)*.
- **Blocking issue:** none

The earlier one-chapter Chinese-first Chapter 1 acceptance remains superseded. The current Chapters 1–3 acceptance is the first valid production acceptance after the full restart.

## Rules that must not be lost

### Semantic versus canonical authority

- Chinese raw = semantic/narrative authority: plot, dialogue meaning, sequence, explicitness, omissions/additions, and identification of what appears in the source.
- English Fandom wiki = canonical English authority for identified names, terms, locations, ranks, skills, monsters, organizations, titles, and other proper nouns.
- English MTL = secondary alignment/phrasing reference only except Chapter 55.
- Wiki material never authorizes adding later revelations or narrative content absent from the Chinese source.
- Do not sanitize source content.

### Continuous title-family processing

- Determine the complete contiguous title-family boundary before accepting a chapter in that family.
- Process the entire family as one continuity/QA batch.
- Completing a chapter, family, PR, or merge is **not a stopping condition**.
- Continue directly into subsequent title families for as long as safe work can be completed, unless the user explicitly pauses/stops, the corpus ends, or a genuine blocker prevents safe editorial work.

### Source exceptions already established

- Chapter 55: Chinese raw missing; verified MTL Chapter 55 fallback.
- Combined raw containers retained intact: `075.txt`→75–76, `267.txt`→267–268, `284.txt`→284–285, `351.txt`→351–352, `353.txt`→353–354, `385.txt`→385–386, `495.txt`→495–496.
- Verified nontrivial MTL mappings already recorded: target 75→MTL 74, 76→75, 267→265, 268→266.
- Do not assume target N == MTL N elsewhere without content verification.

## Completed work — Chapters 1–3

### Family boundary and alignment

- Ch. 1 — Hellhound (1) → MTL 1, verified by title/content/opening/ending.
- Ch. 2 — Hellhound (2) → MTL 2, verified by title/content/opening/ending.
- Ch. 3 — Hellhound (3) → MTL 3, verified by title/content/opening/ending.
- Chinese Ch. 4 changes title family, so 1–3 is complete.

### Accepted output/evidence

- `manuscript/drafts/chapter-0001.md`
- `manuscript/drafts/chapter-0002.md`
- `manuscript/drafts/chapter-0003.md`
- `qa/chapter-0001.md`
- `qa/chapter-0002.md`
- `qa/chapter-0003.md`
- `qa/families/hellhound-0001-0003.md`
- `qa/acceptance/chapter-0001.json`
- `qa/acceptance/chapter-0002.json`
- `qa/acceptance/chapter-0003.json`
- `editorial/provenance/chapter-0001.json`
- `editorial/provenance/chapter-0002.json`
- `editorial/provenance/chapter-0003.json`

The family QA passed the intentional Ch. 1→2 replay, Ch. 2→3 progression, and Ch. 3→4 eight-year-timeskip boundary.

### Accepted canonical/translation decisions from the family

- **Vikir Van Baskerville** — canonical English form.
- **Hugo Le Baskerville** — canonical English form.
- **Marquis** — canonical English title for Hugo; Chinese Ch. 1 uses `伯爵` (“Count”) at one point, and that source conflict is preserved in QA/provenance.
- **Baskerville Clan** / **Iron-Blooded Sword Clan** — canonical organization forms where a formal organization name is intended; ordinary family/kinship prose remains contextual.
- **Cradle of Swords** — canonical English trial name; Chinese variants in Ch. 1–2 refer to the same trial in context.
- **River Styx** — canonical English proper name; mechanics are taken from Chinese.
- **Seven Great Families / Seven Great Clans** — use contextually without importing later lore.
- Ch. 3 snake species uses **Bloody Mamba** as a transparent recovered-English continuity choice because current Fandom retrieval did not expose a dedicated canonical species entry; the limitation is documented.
- Do **not** import MTL-only “Le Rogue Mountains” or “Fang Castle” into Ch. 3 without Chinese/canonical support.

## Key source findings preserved in accepted Chapters 1–3

### Chapter 1

- execution placard retained;
- humanity’s victory carved into stone;
- Vikir’s wish to live and live again retained;
- Cradle/Styx mechanics follow Chinese;
- Hugo’s Demon Realm/watch-my-back dialogue restored;
- final “young master is drinking the water” exchange restored;
- Hugo’s open-mouthed shock restored;
- Chinese 100-days wording inconsistency preserved rather than invented away.

### Chapter 2

- intentional replay of nursery/Cradle events preserved;
- rabbit/hunting-dog proverb preserved;
- Vikir bearing Hugo’s sins / “knowing too much” restored;
- Styx wound/internal-organ/full-body blessing mechanics retained;
- old poisoned-heel Baskerville-warrior anecdote retained;
- final teeth/fangs scene retained.

### Chapter 3

- full past-life age timeline retained and repaired;
- mothers arranging extra nursing for their own children restored;
- snake gore, defecation, and urination retained without sanitization;
- source inconsistency about venomous fangs documented;
- unsupported MTL location additions removed;
- chapter-ending revenge wait + eight-year timeskip retained.

## Next family — Chapters 4–7

### Verified title boundary

| Target | Chinese heading | Aligned English title | Alignment state |
| --- | --- | --- | --- |
| 4 | `巴斯克维家的狗 (1)` | *The Baskerville Dog (1)* | MTL 4 title verified; full content review still required |
| 5 | `巴斯克维家的猎犬们 (2)` | *The Baskerville Dog (2)* | MTL 5 title verified; full content review still required |
| 6 | `巴斯克维家族的猎犬们 (3)` | *The Baskerville Dog (3)* | MTL 6 title verified; full content review still required |
| 7 | `巴斯克维家的猎犬们 (4)` | *The Baskerville Dog (4)* | MTL 7 title verified; full content review still required |
| 8 | `地狱的猎犬 (1)` | *Hounds of Hell (1)* | boundary evidence; begins next family |

### Known terminology work for Chapters 4–7

- Rebuild sword-rank terminology from Chinese + current Fandom evidence. Historical forms **Sword Beginner / Expert / Graduator / Master** are leads only until this family is reviewed.
- Verify any rank definitions/subranks precisely; do not inherit old Chapter 4 acceptance automatically.
- Verify **John Barrymore** / butler terminology when Chapter 6 is reviewed.
- Revalidate any Baskerville techniques, fang numbering/forms, locations, exam terminology, or named people against Fandom when they first appear.
- Protect later-reveal chronology even if wiki pages expose advanced forms or identities.

## Exact next actions

1. Create/open the Hellhound-family PR from `editorial/restart-hellhound-family`, verify it is mergeable, and merge it into `main`.
2. Immediately create a new editorial branch from the merged `main` for Chapters 4–7.
3. Read complete Chinese raws `004.txt` through `007.txt` and inspect `008.txt` only as needed for boundary continuity.
4. Read complete recovered English references `chapter-004.xhtml` through `chapter-007.xhtml`; confirm each target↔MTL mapping by content, not merely title/number.
5. Perform current Fandom canonical-reference research for every consequential proper noun/term in 4–7, especially sword ranks, Barrymore, named techniques/forms, locations, and formal titles.
6. Draft Chapters 4–7 from Chinese in natural modern English, using MTL only as secondary reference and preserving all explicit/source-specific detail.
7. QA each chapter and the full 4–7 family as one unit; verify the Ch. 3→4 eight-year transition and Ch. 7→8 family boundary.
8. Create fresh provenance/acceptance evidence, promote only revalidated glossary entries, and advance tracker/status/progress.
9. Update this `HANDOFF.md` after each meaningful checkpoint and before any session ends.
10. Continue immediately into the Chapter 8 title family after 4–7 is integrated unless a genuine blocker appears.

## Session-end checklist for future agents

Before stopping, ensure:

- checkpoint counts match tracker/status;
- active family and next chapter are explicit;
- in-progress work is described precisely;
- MTL mappings are recorded;
- Fandom checks done/pending are recorded;
- source conflicts and unresolved issues are recorded;
- branch/PR/merge state is current;
- exact next actions are ordered and concrete;
- `HANDOFF.md` has been updated after the latest meaningful work.
