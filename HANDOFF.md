# SwordHound Session Handoff

> **Mandatory:** Read this file before beginning editorial work. Update it after meaningful checkpoints and always before ending a session or handing work to another agent. `AGENTS.md` and `editorial/WORKFLOW.md` define the required handoff protocol.

## Handoff metadata

- **Last updated:** 2026-09-16
- **Updated by:** ChatGPT — workflow-reset session
- **Working branch:** `restart-from-chapter-001-with-handoff`
- **Open PR:** none yet
- **Base:** `main`
- **Main at session start:** `c6195db419baf7344806b0d8a352bc86ccaa5a03`
- **Reason for handoff state:** User requested a full restart from the beginning plus a durable per-session continuation file.

## Authoritative current checkpoint

- **Target edition:** 500 chapters
- **Accepted:** 0
- **Staged:** 0
- **Next chapter:** 1
- **Active title family:** not yet fully bounded under the restarted workflow
- **Current chapter work:** none accepted or staged
- **Blocking issue:** none

The previous Chinese-first Chapter 1 acceptance is **superseded**. Its active draft/QA/acceptance/provenance files were removed on this branch. The old work remains in Git history (notably the earlier Chapter 1 merge at `797810e4e0aafc64b37153395c5e57ffe2354f6e`) and may be consulted only as a non-authoritative analysis lead.

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

1. Created branch `restart-from-chapter-001-with-handoff` from current `main`.
2. Invalidated the previous Chapter 1 active acceptance by removing:
   - `manuscript/drafts/chapter-0001.md`
   - `qa/chapter-0001.md`
   - `qa/acceptance/chapter-0001.json`
   - `editorial/provenance/chapter-0001.json`
3. Reset active state to 0/500, next Chapter 1 in:
   - `PROJECT_STATE.md`
   - `PROGRESS.md`
   - `editorial/reconstruction-status.json`
   - `editorial/chapter-tracker.json`
   - `README.md`
4. Reset `editorial/GLOSSARY.md` so old Chapter 1 decisions are leads, not accepted terms.
5. Updated `AGENTS.md` and `editorial/WORKFLOW.md` to make this handoff file mandatory at session start, meaningful checkpoints, and session end.
6. Restored/retained the corrected authority split and continuous title-family rules.

## Source review state after this restart

No chapter raw has yet been **re-reviewed as current work after this full restart**.

Historical analysis from the superseded Chapter 1 pass identified useful leads such as MTL omissions around the execution placard, Vikir's “live again” wish, Hugo's dialogue, and the ending Styx exchange. Those findings may accelerate review, but every item must be revalidated under the complete workflow, including current Fandom canonical-term evidence and title-family continuity.

## English MTL alignment state

### Current first batch

- Target Chapter 1 → MTL Chapter 1 was historically aligned by title/content, but under the full restart it should be quickly reconfirmed and recorded as current evidence.
- The complete title-family boundary beginning at Chapter 1 is **not yet verified in this restarted session**.
- Do not accept Chapter 1 until the full family boundary is known and the family has been reviewed consistently.

## Fandom canonical-reference state

No Fandom check is counted as completed under the restarted workflow yet.

Likely early terms requiring explicit current verification include, at minimum:

- Vikir Van Baskerville
- Hugo Le Baskerville and his canonical noble title
- Baskerville naming/house terminology where a canonical form exists
- River Styx
- Cradle of Swords / any canonical trial name
- any early sword-rank terminology that appears within the first title family
- any named location, organization, skill, monster, or formal title introduced in the batch

Record exact relevant page/entry evidence or an access limitation in QA/provenance rather than citing the wiki homepage as proof of a specific term.

## Open decisions / blockers

- **No blocker.**
- Need to determine the complete contiguous title-family boundary starting at Chapter 1 before reconstruction acceptance begins.
- Need to establish current Fandom evidence for applicable canonical early terminology.

## Exact next actions for the next agent/session

Perform these in order:

1. Read `AGENTS.md`, this `HANDOFF.md`, `PROJECT_STATE.md`, `PROGRESS.md`, `editorial/WORKFLOW.md`, `editorial/SOURCES.md`, `editorial/chapter-tracker.json`, and `editorial/GLOSSARY.md`.
2. Inspect Chinese chapter headings beginning with Chapters 1 onward until the base title changes; determine the **complete contiguous title-family range** beginning at Chapter 1.
3. Inspect the corresponding recovered English MTL chapter titles/content and verify the target↔MTL mapping for **every chapter in that family**. Do not rely on chapter numbers alone.
4. Consult the English Fandom wiki for every consequential name/term/location/rank/skill/monster/organization/title introduced in the family. Record specific evidence and protect reveal chronology.
5. Read every Chinese raw in the family completely before finalizing English prose.
6. Reconstruct/edit the full family in natural modern English, preserving all source detail and explicitness and correcting MTL omissions/additions/mistranslations.
7. QA the family both per chapter and as a contiguous unit: semantic coverage, canonical English terminology, chronology, repeated/overlapping material, chapter boundaries, windows, scene breaks, grammar, and continuity.
8. Only after the full gate passes, create current drafts/QA/provenance/acceptance records and update tracker/status/glossary/progress.
9. Update this `HANDOFF.md` with the exact accepted/in-progress state.
10. Continue immediately into the next contiguous title family unless an explicit stopping condition exists.

## Session-end checklist for future agents

Before stopping, verify all boxes conceptually:

- checkpoint counts match tracker/status;
- active family and next chapter are explicit;
- in-progress work is described at paragraph/source-review granularity where useful;
- MTL mappings are recorded;
- Fandom checks done/pending are recorded;
- decisions and unresolved issues are recorded;
- branch/PR/merge state is current;
- exact next actions are ordered and concrete;
- `HANDOFF.md` has been updated **after** the latest meaningful work.
