# Full Manuscript Sanitization + Completeness Audit — Cycle 2

**Opened:** 2026-09-21  
**Status:** ACTIVE — IMMEDIATE PROJECT PRIORITY  
**Scope:** Target Chapters 1–500  
**Historical accepted state at opening:** 500 / 500  
**Current audit disposition:** prior acceptance retained as historical evidence, but every chapter requires fresh Cycle-2 revalidation  
**EPUB assembly:** BLOCKED until this audit is formally closed  
**Current stage:** Phase 3 ACTIVE — full-corpus boundary/alignment/exception integrity verification

## Progress

### Phase 1 — COMPLETE

**Full-corpus result**

- reviewed: **500 / 500**
- PASS: **282**
- FAIL: **200**
- SAFETY-LIMITED-REVIEWED: **18**
- manuscript edits during discovery: **0**
- all 200 FAIL chapters remain deferred to Phase 4

Wave accounting:
- Wave A (1–100): **62 PASS / 20 FAIL / 18 safety-limited**
- Wave B (101–202): **70 PASS / 32 FAIL**
- Wave C (203–306): **52 PASS / 52 FAIL**
- Wave D (307–402): **47 PASS / 49 FAIL**
- Wave E (403–500): **51 PASS / 47 FAIL**

Evidence: `qa/cycle2-phase1-summary.md`, the five wave summaries, family evidence under `qa/cycle2/sanitization/`, and `qa/cycle2-ledger.json`.

### Phase 2 — COMPLETE

- completeness reviewed: **500 / 500**
- PASS: **229**
- FAIL: **271**
- 198 failures overlap ordinary Phase-1 FAIL chapters
- 73 are additions beyond the Phase-1 FAIL queue: **42, 48, 55, 61, 63, 69, 70, 71, 72, 78, 79, 80, 82, 101, 103, 141, 150, 151, 152, 153, 154, 156, 165, 168, 175, 178, 180, 181, 182, 183, 184, 187, 190, 192, 193, 200, 207, 211, 212, 216, 217, 236, 259, 264, 266, 271, 273, 275, 281, 282, 283, 300, 307, 326, 329, 331, 332, 335, 399, 400, 403, 406, 412, 422, 425, 446, 451, 471, 483, 496, 497, 498, 499**
- Phase-1-only FAILs that passed completeness: **35, 262**
- combined Phase-1/Phase-2 remediation population: **273 unique chapters**
- remediation metadata: **273 / 273** union chapters queued
- family completeness: **23 PASS / 95 FAIL / 0 pending**
- manuscript edits during Phase-2 discovery: **0**

Closure checkpoint: `qa/cycle2-phase2-checkpoint-0500.md`. Family evidence is under `qa/cycle2/completeness/` and the authoritative live ledger is `qa/cycle2-ledger.json`.

### Phase 3 — ACTIVE

Boundary/alignment review is the immediate project focus.

- reviewed: **402 / 500** targets;
- PASS: **53**;
- FAIL: **2**;
- EXCEPTION-DOCUMENTED: **347**;
- families reviewed: **98 / 118**;
- family PASS: **14**;
- family FAIL: **2**;
- family EXCEPTION-DOCUMENTED: **82**;
- genuine source-exception rows added during Phase 3: **333**;
- manuscript edits during Phase 3: **0**;
- open structural FAILs: **273, 283**;
- latest checkpoint: `qa/cycle2-phase3-checkpoint-0402.md`;
- next family: **Jailbreaker (403–408)**;
- exception-table normalization: **75 redundant replay rows removed; all 36 baseline rows preserved**.

## Phase 3 — Corpus boundary, alignment, and exception integrity pass

**Goal:** verify that chapter-level completeness is not hiding cross-chapter structural defects.

Recheck:

- every contiguous title-family boundary;
- all chapter opening/closing transitions;
- all combined Chinese raw containers;
- the 54/55 overlap case;
- every documented localized Chinese gap;
- every nontrivial target-to-English witness mapping;
- Side Story boundaries and ordering;
- no untranslated gaps and no duplicated overlap across adjacent targets;
- reveal chronology and term timing across families.

Any new exception must be added to source/chinese/chapter-exceptions.tsv and reflected in provenance.

**Exit gate:** every target chapter has a boundary/alignment PASS or a fully documented exception.

## Phase 4 — Remediation and evidence rebinding

**Goal:** repair all Cycle-2 failures without fragmenting family continuity.

Process failures from the earliest target forward.

Rules:

1. If any family member fails sanitization or completeness, reread the complete family before finalizing repairs.
2. Rebuild from Chinese-primary source rather than patching only the flagged sentence when broader compression may exist.
3. Preserve established canonical English terminology and reveal chronology.
4. Re-run both primary gates after edits, even if only one gate originally failed.
5. Refresh:
   - chapter QA;
   - provenance;
   - acceptance artifact;
   - family QA where applicable;
   - tracker acceptance SHA;
   - glossary/exception table where applicable.
6. If family QA changes, rebind every acceptance/provenance artifact that depends on that family-QA hash.

**Exit gate:** remediation queue is empty; all changed families have fresh, internally consistent evidence chains.

## Phase 5 — Independent residual verification and consistency sweep

**Goal:** use a second method to catch misses after direct review.

Run corpus-wide diagnostics again and investigate outliers, including:

- post-remediation size/paragraph anomalies;
- unusual lexical-overlap gaps against aligned English witnesses where useful;
- explicitness-sensitive term mismatches;
- suspicious drops in dialogue/window counts;
- chapter endings/openings that do not match neighboring continuity;
- numeric/stat/rank/item inconsistencies;
- canonical-name drift;
- information-window fragmentation;
- scene-break misclassification.

This phase is a **safety net**, not a substitute for the full manual passes in Phases 1–3.

Re-open any family if the residual sweep produces a credible discrepancy.

**Exit gate:** no unresolved residual discrepancy remains.

## Phase 6 — Closure, hash validation, and release unblock

Cycle 2 closes only when all of the following are true:

- 500 / 500 chapters have sanitization disposition resolved;
- 500 / 500 chapters have completeness disposition resolved;
- all chapter/family boundary and exception checks are resolved;
- no unresolved sanitization failures;
- no unresolved completeness failures;
- no unresolved boundary/alignment failures;
- every changed chapter/family has refreshed QA/provenance/acceptance evidence;
- all tracker acceptance SHAs match live repository blobs;
- provenance-to-draft/QA/family-QA and acceptance-to-provenance bindings validate;
- live docs agree on the final state;
- the Cycle-2 audit record contains a closure summary and residual-check result.

Only after those conditions are satisfied may complete-EPUB assembly and final packaging/layout QA become the immediate project focus again.

## Execution order and checkpoints

Primary processing order is chronological by contiguous title family from Chapter 1 through Chapter 500.

For operational checkpoints, report progress in broad corpus waves without splitting a title family merely to hit a round number:

- Wave A: Chapters 1–100
- Wave B: Chapters 101–200
- Wave C: Chapters 201–300
- Wave D: Chapters 301–400
- Wave E: Chapters 401–500

Each checkpoint must report, at minimum:

- chapters/families reviewed for sanitization;
- chapters/families reviewed for completeness;
- boundary/exception checks completed;
- new failures found;
- failures remediated;
- evidence chains rebound;
- exact next family.

## Immediate next actions

1. Continue Phase 3 from **Jailbreaker (403–408)** and proceed in contiguous title-family order.
2. Continue reconciling shared/combined Chinese raws, localized Chinese gaps, shifted English mappings, and Side Story boundaries against the normalized exception table.
3. Preserve open structural FAILs at Chapters **273 and 283** for Phase 4; investigate any newly discovered duplicated/displaced source blocks without editing manuscript text.
4. Record a Phase-3 PASS / FAIL / EXCEPTION-DOCUMENTED disposition for every target.
5. Keep all **273** remediation chapters frozen until Phase 3 closes, then begin Phase 4 from the earliest affected family.
6. Keep EPUB assembly blocked.
