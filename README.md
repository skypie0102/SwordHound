# Revenge of the Iron-Blooded Sword Hound

Recovered source, reference, and reconstruction material for the English EPUB project.

## Start here

**Every editorial session must read `HANDOFF.md` first.** It is the live cross-session continuation record and must be updated before the session ends or work is handed to another agent.

Current checkpoint: **54 / 500 accepted; next Chapter 55.** Sixteen complete title families are accepted under the restarted workflow, through **Chapters 52–54 — Slaves of the Savage Tribe (1)–(3)**.

The next target family is **Chapters 55–60 — The Hunter and the Hunted**. Chinese Chapter 55 is missing, so recovered English 55 is the sole verified text fallback. Later recovered-English numbering shifts within this family, so alignment must be content-based.

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

The accepted Slaves of the Savage Tribe family adds/revalidates:

- **Akwilla** — source-revealed in Chapter 53 as Aiyen's mother, Ballak chieftain, and the current **Night Fox**. Earlier chapters remain chronology-scoped and are not retroactively rewritten.
- **Thorn-Tree Punishment** — descriptive working term for the Chapter 52 Ballak execution; not promoted as a dedicated canonical proper noun.
- **Tough Life** — Chapter 52 explicitly participates in Vikir's recovery after Madam Eight-Legs, alongside River Styx protection and Aiyen's noose rescue.
- **Ballak slave/husband-hunt distinction** — Aiyen claims Vikir as a slave rather than husband; coercive spouse-capture and reproductive-role context stays source-faithful and non-erotic.
- Ballak internal communal generosity and extreme hostility toward outsiders are both retained.
- Chapter 54 body/reproductive-health customs and toilet humor are kept factual and non-erotic.
- **The Hunter and the Hunted, target 55–60** is the next family; Chapter 55 uses the English fallback and later MTL numbering shifts.

Earlier accepted terminology includes **Aiyen**, **Ahun**, **Divine Archer Adonai**, **Madam Eight-Legs**, **Camus Morgue**, **Rosie Morgue**, **Tough Life**, **Infernal Buffalo ‘Murcielago’**, **Colosseo Academy**, and the established **Baskerville Fang Sword Style** rank/Fang system.

## Accepted evidence

Current accepted production evidence covers Chapters **1–54**:

- `manuscript/drafts/chapter-0001.md` through `chapter-0054.md`
- `qa/chapter-0001.md` through `chapter-0054.md`
- accepted family QA through `qa/families/slaves-savage-tribe-0052-0054.md`
- `editorial/provenance/chapter-0001.json` through `chapter-0054.json`
- `qa/acceptance/chapter-0001.json` through `chapter-0054.json`

Latest family QA: `qa/families/slaves-savage-tribe-0052-0054.md` — **PASS**.

## Editorial quality bar

Every chapter is reviewed for Chinese-source semantic fidelity, complete coverage, no invented/duplicated/sanitized material, Fandom-backed canonical English proper nouns where applicable, title-family continuity, reveal chronology, grammar/natural modern English, information-window and scene-break semantics, source provenance, and MTL alignment.

Formatting decisions preserved for eventual EPUB assembly include dialogue indentation, no narrative indentation, 1.65 line height, single-quote handling, styled information windows, `◆◆◆` scene breaks, and separate side stories. See `editorial/Recovered-Editorial-Decisions.md`.

Superseded reconstruction work remains available in Git history but is not accepted production state.
