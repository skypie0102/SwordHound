# Revenge of the Iron-Blooded Sword Hound

Recovered source, reference, reconstruction, QA, and EPUB-preparation material for the English project.

## Start here

**Every editorial session must read `HANDOFF.md` first.**

Current checkpoint: **full manuscript sanitization + completeness audit — Cycle 2, Phase 3 ACTIVE**.

- Target manuscript files present: **500 / 500**
- Historical accepted state entering Cycle 2: **500 / 500**
- Cycle-2 sanitization: **500 / 500 COMPLETE** — **282 PASS / 200 FAIL / 18 SAFETY-LIMITED-REVIEWED**
- Cycle-2 completeness: **500 / 500 COMPLETE** — **229 PASS / 271 FAIL**
- Phase-1/Phase-2 overlap: **198** completeness failures overlap Phase-1 FAILs
- Completeness-only additions beyond the Phase-1 FAIL queue: **73**
- Combined Phase-4 remediation population: **273 unique chapters**
- Cycle-2 boundary/alignment revalidated: **306 / 500** — **53 PASS / 3 FAIL / 250 EXCEPTION-DOCUMENTED** across **73 / 118 families**
- Current stage: **Phase 3 ACTIVE — reviewed through Chapter 306; next family Hell Tree (307–313)**
- Active Cycle-2 plan: `qa/manuscript-sanitization-completeness-cycle2.md`
- Phase-2 closure checkpoint: `qa/cycle2-phase2-checkpoint-0500.md`
- Historical post-500 audit record: `qa/manuscript-completeness-audit.md`
- Complete-EPUB assembly: **BLOCKED until Cycle 2 closes**

The previous 2026-09-20 completeness audit remains valid historical evidence and closed with **500 accepted / 0 known rework** after repairing confirmed compression failures. Cycle 2 is a new, stricter release-blocking audit: historical acceptance remains evidence, not an automatic Cycle-2 pass.

Phase 0 froze the opening baseline at `8177e1c192cd7fcd55b04009fbe826bbd50f586b`, inventoried all **500 targets / 118 title families**, reconciled **36 source-exception rows**, verified the historical evidence paths and acceptance SHAs, and recorded deterministic diagnostics with no coverage gaps or overlaps.

Phase 1 is complete across Chapters 1–500 at **282 PASS / 200 FAIL / 18 SAFETY-LIMITED-REVIEWED** with no manuscript edits during discovery. Phase 2 is also complete across Chapters 1–500 at **229 PASS / 271 FAIL**; **198** completeness failures overlap Phase-1 FAILs and **73** are completeness-only additions, producing **273 unique remediation chapters**.

Phase 3 is now the immediate focus. Chapters **1–306** across **73 / 118** families are structurally reviewed at **53 PASS / 3 FAIL / 250 EXCEPTION-DOCUMENTED**, with **243 new source-exception rows** and **0 manuscript edits**. Checkpoint: `qa/cycle2-phase3-checkpoint-0306.md`. Open structural FAILs are Chapters **236, 273, and 283**; all are duplicated/displaced-content defects reserved for Phase 4. The next family is **Hell Tree (307–313)**. Phase 3 must still revalidate all remaining title-family/chapter boundaries, combined/shared raws, the 54/55 overlap, localized source gaps, shifted/nontrivial English mappings, Side Story ordering, and duplicated/displaced source blocks before Phase 4 remediation begins.

## Current source policy

- `source/chinese/chapters/` — **semantic/narrative authority** wherever Chinese text exists.
- English *Revenge of the Iron-Blooded Sword Hound* Fandom wiki — **canonical English authority** for identified names, terms, locations, ranks, skills, monsters, organizations, titles, and other proper nouns where an applicable entry exists.
- `source/chapters/` — recovered 493-chapter English MTL/XHTML corpus; secondary alignment/phrasing witness, except for narrowly documented Chinese gaps.
- `source/chinese/chapter-exceptions.tsv` — authoritative exception/mapping table for partial gaps, overlap containers, combined raws, and nontrivial English alignment.
- `editorial/SOURCES.md` and `editorial/WORKFLOW.md` — source and editorial procedures.
- `AGENTS.md` — mandatory agent behavior.
- `HANDOFF.md` — exact operational continuation point.
- `editorial/chapter-tracker.json`, `editorial/reconstruction-status.json`, `PROJECT_STATE.md`, and `PROGRESS.md` — current/historical state records.

### Chapter 55 correction

There is no standalone `055.txt`, but Chapter 55 is **not English-only**. Accepted boundary QA proves that `054.txt` is an overlapping 54–55 container: E55 supplies the missing Chapter-55 opening/title boundary, while most of the Chapter-55 body survives in Chinese inside `054.txt` and remains semantically primary there.

### Chapter 59 residual-audit correction

Chapter 59 was not in the original <0.60 queue; its historical draft/raw byte ratio was about **0.625**. The widened whole-corpus pass nevertheless found ordinary source compression in its tracking and Cold Valley material.

The rebuilt chapter restores the complete tracking logic, scented bait/Bakira trail, mosquito categories, Cold Valley terrain/shelter details, Age-of-Destruction memory context, feeding setup, Bakira exchange, and Oxbear counterattack transition. Safety-limited underage sexualized material remains summarized nonsexually.

### Chapter 95 / 100 audit corrections

Chapter 95 has a verified localized Chinese omission restored only from aligned E94; see `source/chinese/chapter-exceptions.tsv`.

Chapter 100's historical draft crossed into Chapter 101. It now ends at the Bog Salamander cushion, matching Chinese100/E99; the impact and subsequent material belong to target101.

## Critical workflow rules

- Do **not** assume target Chapter N maps to English MTL Chapter N; align by title and content.
- Determine and process complete contiguous title families.
- Do not equate “file exists” or “plot beats are present” with full translation coverage.
- Preserve every material source beat: dialogue, narration, descriptions, transitions, information windows, and explicit content unless a documented safety limit or source gap applies.
- A polished summary is still a QA failure if ordinary source content was dropped.
- Preserve source explicitness within applicable safety limits; do not gratuitously soften or intensify.
- Protect reveal chronology even when the wiki contains later information.
- Keep information windows atomic.
- Numbered Baskerville sword techniques are **Fangs**, not Forms.
- Byte ratio is a triage detector only, never proof of completeness or incompleteness.
- Any future manuscript edit must refresh affected QA/provenance/acceptance bindings before tracker acceptance is considered valid.
- Final visual/layout QA belongs to complete-EPUB assembly.

## Completeness audit

The initial deterministic triage compared draft byte size with Chinese raw byte size for ordinary one-target containers. The original corpus median was about 0.85; chapters under 0.60 were prioritized for direct review, and chapters under 0.50 were treated as strong suspects.

The priority-family pass resolved all **47 / 47** initial targets and all **22 / 22** strong suspects. Direct family review also proved that chapters above a numeric cutoff can still fail, which is why the audit continued after the original queue emptied.

The closing whole-corpus pass found:

- **484** ordinary one-target raw/draft pairs available for direct size comparison;
- post-rebuild median draft/raw byte ratio of about **0.904**;
- **0** unresolved ordinary chapters below the original 0.60 trigger;
- **28** chapters below 0.70 reviewed across **15** title families;
- one newly confirmed residual failure, **Chapter 59**, rebuilt and re-accepted;
- no unresolved completeness failures after residual revalidation.

See `qa/manuscript-completeness-audit.md` for the full queue, rebuilt families, residual methodology, and closure record.

## Editorial quality bar

A chapter may be accepted only after Chinese-source semantic fidelity **and complete coverage** are verified: no dropped, duplicated, invented, or summary-collapsed ordinary material; canonical terminology; title-family continuity; reveal chronology; natural English; information-window/scene-break semantics; provenance; and alignment. Documented source gaps and safety-limited passages must remain explicit in QA rather than being silently rewritten.

Formatting decisions preserved for eventual EPUB assembly include dialogue indentation, unindented narration, 1.65 line height, single-quote handling, styled information windows, `◆◆◆` scene breaks, and separate side stories. See `editorial/Recovered-Editorial-Decisions.md`.

Superseded reconstruction and acceptance artifacts remain available for audit/history but do not override the live tracker and handoff.
