# Revenge of the Iron-Blooded Sword Hound

Recovered source, reference, and reconstruction material for the English EPUB project.

## Start here

**Every editorial session must read `HANDOFF.md` first.**

Current checkpoint: **381 / 500 accepted; next Chapter 382.** Latest accepted family: **targets 377–381 — The Hounds of Nouvelle Vague (1)–(5)**.

The next verified family is **Kennel, targets 382–384**, mapped **382→E380 through 384→E382**. Target 385 begins **The Rotten Dog of Nouvelle Vague (1)** and maps to E383.

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

- **The Hounds of Nouvelle Vague** — accepted five-part family, targets **377–381** / witnesses **E375–E379**.
- **Corrected family boundary** — the earlier provisional 377–380 assumption is superseded; target381 is part (5).
- **Sakkuth sponsor references** — Queen / Boss / “Him” remain unresolved.
- **Kirko Grimm birth trauma** — source-timed to target379; preserve plainly without embellishment.
- **Garam Nord death** — target380; he dies protecting Kirko.
- **Target381 disguise correction** — Chinese green marker/ink + seawater, rejecting shifted witness “green vodka.”
- **Regeneration continuity guard** — local Basilisk wording does not overwrite accepted **Immortality — Gargoyle (S)** continuity.
- **Garam disguise** — rank/uniform/appearance carry the impersonation; Kirko recognizes only “Garam.”
- **Kennel** — next family targets **382–384 / E380–E382**.
- **The Rotten Dog of Nouvelle Vague** — follows at **385–389 / E383–E387**; targets385–386 share Chinese raw `385.txt` and require explicit split verification.

For the full accumulated terminology and continuity record, see `editorial/GLOSSARY.md`.

## Accepted evidence

Current accepted production evidence covers targets **1–381**:

- `manuscript/drafts/chapter-0001.md` through `chapter-0381.md`
- `qa/chapter-0001.md` through `chapter-0381.md`
- accepted family QA through `qa/families/hounds-nouvelle-vague-0377-0381.md`
- `editorial/provenance/chapter-0001.json` through `chapter-0381.json`
- `qa/acceptance/chapter-0001.json` through `chapter-0381.json`

Latest family QA: `qa/families/hounds-nouvelle-vague-0377-0381.md` — **PASS**.

## Editorial quality bar

Every chapter is reviewed for Chinese-source semantic fidelity, complete coverage, no invented/duplicated/sanitized material, Fandom-backed canonical English proper nouns where applicable, title-family continuity, reveal chronology, grammar/natural modern English, information-window and scene-break semantics, source provenance, and MTL alignment.

Formatting decisions preserved for eventual EPUB assembly include dialogue indentation, no narrative indentation, 1.65 line height, single-quote handling, styled information windows, `◆◆◆` scene breaks, and separate side stories. See `editorial/Recovered-Editorial-Decisions.md`.

Superseded reconstruction work remains available in Git history but is not accepted production state.
