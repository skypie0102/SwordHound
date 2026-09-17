# Revenge of the Iron-Blooded Sword Hound

Recovered source, reference, and reconstruction material for the English EPUB project.

## Start here

**Every editorial session must read `HANDOFF.md` first.** It is the live cross-session continuation record and must be updated before the session ends or work is handed to another agent.

Current checkpoint: **25 / 500 accepted; next Chapter 26.** Seven complete title families are accepted under the restarted workflow: Chapters 1–3 (*Hellhound*), 4–7 (*The Baskerville Dog*), 8–11 (*Hounds of Hell*), 12–13 (*The Gluttonous Flies*), 14–17 (*Solitary*), 18–19 (*Bared Teeth*), and 20–25 (*Camus Morgue*). The next verified family is **Chapters 26–27 — The Graduate (1)–(2)**; Chapter 28 changes to *Special Laws of Vikir (1)*.

## Current source policy

- `source/chinese/chapters/` — **semantic/narrative authority** for the 500-chapter target edition.
- English *Revenge of the Iron-Blooded Sword Hound* Fandom wiki — **canonical English authority** for identified names, terms, locations, ranks, skills, monsters, organizations, titles, and other proper nouns where an applicable entry exists.
- `source/chapters/` — recovered 493-chapter English MTL/XHTML corpus; secondary alignment/phrasing reference only, except Chapter 55 where no Chinese raw exists.
- `source/chinese/chapter-exceptions.tsv` — missing/combined raw exceptions and verified nontrivial English-MTL alignments.
- `editorial/SOURCES.md` and `editorial/WORKFLOW.md` — authoritative source and editorial procedures.
- `AGENTS.md` — mandatory agent behavior, including continuous title-family processing and handoff maintenance.
- `HANDOFF.md` — exact operational continuation point for the next session/agent.
- `editorial/chapter-tracker.json`, `editorial/reconstruction-status.json`, `PROJECT_STATE.md`, and `PROGRESS.md` — accepted-state records and project history.

The Chinese corpus contains **492 physical files covering 499 of 500 target chapters**. Chapter **55** is the only confirmed missing Chinese raw. Seven physical files contain two target chapters each and remain intact because the raw files do not expose a safe second-chapter boundary by themselves; English output must still be split into separate target chapters.

## Critical workflow rules

- Do **not** assume Chinese target chapter `N` maps to English MTL chapter `N`; align by title and content.
- Determine the complete contiguous title-family boundary before accepting a chapter.
- Process the full title family as one continuity/QA batch.
- A finished title family or PR is a checkpoint, **not a stopping point**. Continue into the next family until the user pauses work, the corpus ends, or a genuine blocker prevents safe progress.
- Preserve source explicitness; do not sanitize or intensify.
- Protect reveal chronology even when the wiki contains later information.
- Do not import MTL/wiki narrative exposition absent from the Chinese merely because it is smoother or later confirmed elsewhere.
- Defer final visual/layout QA to complete-EPUB assembly unless explicitly requested earlier.
- Keep GitHub-hosted runner use sparse.

## Current canonical terminology notes

Current Fandom evidence establishes numbered Baskerville sword techniques as **Fangs** under the **Baskerville Fang Sword Style**.

The accepted Camus Morgue family adds/revalidates:

- **Camus Morgue**, **Adolf Morgue**, **Raspane Morgue**, **Osiris Le Baskerville**
- **Morgue Clan**
- **Quadra Casting**
- **Fireball / Ice Sphere / Thunder Ring / Mud Wall**
- **Sixth Circle** for Adolf
- source-scoped later title **Ironblood Empress** for future Camus where Chinese explicitly invokes it
- Beelzebub Slot 3 = Troll **Superspeed Regeneration** from Chapter 20 onward

## Accepted evidence

Current accepted production evidence covers Chapters **1–25**:

- `manuscript/drafts/chapter-0001.md` through `chapter-0025.md`
- `qa/chapter-0001.md` through `chapter-0025.md`
- accepted family QA through `qa/families/camus-morgue-0020-0025.md`
- `editorial/provenance/chapter-0001.json` through `chapter-0025.json`
- `qa/acceptance/chapter-0001.json` through `chapter-0025.json`

Latest family QA: `qa/families/camus-morgue-0020-0025.md` — **PASS**.

The earlier pre-restart Chapter 1 acceptance remains in Git history only and is superseded by the current family-reviewed evidence.

## Editorial quality bar

Every chapter is reviewed for Chinese-source semantic fidelity, complete coverage, no invented/duplicated/sanitized material, Fandom-backed canonical English proper nouns where applicable, title-family continuity, reveal chronology, grammar/natural modern English, information-window and scene-break semantics, source provenance, and MTL alignment.

Formatting decisions preserved for eventual EPUB assembly include dialogue indentation, no narrative indentation, 1.65 line height, single-quote handling, styled information windows, `◆◆◆` scene breaks, and separate side stories. See `editorial/Recovered-Editorial-Decisions.md`.

Superseded reconstruction work remains available in Git history but is not accepted production state.
