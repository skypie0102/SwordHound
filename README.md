# Revenge of the Iron-Blooded Sword Hound

Recovered source, reference, and reconstruction material for the English EPUB project.

## Start here

**Every editorial session must read `HANDOFF.md` first.**

Current checkpoint: **67 / 500 accepted; next Chapter 68.** Latest accepted family: **targets 64–67 — Unfair Trade (1)–(4)**.

Recovered-English numbering remains one chapter behind: **64→E63, 65→E64, 66→E65, 67→E66**. The next family is **Blood Relatives, targets 68–71**, mapped **68→E67 through 71→E70**.

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

The accepted Unfair Trade family adds/revalidates:

- **Bourgeois Clan** — canonical clan/family form for the wealth/trade great family.
- **Sir Smuggler** — caravan leader in targets 64–66.
- **Aheul** — canonical spelling; source-revealed in target 65 as Ahun's younger sister.
- **Ahun / Ah'Heman kinship resolved** — target 67 explicitly says Aheul is Ah'Heman's granddaughter; combined with target 65's sibling relation and indexed Fandom, Ahun is Ah'Heman's **grandson**. Target 63 has been rebound to this correction.
- **Vikir's Special Law** — retained for the Underdog regulation the merchants unknowingly cite to Vikir himself.
- Merchant dependency strategy: deliberately non-germinating seed plus harmful narcotics hidden in decorative/personal goods.
- **Fountain of Valor** — reaffirmed as Vikir's target-67 reward; Ah'Heman collusion remains suspicion only.
- **Blood Relatives** — next family, targets 68–71; recovered-English witnesses E67–E70.

## Accepted evidence

Current accepted production evidence covers targets **1–67**:

- `manuscript/drafts/chapter-0001.md` through `chapter-0067.md`
- `qa/chapter-0001.md` through `chapter-0067.md`
- accepted family QA through `qa/families/unfair-trade-0064-0067.md`
- `editorial/provenance/chapter-0001.json` through `chapter-0067.json`
- `qa/acceptance/chapter-0001.json` through `chapter-0067.json`

The Chapter-63 Ahun/Ah'Heman kinship evidence has been rebound after the direct Chapter-65/67 continuity resolution. Latest family QA: `qa/families/unfair-trade-0064-0067.md` — **PASS**.

## Editorial quality bar

Every chapter is reviewed for Chinese-source semantic fidelity, complete coverage, no invented/duplicated/sanitized material, Fandom-backed canonical English proper nouns where applicable, title-family continuity, reveal chronology, grammar/natural modern English, information-window and scene-break semantics, source provenance, and MTL alignment.

Formatting decisions preserved for eventual EPUB assembly include dialogue indentation, no narrative indentation, 1.65 line height, single-quote handling, styled information windows, `◆◆◆` scene breaks, and separate side stories. See `editorial/Recovered-Editorial-Decisions.md`.

Superseded reconstruction work remains available in Git history but is not accepted production state.
