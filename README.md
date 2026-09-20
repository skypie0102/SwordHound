# Revenge of the Iron-Blooded Sword Hound

Recovered source, reference, reconstruction, QA, and EPUB-preparation material for the English project.

## Start here

**Every editorial session must read `HANDOFF.md` first.**

Current checkpoint: **post-500 manuscript completeness audit**.

- Target manuscript files present: **500 / 500**
- Historical state before audit: **500 / 500 accepted**
- Current tracker state: **499 accepted / 1 needs rework**
- Confirmed compressed chapter still requiring rebuild: **420**; Chapters **97, 316, and 319 have been rebuilt and resolved**
- Initial priority-review queue: **47 ordinary one-target chapters** with unusually low draft/raw byte ratios (<0.60); this is a triage heuristic, not an automatic failure rule
- Latest completed audit family: **Surplus Man (314–320)** — all seven rebuilt; confirmed failures 316 and 319 resolved.

Completed audit families: **The Illiad (85–89)**, **The Ghosts of the Ancestors (90–94)**, **Madam Eight-Legs (95–100)**, **Nostalgia (101–104)**, **Attack Land (190–196)**, **Tuition (225–233)**, **National University League (236–244)**, **Hell Tree (307–313)**, and **Surplus Man (314–320)** — rebuilt and passed
- Pending initial-priority chapters: **1**
- Next audit family: **The Lion King (430–433)**
- Active audit record: `qa/manuscript-completeness-audit.md`
- EPUB assembly is **blocked until the completeness audit closes**

The final reconstruction PR (#125, Chapters 494–500) was merged, so the production run really did reach all 500 targets. The project was reopened because direct Chinese-raw comparison proved that some previously accepted drafts preserve only broad plot beats while dropping substantial dialogue, narration, descriptive detail, and transitions.

## Current source policy

- `source/chinese/chapters/` — **semantic/narrative authority** wherever Chinese text exists.
- English *Revenge of the Iron-Blooded Sword Hound* Fandom wiki — **canonical English authority** for identified names, terms, locations, ranks, skills, monsters, organizations, titles, and other proper nouns where an applicable entry exists.
- `source/chapters/` — recovered 493-chapter English MTL/XHTML corpus; secondary alignment/phrasing witness, except for narrowly documented Chinese gaps.
- `source/chinese/chapter-exceptions.tsv` — authoritative exception/mapping table for partial gaps, overlap containers, combined raws, and nontrivial English alignment.
- `editorial/SOURCES.md` and `editorial/WORKFLOW.md` — source and editorial procedures.
- `AGENTS.md` — mandatory agent behavior.
- `HANDOFF.md` — exact operational continuation point.
- `editorial/chapter-tracker.json`, `editorial/reconstruction-status.json`, `PROJECT_STATE.md`, and `PROGRESS.md` — current/historical state records.

### Chapter 95 / 100 audit corrections

Chapter 95 has a verified localized Chinese omission restored only from aligned E94; see `source/chinese/chapter-exceptions.tsv`.

Chapter 100's historical draft crossed into Chapter 101. It now ends at the Bog Salamander cushion, matching Chinese100/E99; the impact and subsequent material belong to target101.

### Chapter 55 correction

There is no standalone `055.txt`, but Chapter 55 is **not English-only**. Accepted boundary QA proves that `054.txt` is an overlapping 54–55 container: E55 supplies the missing Chapter-55 opening/title boundary, while most of the Chapter-55 body survives in Chinese inside `054.txt` and remains semantically primary there.

## Critical workflow rules

- Do **not** assume target Chapter N maps to English MTL Chapter N; align by title and content.
- Determine and process complete contiguous title families.
- Do not equate “file exists” or “plot beats are present” with full translation coverage.
- Preserve every material source beat: dialogue, narration, descriptions, transitions, information windows, and explicit content unless the source itself omits them.
- A polished summary is still a QA failure if source content was dropped.
- Preserve source explicitness; do not sanitize, soften, or intensify.
- Protect reveal chronology even when the wiki contains later information.
- Keep information windows atomic.
- Numbered Baskerville sword techniques are **Fangs**, not Forms.
- Defer final visual/layout QA to complete-EPUB assembly.
- Do **not** begin complete-EPUB assembly while the manuscript completeness audit is active.

## Completeness audit

The initial deterministic triage compares draft byte size with Chinese raw byte size for ordinary one-target containers. The corpus median is about 0.85; chapters under 0.60 are prioritized for direct review, and chapters under 0.50 are strong suspects. Byte ratio is only a detector, never proof.

Direct comparison confirmed four historical failures. **97, 316, and 319 are now rebuilt and resolved.** The sole unresolved confirmed failure is:
- Chapter 420 — *Goodbye, Nouvelle Vague (2)*

Direct family review has also shown that chapters above the byte-ratio threshold can still be compressed: Chapters 85–86 and 90–91 were not initially flagged but failed strict source-coverage review and were rebuilt with their complete title families. See `qa/manuscript-completeness-audit.md` for the review queue, completed families, and family-first order.

## Editorial quality bar

A chapter may be accepted only after Chinese-source semantic fidelity **and complete coverage** are verified: no dropped, duplicated, invented, sanitized, or summary-collapsed material; canonical terminology; title-family continuity; reveal chronology; natural English; information-window/scene-break semantics; provenance; and alignment.

Formatting decisions preserved for eventual EPUB assembly include dialogue indentation, unindented narration, 1.65 line height, single-quote handling, styled information windows, `◆◆◆` scene breaks, and separate side stories. See `editorial/Recovered-Editorial-Decisions.md`.

Superseded reconstruction and acceptance artifacts remain available for audit/history but do not override the live tracker and handoff.
