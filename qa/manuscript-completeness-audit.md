# Post-500 Manuscript Completeness Audit

**Opened:** 2026-09-20  
**Status:** ACTIVE  
**Target manuscript files present:** 500 / 500  
**Historical tracker state before audit:** 500 / 500 accepted  
**Confirmed rework as of opening audit:** Chapters 97, 316, 319, 420

## Why the completion claim was reopened

The 500 target manuscript files do exist, but a deterministic size scan exposed unusually compressed English drafts. Byte ratio is only a triage signal because Chinese UTF-8 and English encode differently, but the lowest-ratio chapters were suspicious enough to require direct raw comparison.

Direct reads confirmed that Chapters **97, 316, 319, and 420** preserve the broad plot while omitting substantial sentence-level narration, dialogue, descriptive detail, and transitions from their Chinese raws. They read as condensed summaries rather than full source-faithful translations. That violates the repository's no-dropped-material acceptance gate, so their prior PASS/accepted records are superseded for current-state purposes.

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
| 96 | Madam Eight-Legs (2) | 4461 | 7478 | 0.597 | priority review |
| 97 | Madam Eight-Legs (3) | 3971 | 10214 | 0.389 | CONFIRMED REWORK |
| 98 | Madam Eight-Legs (4) | 3432 | 8242 | 0.416 | priority review |
| 99 | Madam Eight-Legs (5) | 3542 | 8202 | 0.432 | priority review |
| 101 | Nostalgia (1) | 3928 | 8368 | 0.469 | priority review |
| 102 | Nostalgia (2) | 4906 | 9374 | 0.523 | priority review |
| 103 | Nostalgia (3) | 3233 | 6029 | 0.536 | priority review |
| 104 | Nostalgia (4) | 4585 | 9066 | 0.506 | priority review |
| 192 | Attack Land (3) | 6531 | 10933 | 0.597 | priority review |
| 196 | Attack Land (7) | 9981 | 16893 | 0.591 | priority review |
| 225 | Tuition (1) | 5848 | 9940 | 0.588 | priority review |
| 228 | Tuition (4) | 4510 | 9009 | 0.501 | priority review |
| 230 | Tuition (6) | 4335 | 7841 | 0.553 | priority review |
| 231 | Tuition (7) | 4862 | 8304 | 0.586 | priority review |
| 242 | National University League (7) | 6070 | 10365 | 0.586 | priority review |
| 307 | Hell Tree (1) | 4017 | 8431 | 0.476 | priority review |
| 308 | Hell Tree (2) | 4715 | 9194 | 0.513 | priority review |
| 309 | Hell Tree (3) | 3414 | 7938 | 0.430 | priority review |
| 310 | Hell Tree (4) | 3527 | 8910 | 0.396 | priority review |
| 311 | Hell Tree (5) | 3644 | 9625 | 0.379 | priority review |
| 312 | Hell Tree (6) | 3849 | 8401 | 0.458 | priority review |
| 313 | Hell Tree (7) | 4835 | 10739 | 0.450 | priority review |
| 314 | Surplus Man (1) | 5488 | 10580 | 0.519 | priority review |
| 315 | Surplus Man (2) | 3604 | 9368 | 0.385 | priority review |
| 316 | Surplus Man (3) | 3220 | 10102 | 0.319 | CONFIRMED REWORK |
| 317 | Surplus Man (4) | 4389 | 9656 | 0.455 | priority review |
| 318 | Surplus Man (5) | 3450 | 9299 | 0.371 | priority review |
| 319 | Surplus Man (6) | 3646 | 10996 | 0.332 | CONFIRMED REWORK |
| 320 | Surplus Man (7) | 4473 | 8611 | 0.519 | priority review |
| 321 | Underdogma (1) | 5882 | 10573 | 0.556 | priority review |
| 322 | Underdogma (2) | 5235 | 11796 | 0.444 | priority review |
| 323 | Underdogma (3) | 4592 | 10874 | 0.422 | priority review |
| 324 | Underdogma (4) | 3884 | 8380 | 0.463 | priority review |
| 325 | Underdogma (5) | 6698 | 12100 | 0.554 | priority review |
| 328 | The Shadowless King of the Black Sea (3) | 4534 | 7782 | 0.583 | priority review |
| 333 | The Mating Room (1) | 4485 | 7916 | 0.567 | priority review |
| 334 | The Mating Room (2) | 3927 | 8099 | 0.485 | priority review |
| 419 | Goodbye, Nouvelle Vague (1) | 4378 | 7445 | 0.588 | priority review |
| 420 | Goodbye, Nouvelle Vague (2) | 4622 | 13293 | 0.348 | CONFIRMED REWORK |
| 421 | Goodbye, Nouvelle Vague (3) | 5096 | 10793 | 0.472 | priority review |
| 431 | The Lion King (2) | 3760 | 8319 | 0.452 | priority review |

## Completed family reviews

### The Illiad — Chapters 85–89 — REBUILT / PASS

Direct Chinese comparison showed **all five** historical drafts were materially compressed. Only Chapters 87–89 appeared in the initial <0.60 priority queue; Chapters 85–86 were above the threshold but still failed full-coverage review. All five were rebuilt on 2026-09-20 and rebound to fresh QA/provenance/acceptance evidence.

Important corrections include Aiyen's bow requiring roughly five people's strength rather than having “five strings,” restoration of Ah'Heman's full Leviathan/Bourgeois authority scheme and political trap, restoration of the full Illiad background, and restoration of Chapter89's crushing rear impact before the Oxbear reveal.

**Pending initial priority queue:** 41 chapters (down from 47).  
**Next family:** Madam Eight-Legs (95–100).

### The Ghosts of the Ancestors — Chapters 90–94 — REBUILT / PASS

Direct Chinese comparison showed **all five** historical drafts were materially compressed. Only Chapters 92–94 were in the initial <0.60 queue; Chapters 90–91 were above the threshold but still failed full-coverage review.

The rebuild restores the Oxbear conclusion and Ah'Heman's identity collapse, the full natural-law/Death-Knight explanation, Adonai's master-level bow mechanics, the complete Akwilla–Adonai wind-return duel, the ancestor-blood hostage tactic, salt-river purification, Adonai-bow recovery, and the complete Thorn-Tree Punishment ending.

**Pending initial priority queue:** 41 chapters.  
**Next family:** Madam Eight-Legs (95–100), including confirmed-failure Chapter 97.

## Confirmed failures

### Chapter 97 — Madam Eight-Legs (3)
Direct raw/draft comparison confirms aggressive condensation. The draft retains the monster setup and broad sequence but drops many source sentences and descriptive/causal details.

### Chapter 316 — Surplus Man (3)
Direct raw/draft comparison confirms summary-style compression. Extended survivor dialogue, voting discussion, social dynamics, and narrative transitions are collapsed into terse fragments.

### Chapter 319 — Surplus Man (6)
Direct raw/draft comparison confirms summary-style compression across the Daylily fight, bodily-material bait preparation, reward sequence, and scene-level narration.

### Chapter 420 — Goodbye, Nouvelle Vague (2)
Direct raw/draft comparison confirms summary-style compression. The draft preserves the major escape/fight beats but omits substantial source-level dialogue, action detail, and connective narration.

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
