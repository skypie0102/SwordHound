# Cycle 2 — Phase 0 Baseline Freeze and Audit Inventory

**Status:** COMPLETE  
**Completed:** 2026-09-21  
**Opening main commit:** `8177e1c192cd7fcd55b04009fbe826bbd50f586b`  
**Next phase:** Phase 1 — full-corpus sanitization fidelity sweep  
**Next family:** Hellhound (1–3)

## Inventory result

- Target chapters represented in the Cycle-2 ledger: **500 / 500**
- Contiguous title-family units: **118**
- Manuscript drafts: **500**
- Chapter QA files: **500**
- Provenance files: **500**
- Acceptance files: **500**
- Physical Chinese raw files: **492**
- Recovered English witness files: **493**
- Source-exception rows reconciled: **36**
- Shared Chinese raw containers: **8**
- Ordinary one-target chapters with valid draft/raw byte-ratio baseline: **484**
- Shared-container chapters excluded from per-target raw ratio: **16**

## Evidence-chain freeze

At the opening baseline:

- missing draft/QA/provenance/acceptance/family-QA paths: **0**
- tracker acceptance SHA mismatches: **0**
- source-exception raw/witness reconciliation problems: **0**
- Phase-0 manuscript or accepted-evidence content edits: **0**

The historical accepted state is therefore frozen cleanly at 500/500 as evidence. It does **not** grant Cycle-2 sanitization or completeness clearance.

## Source-exception inventory

The 36 documented exception rows are accounted for. Status classes:

- `combined_embedded_side_story`: **1**
- `combined_main_plus_side_story`: **1**
- `combined_no_internal_heading`: **4**
- `combined_overlap`: **1**
- `combined_partial_gap`: **2**
- `combined_unsplittable`: **2**
- `combined_with_embedded_boundary`: **3**
- `combined_with_embedded_boundary_and_closing_gap`: **1**
- `normal_shifted_alignment`: **16**
- `overlap_duplicate`: **1**
- `partial_combined_overlap`: **1**
- `partial_raw_gap`: **3**

The eight shared physical Chinese containers cover target pairs 54/55, 75/76, 267/268, 284/285, 351/352, 353/354, 385/386, and 495/496. Their per-target byte ratios are intentionally excluded.

## Deterministic baseline diagnostics

Phase 0 created **31** diagnostic files under `qa/cycle2-baseline/`, covering Chapters **1–500 with zero gaps and zero overlaps**.

The baseline freezes:

- draft/raw byte ratios where one target owns one Chinese raw;
- English-manuscript line, nonempty-line, and paragraph counts;
- dialogue-line and quotation-marker signals;
- bracket/window candidate counts;
- high-risk explicitness candidate counts;
- normalized explicitness-candidate density;
- opening and closing signatures.

These are diagnostic signals only. They cannot produce a sanitization/completeness PASS or FAIL. Direct Chinese-source review in later phases is authoritative.

## Family inventory

All **118** contiguous family units are enumerated in `qa/cycle2-family-index.md` and in `qa/cycle2-ledger.json`.

## Phase-0 exit gate

PASS.

- all 500 targets represented;
- all source exceptions accounted for;
- baseline blobs/evidence frozen;
- deterministic diagnostics recorded for all 500 manuscripts;
- no accepted manuscript/evidence content was edited before the freeze.

Phase 1 may begin at **Hellhound (1–3)**.
