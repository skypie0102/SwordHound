# SwordHound Session Handoff

> **Mandatory:** Read this file before beginning editorial work. Update it after meaningful checkpoints and always before ending a session or handing work to another agent. `AGENTS.md` and `editorial/WORKFLOW.md` define the required handoff protocol.

## Handoff metadata

- **Last updated:** 2026-09-16
- **Updated by:** ChatGPT — Gluttonous Flies source/canonicalization checkpoint
- **Working branch:** `editorial/restart-gluttonous-flies-family`
- **Previous merged PR:** #9 — Hounds of Hell Chapters 8–11
- **Merged main checkpoint:** `f4085b0451588b9c917e19c3c972954c3446ead5`
- **Open PR for current branch:** none yet

## Authoritative current checkpoint

- **Target edition:** 500 chapters
- **Accepted:** **11**
- **Staged:** **0**
- **Next chapter:** **12**
- **Accepted title families:**
  - Chapters 1–3 — *Hellhound (1)–(3)*
  - Chapters 4–7 — *The Baskerville Dog (1)–(4)*
  - Chapters 8–11 — *Hounds of Hell (1)–(4)*
- **Active family:** **Chapters 12–13 — The Gluttonous Flies (1)–(2)**
- **Family boundary:** **VERIFIED**. Chinese Chapter 14 changes to `独食 (1)`; recovered English Chapter 14 is *Solitary (1)*.
- **Blocking issue:** none

## Rules that must not be lost

- Chinese raw = semantic/narrative authority.
- English Fandom wiki = canonical English authority for identified names/terms/locations/ranks/skills/monsters/organizations/titles where applicable.
- English MTL/XHTML = secondary alignment/phrasing witness only except Chapter 55.
- Do not sanitize or soften source content.
- Do not import wiki/MTL exposition that is absent from Chinese.
- Process complete contiguous title families; chapter/family/PR completion is a checkpoint, not a stopping condition.
- Never assume target N == MTL N without title/content verification.
- Protect reveal chronology.
- Keep information windows complete and atomic.

## Chapter 11 accepted-evidence reopen — completed

A stronger current Fandom result established that the numbered Baskerville techniques are canonically **Fangs**, not the earlier project fallback **Forms**.

Current Fandom evidence:
- `Sword Skills` / `Baskerville Clan/Swordsmanship` explicitly uses **Baskerville Fang Sword Style**, **1st Fang**, **2nd Fang**, **3rd Fang**, **4th Fang**, through **10th Fang**.

Chapter 11 was reopened for **canonical terminology only**; Chinese-governed semantics/mechanics were unchanged.

Updated evidence on this branch:
- `manuscript/drafts/chapter-0011.md` — draft SHA `eed36a1afd207edcf761034350426ff39c1fa8db`
- `qa/chapter-0011.md` — QA SHA `394d7610011f25000acda6a5d5e43bd02ac75571`
- `qa/families/hounds-of-hell-0008-0011.md` — family QA SHA `81e2e1f230a38e6693bf06c01908c910cdd35eec`
- `editorial/provenance/chapter-0011.json` — provenance SHA `d53caf5e2c825c9f2c85b399bf5c1b81ff99520c`
- `qa/acceptance/chapter-0011.json` — acceptance SHA `1b3e6c4906e5d13005a41bdc864f7bb5329f38d1`

Still pending synchronization after the current 12–13 batch: update Chapter 11’s acceptance SHA in `editorial/chapter-tracker.json` and replace remaining `Forms` wording in `editorial/GLOSSARY.md` / human-readable state as applicable.

## Active family boundary and mapping

Chinese:
- `012.txt` — `贪食的苍蝇 (1)` — SHA `9cbd4648873cda28a0e9410966d0643dda873968`
- `013.txt` — `贪食的苍蝇 (2)` — SHA `9187c6e887445ee9cd416f323939e7165f0ada4b`
- `014.txt` — `独食 (1)` — SHA `6985275ffc44d7d6cb13674567aeb7b4eb2abe57`, proving a new family starts at 14

Recovered English mappings are **verified by full content**, not merely title/number:
- target 12 → `source/chapters/chapter-012.xhtml` — *The Gluttonous Flies (1)* — SHA `594ce3566f95cc8983e1298a593967f41ab73c3f`
  - matches collapsed Cerberus opening, hidden dungeon, Cain/Abel note and riddle, ruby/shadow solution, sword-hilt endpoint.
- target 13 → `source/chapters/chapter-013.xhtml` — *The Gluttonous Flies (2)* — SHA `63a478d5df24e966953d739028801391a3d09727`
  - matches Beelzebub inscription/reveal, hunger, Hellhound/Cerberus feeding, three skill slots, Vikir sword-rank/Fang progression goal.

## Canonical English evidence for Chapters 12–13

Current indexed Fandom evidence establishes:

- **Cain Baskerville** / **Abel Baskerville** — twin Baskerville ancestors associated with the ancient dungeon.
- **Beelzebub** — canonical relic/demonic weapon name.
- **The Fly of Gluttony** — canonical alias/title associated with Beelzebub.
- **Gluttonous Blade** — canonical weapon title/description.
- **Seven Calamities** — canonical English form for the ancient group referenced by Chinese `七大灾难`.
- **Red Fang Mountain** — canonical location; Fandom Dungeon material identifies the dungeon as connected to Red Fang Mountain, a branch of Le Rouge et Le Noir Mountain.
- **Hemorrhage** — Hellhound (B+) slot ability.
- **Incinerate** — Cerberus (A+) slot ability.
- **Rapid Regeneration** — Brown Rat Norvegicus (F) slot ability.
- **Baskerville Fang Sword Style** / numbered **Fangs** for 1st–10th techniques.

Direct Fandom page access can be blocked by robots rules. Current search-indexed Fandom results are available and should be cited/recorded as indexed evidence rather than falsely described as successful direct-page refreshes.

## Chapter 12 source findings

- Opens directly on the collapsed/dead Cerberus from Chapter 11; greasy saliva and feces flow from its three mouths/anus.
- Cerberus’s post-death soul/karma/experience enters Vikir and strengthens body/spirit.
- Vikir cannot practically carry the corpse and plans to preserve important parts/organs and evidence.
- He infers a territory-guarding Cerberus likely protected a **dungeon** containing a strong demonic relic.
- He tracks it using Baskerville-hound perception; Cerberus scent/feces repel ordinary monsters.
- The dungeon connects toward **Red Fang Mountain**, a branch of Le Rouge et Le Noir Mountain; exposed ruby veins illuminate the chamber.
- Chinese shows **one skeleton** in the final chamber; recovered English incorrectly says **two skeletons**. Use Chinese.
- The note writer says to call him **Cain**; he and younger twin **Abel** spent three years misunderstanding the final riddle and Cain ultimately killed Abel.
- Riddle meaning is **shadow**, not fratricide: one person in darkness → person + shadow in ruby light → one again when ruby light is destroyed.
- Vikir smashes the ruby, opening an enormous hidden wall/door.
- Cain and Abel had already cleared the preceding monsters, leaving the reward path safe.
- Chapter ends as Vikir touches a sword hilt and reads an inscription stating only Baskerville blood may draw the named sword; the raw cuts at/around the relic-name revelation and Chapter 13 intentionally repeats/completes it.

## Chapter 13 source findings

- Opens by completing/repeating the inscription: only Baskerville blood can draw **Beelzebub**.
- Relic resembles an elongated black spike/rapier-like blade with three reddish bead-like structures and a green, fly-like hilt/form.
- Chinese calls it `贪食的苍蝇 巴尔泽布`; use canonical **The Fly of Gluttony, Beelzebub** where natural.
- Chinese establishes ancient **Seven Calamities** whose remains persisted with portions of their old power; Beelzebub is one such relic.
- **Critical MTL addition:** recovered English inserts several paragraphs about the seven family heads defeating one calamity each, Beelzebub being stored on the estate, later stolen by demons, battlefield ownership, and explicit fusion into Vikir’s palm. These paragraphs are **absent from Chinese Chapter 13** and must NOT be imported into the draft.
- The raw jumps from the basic Seven Calamities/remains explanation into Vikir’s abnormal hunger and Beelzebub responding to that hunger. Preserve the Chinese sequence even if the MTL is smoother.
- Beelzebub feeds on the dead Hellhound and gains a three-slot ability system.
- First window: **Hemorrhage — Hellhound (B+)** in Slot 1; Slots 2–3 empty.
- Beelzebub keeps feeding until the Hellhound corpse is nearly mummified.
- It then attacks the Cerberus corpse; Vikir stops it from damaging his exam evidence too badly.
- Second window after Cerberus/Brown Rat absorption:
  - Slot 1: **Incinerate — Cerberus (A+)**
  - Slot 2: **Hemorrhage — Hellhound (B+)**
  - Slot 3: **Rapid Regeneration — Brown Rat Norvegicus (F)**
- Stronger monster abilities can displace earlier/weaker slot occupants; do not over-systematize beyond source wording.
- Incinerate inflicts Cerberus hellfire burns that do not naturally heal; the source explicitly emphasizes severe burning pain lasting until death.
- Vikir assesses his current mana as roughly **4th Circle quantity**, while practical sword output remains around **High Sword Expert**, perhaps nearing **Low Sword Graduator**; he can draw three, perhaps four Fangs.
- In the previous life Vikir was limited to four Fangs; current Hugo can draw seven; future/pre-regression Hugo could draw nine.
- The **9th Fang** is restricted high-level family swordsmanship; Vikir knows of the legendary **10th Fang** material derived from the first patriarch / Seven Calamities experience.
- Vikir knows the 10th-Fang material is hidden among ordinary nearby books and expects **Hugo Le Baskerville** himself will unknowingly hand it to him.
- Chapter 14 begins after the practical examination, so Chapter 13 must stop before Chapter 14’s assessment-return sequence.

## Exact next actions

1. Draft Chapters 12–13 directly from Chinese using the verified canonical forms above.
2. Preserve the Chapter 12→13 deliberate inscription/relic overlap.
3. Exclude the MTL-only Beelzebub history/fusion paragraphs absent from Chinese.
4. Keep all Beelzebub ability windows atomic and use **Hemorrhage / Incinerate / Rapid Regeneration**.
5. Use **Fang** consistently for Baskerville numbered techniques.
6. QA Chapters 12 and 13 individually, then run a family QA across 11→12, 12→13, and 13→14.
7. Create hash-bound provenance/acceptance records.
8. Synchronize Chapter 11 reopened hashes plus new 12–13 acceptance into tracker/status/glossary/project/progress/handoff.
9. Merge the 12–13 family if clean.
10. Immediately determine and begin the Chapter 14 *Solitary* family; do not stop merely because the 12–13 PR merges.

## Persistent exceptions

- Chapter 55 Chinese raw missing; verified MTL 55 fallback.
- Combined raw containers retained intact: `075.txt`→75–76, `267.txt`→267–268, `284.txt`→284–285, `351.txt`→351–352, `353.txt`→353–354, `385.txt`→385–386, `495.txt`→495–496.
- Verified nontrivial mappings already recorded: target 75→MTL 74, 76→75, 267→265, 268→266.
