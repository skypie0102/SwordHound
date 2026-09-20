# Post-500 Manuscript Completeness Audit

**Opened:** 2026-09-20  
**Status:** COMPLETE  
**Target manuscript files present:** 500 / 500  
**Historical tracker state before audit:** 500 / 500 accepted  
**Confirmed rework as of opening audit:** Chapters 97, 316, 319, 420

## Why the completion claim was reopened

The 500 target manuscript files do exist, but a deterministic size scan exposed unusually compressed English drafts. Byte ratio is only a triage signal because Chinese UTF-8 and English encode differently, but the lowest-ratio chapters were suspicious enough to require direct raw comparison.

Direct reads confirmed that Chapters **97, 316, 319, and 420** originally preserved the broad plot while omitting substantial sentence-level narration, dialogue, descriptive detail, and transitions from their Chinese raws. All four were rebuilt and re-accepted during the priority-family pass. A later whole-corpus residual pass then found one additional completeness failure above the original cutoff: **Chapter 59**, which was likewise rebuilt and re-bound.

Representative example: Chapter 316 is **3,220 draft bytes vs 10,102 Chinese-raw bytes (0.319)**. The raw contains extended dialogue and narrative beats that the draft collapses into short bullet-like fragments. Chapter 319 (0.332), Chapter 420 (0.348), and Chapter 97 (0.389) show the same pattern on direct inspection.

## Triage methodology

For ordinary one-target Chinese containers, compute:

`draft byte size / Chinese raw byte size`

This is **not** a quality score and must never be used alone to reject a chapter. It is only a fast omission/compression detector. Shared/combined raw containers are excluded because one physical raw can cover multiple targets. The Chapter 54/55 overlap container is also excluded.

The corpus median is about **0.85**. The initial priority queue is every ordinary chapter below **0.60**. Chapters below **0.50** are strong suspects and should be inspected first within their complete title family.

## Priority review queue

| Chapter | Title | Draft bytes | Raw bytes | Ratio | State |
| ---: | --- | ---: | ---: | ---: | --- |
| 87 | The Illiad (3) | 5679 | 10774 | 0.527 | REBUILT — PASS |
| 88 | The Illiad (4) | 5530 | 9280 | 0.596 | REBUILT — PASS |
| 89 | The Illiad (5) | 4972 | 9514 | 0.523 | REBUILT — PASS |
| 92 | The Ghosts of the Ancestors (3) | 4699 | 8364 | 0.562 | REBUILT — PASS |
| 93 | The Ghosts of the Ancestors (4) | 5561 | 10276 | 0.541 | REBUILT — PASS |
| 94 | The Ghosts of the Ancestors (5) | 4847 | 8456 | 0.573 | REBUILT — PASS |
| 96 | Madam Eight-Legs (2) | 4461 | 7478 | 0.597 | REBUILT — PASS |
| 97 | Madam Eight-Legs (3) | 3971 | 10214 | 0.389 | REBUILT — PASS |
| 98 | Madam Eight-Legs (4) | 3432 | 8242 | 0.416 | REBUILT — PASS |
| 99 | Madam Eight-Legs (5) | 3542 | 8202 | 0.432 | REBUILT — PASS |
| 101 | Nostalgia (1) | 3928 | 8368 | 0.469 | REBUILT — PASS |
| 102 | Nostalgia (2) | 4906 | 9374 | 0.523 | REBUILT — PASS |
| 103 | Nostalgia (3) | 3233 | 6029 | 0.536 | REBUILT — PASS |
| 104 | Nostalgia (4) | 4585 | 9066 | 0.506 | REBUILT — PASS |
| 192 | Attack Land (3) | 6531 | 10933 | 0.597 | REBUILT — PASS |
| 196 | Attack Land (7) | 9981 | 16893 | 0.591 | REBUILT — PASS |
| 225 | Tuition (1) | 5848 | 9940 | 0.588 | REBUILT — PASS |
| 228 | Tuition (4) | 4510 | 9009 | 0.501 | REBUILT — PASS |
| 230 | Tuition (6) | 4335 | 7841 | 0.553 | REBUILT — PASS |
| 231 | Tuition (7) | 4862 | 8304 | 0.586 | REBUILT — PASS |
| 242 | National University League (7) | 6070 | 10365 | 0.586 | REBUILT — PASS |
| 307 | Hell Tree (1) | 4017 | 8431 | 0.476 | REBUILT — PASS |
| 308 | Hell Tree (2) | 4715 | 9194 | 0.513 | REBUILT — PASS |
| 309 | Hell Tree (3) | 3414 | 7938 | 0.430 | REBUILT — PASS |
| 310 | Hell Tree (4) | 3527 | 8910 | 0.396 | REBUILT — PASS |
| 311 | Hell Tree (5) | 3644 | 9625 | 0.379 | REBUILT — PASS |
| 312 | Hell Tree (6) | 3849 | 8401 | 0.458 | REBUILT — PASS |
| 313 | Hell Tree (7) | 4835 | 10739 | 0.450 | REBUILT — PASS |
| 314 | Surplus Man (1) | 5488 | 10580 | 0.519 | REBUILT — PASS |
| 315 | Surplus Man (2) | 3604 | 9368 | 0.385 | REBUILT — PASS |
| 316 | Surplus Man (3) | 3220 | 10102 | 0.319 | REBUILT — PASS |
| 317 | Surplus Man (4) | 4389 | 9656 | 0.455 | REBUILT — PASS |
| 318 | Surplus Man (5) | 3450 | 9299 | 0.371 | REBUILT — PASS |
| 319 | Surplus Man (6) | 3646 | 10996 | 0.332 | REBUILT — PASS |
| 320 | Surplus Man (7) | 4473 | 8611 | 0.519 | REBUILT — PASS |
| 321 | Underdogma (1) | 5882 | 10573 | 0.556 | REBUILT — PASS |
| 322 | Underdogma (2) | 5235 | 11796 | 0.444 | REBUILT — PASS |
| 323 | Underdogma (3) | 4592 | 10874 | 0.422 | REBUILT — PASS |
| 324 | Underdogma (4) | 3884 | 8380 | 0.463 | REBUILT — PASS |
| 325 | Underdogma (5) | 6698 | 12100 | 0.554 | REBUILT — PASS |
| 328 | The Shadowless King of the Black Sea (3) | 4534 | 7782 | 0.583 | REBUILT — PASS |
| 333 | The Mating Room (1) | 4485 | 7916 | 0.567 | REBUILT — PASS |
| 334 | The Mating Room (2) | 3927 | 8099 | 0.485 | REBUILT — PASS |
| 419 | Goodbye, Nouvelle Vague (1) | 4378 | 7445 | 0.588 | REBUILT — PASS |
| 420 | Goodbye, Nouvelle Vague (2) | 4622 | 13293 | 0.348 | REBUILT — PASS |
| 421 | Goodbye, Nouvelle Vague (3) | 5096 | 10793 | 0.472 | REBUILT — PASS |
| 431 | The Lion King (2) | 3760 | 8319 | 0.452 | REBUILT — PASS |

## Completed family reviews

### The Illiad — Chapters 85–89 — REBUILT / PASS

Direct Chinese comparison showed **all five** historical drafts were materially compressed. Only Chapters 87–89 appeared in the initial <0.60 priority queue; Chapters 85–86 were above the threshold but still failed full-coverage review. All five were rebuilt on 2026-09-20 and rebound to fresh QA/provenance/acceptance evidence.

Important corrections include Aiyen's bow requiring roughly five people's strength rather than having “five strings,” restoration of Ah'Heman's full Leviathan/Bourgeois authority scheme and political trap, restoration of the full Illiad background, and restoration of Chapter89's crushing rear impact before the Oxbear reveal.

**Pending initial priority queue:** 0 chapters (down from 47).  
**Next family:** Attack Land (190–196).

### The Ghosts of the Ancestors — Chapters 90–94 — REBUILT / PASS

Direct Chinese comparison showed **all five** historical drafts were materially compressed. Only Chapters 92–94 were in the initial <0.60 queue; Chapters 90–91 were above the threshold but still failed full-coverage review.

The rebuild restores the Oxbear conclusion and Ah'Heman's identity collapse, the full natural-law/Death-Knight explanation, Adonai's master-level bow mechanics, the complete Akwilla–Adonai wind-return duel, the ancestor-blood hostage tactic, salt-river purification, Adonai-bow recovery, and the complete Thorn-Tree Punishment ending.

**Pending initial priority queue:** 0 chapters (down from 47).  
**Next family:** Madam Eight-Legs (95–100), including confirmed-failure Chapter 97.

### Madam Eight-Legs — Chapters 95–100 — REBUILT / PASS

All six historical drafts had completeness or boundary-integrity problems. Chapters 96–99 were in the initial priority queue; Chapter97 was one of the four directly confirmed failures. Chapter95 was above the threshold but compressed and contains a verified localized Chinese omission. Chapter100 crossed into target101.

Repairs include the full Ballak-village/altar sequence, scoped E94 restoration for the C095 Aheul bridge, complete Bakira/Aiyen departure scene, full Bog Salamander/Bone-Sucking Mosquito preparation, summit climb and named dead, detailed Madam combat/regeneration mechanics, and a corrected target100 ending at the prepared Bog Salamander cushion.

**Chapter97 confirmed failure: RESOLVED.**  
**Current unresolved confirmed failures:** 420.  
**Pending initial priority queue:** 0 chapters (down from 47).  
**Next family:** Attack Land (190–196).

### Nostalgia — Chapters 101–104 — REBUILT / PASS

All four historical drafts were materially compressed and have been rebuilt. The family also closes the corrected target100/101 boundary: target100 ends before impact; target101 exclusively owns the landing, Madam death, Venom acquisition, collapse, and rescue sequence.

Restored material includes the full Bog Salamander impact mechanics, Madam's death/karma and Beelzebub slot struggle, Aiyen's three-day rescue and the >4,000-person tribal gathering, Peak Sword Graduator/Seventh Fang analysis, Bakira husbandry sequence, Ballak's no-goodbye philosophy, complete multi-tribe farewell, Camus/Colosseo recollection, and Aiyen's Anubis/collar/farewell sequence.

**Pending initial priority queue:** 0 chapters (down from 47).  
**Next family:** Attack Land (190–196), containing priority targets 192 and 196.

### Attack Land — Chapters 190–196 — REBUILT / PASS

All seven historical drafts were materially compressed, not only priority targets 192 and 196. The rebuild restores the complete attack-test mechanics, Sadi/Banshee institutional conflict, Sinclaire and Pigi examinations, Vikir's joint-targeting setup, returning-arrow sequence, Sadi aftermath, final rankings, faction attention, and Cindywendy hook.

Verified raw repairs remain explicit: C192's endpoint name slip resolves to **Pigi**, and C193's isolated department-label drift does not move Pigi out of **Cold Department Class B**.

**Pending initial priority queue:** 0 chapters (down from 47).

### Tuition — Chapters 225–233 — REBUILT / PASS

All nine historical drafts were materially compressed, not only priority targets 225, 228, 230, and 231. The rebuild restores the newspaper/tuition setup, financial-security reasoning, Sherpa/MiniPin recruitment arc, repeated home intrusions, Gnoll colony extermination, Poison Gnoll and hidden-bank-gold sequence, full Ms. Ouroboros encounter, appraisal/recruitment details, Thrifty Bazaar economics, and the anonymous Peri Award scholarship donation.

**Pending initial priority queue:** 0 chapters (down from 47).  
**Next family:** National University League (236–244), containing priority target 242.

### National University League — Chapters 236–244 — REBUILT / PASS

All nine historical drafts were materially compressed, not only priority target 242. Rebuild restores the four-school League setup, Decarabia-vault motive, Magic Train journey, Granola/triplet compartment sequence, train-roof escape, Lovegood/Sinclaire confrontation, Mage Tower dimensional lore, competitor profiles, corrected 70%-of-original lodging charge, Varangian buffet conflict, Bollason arm-wrestling sequence, >30 challengers, and Bakilaga/Ballak recognition.

Progression guards remain intact: Bakilaga's prior public level is peak Sword Expert with current Sword Graduator only rumored; Eighth Fang remains future setup; Vikir/Bakilaga has no pin or declared winner.

**Pending initial priority queue:** 0 chapters (down from 47).  
**Next family:** Underdogma (321–325).

### Hell Tree — Chapters 307–313 — REBUILT / PASS

All seven historical drafts were materially compressed and all seven were initial-priority targets. The rebuild restores the exterior rescue crisis and inverted-tree lore; Amdusias tower / Level System mechanics; acid-vomit stat-candy recovery; corrupted Colosseo and scent-bait setup; exact 108 students / 108 Hell Hounds / 108 minutes mission; Granola betrayal/rescue; B+ Hell Hound pack clear; Sabik-ginkgo strategy; A+ Cerberus Bonus Stage; exact 230/219/244 candy spike; project-canonical Immortality — Gargoyle (S) regeneration; Physical Resistance unlock; Fairy Candy Shop; deliberate Level1 reward exploitation; and the 69-survivor Floor3 transition.

**Pending initial priority queue:** 0 chapters (down from 47).  
**Next family:** Underdogma (321–325).

### Surplus Man — Chapters 314–320 — REBUILT / PASS

All seven historical drafts were materially compressed; all seven were initial-priority targets. Confirmed failures **316** and **319** were fully rebuilt and re-accepted. The rebuild restores the ruined-Capital warmth/hunger setup, Daylily awakening and Random Box/Mimic rules, full survivor sacrifice/cannibalism debate and vote, Vikir's anti-sacrifice plan, pooled Random Boxes/items, Silver Reflexes unlock, complete S-rank Daylily battle, pooled nonlethal biological bait, exact reward sequence, Conversion Bug reward-skimming reveal, Daylily seed harvest, and the forced Floor4 transition.

**Current tracker state:** 499 accepted / 1 confirmed needs rework.  
**Current unresolved confirmed failures:** none.  
**Pending initial priority queue:** 0 chapters.  
**Next family:** Underdogma (321–325).

### Underdogma — Chapters 321–325 — REBUILT / PASS

All five historical drafts were materially compressed and all five were initial-priority targets. The rebuild restores Black Sea no-buoyancy mechanics, fungal-sand/world-fragment ecology, Hell Tree sap limits, Dogma/Commoner-Faction chronology, chained-triplet abuse and survival logic, Dogma's Dolores/grievance history, Vikir's demonization analysis, Beetleman encounter and Giant Beetle Island lore, Dogma's sap-driven Majin transformation, dual mission state, full A+ Underdogma fight, reverse Candy Shop exchange, Conversion Bug losses, and final **Magic Resistance +1** sixth-stat unlock.

**Pending initial priority queue:** 0 chapters.  
**Next family:** The Shadowless King of the Black Sea (326–330), containing priority target 328.

### The Shadowless King of the Black Sea — Chapters 326–330 — REBUILT / PASS

All five historical drafts were materially compressed, not only priority target 328. The rebuild restores six-stat/Level1 reward logic, Fire of Inferiority — Blaze, Beetlemen ship construction and salvage, Black Sea dive mechanics, the independent S-rank Shadowless King profile, canonical Beelzebub slots, Starvation Drought anti-regeneration, Daylily-seed buoyancy, timed oil-paper-bag dissolution, story-world pressure-ascent damage, Beetlemen ship propulsion, field-knot gas-sac clustering, Baby Madam silk extraction, Bianca's tactical precedent, and separate A+ Majin / S-rank achievement notices.

**Pending initial priority queue:** 0 chapters.  
**Next family:** The Mating Room (333–338), containing priority targets 333 and 334.

### The Mating Room — Chapters 333–338 — REBUILT / PASS

All six historical drafts were materially compressed, with the strongest losses in initial-priority targets 333–334. The rebuild restores the Floor4→Floor9 skip, full Dragon Majin laboratory/specimen-room worldbuilding, three-stage coercive enclosure mechanics, Giant Mantis demonstration, temperature/hypothermia pressure, complete Floor5 friendship-game mission, Return Scroll logic, Sinclaire's Bourgeois/Bartolomeo memory, clinically framed hypothermia treatment, blue-mist escalation, exact 300/300/300 stat state, rain-apparatus sabotage, source-timed Night Hound reveal, enclosure escape, Lost Paradise gate, and forced Sinclaire rescue.

**Pending initial priority queue:** 0 chapters.  
**Next family:** Goodbye, Nouvelle Vague (419–421), containing priority targets 419–421 and confirmed failure 420.

### Goodbye, Nouvelle Vague — Chapters 419–421 — REBUILT / PASS

All three chapters were re-audited and rebuilt for complete coverage. Chapter **420**, the final confirmed completeness failure, is fully resolved. The family rebuild restores the Level-Five escape route and Current3021 logic, Rain of Fear memory, source-gap-safe Garam/Kirko exchange, deep-sea Marquis de Sade/Sadi hitch sequence, Orca's killer-whale advantages, ten-thousand-meter combat, deliberate Aiyen/Sadi separation, exact Gate of Good and Evil dimensions/impact, volcanic uncorking, Gate+Wailing Wall ascent shell, original-timeline Orca/Sade/Poseidon history, and canonical Gargoyle regeneration.

**Current tracker:** 500 accepted / 0 needs rework.  
**Pending initial priority queue:** 0 chapters.  
**Next/final priority family:** The Lion King (430–433), containing target431.

### The Lion King — Chapters 430–433 — REBUILT / PASS

All four historical drafts were materially compressed, not only final priority target 431. The rebuild restores the coastal anomaly/civilian-fear setup, secret Donquixote infiltration, fully demonized guards, Cervantes's self-sacrifice before possession, advanced Red Death/Leviathan toxin continuity, Gungnir succession, Chimeries's decade-long replacement-body plan, recklessness authority, Amdusias S+ remnant logic, Hell-Tree mental trap, Vikir's inner-world landscape, and the inner-world-only Vikir endpoint.

**Final initial-priority target 431: RESOLVED.**  
**Original priority queue:** 47 / 47 resolved.  
**Strong-suspect queue:** 22 / 22 resolved.  
**Confirmed needs rework:** none.  
**Current tracker:** 500 accepted / 0 needs rework.  
**Completeness audit:** COMPLETE.

## Confirmed failures

### Chapter 97 — Madam Eight-Legs (3) — RESOLVED

Historical draft was confirmed summary-compressed. The complete Madam Eight-Legs family (95–100) was rebuilt on 2026-09-20; Chapter97 now has fresh draft/QA/provenance/acceptance evidence and is accepted again.


### Chapter 316 — Surplus Man (3) — RESOLVED
Historical draft was confirmed summary-compressed. The complete Surplus Man family (314–320) was rebuilt on 2026-09-20; Chapter316 now restores the full survivor debate, voting process, hierarchy collapse, coercion, and social transitions and is accepted again.

### Chapter 319 — Surplus Man (6) — RESOLVED
Historical draft was confirmed summary-compressed. The complete Surplus Man family (314–320) was rebuilt on 2026-09-20; Chapter319 now restores the full Daylily fight, pooled nonlethal biological bait preparation, reward sequence, and connective narration and is accepted again.

### Chapter 420 — Goodbye, Nouvelle Vague (2) — RESOLVED
Historical draft was confirmed summary-compressed and has now been fully rebuilt against Chinese source coverage. The rebuilt version restores the omitted dialogue, action detail, and connective narration while preserving the source boundary and terminology guards.

## Audit rules going forward

1. Do not equate file existence with editorial completeness.
2. Audit the **entire contiguous title family** whenever any member is flagged.
3. Compare full Chinese source coverage, not only plot-event coverage.
4. A polished summary is still a failure if source information, dialogue, descriptive beats, or transitions were dropped.
5. Byte ratio remains triage only; unflagged chapters can still fail and flagged chapters can still pass after direct review.
6. Do not proceed to complete-EPUB assembly until this completeness audit is closed.
7. When a chapter is rebuilt, replace its stale QA/provenance/acceptance evidence and restore tracker status only after full coverage QA.

## Family-first review order

Start from the earliest flagged family and proceed in target order:

- The Illiad — 85–89
- The Ghosts of the Ancestors — 90–94
- Madam Eight-Legs — 95–100
- Nostalgia — 101–104
- Attack Land — audit the complete family containing 192 and 196
- Tuition — audit the complete family containing 225, 228, 230, 231
- National University League — audit the complete family containing 242
- Hell Tree — 307–313
- Surplus Man — 314–320
- Underdogma — 321–325
- The Shadowless King of the Black Sea — audit the complete family containing 328
- The Mating Room — audit the complete family containing 333–334
- Goodbye, Nouvelle Vague — 419–421
- The Lion King — 430–433

After priority families, run a whole-corpus completeness pass so chapters above the size threshold are not assumed safe.

## Whole-corpus residual pass

After the original 47-chapter priority queue and 22 strong-suspect queue were cleared, the audit did **not** close immediately. A fresh post-rebuild size scan was run across the ordinary one-target Chinese containers.

### Residual scan result

- Ordinary one-target raw/draft pairs compared: **484**
- Post-rebuild median draft/raw byte ratio: **~0.904**
- Unresolved ordinary chapters below the original **0.60** trigger: **0**
- Expanded low-tail review threshold: **<0.70** (triage only)
- Expanded low-tail chapters: **28**
- Title families represented: **15**

The 28 expanded low-tail chapters were:

`57, 59, 64, 65, 66, 67, 70, 77, 80, 81, 136, 176, 181, 211, 213, 214, 220, 300, 301, 331, 409, 422, 423, 424, 443, 445, 446, 448`.

Review used multiple signals rather than byte ratio alone:

1. raw/draft structural retention;
2. paragraph-level coverage against the verified aligned English witness where available;
3. existing title-family boundary/QA records;
4. direct Chinese reads for suspicious outliers.

### New residual failure: Chapter 59 — RESOLVED

The expanded pass found that **Chapter 59 — The Hunter and the Hunted (5)** was materially compressed even though its historical byte ratio (**0.625**) sat above the original 0.60 trigger.

Direct C059 comparison showed ordinary source material had been collapsed around:

- tracking cues and rain-erased trail logic;
- scented-fruit bait / Bakira smell tracking;
- the exact swamp mosquito categories and prior casualty context;
- Cold Valley terrain, shelter construction, and temperature detail;
- Vikir's Age-of-Destruction memories and near-instant sleep habit;
- the jerky/liquor feeding setup, weight banter, Bakira exchange, and attack transition.

Chapter 59 was rebuilt and re-QA'd on 2026-09-20. Its Hunter-and-Hunted family QA plus provenance/acceptance chain for Chapters 55–60 were rebound to fresh hashes. Underage sexualized body-contact detail remains safety-limited and summarized nonsexually; ordinary narrative, plot, survival, and continuity information is restored.

Post-rebuild, only **1 / 132** aligned E58 paragraphs fell below the conservative lexical-overlap floor used as a secondary coverage detector (**0.8%**), consistent with paraphrase rather than missing content.

### Residual families revalidated

The remaining low-tail families were revalidated and did not produce additional completeness failures:

- Unfair Trade (64–67)
- Blood Relatives (68–71)
- The Hound of the Night (75–77)
- The Saintess (78–82)
- Test Your Skills (133–138)
- The 99 Hits With 100 Shots (176–178)
- Midterm Random Defense (179–185)
- Festival Night (206–215)
- That Day, Him and Me (220–224)
- The Age of the Warmonger (299–306)
- Draw (331–332)
- End game (409–418)
- How to Become a Wandering Knight (422–424)
- The Fall of Usher (441–449)

Direct reads of the strongest mismatch cases confirmed that their low ratios or low lexical overlap came from encoding/prose style/heavy rephrasing rather than missing source sequence coverage.

**Residual pass result:** **PASS — no unresolved completeness failures remain.**

## Audit completion

The post-500 manuscript completeness audit is **COMPLETE** as of 2026-09-20.

- Initial priority queue: **47 / 47 resolved**.
- Strong-suspect queue: **22 / 22 resolved**.
- Original confirmed completeness failures resolved: **97, 316, 319, 420**.
- Additional residual failure found and resolved: **59**.
- Whole-corpus residual low-tail pass: **COMPLETE**.
- Current tracker: **500 accepted / 0 needs rework**.
- No unresolved completeness failures remain.
