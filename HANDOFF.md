# SwordHound Session Handoff

> **Mandatory:** Read this file before beginning editorial work. Update it after meaningful checkpoints and always before ending a session or handing work to another agent. `AGENTS.md` and `editorial/WORKFLOW.md` define the required handoff protocol.

## Handoff metadata

- **Last updated:** 2026-09-16
- **Updated by:** ChatGPT — Hounds of Hell acceptance checkpoint
- **Working branch:** `editorial/restart-hounds-of-hell-family`
- **Previous merged PR:** #8 — The Baskerville Dog Chapters 4–7
- **Base main checkpoint:** `c4bf56635b966ba5f7f7b9d67dc4b724f93c723f`
- **Open PR for current branch:** pending creation

## Authoritative current checkpoint

- **Target edition:** 500 chapters
- **Accepted:** **11**
- **Staged:** **0**
- **Next chapter:** **12**
- **Accepted title families:**
  - Chapters 1–3 — *Hellhound (1)–(3)*
  - Chapters 4–7 — *The Baskerville Dog (1)–(4)*
  - Chapters 8–11 — *Hounds of Hell (1)–(4)*
- **Latest family QA:** `qa/families/hounds-of-hell-0008-0011.md` — **PASS**
- **Next title family:** **Chapters 12–13 — The Gluttonous Flies (1)–(2)**
- **Next-family boundary:** **VERIFIED**. Chinese Chapters 12–13 carry parts (1)–(2); Chinese Chapter 14 changes to `独食 (1)`.
- **Blocking issue:** none

## Rules that must not be lost

- Chinese raw = semantic/narrative authority.
- English Fandom wiki = canonical English authority for identified names/terms/locations/ranks/skills/monsters/organizations/titles where applicable.
- English MTL/XHTML = secondary alignment/phrasing witness only except Chapter 55.
- Do not sanitize or soften source content.
- Process complete contiguous title families; chapter/family/PR completion is a checkpoint, not a stopping condition.
- Never assume target N == MTL N without title/content verification.
- Protect reveal chronology even when canonical references contain later information.
- Keep information windows complete and atomic.

## Completed family — Chapters 8–11

### Boundary and alignment

Chinese headings:
- Ch. 8 — *Hounds of Hell (1)*
- Ch. 9 — *Hounds of Hell (2)*
- Ch. 10 — *Hounds of Hell (3)*
- Ch. 11 — *Hounds of Hell (4)*
- Ch. 12 changes to *The Gluttonous Flies (1)*

Verified recovered-English mappings:
- target 8 → MTL 8 — SHA `1ec6b7bff255d7ea718dcca063e5ded4ee5ba523`
- target 9 → MTL 9 — SHA `d765e36aa4083e8054c7ea179c89730cd347e398`
- target 10 → MTL 10 — SHA `8c2442bf760ee8ca0c3174c5d49556dab379cdac`
- target 11 → MTL 11 — SHA `26e15feb304acd8e94d8f902c82a369dc900fb7e`

Chinese source SHAs:
- `008.txt` — `d62d365170a0107c5c726c9da1901d996d2d508d`
- `009.txt` — `316950c50ba6c3774ffbc779fb319bd1bcff8874`
- `010.txt` — `6be1944dd10561d5246cff6ab830e6f5e39bc736`
- `011.txt` — `db1c2c6ec0304cf4e19390cf88de0f5d4a8a9b44`
- boundary witness `012.txt` — `9cbd4648873cda28a0e9410966d0643dda873968`

### Final drafts

- `manuscript/drafts/chapter-0008.md` — `33ead486847f4fdb3cff95e00778d85dddc69315`
- `manuscript/drafts/chapter-0009.md` — `e9cfd93a9030a2d1bc6c3c9e241ec780ca46c2f2`
- `manuscript/drafts/chapter-0010.md` — `5a340ea07718a4119488d153a9f37a265ba90781`
- `manuscript/drafts/chapter-0011.md` — `15673ea64dfa3d9375c97a3bcd1ff605f3984ade`

### Chapter QA

- `qa/chapter-0008.md` — PASS — `c511faeada26320a8e764819051b15f570db622f`
- `qa/chapter-0009.md` — PASS — `1406b60bb5f13639eab798b9a946446fca526893`
- `qa/chapter-0010.md` — PASS — `ef0b10235e9dfd9b99a97abb37904bae05909e52`
- `qa/chapter-0011.md` — PASS — `5f8d12c1c8c9ffeb3116940ce23e393490fcb0ae`

### Family QA

- `qa/families/hounds-of-hell-0008-0011.md` — PASS — `a5c43f7276f0bfe5e86f12a34238abcdcc79d003`

Continuity gates passed:
- 7→8: Bloody Beans → practical-exam setup
- 8→9: Pavlov bell → exam action
- 9→10: chocolate setup → Hellhound poisoning payoff
- 10→11: Cerberus reveal → continuous Cerberus fight
- 11→12: seven-step Cerberus collapse → Chapter 12 opens on collapsed Cerberus

### Provenance

- `editorial/provenance/chapter-0008.json` — `03106e337c848627c611eec212d110be7fec0710`
- `editorial/provenance/chapter-0009.json` — `5654c0b34c92d41653365c07f018a1d1f33c4895`
- `editorial/provenance/chapter-0010.json` — `c32728ab4962a6461a77538d76d7f47159a73f69`
- `editorial/provenance/chapter-0011.json` — `d857a77cfca1a027aba71eeb12091c2514c09ced`

### Acceptance records

- `qa/acceptance/chapter-0008.json` — `08bb5f82d60975a0b7905f9111df92cff32fccc9`
- `qa/acceptance/chapter-0009.json` — `e307b687650f1e3c74172b3e2539e811650bbc5b`
- `qa/acceptance/chapter-0010.json` — `127831a7386c1d2e55cda9e11a7a6e01942560b7`
- `qa/acceptance/chapter-0011.json` — `1430850ac6559c96234f044c34e4e92d46a61617`

## Accepted Hounds of Hell terminology / decisions

- **Le Rouge et Le Noir Mountain**
- **Guide Dog**
- **Pavlov Van Baskerville**
- **Brown Rat ‘Norvegicus’**
- **Hellhound** — Danger Rating B+, 3 m, 2nd Ridge
- **Cerberus** — Danger Rating A+, 7 m, 7th Ridge
- **Hell’s Watchdog**
- **Camus Morgue / Ironblood Empress** only within the future-war retrospective already present in Chinese
- **Sword Expert / Sword Graduator / Sword Master** with Low/Mid/High substages
- Sword/mage equivalence: Expert Low/Mid/High = 1st/2nd/3rd Circle; Graduator Low/Mid/High = 4th/5th/6th Circle; Sword Master = 7th Circle
- **Baskerville 1st / 2nd / 3rd Form**; first-life Vikir had mastered through the 4th Form
- **Cradle of Needles** as Vikir’s contextual label for the stake pit
- **Bloody Beans** revalidated through the combat payoff
- **Bloody Mamba** remains a scoped recovered-English fallback, not a newly claimed direct Fandom canonicalization

Key repairs include:
- Chapter 8 scoring rebuilt from Chinese rather than MTL interpretation;
- Chapter 9 Brown Rat/Hellhound windows restored as complete blocks;
- Chapter 10 MTL `height` corrected to **kidneys**;
- Chapter 10 near-impervious-body and post-coming-of-age High Sword Expert comparison restored;
- Cerberus taxonomy corrected to **pinnacle of underworld-type monsters**;
- Chapter 11 rank table and Baskerville Forms normalized;
- explicit poisoning/waste/broken-rib details retained without sanitization;
- exact seven-step Bloody Mamba payoff retained.

## Fandom access note

The principal Fandom evidence for this family was successfully retrieved earlier during the active-family research pass. A later refresh attempt on 2026-09-16 was blocked by Fandom robots rules. QA/provenance records explicitly scope that limitation. Do not claim the blocked refresh succeeded, and do not invent canonical facts from it.

## Next family — Chapters 12–13

### Boundary

Chinese:
- `012.txt` — `贪食的苍蝇 (1)` — SHA `9cbd4648873cda28a0e9410966d0643dda873968`
- `013.txt` — `贪食的苍蝇 (2)` — SHA `9187c6e887445ee9cd416f323939e7165f0ada4b`
- `014.txt` — `独食 (1)` — SHA `6985275ffc44d7d6cb13674567aeb7b4eb2abe57`, proving a new family starts at 14

Recovered English title witnesses:
- target 12 candidate → `source/chapters/chapter-012.xhtml`, title *The Gluttonous Flies (1)* — SHA `594ce3566f95cc8983e1298a593967f41ab73c3f`
- target 13 candidate → `source/chapters/chapter-013.xhtml`, title *The Gluttonous Flies (2)* — SHA `63a478d5df24e966953d739028801391a3d09727`

**Important:** title matching is promising but full 12→12 and 13→13 content alignment still requires normal verification from complete Chinese/English reads. Do not mark it verified solely from numbering/title.

### Exact next actions

1. Open and merge the current Chapters 8–11 PR after verifying it is mergeable.
2. Create a fresh branch from the new merged main for *The Gluttonous Flies*.
3. Read complete Chinese Chapters 12 and 13; read Chapter 14 opening/endpoint context as needed.
4. Read the full recovered English Chapters 12 and 13 and verify target↔MTL alignment by opening, event sequence, distinctive entities, information windows, and endpoints.
5. Canonicalize every newly introduced name/term against the English Fandom wiki where accessible. **Do not assume the English spelling of the Chinese `巴尔泽布`/related fly-demon or weapon term; establish the canonical form from evidence before locking it.**
6. Reconstruct Chapters 12–13 from Chinese, preserving explicit source detail and information-window integrity.
7. QA both chapters individually and as one title-family unit, including the 11→12 collapsed-Cerberus handoff and the 13→14 title-family boundary.
8. Create hash-bound provenance/acceptance records; update glossary/tracker/status/project/progress/handoff.
9. Merge the 12–13 family if clean, then immediately determine and begin the Chapter 14 family.

## Persistent exceptions

- Chapter 55 Chinese raw missing; verified MTL 55 fallback.
- Combined raw containers retained intact: `075.txt`→75–76, `267.txt`→267–268, `284.txt`→284–285, `351.txt`→351–352, `353.txt`→353–354, `385.txt`→385–386, `495.txt`→495–496.
- Verified nontrivial mappings already recorded: target 75→MTL 74, 76→75, 267→265, 268→266.
