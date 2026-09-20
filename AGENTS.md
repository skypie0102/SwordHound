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

**Do not hard-code a project checkpoint into this rules file.** The live accepted/staged counts, next chapter, active title family, branch/PR state, and exact continuation point belong in `HANDOFF.md`, `PROJECT_STATE.md`, and `editorial/chapter-tracker.json`. This keeps agent rules stable while work advances.

### During every work session

Keep `HANDOFF.md` current after meaningful checkpoints, especially after:

- determining a title-family boundary;
- verifying or changing MTL alignment;
- resolving a consequential canonical-name/term decision;
- accepting/staging chapters;
- opening, updating, or merging a PR;
- encountering a blocker that would matter to the next agent.

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

The project uses separate authorities for **semantic content** and **canonical English terminology**.

### Semantic / narrative authority

1. **Chinese raw** in `source/chinese/chapters/` — primary authority for plot, meaning, sequence, chapter content, explicitness, omissions/additions, and the identity of what is actually present in the source.
2. **Recovered English MTL** in `source/chapters/` — secondary reference for English phrasing and source alignment only. It may be heavily rewritten and must never override the Chinese raw.
3. **House style / recovered editorial decisions** — presentation and consistency only; never use style to alter source meaning.

The old Korean raw set is retired. Do not recreate, import, align against, or use Korean raws in the active workflow.

### Canonical English names and terminology

The user-designated English Fandom wiki is the canonical English reference for **names, recurring terminology, locations, ranks, skills, monsters, organizations, titles, and other proper nouns**:

- https://revenge-of-the-ironblooded-sword-hound.fandom.com/wiki/Revenge_of_the_Iron-Blooded_Sword_Hound_Wiki

Use the wiki to normalize the English rendering of an entity or term once the Chinese source establishes what entity or term is present. The wiki does **not** outrank the Chinese raw for plot, dialogue, omitted material, event sequence, characterization, or chapter-specific facts, and it must not be used to introduce later revelations early.

If a relevant Fandom entry cannot be found or accessed, record that limitation. Do not pretend a generic wiki mention formally canonizes a proper term. Namu Wiki and other supporting sources may be used for context/disambiguation.

### Partial / missing Chinese source

There is currently no known target chapter that is wholly English-only.

**Chapter 55 has no standalone `055.txt`, but it is not missing in full.** Accepted boundary QA proves that `054.txt` is an overlapping 54–55 container. Recovered English Chapter 55 supplies the missing opening/title boundary; most of the Chapter-55 body survives in Chinese inside `054.txt`, and Chinese remains semantic authority wherever the texts overlap.

Other localized Chinese gaps/splices are documented in `source/chinese/chapter-exceptions.tsv`. Use the English witness only for the explicitly missing span and record the limitation in QA/provenance.

### Combined Chinese raws

Some physical Chinese files contain two target chapters. See `source/chinese/chapter-exceptions.tsv`.

Do not split a source file merely to make filenames sequential. Split the raw only when the boundary is directly defensible from the source itself. Otherwise keep the raw intact as a shared source container. The translated result must still produce **one output chapter per target chapter**, with the division established by source sequence plus verified title/content alignment to English references.

## Numbering and English alignment

The target edition has **500 chapters** and the recovered English MTL corpus has **493 chapters**. Numbering is not globally one-to-one.

Never infer `target N == MTL N` unless explicitly verified. Align by chapter title, neighboring title family, opening/closing events, named entities, and scene sequence. Record verified nontrivial mappings in `source/chinese/chapter-exceptions.tsv` or a future complete alignment table, and summarize newly verified mappings in `HANDOFF.md`.

## Continuous title-family processing

**Process reconstruction in contiguous chapter-title families, not isolated one-chapter stopping points.** Chapters sharing the same base title with numbered parts form one editorial/QA batch whenever contiguous in the target edition.

Before accepting any chapter in a batch, determine the complete contiguous title-family boundary from Chinese headings, verified English alignment, and available tracker/index evidence. Keep terminology, continuity, chronology, and source decisions consistent across the whole family.

**A completed title family is a checkpoint, not a stopping condition.** After one family is editorially completed and integrated, immediately identify the next contiguous title family and continue processing it. Continue for as many chapters/title families as can be safely completed in the active work session until one of these conditions occurs:

- the user explicitly asks to stop or pause;
- the source corpus ends; or
- a genuine blocking issue prevents safe editorial work.

Do **not** stop merely because one chapter, one PR, or one title-family batch has finished. If a family is unusually large or a genuine blocker forces a split, document the exception and exact continuity handoff in `HANDOFF.md`.

## Editorial-first reconstruction workflow

Work in target-chapter order from the current dynamic checkpoint.

For every chapter within the active title-family batch:

1. Resolve the Chinese raw container and any source exception.
2. Read the complete Chinese source before editing.
3. Align any English MTL reference by title/content; do not trust the number alone.
4. Identify canonical English names/terms/locations and other proper nouns through the English Fandom wiki where applicable; record conflicts/limitations.
5. Produce faithful natural modern English. Preserve explicitness, tone, sequence, and information. Do not invent connective material to smooth over MTL problems.
6. **Do not sanitize the source.** Preserve violence, gore, profanity, anatomical language, degradation, sexual material, and other harsh or explicit content when present. Do not euphemize, omit, or soften it for palatability; equally, do not intensify beyond the evidence.
7. Check proper nouns and recurring terminology against Fandom, `editorial/GLOSSARY.md`, and neighboring accepted chapters while protecting reveal chronology.
8. Run chapter QA: semantic fidelity; no dropped, duplicated, invented, or sanitized material; canonical names/terms; title-family and chapter-boundary continuity; grammar and naturalness; information-window and scene-break semantics; provenance/alignment; and combined-pair integrity where relevant.
9. Only then mark the chapter accepted.
10. Update `HANDOFF.md` at meaningful checkpoints and continue through the rest of the title family and subsequent families unless an explicit stopping condition applies.

For Chapter 55, use the documented hybrid-overlap workflow: E55 supplies only the missing opening/title boundary, while Chinese `054.txt` controls the surviving target-55 body. Compare neighboring chapters and avoid speculative restoration beyond the documented gap.

## Manuscript completeness audit guard

When the live handoff/tracker says a post-run completeness audit is active:

- do not treat prior PASS/accepted artifacts as proof that full source coverage was achieved;
- do not equate a coherent plot summary with a complete translation;
- directly compare the complete Chinese source against the draft for dialogue, narration, descriptions, transitions, windows, and explicit details;
- use size/length anomalies only as triage signals, never as automatic pass/fail rules;
- audit the complete title family when one member is suspicious;
- supersede stale QA/provenance/acceptance evidence when a chapter is rebuilt;
- do not advance to complete-EPUB assembly until the completeness audit is formally closed in the live state files.

## Full sanitization + completeness audit guard

When the live handoff/tracker marks a full sanitization + completeness audit cycle active:

- make that audit the immediate project priority;
- treat all historical acceptance/PASS artifacts as evidence only until the target clears the active cycle;
- review every target chapter directly; do not limit work to low-ratio or previously suspicious chapters;
- record sanitization fidelity and completeness as separate gates;
- check for both unsupported softening/euphemism/omission and unsupported intensification;
- verify complete source coverage for dialogue, narration, description, transitions, thoughts, windows, numbers/mechanics, scene order, and endings;
- keep title-family, chapter-boundary, combined-raw, overlap, source-gap, and English-alignment checks explicit;
- document safety-limited passages separately and still verify all surrounding ordinary material in full;
- remediate by complete family when needed, then refresh all affected QA/provenance/acceptance/family-QA/hash bindings;
- run a residual consistency sweep after remediation;
- do not begin or resume complete-EPUB assembly until the active audit is formally closed in the live state files.

## Editorial versus presentation QA

Editorial work comes first. Prioritize source fidelity, grammar, awkward wording, mistranslations, names/terms, speaker attribution, continuity, chronology, information-window content/structure, scene-break semantics, provenance/alignment, historical-audit triage, and readable final prose.

Defer presentation/layout QA until the complete EPUB phase. Do not spend ordinary chapter-processing time or GitHub runners on Playwright/browser rendering, screenshots, dialogue-indent measurements, 1.65 line-height checks, viewport overflow checks, visual CSS tuning, or other final presentation validation unless the user specifically requests an earlier visual check.

Editorial acceptance must not depend on browser screenshots or layout metrics.

## Repository hygiene

- Work on a dedicated branch for meaningful editorial batches/infrastructure changes.
- Preserve user-supplied Chinese raws byte-for-byte unless a source-file repair is explicitly justified.
- Do not physically split the seven audited combined raws without new evidence of a reliable boundary.
- Keep generated draft/QA/provenance artifacts out of accepted state until they pass the current workflow.
- Record explicit edits, provenance, QA questions, evidence, review mode, canonical-reference decisions, and title-family continuity decisions.
- Update `PROGRESS.md`, `PROJECT_STATE.md`, `editorial/reconstruction-status.json`, `editorial/chapter-tracker.json`, `editorial/GLOSSARY.md` where applicable, and `HANDOFF.md` as accepted batches advance.

## GitHub Actions / runner policy

- **Use GitHub-hosted runners as sparsely as possible.** Treat GitHub Actions as a last resort, not the default execution environment.
- Prefer direct repository/API edits, deterministic reasoning, static validation, and existing evidence over starting a workflow run.
- Do not create or trigger a runner merely to materialize files, update trackers, calculate hashes, perform text-only QA, run chapter-level formatting checks, or perform browser/layout QA deferred to complete-EPUB assembly.
- Batch genuinely unavoidable runner work at a much larger checkpoint, preferably complete-EPUB/release validation rather than individual title-family batches.
- Before triggering Actions, ask: **Can this be completed safely without a GitHub runner?** If yes, do that instead.
