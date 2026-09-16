# SwordHound Session Handoff

> **Mandatory:** Read this file before beginning editorial work. Update it after meaningful checkpoints and always before ending a session or handing work to another agent. `AGENTS.md` and `editorial/WORKFLOW.md` define the required handoff protocol.

## Handoff metadata

- **Last updated:** 2026-09-16
- **Updated by:** ChatGPT — restarted Hellhound-family editorial session
- **Working branch:** `editorial/restart-hellhound-family`
- **Open PR:** none yet
- **Base:** `main`
- **Base main commit:** `6186004e6e095401e457b1b258a6545bb07b7640`
- **Reason for current session:** Begin actual reconstruction from Chapter 1 after the full reset/handoff infrastructure was merged.

## Authoritative current checkpoint

- **Target edition:** 500 chapters
- **Accepted:** 0
- **Staged:** 0
- **Next chapter:** 1
- **Active title family:** **Chapters 1–3 — Hellhound (1)–(3)**
- **Family boundary:** **VERIFIED**. Chinese Chapters 1–3 carry Hell Hound parts (1), (2), and (3); Chinese Chapter 4 changes base title to `巴斯克维家的狗 (1)` / *The Baskerville Dog (1)*.
- **Current chapter work:** Chinese and aligned MTL for Chapters 1–3 have been read; canonical-reference research is substantially complete; drafting/QA remains.
- **Blocking issue:** none

The previous Chinese-first Chapter 1 acceptance remains **superseded**. Its old draft/QA/acceptance/provenance exist only in Git history (earlier merge `797810e4e0aafc64b37153395c5e57ffe2354f6e`) and are non-authoritative leads.

## Rules that must not be lost again

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

## Work completed in this session

1. Read the merged reset handoff from `main` and created `editorial/restart-hellhound-family`.
2. Verified the first contiguous title-family boundary:
   - Ch. 1 — Hell Hound (1)
   - Ch. 2 — Hell Hound (2)
   - Ch. 3 — Hell Hound (3)
   - Ch. 4 changes to *The Baskerville Dog (1)*, so it begins the next family.
3. Read complete Chinese raws:
   - `source/chinese/chapters/001.txt` — SHA `fa9dfcf2f15c575d3a5971a93b9951d1ae0d0431`
   - `source/chinese/chapters/002.txt` — SHA `9993c01485cee99e207f7dd366c6bdb1a63a3706`
   - `source/chinese/chapters/003.txt` — SHA `76a0aa87980a8c0f680bd66c90872472833c693c`
4. Re-read/checked the corresponding recovered English references and verified current alignment:
   - target 1 → MTL 1, `chapter-001.xhtml`, SHA `93188cc599feec0ec8bbfc1e326fe3b70d2be0eb`
   - target 2 → MTL 2, `chapter-002.xhtml`, SHA `e40f701a687b0e9dfc8faef2544a3c098c44748c`
   - target 3 → MTL 3, `chapter-003.xhtml`, SHA `3970e9dffdabc773bfefd29674785430679ccec5`
   Alignment is supported by matching title part, opening scene, distinctive events/entities, full scene order, and chapter endpoint.
5. Performed current Fandom canonical-reference research for early-family entities/terms.

## Current source findings for Chapters 1–3

### Chapter 1

Current Chinese review reconfirms historical leads:

- execution placard is present and must be retained: Vikir Van Baskerville / charge for collusion with demons;
- humanity's victory is carved into stone, not merely written in books;
- Vikir's final pre-execution wish includes both wanting to live and wanting to live again;
- the MTL corrupts the Baskerville birth-celebration sentence;
- the Cradle/Styx mechanics must follow Chinese, not broken MTL pronouns;
- Hugo asks how these children can fight the Demon Realm and when he can raise them to guard his back; the MTL's generic survival-of-the-fittest replacement is not source-faithful;
- final knights' line is that the young master is drinking the water;
- Hugo's final reaction is open-mouthed shock, not a grin;
- Chinese internally says Vikir had just reached 100 days and later says he was not yet 100 days old. Do not invent a reconciliation.

### Chapter 2

Key current decisions/findings:

- Chapter 2 intentionally replays the nursery/Cradle sequence from Vikir's internal perspective; preserve the overlap.
- Chinese variants `刀尖摇篮` / related blade-cradle wording refer to the same established Cradle of Swords trial in context; do not create a separate location from MTL's erroneous “Tower of Swords.”
- Preserve the proverb image: once the rabbit is gone, the hunting dog is boiled/discarded.
- Chinese explicitly says Vikir was made to bear Hugo's sins and was executed because he “knew too much.”
- Styx mechanics include wound penetration, bone/flesh/mana-channel strengthening, internal-organ strengthening by drinking, and the rule that a body part exposed after leaving the river cannot regain the blessing.
- The Achilles-like old Baskerville warrior anecdote is source content and must remain.
- Chapter ends with Vikir surfacing after drinking Styx water and Hugo laughing at the infant already having teeth.

### Chapter 3

Key current decisions/findings:

- Preserve Vikir's past-life age timeline (8/15/20/25/29/30/35/39/40) but rewrite MTL distortions from Chinese.
- Fandom independently supports **1 Circle of mana** / faint aura around age 15 and Vikir's early sword progression; do not import later rank revelations beyond what Chapter 3 establishes.
- The nanny/mother favoritism scene must reflect mothers arranging extra nursing for their own children; MTL's “half-brother” wording is wrong.
- Chinese explicitly depicts two venomous snakes and later gives them a notorious species label. Recovered English consistently calls the species **Bloody Mamba**, while retrieved Fandom synopsis describes the same nursery snakes generically as **black mambas** and exposes no dedicated canonical monster entry. Therefore do not claim Fandom definitively settles this proper name; document the fallback evidence if `Bloody Mamba` is retained.
- Chinese does **not** place the snakes in Le Rogue Mountain in this chapter; the MTL adds that location. Do not import the location solely from MTL.
- Chinese explicitly includes the snakes defecating and urinating as they die. Preserve it; do not sanitize.
- Chinese says their venomous fangs had already been removed by the next-day inspection, despite the preceding paragraph describing venom dripping from exposed fangs. Preserve/document the source inconsistency rather than silently rewriting causality.
- Chinese says Hugo hurries from the main castle to the nursery/child-rearing castle. MTL's proper name “Fang Castle” is not presently supported by retrieved Fandom evidence; do not force the MTL location name without stronger canonical support.
- Chapter ends with Vikir waiting for revenge, followed by an eight-year timeskip, cleanly handing into Chapter 4.

## English MTL alignment state

### Hellhound family — VERIFIED

| Target | Chinese title | English MTL | Status |
| --- | --- | --- | --- |
| 1 | Hell Hound (1) | Chapter 1: Hellhound (1) | verified by title/content/opening/ending |
| 2 | Hell Hound (2) | Chapter 2: Hellhound (2) | verified by title/content/opening/ending |
| 3 | Hell Hound (3) | Chapter 3: Hellhound (3) | verified by title/content/opening/ending |

Use **Hellhound** as the English chapter-title form because the designated Fandom pages identify novel appearances as `Hellhound (1)` etc., despite the Chinese embedded English writing `Hell Hound`.

## Fandom canonical-reference state

Current retrieved Fandom evidence supports:

- **Vikir Van Baskerville** — dedicated character page; Novel first appearance Ch. 1 — Hellhound (1).
- **Hugo Le Baskerville** — dedicated character page; Patriarch; explicit title **Marquis**; Novel first appearance Ch. 1 — Hellhound (1).
- **Baskerville Clan** — dedicated organization page; alias **Iron-Blooded Sword Clan**. The wiki also uses “Baskerville Family” contextually, so ordinary kinship prose need not be mechanically rewritten to “Clan.”
- **Cradle of Swords** — explicitly named on Baskerville/Grand Mansion pages.
- **River Styx** — explicitly named on Grand Mansion/location material and Vikir pages.
- **The Seven Great Families / Seven Great Clans of the Rok Empire** — Fandom novel/worldbuilding and Baskerville pages support the concept; choose contextually without importing later lore.
- **Marquis** for Hugo conflicts with Chinese Chapter 1 `伯爵` (“Count”). Under project authority rules, retain the Chinese conflict in QA/provenance but use the canonical English noble title **Marquis**.

Not definitively settled by current Fandom retrieval:

- Chapter 3 snake species proper name. Fandom synopsis says “black mambas”; recovered English novel repeatedly uses **Bloody Mamba**. Treat this as a documented fallback/canonicalization limitation rather than a fake wiki verification.
- **Fang Castle** was not found in current Fandom retrieval. Chinese gives a descriptive nursery/child-rearing castle reference; avoid importing the MTL proper name until stronger canonical evidence exists.

## Open decisions / blockers

- **No blocking issue.**
- Editorial choice still to finalize in Chapter 3: whether to render the snake species as **Bloody Mamba** (strong recovered-English continuity, later repeated usage) while explicitly marking the lack of a dedicated Fandom canonical entry. This is not a blocker because the evidence can be transparently scoped.
- Need to draft and QA all three family chapters before any acceptance.

## Exact next actions

1. Draft Chapter 1 from the fully reviewed Chinese source, using current canonical forms and documenting the Count→Marquis conflict.
2. Draft Chapter 2 from Chinese, preserving the intentional overlap, rabbit/hound proverb, Styx mechanics, old-warrior anecdote, and final fangs scene.
3. Draft Chapter 3 from Chinese, preserving the full age timeline, nursing favoritism, snake gore/excretion, source fang inconsistency, and eight-year timeskip; do not import unsupported Le Rogue/Fang Castle details.
4. QA Chapters 1–3 individually and as one title-family unit against complete Chinese sources and aligned MTL references.
5. Create fresh provenance and acceptance records with Fandom evidence/limitations explicitly described.
6. Update `editorial/GLOSSARY.md` only with terms accepted under this restarted batch.
7. Update tracker/status/project/progress and this handoff.
8. Open and merge the Hellhound-family PR once evidence is internally consistent.
9. Immediately determine and begin the next contiguous title family from Chapter 4; do not stop merely because Chapters 1–3 merge.

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
