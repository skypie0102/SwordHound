# Full Manuscript Sanitization + Completeness Audit — Cycle 2

**Opened:** 2026-09-21  
**Status:** ACTIVE — IMMEDIATE PROJECT PRIORITY  
**Scope:** Target Chapters 1–500  
**Historical accepted state at opening:** 500 / 500  
**Current audit disposition:** prior acceptance retained as historical evidence, but every chapter requires fresh Cycle-2 revalidation  
**EPUB assembly:** BLOCKED until this audit is formally closed  
**Current stage:** Phase 2 ACTIVE — completeness reviewed through Chapter 11; next `The Gluttonous Flies (12–13)`

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

### Phase 2 — ACTIVE

- completeness reviewed: **11 / 500**
- PASS: **11**
- FAIL: **0**
- manuscript edits during discovery: **0**
- next family: **The Gluttonous Flies (12–13)**

Evidence is recorded under `qa/cycle2/completeness/` and in `qa/cycle2-ledger.json`.

### Phase 0 — COMPLETE

Baseline frozen at main commit `8177e1c192cd7fcd55b04009fbe826bbd50f586b`.

- 500 / 500 targets represented.
- 118 contiguous title-family units enumerated.
- 36 source-exception rows reconciled.
- 500 draft, QA, provenance, and acceptance files verified.
- 0 acceptance-SHA mismatches.
- 31 deterministic diagnostic files cover Chapters 1–500 with 0 gaps / 0 overlaps.
- 0 manuscript/evidence content edits occurred before baseline closure.

Evidence: `qa/cycle2-phase0-baseline.md`, `qa/cycle2-family-index.md`, `qa/cycle2-ledger.json`, and `qa/cycle2-baseline/`.

## Purpose

The previous post-500 completeness audit successfully found and repaired major compression failures, but it was still driven partly by anomaly triage and targeted family review. This new cycle is deliberately broader.

Cycle 2 has two independent goals:

1. **Sanitization fidelity:** verify that the English manuscript has not softened, euphemized, generalized, omitted, or otherwise sanitized source material such as violence, gore, profanity, anatomical language, degradation, coercion, sexual material, bodily detail, horror, cruelty, death, and other harsh content where that material is present in the source.
2. **Full completeness:** verify every target chapter against its complete Chinese source coverage, not merely low-ratio chapters or previously suspicious families, so that dialogue, narration, description, transitions, information windows, numeric/mechanical details, scene rhythm, and chapter boundaries are all retained.

These are separate gates. A chapter can be complete in broad plot terms and still fail sanitization fidelity; it can preserve explicitness and still fail completeness.

## Governing rules

- The Chinese raw is semantic/narrative authority wherever Chinese exists.
- The English Fandom wiki remains canonical authority for established English names and terminology, not for plot.
- The recovered English XHTML is a secondary witness/alignment aid only, except for documented Chinese gaps.
- **Every target chapter 1–500 must be reviewed.** No chapter is pre-cleared by historical acceptance, prior QA, byte ratio, or earlier audit status.
- Review proceeds in contiguous title-family order. A title family is the minimum continuity/QA unit.
- Byte/word/paragraph ratios, lexical overlap, punctuation counts, and other metrics are diagnostic signals only.
- Sanitization review checks for both **softening** and **unwarranted intensification**.
- Source gaps, combined raws, overlap containers, and shifted English mappings must use the documented exception workflow.
- Safety-limited material that cannot be reproduced directly must be recorded explicitly as a safety-limited exception; surrounding ordinary narrative/plot coverage must still be verified in full. A safety limit must never be used to hide unrelated omissions.
- If one chapter fails either primary gate, review the complete contiguous family before remediation is accepted.
- Any changed chapter must receive refreshed chapter QA, provenance, acceptance evidence, and affected family-QA/hash bindings before it can clear the audit.
- EPUB assembly and final layout work remain blocked until Phase 6 closure.

## Audit evidence model

Cycle 2 will maintain a fresh audit ledger rather than rewriting the historical post-500 audit record.

For each target chapter, record at minimum:

- target chapter and title family;
- Chinese source container(s);
- verified English witness mapping, if any;
- sanitization status: **PENDING / PASS / FAIL / SAFETY-LIMITED-REVIEWED**;
- completeness status: **PENDING / PASS / FAIL**;
- boundary/alignment status: **PENDING / PASS / FAIL / EXCEPTION-DOCUMENTED**;
- findings and exact source spans/scenes affected;
- remediation required;
- final QA/provenance/acceptance rebinding state.

A family is not Cycle-2 complete until all member chapters have both primary gates resolved and the family boundary/continuity check passes.

## Phase 0 — Baseline freeze and audit inventory

**Goal:** establish an immutable starting point and a complete review map before editing manuscripts.

Tasks:

1. Snapshot the opening main-branch commit and the current draft/QA/provenance/acceptance blob bindings.
2. Confirm all 500 target manuscript files and all available Chinese source containers.
3. Reconcile source/chinese/chapter-exceptions.tsv against the live corpus:
   - overlap containers;
   - combined raws;
   - localized Chinese gaps;
   - shifted/nontrivial English mappings;
   - Side Story containers.
4. Enumerate every contiguous title family from Chapter 1 through 500.
5. Create the Cycle-2 chapter/family ledger with all statuses initially pending.
6. Record deterministic baseline diagnostics for later comparison:
   - draft/raw size ratios where valid;
   - paragraph/line counts;
   - information-window counts;
   - quote/dialogue density;
   - high-risk explicitness term candidates;
   - chapter opening/closing signatures.

**Exit gate:** all 500 targets are represented in the audit ledger; all special source containers/exceptions are accounted for; no manuscript edits have occurred without a recorded baseline.

## Phase 1 — Full-corpus sanitization fidelity sweep

**Goal:** inspect every chapter for source softening, euphemism, omission, or inappropriate intensification.

Review every title family in target order, Chapters 1–500.

Check specifically for:

- violence, gore, injury, torture, death, mutilation;
- profanity, insults, threats, humiliating/degrading language;
- anatomical and medical terms;
- bodily fluids/functions and visceral detail;
- coercion, captivity, abuse, fear, horror, cruelty;
- sexual or suggestive source material where applicable;
- intoxication/drug/poison descriptions;
- morally harsh or socially uncomfortable narration/dialogue;
- system/window language whose force was weakened;
- culturally blunt wording that may have been over-localized into a softer statement;
- any place the English adds stronger explicitness than the Chinese supports.

For each suspicious passage, classify it as:

- faithful;
- softened/euphemized;
- omitted/generalized;
- intensified;
- mistranslated;
- safety-limited but surrounding coverage intact.

Do not use the English MTL as permission to sanitize Chinese-primary content.

**Exit gate:** every chapter has a recorded sanitization disposition; all failures are entered into the remediation queue with source evidence.

## Phase 2 — True full-corpus completeness pass

**Goal:** independently verify complete source coverage for all 500 chapters.

This phase does **not** use thresholds to decide what gets read. Every chapter receives direct source-to-draft review.

For each chapter verify:

1. opening state and title boundary;
2. every scene in source order;
3. all dialogue exchanges and speaker turns;
4. narrative exposition and descriptive beats;
5. action choreography and causal transitions;
6. internal thoughts/recollections;
7. information windows, lists, ranks, numbers, mechanics, item/skill details;
8. named entities and continuity-relevant descriptors;
9. tonal/rhetorical beats that carry information;
10. final scene and handoff into the next chapter.

Explicitly reject:

- summary-style condensation;
- merged dialogue that loses distinct information;
- dropped connective narration;
- omitted repeated-but-meaningful beats;
- missing numeric/mechanical details;
- duplicated material from adjacent chapters;
- invented connective material used to conceal source gaps.

**Exit gate:** all 500 chapters have a completeness PASS or a documented FAIL requiring remediation.

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

1. Continue Phase 2 at **The Gluttonous Flies (12–13)**.
2. Directly verify complete Chinese-source coverage for every target chapter in contiguous family order; do not repeat Chapters 1–11.
3. Record completeness independently from sanitization and preserve all existing Phase-1 dispositions.
4. Keep manuscript text unchanged during Phase-2 discovery; remediation/evidence rebinding remain Phase 4 work.
5. Synchronize live state documents and the master ledger at meaningful completeness checkpoints.
