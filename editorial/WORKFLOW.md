# Chinese-First Reconstruction Workflow

## Goal

Produce one polished English chapter for each target Chapter 1–500, using the Chinese raw as the semantic authority wherever available, the English Fandom wiki as the canonical English naming/terminology reference, and a full editorial/QA pass for every chapter.

## Continuous title-family processing

Reconstruct chapters as **contiguous title families**. Before starting, determine the complete family boundary from the target titles, `editorial/chapter-tracker.json`, Chinese headings, and verified English-reference alignment. A family such as `Hellhound (1)` through its last contiguous numbered part is one editorial batch for continuity and QA purposes.

Finishing one title family is a checkpoint, **not a stopping condition**. After integrating a completed family, immediately identify the next base-title family and continue editorial work. Continue across title families for as many chapters as can be safely completed until the user explicitly asks to stop/pause, the corpus ends, or a genuine editorial blocker prevents safe progress.

Do not stop merely because one chapter, one PR, or one title-family batch has finished. Start a new batch when the base title changes. If a title family is unusually large or a genuine blocker forces a split, document the exception and preserve a clear continuity handoff.

## 1. Resolve the source container

Read `source/chinese/chapter-exceptions.tsv`.

- Normal chapter: use `source/chinese/chapters/NNN.txt`.
- Missing Chapter 55: use verified English MTL Chapter 55 as the sole text source.
- Combined chapter: use the shared Chinese container listed in the exception table. Do not require a physical raw split.

Record the source path(s) in provenance.

## 2. Read Chinese before touching the English draft

For Chinese-backed chapters, read the complete relevant raw/container first. Establish scene order, title/title-family information, entities, terminology, explicit content, windows/lists, and chapter-ending transition. The recovered English MTL is not an authority when it conflicts with the Chinese.

The Chinese raw governs **what happens and what is said**. Canonical English rendering of established names, terms, locations, ranks, skills, monsters, organizations, and other proper nouns is handled separately through the English Fandom wiki.

## 3. Align the English MTL reference

The 493-chapter MTL numbering diverges from the 500-chapter target. Align by content, not by number: title/title-family sequence; first and last scene; distinctive proper nouns/skills/monsters; scene ordering/transitions; and neighboring continuity.

If alignment is uncertain, do not silently use a same-number chapter. Record the uncertainty and resolve it before acceptance.

## 4. Canonical English terminology check

Use the user-designated English Fandom wiki as the canonical English reference for names, terminology, locations, ranks, skills, monsters, organizations, titles, and other proper nouns:

https://revenge-of-the-ironblooded-sword-hound.fandom.com/wiki/Revenge_of_the_Iron-Blooded_Sword_Hound_Wiki

Use the wiki to choose the established English rendering **after the Chinese source identifies the underlying entity or term**. Do not use a wiki summary to override source dialogue, invent omitted events, alter characterization, or introduce future revelations before the chapter establishes them.

Consult `editorial/GLOSSARY.md` and neighboring accepted chapters for project continuity. Where the wiki, Chinese transliteration, MTL, and existing glossary differ, record the alternatives and adjudication. Namu Wiki and other supporting sources may be used for additional context and disambiguation.

## 5. Translate/edit

Create natural modern English that preserves the Chinese meaning, tone, explicitness, sequence, and level of detail. The MTL may provide a useful scaffold, but rewrite mistranslations, omissions, additions, awkward syntax, pronoun errors, terminology drift, and machine-like phrasing. Do not add explanatory material absent from the source.

**Do not sanitize.** Preserve violence, gore, profanity, anatomical language, degradation, sexual material, and other harsh or explicit content when present. Do not euphemize, generalize, omit, or soften it for palatability, and do not intensify beyond the evidence.

## 6. Combined-container chapter division

For a shared raw container:

1. Determine the two English target chapter identities through title/content alignment.
2. Locate the most defensible source-sequence boundary using the paired English references and event continuity.
3. Keep the original Chinese file intact unless the raw itself gives a reliable direct split marker.
4. Produce two separate translated chapter files.
5. QA the pair together and verify that the shared source has no untranslated gap and no duplicated overlap.
6. Record the chosen division in provenance/review notes.

The absence of a safe physical split is not permission to merge the English output.

## 7. Chapter QA gate

Every chapter must pass:

- semantic fidelity to the Chinese primary source;
- full coverage with no dropped, duplicated, invented, or sanitized material;
- canonical English proper nouns/terminology checked against the Fandom wiki where applicable;
- neighboring and title-family continuity;
- chapter-specific reveal chronology;
- polished grammar and natural modern English;
- correct information-window and scene-break semantics;
- source provenance and English-reference alignment;
- combined-pair split integrity where applicable.

Chapter 55 additionally requires explicit neighboring-context and uncertainty review because Chinese source evidence is unavailable.

## 8. Acceptance and batch continuation

Only after the QA gate:

1. write the accepted draft and QA/provenance evidence;
2. mark the chapter accepted in `editorial/chapter-tracker.json`;
3. update `editorial/reconstruction-status.json`, `PROJECT_STATE.md`, and `PROGRESS.md` at the appropriate batch checkpoint;
4. complete the rest of the current contiguous title family;
5. once that family is integrated, immediately determine the next title family and continue unless the user has asked to stop, the corpus has ended, or a genuine blocker exists.

A successful acceptance or PR merge is **not** itself a reason to stop processing.

## Editorial-first checks

During ordinary chapter processing, prioritize translation/source comparison, terminology, continuity, provenance, and text QA. Use deterministic text/integrity checks when available and practical.

Do not require Playwright, browser screenshots, CSS measurements, viewport checks, or GitHub Actions for ordinary title-family editorial acceptance. Presentation/layout QA belongs to the complete-EPUB phase unless the user explicitly requests an earlier visual check.

GitHub-hosted runners are a last resort. Prefer direct repository/API work, deterministic reasoning, and static validation; batch unavoidable runner work at a larger release checkpoint.

## Complete-EPUB presentation/release phase

At complete-EPUB assembly, apply and verify the preserved formatting requirements, including dialogue indentation, unindented narration, 1.65 line height, single-quote handling, information-window presentation, `◆◆◆` scene breaks, typography, CSS behavior, viewport/device rendering, EPUB packaging, and EPUBCheck.

## Working style

Use past-tense narration with intentional exceptions for general descriptions, direct thoughts, dialogue, and system/window text. Preserve rhetorical fragments where useful. Keep curly quotation marks; repair accidental point-of-view shifts. Normalize ellipses only where editorially reviewed.

Keep source-dependent terminology decisions documented in `editorial/GLOSSARY.md`. Canonical English wiki spellings should be preferred for identified entities, but do not flatten genuinely distinct source concepts merely because their translations look similar.

## Current restart state

The 2026-09-16 source migration superseded all earlier Korean-assisted draft/acceptance state. Reconstruction restarted from Chapter 1 under this Chinese-first policy. Chapter 1 has now been accepted; processing resumes at Chapter 2 and should proceed continuously by title family.
