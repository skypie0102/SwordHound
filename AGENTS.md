# SwordHound Agent Instructions

These instructions govern reconstruction and editorial work in this repository.

## Mandatory session startup and handoff

`HANDOFF.md` is the live operational continuation record for this project.

### At the start of every work session

Read these files **before editing any chapter**:

1. `AGENTS.md`
2. `HANDOFF.md`
3. `PROJECT_STATE.md`
4. `PROGRESS.md`
5. `editorial/WORKFLOW.md`
6. `editorial/SOURCES.md`
7. `editorial/chapter-tracker.json`
8. `editorial/GLOSSARY.md`

Reconcile the handoff against accepted tracker/provenance evidence. Never assume a chapter is complete solely because `HANDOFF.md` or a historical progress note says so.

### During every work session

Keep `HANDOFF.md` current after meaningful checkpoints, especially after:

- determining a title-family boundary;
- verifying or changing MTL alignment;
- resolving a consequential canonical-name/term decision;
- accepting/staging chapters;
- opening, updating, or merging a PR;
- encountering a blocker that would matter to the next agent.

This reduces lost work if a session ends unexpectedly.

### Before ending or handing off every session

Updating `HANDOFF.md` is **mandatory**, even if no chapter was accepted. It must state:

- accepted/staged counts and exact next chapter;
- current contiguous title family and verified boundary, or why the boundary is still unresolved;
- chapter(s) actively in progress and their exact state;
- Chinese source container(s) reviewed;
- verified English-MTL mapping(s) and evidence;
- Fandom canonical-name/term/location checks completed and still pending;
- consequential translation/continuity decisions;
- unresolved questions/blockers;
- branch, PR, and merge state;
- files created/updated during the session;
- **the exact next actions another agent should perform**, in order.

Never leave the next agent with a vague instruction such as “continue Chapter N.” Preserve enough detail to resume without rediscovering completed analysis.

If `HANDOFF.md` conflicts with accepted chapter tracker/provenance evidence, accepted evidence wins and the handoff must be corrected immediately.

## Source authority

Effective **2026-09-16**, the project uses separate authorities for **semantic content** and **canonical English terminology**.

### Semantic / narrative authority

1. **Chinese raw** in `source/chinese/chapters/` — primary authority for plot, meaning, sequence, chapter content, explicitness, omissions/additions, and the identity of what is actually present in the source.
2. **Recovered English MTL** in `source/chapters/` — secondary reference for English phrasing and source alignment only. It may be heavily rewritten and must never override the Chinese raw.
3. **House style / recovered editorial decisions** — presentation and consistency only; never use style to alter source meaning.

The old Korean raw set is retired. Do not recreate, import, align against, or use Korean raws in the active workflow.

### Canonical English names and terminology

The user-designated English Fandom wiki is the canonical English reference for **names, recurring terminology, locations, ranks, skills, monsters, organizations, titles, and other proper nouns**:

- https://revenge-of-the-ironblooded-sword-hound.fandom.com/wiki/Revenge_of_the_Iron-Blooded_Sword_Hound_Wiki

Use the wiki to normalize the English rendering of an entity or term once the Chinese source establishes what entity or term is present. The wiki does **not** outrank the Chinese raw for plot, dialogue, omitted material, event sequence, characterization, or chapter-specific facts, and it must not be used to introduce later revelations early.

Namu Wiki and other supporting sources may be used for additional context and disambiguation. Record consequential conflicts and decisions rather than silently flattening variants.

### Missing Chinese raws

When no Chinese raw exists, the English MTL becomes the sole text source. Currently this applies to **Chapter 55**. Such chapters still require a full line edit, continuity pass, terminology pass, Fandom canonicalization pass, and QA. Record the absence of the primary source explicitly.

### Combined Chinese raws

Some physical Chinese files contain two target chapters. See `source/chinese/chapter-exceptions.tsv`.

Do not split a source file merely to make filenames look sequential. Split the raw only when the boundary is directly defensible from the source itself. When the source boundary is not reliable, keep the raw file intact and treat it as a shared source container. The translated result must still produce **one output chapter per target chapter**, with the division established by source sequence plus verified title/content alignment to the English reference.

## Numbering and English alignment

The target edition has **500 chapters**. The recovered English MTL corpus has **493 chapters**, and its numbering is not globally one-to-one with the Chinese target edition.

Never infer `target N == MTL N` unless explicitly verified. Before using an English MTL chapter as a reference, align it by chapter title, neighboring title family, opening/closing events, named entities, and scene sequence. Store verified nontrivial mappings in `source/chinese/chapter-exceptions.tsv` or a future complete alignment table, and summarize newly verified mappings in `HANDOFF.md`.

## Continuous title-family processing

**Process reconstruction in contiguous chapter-title families, not as isolated one-chapter stopping points.** Chapters sharing the same base title with numbered parts form one editorial/QA batch whenever they are contiguous in the target edition.

Before accepting any chapter in a batch, determine the complete contiguous title-family boundary from Chinese headings, verified English alignment, and available tracker/index evidence. Keep terminology, continuity, chronology, and source decisions consistent across the whole family.

**A completed title family is a checkpoint, not a stopping condition.** After one family has been editorially completed and integrated, immediately identify the next contiguous title family and continue processing it. Continue for as many chapters/title families as can be safely completed in the active work session until one of these conditions occurs:

- the user explicitly asks to stop or pause;
- the source corpus ends; or
- a genuine blocking issue prevents safe editorial work.

Do **not** stop merely because one chapter, one PR, or one title-family batch has finished. If a family is unusually large or a genuine blocker forces a split, document the exception and exact continuity handoff in `HANDOFF.md`.

## Editorial-first reconstruction workflow

Work in target-chapter order, beginning from the current `next_chapter` checkpoint.

For every chapter within the active title-family batch:

1. Resolve the Chinese raw container and any source exception.
2. Read the complete Chinese source before editing.
3. Align any English MTL reference by title/content; do not trust the number alone.
4. Identify canonical English names/terms/locations and other proper nouns through the English Fandom wiki where applicable; record meaningful conflicts or uncertainty.
5. Produce a faithful natural-English chapter. Preserve explicitness, tone, sequence, and information. Do not invent connective material to smooth over MTL problems.
6. **Do not sanitize the source.** Preserve violence, gore, profanity, anatomical language, degradation, sexual material, and other harsh or explicit content when present. Do not euphemize, generalize, omit, or soften it for palatability; equally, do not intensify beyond the evidence.
7. Check proper nouns and recurring terminology against the Fandom wiki, `editorial/GLOSSARY.md`, and neighboring accepted chapters while protecting reveal chronology.
8. Run chapter QA: semantic fidelity; no dropped, duplicated, invented, or sanitized material; canonical names/terms; title-family and chapter-boundary continuity; grammar and naturalness; information-window and scene-break semantics; provenance/alignment; and combined-pair integrity where relevant.
9. Only then mark the chapter accepted.
10. Update `HANDOFF.md` at the meaningful checkpoint and continue through the rest of the title family and subsequent families unless an explicit stopping condition applies.

For MTL-only Chapter 55, add a dedicated uncertainty pass: compare both neighboring chapters, resolve terminology from established context and the canonical English wiki, and avoid speculative fixes that cannot be supported.

## Editorial versus presentation QA

Editorial work comes first. During chapter reconstruction, prioritize source fidelity, grammar, awkward wording, mistranslations, names/terms, speaker attribution, continuity, chronology, information-window content/structure, scene-break semantics, provenance/alignment, historical-audit triage, and readable final prose.

Defer presentation/layout QA until the complete EPUB phase. Do not spend ordinary chapter-processing time or GitHub runners on Playwright/browser rendering, screenshots, dialogue-indent measurements, 1.65 line-height checks, viewport overflow checks, visual CSS tuning, or other final presentation validation unless the user specifically requests an earlier visual check.

Editorial acceptance must not depend on browser screenshots or layout metrics.

## Current checkpoint

The project has been fully restarted under the restored workflow.

- Accepted: **0 / 500**
- Staged: **0**
- Next target: **Chapter 1**
- Active family: must be determined before acceptance
- Live continuation record: `HANDOFF.md`
- Current policy/state: `PROJECT_STATE.md`
- Detailed procedure: `editorial/WORKFLOW.md`
- Source exceptions: `source/chinese/chapter-exceptions.tsv`

The earlier Chinese-first Chapter 1 acceptance is superseded and may be consulted only as historical analysis; it is not current accepted evidence.

## Repository hygiene

- Work on a dedicated branch for meaningful editorial batches/infrastructure changes.
- Preserve user-supplied Chinese raws byte-for-byte unless a source-file repair is explicitly justified.
- Do not physically split the seven audited combined raws without new evidence of a reliable boundary.
- Keep generated draft/QA/provenance artifacts out of accepted state until they pass the current workflow.
- Record explicit edits, provenance, QA questions, evidence, review mode, canonical-reference decisions, and title-family continuity decisions.
- Update `PROGRESS.md`, `PROJECT_STATE.md`, `editorial/reconstruction-status.json`, `editorial/chapter-tracker.json`, and `HANDOFF.md` as accepted batches advance.

## GitHub Actions / runner policy

- **Use GitHub-hosted runners as sparsely as possible.** Treat GitHub Actions as a last resort, not the default execution environment.
- Prefer direct repository/API edits, deterministic reasoning, static validation, and existing evidence over starting a workflow run.
- Do not create or trigger a runner merely to materialize files, update trackers, calculate hashes, perform text-only QA, run chapter-level formatting checks, or perform browser/layout QA deferred to complete-EPUB assembly.
- Batch any genuinely unavoidable runner work together at a much larger checkpoint, preferably complete-EPUB/release validation rather than individual title-family batches.
- Before triggering Actions, ask: **Can this be completed safely without a GitHub runner?** If yes, do that instead.
