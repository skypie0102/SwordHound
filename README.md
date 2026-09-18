# Revenge of the Iron-Blooded Sword Hound

Recovered source, reference, and reconstruction material for the English EPUB project.

## Start here

**Every editorial session must read `HANDOFF.md` first.**

Current checkpoint: **132 / 500 accepted; next Chapter 133.** Latest accepted family: **targets 130–132 — The Freshman Talent Show (1)–(3)**.

The next verified family is **Test Your Skills, targets 133–138**, mapped **133→E132 through 138→E137**. Target 139 begins **Men are Power (1)** and maps to E138.

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

The accepted Freshman Talent Show family adds/revalidates:

- **The Freshman Talent Show** — accepted production family title for targets 130–132; witnesses E129–E131.
- **Pigi paired performance** — Vikir sings while Pigi performs the simple fist-and-step motion.
- **Military-song memorial** — paraphrased wording; source emotional function preserved.
- **Test Your Skills** — next family targets 133–138; witnesses E132–E137.
- **Men are Power** begins target 139 / E138.

The accepted Admission to the Academy family adds/revalidates:

- **Admission to the Academy** — accepted production family title for targets 126–129; witnesses E125–E128.
- **Cold Department / Hot Department** — accepted broad Colosseo divisions.
- **Tudor Donquixote / Bianca Fo Usher / Sinclaire / Pigi / Sancho Barataria** — canonical Academy student register.
- **Glorious Generation** — label for the unusually strong 20th class.
- **Commoner Vikir cover** — Vikir temporarily omits Van Baskerville at Colosseo.

- **The Hunt for the Second Son** — accepted production family title for targets 120–125; witnesses E119–E124.
- **Andromalius / Tenth Corpse** — source-revealed in target 121; Danger Level S+.
- **Ten Corpses** — canonical collective name for the ten Demon Kings and their human vessels.
- **Anubis** — legendary black bow formerly wielded by Adonai.
- **Nute Baskerville** — canonical spelling for Seth's mother.
- **Boston Terrier Le Baskerville / Pit Bull Knights** — Count and commander; 100-Graduator extermination-specialist order.
- **Great Dane Le Baskerville / Mastiff Knights** — Count and commander; 100-Graduator formal-war-specialist order.
- **Seven Counts** — major Baskerville military/political bloc; all seven sought to attend Vikir's banquet.
- **Osiris Le Baskerville** — first heir; Peak Sword Graduator in this scope.
- **Seth Le Baskerville** — second heir; Intermediate Sword Graduator / Underdog Magistrate; target 114 onward establishes nonhuman/demonic evidence without naming the later demon identity.
- **Intermediate Sword Graduator / Peak Sword Graduator** — public Vikir versus hidden Vikir in this family.
- **Sixth Fang / Seventh Fang** — target 116 combat comparison; never “Forms.”
- **Baskerville Trident** — accepted contextual label for Highbro / Middlebro / Lowbro.
- **Lady Roxana → Penelope La Baskerville → Pomeranian La Baskerville** — reaffirmed family line; raw Lucina/Freya/Firian-type drift remains normalized.
- **Baskerville Trident** — Highbro / Middlebro / Lowbro formally swear their lives to Vikir.
- **Seven Baskerville Knight Orders** — Vikir requests all seven for half a day at the close of target 119.

## Accepted evidence

Current accepted production evidence covers targets **1–132**:

- `manuscript/drafts/chapter-0001.md` through `chapter-0132.md`
- `qa/chapter-0001.md` through `chapter-0132.md`
- accepted family QA through `qa/families/freshman-talent-show-0130-0132.md`
- `editorial/provenance/chapter-0001.json` through `chapter-0132.json`
- `qa/acceptance/chapter-0001.json` through `chapter-0132.json`

Latest family QA: `qa/families/freshman-talent-show-0130-0132.md` — **PASS**.

## Editorial quality bar

Every chapter is reviewed for Chinese-source semantic fidelity, complete coverage, no invented/duplicated/sanitized material, Fandom-backed canonical English proper nouns where applicable, title-family continuity, reveal chronology, grammar/natural modern English, information-window and scene-break semantics, source provenance, and MTL alignment.

Formatting decisions preserved for eventual EPUB assembly include dialogue indentation, no narrative indentation, 1.65 line height, single-quote handling, styled information windows, `◆◆◆` scene breaks, and separate side stories. See `editorial/Recovered-Editorial-Decisions.md`.

Superseded reconstruction work remains available in Git history but is not accepted production state.
