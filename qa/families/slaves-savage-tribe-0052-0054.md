# Title-Family QA — Slaves of the Savage Tribe (1)–(3)

**Family status:** PASS — REBOUND AFTER 54/55 BOUNDARY AUDIT  
**Target range:** Chapters 52–54  
**Following family:** target Chapter 55 begins *The Hunter and the Hunted (1)*.

## Evidence

| Target | Chinese evidence | English witness | Draft SHA | Chapter QA |
|---|---|---|---|---|
| 52 | `052.txt` — `e2bc13949910b9abb7d4085e9cd858de1cca0e25` | E52 — `bfb4389c3f6342b2426691d03ea07af21e3c30cf` | `55c7ca51c4886c8b70ccb4121b341155f8362886` | `081f4684327d130cd87dcb20db5f13b298e8e752` |
| 53 | `053.txt` — `5205b110cfd0e74607d4dfcf49c71250c0d990cd` | E53 — `910996f812cb9ce17380cda49af7e5a9e3889e99` | `6864d9f5d6647ed4d048d718ebd691bf632fddb5` | `12dca40cfa5c826c88bb8f8950966a45afea8867` |
| 54 | `054.txt` — `4e16871bc046c162978c419dc585f526b37d2dc4` (container also appends most target 55) | E54 — `eb3146da8a6b112d89944b9142280e8282c375d2` | `a73d3e3b1b8767cf932fd1a98963fbd0abe6aa69` | `c4fb3c2ed5166507df32fffe3262458e03fe9580` |
| 55 boundary | no standalone 055.txt; most body overlaps inside 054.txt | E55 — `b3d243ed6bdbd0268e0281d18589d0b4c308604e` | next family | *The Hunter and the Hunted (1)* |

## Corrected 54/55 boundary

A direct overlap audit overturned the earlier assumption that `054.txt` was Chapter-54-only and target 55 had no Chinese content.

Physical `054.txt` contains:
1. the semantic body of target Chapter 54;
2. then, after the Chapter-54 hunt/freedom setup, most of target Chapter 55's hunting-ceremony → public-urination joke → wolf ride → Ahun conflict → Aiyen punishment sequence, without a new chapter heading.

Recovered E54 supplies a short Chapter-54 closing exchange missing at the splice: Vikir agrees to the hunt, Aiyen sets departure for dawn, and her suspicious reaction closes the chapter. Recovered E55 supplies the unique Chapter-55 opening about Ballak language/culture before converging with the Chinese overlap.

Accordingly:
- corrected Ch.54 stops at the E54 endpoint;
- appended Hunter/Hunted material is removed from Ch.54;
- target Ch.55 uses hybrid evidence rather than an English-only fallback.

This discovery is now recorded in `source/chinese/chapter-exceptions.tsv`.

## Family continuity / decisions

- Ch.52: post–Madam Eight-Legs survival, Ballak village, Thorn-Tree Punishment, Ahun hostility, Aiyen pool endpoint.
- Ch.53: debt repayment / husband-hunt vs slave distinction, Ballak communal culture, Akwilla reveal as chieftain/Aiyen's mother/current Night Fox.
- Ch.54: Vikir's shelter/domestic survival skills, Akwilla-tent repair, Ballak body/reproductive-health culture, slave/freedom discussion, and **hunt offer / dawn-departure endpoint**.
- The hunting rite, public-urination joke, wolf-riding lesson, Ahun challenge, pickpocketing, and Aiyen's punishment belong to **target Ch.55**, not Ch.54.
- Body/reproductive-health material remains factual and non-erotic.
- Akwilla's identity is allowed only from Ch.53 onward.

## Acceptance result

**PASS.** Chapters 52–54 remain a complete accepted family after correcting the 54/55 split. All dependent provenance/acceptance records must bind this revised family-QA hash and the corrected Chapter-54 draft/QA hashes.
