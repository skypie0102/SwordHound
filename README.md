# Revenge of the Iron-Blooded Sword Hound

Recovered source, reference, reconstruction, QA, and EPUB-preparation material for the English project.

## Start here

**Every editorial session must read `HANDOFF.md` first.**

Current checkpoint: **full manuscript sanitization + completeness audit — Cycle 2 ACTIVE**.

- Target manuscript files present: **500 / 500**
- Historical accepted state entering Cycle 2: **500 / 500**
- Cycle-2 sanitization revalidated: **0 / 500**
- Cycle-2 completeness revalidated: **0 / 500**
- Cycle-2 boundary/alignment revalidated: **0 / 500**
- New confirmed Cycle-2 failures: **none yet; substantive review has not started**
- Current stage: **Phase 0 — baseline freeze and audit inventory**
- Active Cycle-2 plan: qa/manuscript-sanitization-completeness-cycle2.md
- Historical post-500 audit record: qa/manuscript-completeness-audit.md
- Complete-EPUB assembly: **BLOCKED until Cycle 2 closes**

The previous 2026-09-20 completeness audit remains valid historical evidence and closed with **500 accepted / 0 known rework** after repairing confirmed compression failures. Cycle 2 is a new, stricter audit opened before packaging: it requires fresh sanitization-fidelity review and direct full-source completeness revalidation for **every Chapter 1–500**, regardless of prior PASS state or size ratio.

The audit has separate gates for sanitization fidelity, complete source coverage, and boundary/alignment integrity. Prior acceptance is evidence, not an automatic Cycle-2 pass. EPUB assembly will not resume until all 500 targets clear the new closure criteria.

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
