# Revenge of the Iron-Blooded Sword Hound

Recovered source, reference, and reconstruction material for the English EPUB project.

## Start here

**Every editorial session must read `HANDOFF.md` first.**

Current checkpoint: **63 / 500 accepted; next Chapter 64.** Latest accepted family: **targets 61–63 — The Protagonist of Hunting (1)–(3)**.

The recovered-English sequence remains one chapter behind current targets: **61→E60, 62→E61, 63→E62**. The next family is **Unfair Trade, targets 64–67**, mapped **64→E63 through 67→E66**.

## Current source policy

- `source/chinese/chapters/` — **semantic/narrative authority** for the 500-chapter target edition.
- English *Revenge of the Iron-Blooded Sword Hound* Fandom wiki — **canonical English authority** for identified names, terms, locations, ranks, skills, monsters, organizations, titles, and other proper nouns where an applicable entry exists.
- `source/chapters/` — recovered 493-chapter English MTL/XHTML corpus; secondary alignment/phrasing reference only, except Chapter 55 where no Chinese raw exists.
- `source/chinese/chapter-exceptions.tsv` — missing/combined raw exceptions and verified nontrivial English-MTL alignments.
- `editorial/SOURCES.md` and `editorial/WORKFLOW.md` — authoritative source and editorial procedures.
- `AGENTS.md` — mandatory agent behavior, including continuous title-family processing and handoff maintenance.
- `HANDOFF.md` — exact operational continuation point for the next session/agent.
- `editorial/chapter-tracker.json`, `editorial/reconstruction-status.json`, `PROJECT_STATE.md`, and `PROGRESS.md` — accepted-state records and project history.

The Chinese corpus contains **492 physical files covering 499 of 500 target chapters**. Chapter **55** is the only confirmed missing Chinese raw. Seven physical files contain two target chapters each and remain intact; English output must still be split into separate target chapters.

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

The accepted Protagonist of Hunting family adds/revalidates:

- **Kilogram Hammer — Oxbear (A)** — canonical Beelzebub ability name; replaces the MTL's `Sacral Spine` / `Thousand Muscles`.
- Post-Oxbear active Beelzebub slots: **Incinerate — Cerberus (A+) / Kilogram Hammer — Oxbear (A) / Tough Life — Infernal Buffalo (A)**.
- **Piranha Natteri** — target-62 monster: D individual / A school, 30 cm standard size, Le Rouge et Le Noir Mountain 6th Ridge.
- **Ah'Heman** — canonical Ballak shaman name, source-revealed in target 63.
- **Ahun/Ah'Heman kinship conflict** — current source says son; later Fandom biography says grandson. Preserve current source semantics until later text resolves it.
- **Fountain of Valor** — working rendering for Ballak's sacred healing spring.
- **The Protagonist of Hunting** — normalized production family title for targets 61–63 despite Chinese title variants.
- **Unfair Trade** — next family, targets 64–67; shifted witnesses E63–E66.

## Accepted evidence

Current accepted production evidence covers targets **1–63**:

- `manuscript/drafts/chapter-0001.md` through `chapter-0063.md`
- `qa/chapter-0001.md` through `chapter-0063.md`
- accepted family QA through `qa/families/protagonist-hunting-0061-0063.md`
- `editorial/provenance/chapter-0001.json` through `chapter-0063.json`
- `qa/acceptance/chapter-0001.json` through `chapter-0063.json`

Latest family QA: `qa/families/protagonist-hunting-0061-0063.md` — **PASS**.

## Editorial quality bar

Every chapter is reviewed for Chinese-source semantic fidelity, complete coverage, no invented/duplicated/sanitized material, Fandom-backed canonical English proper nouns where applicable, title-family continuity, reveal chronology, grammar/natural modern English, information-window and scene-break semantics, source provenance, and MTL alignment.

Formatting decisions preserved for eventual EPUB assembly include dialogue indentation, no narrative indentation, 1.65 line height, single-quote handling, styled information windows, `◆◆◆` scene breaks, and separate side stories. See `editorial/Recovered-Editorial-Decisions.md`.

Superseded reconstruction work remains available in Git history but is not accepted production state.
