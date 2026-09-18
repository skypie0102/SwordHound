# Revenge of the Iron-Blooded Sword Hound

Recovered source, reference, and reconstruction material for the English EPUB project.

## Start here

**Every editorial session must read `HANDOFF.md` first.**

Current checkpoint: **74 / 500 accepted; next Chapter 75.** Latest accepted family: **targets 72–74 — The Red Death (1)–(3)**.

Recovered-English numbering remains one chapter behind: **72→E71, 73→E72, 74→E73**. The next family is **The Hound of the Night, targets 75–77**, mapped **75→E74, 76→E75, 77→E76**. Target 78 begins **The Saintess (1)**.

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

The accepted Red Death family adds/revalidates:

- **Red Death** — fictional in-world plague; source-level transmission/prevention details are narrative mechanics, not real-world medical guidance.
- **Mushuhushu** — target-73 giant serpent. **Danger Rating A+ / 32 m / Le Rouge et Le Noir Mountain, 8th Ridge / ‘Nation-Swallowing Snake’**.
- **Ka'ah** — local old Mushuhushu individual known to Ballak; escapes target 73 wounded.
- **High Sword Graduator / six Fangs** — reaffirmed in the Mushuhushu fight; `Superior Gradient` / `Teeth` rejected.
- **Aheul** — fourteen in target 74; illness material remains strictly medical/nonsexual.
- **Ah'Heman** — grandfather of Ahun/Aheul; target-74 insult refers to their **parents**, not the MTL's `mother-in-law`.
- Ballak outsider-exit rule: >2 years residence plus a native family bond including at least three children; retained as source-level tribal law without sexualization.
- **The Hound of the Night** — next family spans targets 75–77.
- Physical `075.txt` combines targets 75–76 but lacks a safe internal source seam; do not invent a raw split.
- **The Saintess** begins target 78 / E77.

## Accepted evidence

Current accepted production evidence covers targets **1–74**:

- `manuscript/drafts/chapter-0001.md` through `chapter-0074.md`
- `qa/chapter-0001.md` through `chapter-0074.md`
- accepted family QA through `qa/families/red-death-0072-0074.md`
- `editorial/provenance/chapter-0001.json` through `chapter-0074.json`
- `qa/acceptance/chapter-0001.json` through `chapter-0074.json`

Latest family QA: `qa/families/red-death-0072-0074.md` — **PASS**.

## Editorial quality bar

Every chapter is reviewed for Chinese-source semantic fidelity, complete coverage, no invented/duplicated/sanitized material, Fandom-backed canonical English proper nouns where applicable, title-family continuity, reveal chronology, grammar/natural modern English, information-window and scene-break semantics, source provenance, and MTL alignment.

Formatting decisions preserved for eventual EPUB assembly include dialogue indentation, no narrative indentation, 1.65 line height, single-quote handling, styled information windows, `◆◆◆` scene breaks, and separate side stories. See `editorial/Recovered-Editorial-Decisions.md`.

Superseded reconstruction work remains available in Git history but is not accepted production state.
