# Revenge of the Iron-Blooded Sword Hound

Recovered source, reference, and reconstruction material for the English EPUB project.

## Start here

**Every editorial session must read `HANDOFF.md` first.** It is the live cross-session continuation record and must be updated before the session ends or work is handed to another agent.

Current checkpoint: **60 / 500 accepted; next Chapter 61.** The latest accepted family is **Chapters 55–60 — The Hunter and the Hunted (1)–(6)**.

The 54/55 source exception has been corrected: physical `054.txt` overlaps targets 54 and 55. Target 55 is hybrid Chinese-overlap + E55 missing opening, not English-only.

The next verified family is **target Chapters 61–63 — The Protagonist of Hunting**, with shifted recovered-English witnesses **61→E60, 62→E61, 63→E62**. Target 64 begins **Unfair Trade (1)** and aligns to E63.

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

The accepted Hunter and Hunted family adds/revalidates:

- **54/55 combined-overlap exception** — `054.txt` contains target 54 plus most target 55. Target 54 ends at the hunt-offer/dawn-departure setup; target 55 begins with the E55 Ballak-language opening and then converges with the Chinese overlap.
- **Bakira** — Aiyen's wolf and hunting companion.
- **Oxbear** — standard window remains **Danger Rating A / 5 m / Le Rouge et Le Noir Mountain, 7th Ridge**; the old female encountered in the wild is an exceptional ~8 m individual.
- **Low Sword Graduator** — Aiyen's liquid aura in target 60; `Gradient` remains rejected.
- **Beelzebub Slot 1: Incinerate — Cerberus (A+)** — reaffirmed in target 60.
- **Cold Valley** — descriptive working rendering for the target-59 camp location; not promoted as a dedicated canonical proper noun absent stronger evidence.
- Recovered-English mapping through this family is content-shifted: **55 hybrid C054/E55, 56→E56, 57 no clean standalone E chapter, 58→E57, 59→E58, 60→E59**.
- Chinese target coverage is now 500/500 at least partially; Chapters **49 and 55** carry documented localized gaps.
- Next family: **The Protagonist of Hunting, target 61–63**; mapping **61→E60, 62→E61, 63→E62**.

Earlier accepted terminology includes **Akwilla / Night Fox**, **Aiyen**, **Ahun**, **Divine Archer Adonai**, **Madam Eight-Legs**, **Tough Life**, **Infernal Buffalo ‘Murcielago’**, **Colosseo Academy**, and the established Baskerville Fang/rank system.

## Accepted evidence

Current accepted production evidence covers targets **1–60**:

- `manuscript/drafts/chapter-0001.md` through `chapter-0060.md`
- `qa/chapter-0001.md` through `chapter-0060.md`
- accepted family QA through `qa/families/hunter-hunted-0055-0060.md`
- `editorial/provenance/chapter-0001.json` through `chapter-0060.json`
- `qa/acceptance/chapter-0001.json` through `chapter-0060.json`

The corrected Chapter-54 family evidence is rebound after the 54/55 split audit. Latest family QA: `qa/families/hunter-hunted-0055-0060.md` — **PASS**.

## Editorial quality bar

Every chapter is reviewed for Chinese-source semantic fidelity, complete coverage, no invented/duplicated/sanitized material, Fandom-backed canonical English proper nouns where applicable, title-family continuity, reveal chronology, grammar/natural modern English, information-window and scene-break semantics, source provenance, and MTL alignment.

Formatting decisions preserved for eventual EPUB assembly include dialogue indentation, no narrative indentation, 1.65 line height, single-quote handling, styled information windows, `◆◆◆` scene breaks, and separate side stories. See `editorial/Recovered-Editorial-Decisions.md`.

Superseded reconstruction work remains available in Git history but is not accepted production state.
