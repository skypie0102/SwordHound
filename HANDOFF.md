# SwordHound Session Handoff

> **Mandatory:** Read this file before beginning editorial work. Update it after every meaningful checkpoint and always before ending or handing work to another agent. Hash-bound accepted evidence wins over this file if they ever conflict.

## Handoff metadata

- **Last updated:** 2026-09-18
- **Updated by:** ChatGPT — Hunter and Hunted acceptance + 54/55 source repair
- **Working branch:** `editorial/restart-hunter-hunted-family`
- **Base main checkpoint:** `78647c415ffcbb15d23c3e456380c8ca85717975` (PR #22, Slaves of the Savage Tribe 52–54, merged)
- **Current PR:** #23 — `Rebuild The Hunter and the Hunted Chapters 55–60`
- **Pre-PR-stamp branch head:** `94408137b9568c9e4158721900849a669eb3179b`
- **Blocking issue:** none

## Authoritative current checkpoint

- **Target:** 500 chapters
- **Accepted:** **60**
- **Staged:** **0**
- **Next:** **Chapter 61**
- **Latest accepted family:** **Chapters 55–60 — The Hunter and the Hunted (1)–(6)**
- **Latest family QA:** `qa/families/hunter-hunted-0055-0060.md` — **PASS** — `7548d17fb51f4bd34059e026dcb523adcd21809e`
- **Next family:** **target Chapters 61–63 — The Protagonist of Hunting**
- **Following family begins:** target 64 — **Unfair Trade (1)**

## Rules that must not be lost

- Chinese raw = semantic/narrative authority wherever present.
- English Fandom/project canonical register = canonical English terminology authority.
- Recovered English MTL/XHTML = aligned secondary witness unless an explicitly documented Chinese gap requires scoped restoration.
- Never assume target N == recovered-English N; verify by complete content.
- Preserve explicitness; do not sanitize or intensify.
- Reproductive/body material must remain source-faithful and non-erotic unless the source itself explicitly requires otherwise.
- Protect reveal chronology.
- Process complete title families.
- Numbered Baskerville techniques are **Fangs**, not Forms.
- Every editorial session must update this file.

## Critical corpus repair — targets 54–55

The previous checkpoint incorrectly treated physical `054.txt` as target-54-only and target 55 as wholly missing in Chinese.

Direct overlap audit proved:

- physical `054.txt` is a **combined/overlapping 54–55 container**;
- corrected target 54 ends after Aiyen offers hunting as a route toward freedom and says they leave at dawn;
- `054.txt` then appends most target-55 body without a Chapter-55 heading;
- E54 supplies a short target-54 closing exchange missing at the Chinese splice;
- E55 supplies the missing target-55 opening/title boundary, then overlaps the Chinese target-55 body.

`source/chinese/chapter-exceptions.tsv` now records:
- target 54 → `054.txt` combined overlap;
- target 55 → `054.txt` partial combined overlap + E55 missing opening.

Chinese target coverage is therefore **500/500 at least partially**, with localized partial gaps in targets **49 and 55**.

### Rebound Slaves of the Savage Tribe evidence

Family QA: `qa/families/slaves-savage-tribe-0052-0054.md` — **PASS / rebound** — `ddde14abfe993392e9ea56dbfdb6f8e416896878`

| Ch. | Draft SHA | QA SHA | Provenance SHA | Acceptance SHA |
|---|---|---|---|---|
| 52 | `55c7ca51c4886c8b70ccb4121b341155f8362886` | `081f4684327d130cd87dcb20db5f13b298e8e752` | `7ac8c70900a00d99eb4b196ad12abed38e881b68` | `eece5f129c7d7f06d8bfc22f319f77c132054ef9` |
| 53 | `6864d9f5d6647ed4d048d718ebd691bf632fddb5` | `12dca40cfa5c826c88bb8f8950966a45afea8867` | `023e73bc5c5dad21c2129694ebc2c2be2bfb4245` | `1e71b783e085df4c8b5b8a6385bfc431f707f5c6` |
| 54 | `a73d3e3b1b8767cf932fd1a98963fbd0abe6aa69` | `c4fb3c2ed5166507df32fffe3262458e03fe9580` | `eef1d5b258b5c659ec710f7f3ee89005e96099c6` | `ab1dd4ed64c3630d8d3a9d5cd0e1a1c01905873c` |

## Accepted family — Chapters 55–60: The Hunter and the Hunted

### Resolved source mapping

- **55:** E55 unique opening/title boundary + target-55 Chinese body appended inside physical C054
- **56 → E56**
- **57:** no clean standalone recovered-English chapter; E56 partially overlaps Oxbear-selection setup
- **58 → E57**
- **59 → E58**
- **60 → E59**
- **E60 → target 61**, not target 60

### Immutable evidence

| Ch. | Chinese evidence SHA | English witness SHA | Draft SHA | QA SHA | Provenance SHA | Acceptance SHA |
|---|---|---|---|---|---|---|
| 55 | C054 `4e16871bc046c162978c419dc585f526b37d2dc4` | E55 `b3d243ed6bdbd0268e0281d18589d0b4c308604e` | `e18c5c382ca2fab4bb721c5b33e552f752b986bd` | `2b86dbfce94de0f26e8b77c5960909e35d12eed9` | `1c2bb41a273cc4c66e479694ec3ef190e7040e91` | `476c0641c59bffb1608ab58a34d2b9cbf075ff71` |
| 56 | `3347b3a5328b1e4629b4fea513c910aae2d851d5` | E56 `684b391e07bb916d944c1bea14ff642eb3007cac` | `ffa0d115bc4ab4ce7f147ad8e0755eb8d4a08694` | `cfb11c27d12eccfa7ceb398cf45e6b7594c92b9d` | `c8ed01bbdc6fad04508cfb531a5686f993084b55` | `4b26f3f5927c0212b89ac8078c12c622d596bd21` |
| 57 | `f54503f85e50714fca60b34ff319f4f7ae46166b` | partial E56 `684b391e07bb916d944c1bea14ff642eb3007cac` | `d899cea4cc984265211b60bea59fd46a545ee431` | `7f071afca07011058b38a354d119dac7bc5c7f48` | `15b2a77a50c8af73815dcdfcf84d9dc81563539e` | `b07414e9eebaf28018737dde31e6621a72b3c4a0` |
| 58 | `230b6b91bc511e93968956eb799aac9c44441c5e` | E57 `33f218cebdc7c91bdd8994b20d30465ecbaaebfa` | `b33b412e3aa3b789dc093dbee5cf9ac83e8fa6b0` | `403129422383f71784e7497e3b01764ab872e574` | `305ab77cc270e7610b739eeb43bd4e6dd171b72d` | `598dea0ed691896c7c289894b3ab2609c51b7431` |
| 59 | `c75833db41cf967973b4679cd6e43c9cfb774770` | E58 `1e572c7583b36443b10599e7128398bcf5529ea9` | `81f795ca217e845ef43e135d749081c3c12d5779` | `54d5b0e4a460771b9f5f34700f32db1f9bc7e8c2` | `b778217d3545828738c52f8dad3b130719c1a06b` | `f3ef9c8df491c47d3b02a23f04b548cdd27272df` |
| 60 | `406e7fe32dc61ee383a11d2405bf85f0684e4814` | E59 `5e13cc1bc24061a5a94eba0ad352e5126ee65bdd` | `df77f7700668f8d28bc7ec5f8afa83a02c8b5513` | `c35796d733c7b5b9728803a382be31d8214bcc95` | `3e109c419c440b2a3e6cbd5bff93b74a89ace4f0` | `d088b32bfb76859cbdbe26c10aa4b093d5162e30` |

### Accepted decisions

- Target 55 owns the hunting rite, public-urination joke, wolf-riding lesson, Ahun challenge, quiver theft, Aiyen punishment, and “Did it hurt?” endpoint.
- Target 56 preserves Bakira, Aiyen's archery lesson, and standard **Oxbear** window: **Danger Rating A / 5 m / Le Rouge et Le Noir Mountain, 7th Ridge**.
- The observed old female Oxbear is exceptional at roughly 8 m and is not forced into the standard 5 m specimen description.
- Target 57 preserves Ahun's >300 kg boar, waterfall ecology, cub/maternal behavior, mate-selection logic, and the coercive Ballak reproductive comparison.
- Target 58 preserves the three-day Oxbear breeding/exhaustion strategy clinically and non-graphically.
- Target 59 preserves bone/flesh-sucking mosquito danger, Cold Valley, practical liquor/jerky transfer, and the Oxbear counterattack.
- Target 60 uses **Low Sword Graduator**, not Gradient.
- Target 60 Beelzebub window: **Slot 1 Incinerate — Cerberus (A+)**.
- Oxbear kill remains explicit: heated arrows destroy the injured left eye; Beelzebub enters through mouth/palate/skull and burns the brain.
- Closing seed-collection contingency is retained clinically/non-erotically.

## Next family — target Chapters 61–63: The Protagonist of Hunting

Chinese:
- 61 `丰收节的主角 (1)` — `834abb36714ce9d7329e7854720ea20170ce5586`
- 62 `丰收祭的主角 (2)` — `68c0110eec864429aebd42142991ba3694d8130f`
- 63 `捕获祭典的主角 (3)` — `9db84e3df9443b7dbe9591327707cf2ff8677504`
- 64 switches to `不正当交易 (1)` — `332ef149eb32e1c0ba4aa67a53410d8d310f5844`

Recovered English:
- **E60** *The Protagonist of Hunting (1)* — `cf367731f723c719b61b06070cb648fa9cf23a95`
- **E61** *The Protagonist of Hunting (2)* — `c03318d7153f27b179a5d2d7c36f4fa1e78d9dc2`
- **E62** *The Protagonist of Hunting (3)* — `72c9b67ea93f772a9ab6adfce10f33f7de34ad`
- **E63** *Unfair Trade (1)* — `54c7cd980ebb6bc505aab824a8e5a26bbe40edfd`

Verified mapping:
- **target 61 → E60**
- **target 62 → E61**
- **target 63 → E62**
- **target 64 → E63**

## Exact next actions

1. Compare this branch against main; intended changes only.
2. Open and merge the 55–60 PR including the 54/55 corpus repair.
3. Create a fresh branch from merged main for target 61–63.
4. Read C61–63 + E60–62 completely, with C64/E63 as boundary witnesses.
5. Reconstruct, QA, provenance-bind, acceptance-bind, synchronize, merge, and continue into Unfair Trade.

## Persistent exceptions

- Target 49 — localized Chinese raw gap restored only from aligned English.
- Targets 54–55 — physical `054.txt` combined/overlapping container; target 55 missing opening supplied by E55.
- Other combined containers remain: `075.txt`→75–76, `267.txt`→267–268, `284.txt`→284–285, `351.txt`→351–352, `353.txt`→353–354, `385.txt`→385–386, `495.txt`→495–496.
