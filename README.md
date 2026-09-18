# Revenge of the Iron-Blooded Sword Hound

Recovered source, reference, and reconstruction material for the English EPUB project.

## Start here

**Every editorial session must read `HANDOFF.md` first.**

Current checkpoint: **77 / 500 accepted; next Chapter 78.** Latest accepted family: **targets 75–77 — The Hound of the Night (1)–(3)**.

The next verified family is **The Saintess, targets 78–82**, mapped **78→E77 through 82→E81**. Target 83 begins **Lovesickness (1)**.

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

The accepted Hound of the Night family adds/revalidates:

- **Hound of the Night** — Vikir's masked alias, derived from Akwilla's **Night Fox** title.
- **075.txt combined-source exception** — targets 75–76 share one physical raw with no internal target-76 marker and no safe byte-level seam.
- Target 75 reconstruction mode: Chinese body + scoped E74 missing close.
- Target 76 reconstruction mode: scoped E75 missing opening/context + Chinese body.
- **Saint Mecca** — Quovadis central city used for this arc.
- **Dolores L. Quovadis** — canonical/source-supported spelling; detailed profile begins in target 78.
- **Mozgus Quovadis** — source-revealed in target 77; current combat estimate between Mid and High Sword Graduator.
- **Kilogram Hammer — Oxbear (A)** / **Incinerate — Cerberus (A+)** / six Fangs — reaffirmed in target 77.
- **The Saintess** — next family spans targets 78–82; witnesses E77–E81.
- **Lovesickness** begins target 83 / E82.

## Accepted evidence

Current accepted production evidence covers targets **1–77**:

- `manuscript/drafts/chapter-0001.md` through `chapter-0077.md`
- `qa/chapter-0001.md` through `chapter-0077.md`
- accepted family QA through `qa/families/hound-night-0075-0077.md`
- `editorial/provenance/chapter-0001.json` through `chapter-0077.json`
- `qa/acceptance/chapter-0001.json` through `chapter-0077.json`

Latest family QA: `qa/families/hound-night-0075-0077.md` — **PASS**.

## Editorial quality bar

Every chapter is reviewed for Chinese-source semantic fidelity, complete coverage, no invented/duplicated/sanitized material, Fandom-backed canonical English proper nouns where applicable, title-family continuity, reveal chronology, grammar/natural modern English, information-window and scene-break semantics, source provenance, and MTL alignment.

Formatting decisions preserved for eventual EPUB assembly include dialogue indentation, no narrative indentation, 1.65 line height, single-quote handling, styled information windows, `◆◆◆` scene breaks, and separate side stories. See `editorial/Recovered-Editorial-Decisions.md`.

Superseded reconstruction work remains available in Git history but is not accepted production state.
