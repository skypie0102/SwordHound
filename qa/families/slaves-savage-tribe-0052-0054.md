# Title-Family QA — Slaves of the Savage Tribe (1)–(3)

**Family status:** PASS — REBOUND AFTER 54/55 BOUNDARY AUDIT  
**Target range:** Chapters 52–54  
**Following family:** target Chapter 55 begins *The Hunter and the Hunted (1)*.

## Evidence

| Target | Chinese evidence | English witness | Draft SHA | Chapter QA |
|---|---|---|---|---|
| 52 | `052.txt` — `e2bc13949910b9abb7d4085e9cd858de1cca0e25` | E52 — `bfb4389c3f6342b2426691d03ea07af21e3c30cf` | `2362b01b00650b2debfb9e4bbf50250197637bb0` | `8fa90d057e51c40a54e2682b343b3783ec19510f` |
| 53 | `053.txt` — `5205b110cfd0e74607d4dfcf49c71250c0d990cd` | E53 — `910996f812cb9ce17380cda49af7e5a9e3889e99` | `6864d9f5d6647ed4d048d718ebd691bf632fddb5` | `e6bc04e6c9fdd7f09d3382d2cfbe5e69b78d968f` |
| 54 | `054.txt` — `4e16871bc046c162978c419dc585f526b37d2dc4` (container also appends most target 55) | E54 — `eb3146da8a6b112d89944b9142280e8282c375d2` | `274fc97929edfe3ea8d48611c9aae775e45a9297` | `f5b85da05d2ba5d08c00033cda2baf2af3b6ef62` |
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

## Cycle-2 Phase 4 remediation and rebind

**Resolved:** 2026-09-26  
**Family result:** PASS after remediation and complete-family reread.

- Chapter 52: restored the explicit source injury mechanism—sharp rib ends from spiral fractures **pierce into Vikir's internal organs**.
- Chapter 53: full-family reread found no ordinary manuscript defect; safety-limited material remains unchanged.
- Chapter 54: narrative remains unchanged; its draft source note was corrected to match the already-established `054.txt` 54/55 overlap and E54 localized closing-gap repair.
- Sanitization and completeness gates were rerun across Chapters 52–54 after the repair.
- The 54→55 combined/overlap exception remains valid and unchanged.
- Chapter QA, provenance, acceptance, family QA, tracker bindings, and Cycle-2 ledger are refreshed across the family.

**Phase-4 disposition:** family clear; continue to **The Hunter and the Hunted (55–60)**.
