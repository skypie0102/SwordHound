# Revenge of the Iron-Blooded Sword Hound

Recovered source, reference, and reconstruction material for the English EPUB project.

## Start here

**Every editorial session must read `HANDOFF.md` first.**

Current checkpoint: **389 / 500 accepted; next Chapter 390.** Latest accepted family: **targets 385–389 — The Rotten Dog of Nouvelle Vague (1)–(5)**.

The next verified family is **The Worst Torture, targets 390–395**, mapped **390→E388 through 395→E393**. Target 396 begins **Dead Man Walking (1)**.

## Current source policy

- `source/chinese/chapters/` — **semantic/narrative authority** for the 500-chapter target edition.
- English *Revenge of the Iron-Blooded Sword Hound* Fandom wiki — **canonical English authority** for identified names, terms, locations, ranks, skills, monsters, organizations, titles, and other proper nouns where an applicable entry exists.
- `source/chapters/` — recovered 493-chapter English MTL/XHTML corpus; secondary alignment/phrasing reference, with scoped restoration only for documented Chinese gaps/splices.
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

The latest accepted family adds/revalidates:

- **The Rotten Dog of Nouvelle Vague** — accepted five-part family, targets **385–389 / E383–E387**.
- **385/386 shared raw** — explicit embedded Chapter386 marker; target385 receives only the localized missing closing handoff from E383.
- **Flubber J Tarbond** — lieutenant-colonel officer, distinct from the Flubber barrier substance.
- **Garam Nord** — Vikir’s active guard disguise; Gargoyle regeneration continuity remains locked.
- **Pal Euspear** — source-local aligned-witness form; no accessible Fandom entry found.
- **Kirko guard** — suspicion/competition increases, but Vikir’s identity remains hidden.
- **Monthly evaluation** — Garam 108%, Kirko 96%.
- **The Worst Torture** — next family targets **390–395 / E388–E393**.
- **Dead Man Walking** — begins target396.

For the full accumulated terminology and continuity record, see `editorial/GLOSSARY.md`.

## Accepted evidence

Current accepted production evidence covers targets **1–389**:

- `manuscript/drafts/chapter-0001.md` through `chapter-0389.md`
- `qa/chapter-0001.md` through `chapter-0389.md`
- accepted family QA through `qa/families/rotten-dog-0385-0389.md`
- `editorial/provenance/chapter-0001.json` through `chapter-0389.json`
- `qa/acceptance/chapter-0001.json` through `chapter-0389.json`

Latest family QA: `qa/families/rotten-dog-0385-0389.md` — **PASS**.

## Editorial quality bar

Every chapter is reviewed for Chinese-source semantic fidelity, complete coverage, no invented/duplicated/sanitized material, Fandom-backed canonical English proper nouns where applicable, title-family continuity, reveal chronology, grammar/natural modern English, information-window and scene-break semantics, source provenance, and MTL alignment.

Formatting decisions preserved for eventual EPUB assembly include dialogue indentation, no narrative indentation, 1.65 line height, single-quote handling, styled information windows, `◆◆◆` scene breaks, and separate side stories. See `editorial/Recovered-Editorial-Decisions.md`.

Superseded reconstruction work remains available in Git history but is not accepted production state.
