# Revenge of the Iron-Blooded Sword Hound

Recovered source, reference, and reconstruction material for the English EPUB project.

## Start here

**Every editorial session must read `HANDOFF.md` first.**

Current checkpoint: **109 / 500 accepted; next Chapter 110.** Latest accepted family: **targets 105–109 — The Returned Hero (1)–(5)**.

The next verified family is **The Great Banquet, targets 110–116**, mapped **110→E109 through 116→E115**. Target 117 begins **Falling in Love (1)** and maps to E116.

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

The accepted Returned Hero family adds/revalidates:

- **The Returned Hero** — production family title for targets 105–109; witnesses E104–E108.
- **Highsis / Middlesis / Lowsis Morgue** — canonical triplet forms retained; source semantic ordering remains plant / earth / water.
- **Light Faction / Dark Faction** — Morgue’s practical field branch and secluded research branch respectively.
- **Snake Morgue** — source-revealed target-107 Dark Faction leader; later plot information remains spoiler-guarded.
- **Pomeranian La Baskerville** — age five in target 108; corpse revival / negative mana aptitude source-revealed.
- **Lady Roxana / Penelope La Baskerville / Pomeranian La Baskerville** — canonical lineage forms override target-109 raw-layer name drift.
- **The Great Banquet** — next family spans targets 110–116; witnesses E109–E115.
- **Falling in Love** begins target 117 / E116.

## Accepted evidence

Current accepted production evidence covers targets **1–109**:

- `manuscript/drafts/chapter-0001.md` through `chapter-0109.md`
- `qa/chapter-0001.md` through `chapter-0109.md`
- accepted family QA through `qa/families/returned-hero-0105-0109.md`
- `editorial/provenance/chapter-0001.json` through `chapter-0109.json`
- `qa/acceptance/chapter-0001.json` through `chapter-0109.json`

Latest family QA: `qa/families/returned-hero-0105-0109.md` — **PASS**.

## Editorial quality bar

Every chapter is reviewed for Chinese-source semantic fidelity, complete coverage, no invented/duplicated/sanitized material, Fandom-backed canonical English proper nouns where applicable, title-family continuity, reveal chronology, grammar/natural modern English, information-window and scene-break semantics, source provenance, and MTL alignment.

Formatting decisions preserved for eventual EPUB assembly include dialogue indentation, no narrative indentation, 1.65 line height, single-quote handling, styled information windows, `◆◆◆` scene breaks, and separate side stories. See `editorial/Recovered-Editorial-Decisions.md`.

Superseded reconstruction work remains available in Git history but is not accepted production state.
