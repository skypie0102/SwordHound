# SwordHound Session Handoff

> **Mandatory:** Read this file before beginning editorial work. Update it after every meaningful checkpoint and always before ending or handing work to another agent. Hash-bound accepted evidence wins over this file if they conflict.

## Handoff metadata

- **Last updated:** 2026-09-18
- **Updated by:** ChatGPT — Hound of the Night acceptance checkpoint
- **Working branch:** `editorial/restart-hound-night-family`
- **Base main checkpoint:** `363e0a3b3d7659e5eb3e52944fdceb01b0ffed6c` (PR #27, The Red Death 72–74, merged)
- **Current PR:** pending
- **Blocking issue:** none

## Authoritative checkpoint

- **Accepted:** **77 / 500**
- **Staged:** **0**
- **Next:** **78**
- **Latest family:** targets **75–77 — The Hound of the Night (1)–(3)**
- **Family QA:** `qa/families/hound-night-0075-0077.md` — PASS — `ddfa912df3b33b86a1ee67c4315865c7d67bafc5`
- **Next family:** targets **78–82 — The Saintess (1)–(5)**
- **Following family:** target **83 — Lovesickness (1)**

## Source rules

- Chinese = semantic/narrative authority wherever present.
- Fandom/project register = canonical English proper names/terms.
- Recovered English = secondary alignment witness; scoped restoration only for documented Chinese gaps/splices.
- Preserve reveal chronology.
- Process full title families.
- Numbered Baskerville techniques = **Fangs**.
- Disease mechanics are fictional story content, not real-world medical guidance.
- Every session reads/updates this file.

## Corpus exceptions

- 500/500 targets have at least partial Chinese coverage.
- Localized gaps: targets 49 and 55.
- `054.txt` overlaps targets 54–55.
- `075.txt` combines targets 75–76 and is **unsplittable at raw-file level**:
  - no internal Chapter-76 marker;
  - target boundary contains an omission/overlap against E74/E75;
  - keep source intact; split reconstructed output by content.

## Accepted family — The Hound of the Night 75–77

Mapping:
- 75→E74
- 76→E75
- 77→E76
- 78→E77 begins The Saintess

| Ch. | Chinese evidence | English witness | Draft | QA | Provenance | Acceptance |
|---|---|---|---|---|---|---|
| 75 | C075 `e65af08f559f82f470687cc42c1d1420e1e55e15` | E74 `1bc968f310582423381420fc7e09e84aa4cf7e72` | `d5f09a9758fe8fc1b98a70bee19b586ffe1043a8` | `c1a6ed52d6982d2a3d0dd53bfa9580458ee2093b` | `4adb740e03554271a026abbee41bc99e188e1ad6` | `328c7ad3ba41eeee00e93e63775a3ca99ac21edf` |
| 76 | C075 `e65af08f559f82f470687cc42c1d1420e1e55e15` | E75 `68c385dab862c292c4fbf2cc571beb1b6483e9c0` | `d25cee273318020cce6b9c999cfdab91447c2795` | `966144f8bf892fd4e43f450507af2474ab19faa3` | `9e927e350e2297b0249b70ce18c5cf14b77a39f6` | `fbe936505d510ff62c73f619ec53f6a2e4f10558` |
| 77 | C077 `8800f5f079d10442f23e0d46f2674fcb3d8282ba` | E76 `47f1a314662aacaf5d0117a6fd461d15258c8b14` | `e1e686eb4c3ad3279809cda2f260ba5105d49a99` | `8a0eb293de2412bc54fe3073cfb64a5876e1344a` | `5a613b08198da8c4c60e0158d97bdd128ae37afa` | `054bb498e70fe1345c3f1a874e4ec710bb5c511e` |

### Key decisions

- Target75 = Chinese body + E74 missing close toward Quovadis.
- Target76 = E75 missing opening/context + Chinese slum/well/residence body.
- C075 travel-time contradiction resolved to **four days** from the explicit 2+1+1 itinerary plus E74.
- Pomeranian entrusted to Chihuahua in Underdog; Cindywendy/Judy trade-plan continuity retained.
- Target76's deliberate Red Death well contamination is kept only as source narrative wrongdoing; no added biological procedure.
- Vikir warns children away and seeks immediate Quovadis response.
- **Dolores L. Quovadis** spelling accepted; detailed age/profile held until target78.
- **Mozgus Quovadis** source-revealed target77; current estimate between Mid and High Sword Graduator.
- Vikir: High Sword Graduator, Kilogram Hammer (~600 kg), six Fangs, Incinerate—Cerberus(A+).
- Vikir defeats Mozgus nonlethally; Dolores appears to stop the fight.

## Next family — The Saintess 78–82

Verified headings/mapping:
- 78 C78 `155a238a81adfdc32ce7b97d9e28e05f4133c395` → E77 `64c564988053d5a39bde90c0f81685055f2bf13f`
- 79 C79 `97b3cae4efb581b22237affbbb71876d4178b3b3` → E78 `ec5ea6dada4c16d0f1b89b4d9c4ade8a701767b5`
- 80 C80 `207f6ca71403141a65fa7b56706adab81cc1d37d` → E79 `f5a35581349ff821b8085433f3f5e7221b3ee5ff`
- 81 C81 `b2ad1726acd434f02ec425e8736f672f4e07ca21` → E80 `292720b33c709d7fb636046cc50c3c3cea2e9eb8`
- 82 C82 `704f31d597c22867b02a29e256029d3c428c0fa3` → E81 `51f77bde7626a47169fb61b26b27cdbb16fda8b8`
- 83 C83 `482b93a20ef26c3c9dccceb3589f35cc09d1f12c` → E82 `43b6d40e033dbb1c5d0bf564cfe4d4a7fab22e1c` begins **Lovesickness (1)**.

## Exact next actions

1. Diff/open/merge the 75–77 checkpoint (expected PR #28).
2. Fresh branch from merged main.
3. Read C78–82 + E77–81 fully, with C83/E82 boundary.
4. Reconstruct/QA/provenance/accept all five Saintess chapters.
5. Promote state and continue into Lovesickness.
