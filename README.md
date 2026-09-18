# Revenge of the Iron-Blooded Sword Hound

Recovered source, reference, and reconstruction material for the English EPUB project.

## Start here

**Every editorial session must read `HANDOFF.md` first.**

Current checkpoint: **82 / 500 accepted; next Chapter 83.** Latest accepted family: **targets 78–82 — The Saintess (1)–(5)**.

The next verified family is **Lovesickness, targets 83–84**, mapped **83→E82, 84→E83**. Target 85 begins **The Illiad (1)**.

## Current source policy

- `source/chinese/chapters/` — **semantic/narrative authority** for the 500-chapter target edition.
- English *Revenge of the Iron-Blooded Sword Hound* Fandom wiki — **canonical English authority** for identified names, terms, locations, ranks, skills, monsters, organizations, titles, and other proper nouns where an applicable entry exists.
- `source/chapters/` — recovered 493-chapter English MTL/XHTML corpus; secondary alignment/phrasing reference only, except Chapter 55 where no Chinese raw exists.
- `source/chinese/chapter-exceptions.tsv` — missing/combined raw exceptions and verified nontrivial English-MTL alignments.
- `editorial/SOURCES.md` and `editorial/WORKFLOW.md` — authoritative source and editorial procedures.
- `AGENTS.md` — mandatory agent behavior, including continuous title-family processing and handoff maintenance.
- `HANDOFF.md` — exact operational continuation point for the next session/agent.
- `editorial/chapter-tracker.json`, `editorial/reconstruction-status.json`, `PROJECT_STATE.md`, and `PROGRESS.md` — accepted-state records and project history.

The Chinese corpus contains **492 physical files with at least partial Chinese coverage for all 500 targets**. Targets **49 and 55** contain documented localized gaps. Combined/overlapping physical containers remain intact where no safe source-level seam exists; reconstructed English output is still split into separate target chapters.

## Critical workflow rules

- Do **not** assume Chinese target chapter `N` maps to English MTL chapter `N`; align by title and content.
- Determine the complete contiguous title-family boundary before accepting a chapter.
- Process the full title family as one continuity/QA batch.
- A finished title family or PR is a checkpoint, **not a stopping point**.
- Preserve source explicitness; do not sanitize, soften, or intensify.
- Protect reveal chronology even when the wiki contains later information.
- Do not import MTL/wiki narrative exposition absent from Chinese.
- Keep information windows atomic.
- Numbered Baskerville sword techniques are **Fangs**, not Forms.
- Defer final visual/layout QA to complete-EPUB assembly unless explicitly requested earlier.

## Current terminology / editorial notes

The accepted Saintess family adds/revalidates:

- **Dolores L. Quovadis** — canonical form; sixteen during targets 78–82.
- **Humbert L. Quovadis** — canonical Fandom form; raw/recovered `Humbert Humbert L. Quovadis` is not used.
- **Nabokov I Quovadis** — Pope-level authority referenced in target 79.
- **Plany de la Verge / Saintess's Tears** — three concentrated holy-water drops completed in target 82.
- **Old Testament Faction / New Testament Faction** — Quovadis internal factions.
- **Bourgeois emblem** in target 82 = Chinese-source **nail and hammer**; recovered-English `scythe and hammer` rejected.
- **Target-79 case correction** — primary contaminated-water cases only; no secondary saliva/waste cases yet.
- **Divine-power short selling** — target-81 fantasy magic mechanic; not real-world medical/religious guidance.
- **Lovesickness** — next family targets 83–84; witnesses E82–E83.
- **The Illiad** begins target 85 / E84.

## Accepted evidence

Current accepted production evidence covers targets **1–82**:

- `manuscript/drafts/chapter-0001.md` through `chapter-0082.md`
- `qa/chapter-0001.md` through `chapter-0082.md`
- accepted family QA through `qa/families/saintess-0078-0082.md`
- `editorial/provenance/chapter-0001.json` through `chapter-0082.json`
- `qa/acceptance/chapter-0001.json` through `chapter-0082.json`

Latest family QA: `qa/families/saintess-0078-0082.md` — **PASS**.

## Editorial quality bar

Every chapter is reviewed for Chinese-source semantic fidelity, complete coverage, no invented/duplicated/sanitized material, Fandom-backed canonical English proper nouns where applicable, title-family continuity, reveal chronology, grammar/natural modern English, information-window and scene-break semantics, source provenance, and MTL alignment.

Formatting decisions preserved for eventual EPUB assembly include dialogue indentation, no narrative indentation, 1.65 line height, single-quote handling, styled information windows, `◆◆◆` scene breaks, and separate side stories. See `editorial/Recovered-Editorial-Decisions.md`.

Superseded reconstruction work remains available in Git history but is not accepted production state.
