# Revenge of the Iron-Blooded Sword Hound

Recovered source, reference, and reconstruction material for the English EPUB project.

## Start here

**Every editorial session must read `HANDOFF.md` first.**

Current checkpoint: **71 / 500 accepted; next Chapter 72.** Latest accepted family: **targets 68–71 — Blood Relatives (1)–(4)**.

Recovered-English numbering remains one chapter behind: **68→E67, 69→E68, 70→E69, 71→E70**. The next family is **The Red Death, targets 72–74**, mapped **72→E71 through 74→E73**. Target 75 begins **The Hound of the Night (1)** and the Chinese `075.txt` container covers targets 75–76.

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

The accepted Blood Relatives family adds/revalidates:

- **High Sword Graduator** — Vikir's formal target-68 rank after the two-year time skip.
- **Sixth Fang** — mastered in target 68; never `Sixth Teeth` or `Sixth Form`.
- **Peak Sword Graduator** — Vikir's pre-regression ceiling and current all-out combat estimate, not his formal target-68 rank.
- **Leviathan Clan** — canonical family/clan form for the serpent-emblem poison house; only this identity is source-revealed in target 69.
- **Red Death** — source-recognized epidemic in target 70.
- **Pomeranian La Baskerville** — canonical child name; about five years old at reveal.
- **Penelope La Baskerville** — canonical Hugo/Roxana daughter and Pomeranian's mother.
- **Lady Roxana** — canonical Hugo first-wife / Penelope mother form.
- **John Barrymore** — old Baskerville butler; `Deacon Barrymore` remains rejected.
- **The Red Death** — next family spans targets 72–74; recovered-English witnesses are E71–E73.
- **The Hound of the Night** begins at target 75; physical `075.txt` is combined targets 75–76.

## Accepted evidence

Current accepted production evidence covers targets **1–71**:

- `manuscript/drafts/chapter-0001.md` through `chapter-0071.md`
- `qa/chapter-0001.md` through `chapter-0071.md`
- accepted family QA through `qa/families/blood-relatives-0068-0071.md`
- `editorial/provenance/chapter-0001.json` through `chapter-0071.json`
- `qa/acceptance/chapter-0001.json` through `chapter-0071.json`

Latest family QA: `qa/families/blood-relatives-0068-0071.md` — **PASS**.

## Editorial quality bar

Every chapter is reviewed for Chinese-source semantic fidelity, complete coverage, no invented/duplicated/sanitized material, Fandom-backed canonical English proper nouns where applicable, title-family continuity, reveal chronology, grammar/natural modern English, information-window and scene-break semantics, source provenance, and MTL alignment.

Formatting decisions preserved for eventual EPUB assembly include dialogue indentation, no narrative indentation, 1.65 line height, single-quote handling, styled information windows, `◆◆◆` scene breaks, and separate side stories. See `editorial/Recovered-Editorial-Decisions.md`.

Superseded reconstruction work remains available in Git history but is not accepted production state.
