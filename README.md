# Revenge of the Iron-Blooded Sword Hound

Recovered source, reference, and reconstruction material for the English EPUB project.

## Start here

**Every editorial session must read `HANDOFF.md` first.** It is the live cross-session continuation record and must be updated before the session ends or work is handed to another agent.

Current checkpoint: **34 / 500 accepted; next Chapter 35.** Ten complete title families are accepted under the restarted workflow: Chapters 1–3 (*Hellhound*), 4–7 (*The Baskerville Dog*), 8–11 (*Hounds of Hell*), 12–13 (*The Gluttonous Flies*), 14–17 (*Solitary*), 18–19 (*Bared Teeth*), 20–25 (*Camus Morgue*), 26–27 (*The Graduate*), 28–31 (*Special Laws of Vikir*), and 32–34 (*The Social Club*).

The next verified family is **Chapters 35–37 — Slave Auction (1)–(3)**. Chinese Chapter 35 has an anomalous translated heading `拍卖场之花 (1)`, but recovered English 35 and Chinese 36–37 establish the numbered Slave Auction family. Chapter 38 changes to **Sponsor (1)**.

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

The accepted Social Club family adds/revalidates:

- **Burning Suspension** — elite club in Underdog City.
- **Messinadnaro Family** — removed eighth local/merchant house; later details remain chronology-scoped.
- **Youth Self-Governance Committee** — descriptive rendering for the local heirs' organization.
- **Sword Graduator** — established rank; recovered-English `Gradient` rejected.
- Seven active local houses: **Montblanc, Pierre, Louis Vuitton, Chanel, Ferragamo, Hermes, Prada** — source/transliteration controlled where dedicated Fandom entries are unavailable.
- Chapter 32 tower arithmetic: **385 glasses**, with the 9×9 tier fixed at **81** despite an isolated later Chinese `80` slip.
- Chapter 34's isolated Hugo/Deputy-Magistrate referent is corrected to **Vikir** from immediate continuity.

Earlier accepted terminology includes **Underdog City**, **Chihuahua Baskerville**, **Kamu Morgue**, **Staffordshire Baskerville**, **Oxbear**, **Colosseo Academy**, recognized Baskerville knight-order names, and the established **Baskerville Fang Sword Style** rank/Fang system.

## Accepted evidence

Current accepted production evidence covers Chapters **1–34**:

- `manuscript/drafts/chapter-0001.md` through `chapter-0034.md`
- `qa/chapter-0001.md` through `chapter-0034.md`
- accepted family QA through `qa/families/social-club-0032-0034.md`
- `editorial/provenance/chapter-0001.json` through `chapter-0034.json`
- `qa/acceptance/chapter-0001.json` through `chapter-0034.json`

Latest family QA: `qa/families/social-club-0032-0034.md` — **PASS**.

## Editorial quality bar

Every chapter is reviewed for Chinese-source semantic fidelity, complete coverage, no invented/duplicated/sanitized material, Fandom-backed canonical English proper nouns where applicable, title-family continuity, reveal chronology, grammar/natural modern English, information-window and scene-break semantics, source provenance, and MTL alignment.

Formatting decisions preserved for eventual EPUB assembly include dialogue indentation, no narrative indentation, 1.65 line height, single-quote handling, styled information windows, `◆◆◆` scene breaks, and separate side stories. See `editorial/Recovered-Editorial-Decisions.md`.

Superseded reconstruction work remains available in Git history but is not accepted production state.
