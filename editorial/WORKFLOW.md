# Chinese-First Reconstruction Workflow

## Goal

Produce one polished English chapter for each target Chapter 1–500, using the Chinese raw as the semantic authority wherever available, the English Fandom wiki as the canonical English naming/terminology reference, and a full editorial/QA pass for every chapter.

## 0. Resume from the handoff

Before chapter work, read `HANDOFF.md` and reconcile it against:

- `PROJECT_STATE.md`
- `PROGRESS.md`
- `editorial/chapter-tracker.json`
- accepted QA/provenance files, if any
- `editorial/GLOSSARY.md`

`HANDOFF.md` is the operational continuation record, not a substitute for accepted evidence. If it is stale or conflicts with accepted tracker/provenance state, correct it before proceeding.

At minimum, identify from the handoff:

- exact next chapter;
- active title family and whether its complete boundary is verified;
- in-progress chapters and what review steps remain;
- Chinese source containers already read;
- English MTL mappings already verified;
- Fandom canonical terminology already checked and remaining checks;
- unresolved decisions/blockers;
- current branch/PR state;
- exact next actions.

**Do not hard-code the live project checkpoint into this workflow file.** The current accepted/staged counts, next chapter, active family, and branch/PR state belong in `HANDOFF.md`, `PROJECT_STATE.md`, and `editorial/chapter-tracker.json`.

Update `HANDOFF.md` after meaningful checkpoints and always before ending the session.

## 1. Continuous title-family processing

Reconstruct chapters as **contiguous title families**. Before accepting any chapter in a family, determine the complete family boundary from Chinese headings, verified English-reference alignment, `editorial/chapter-tracker.json`, and other available index/title evidence.

A family such as `Hellhound (1)` through its final contiguous numbered part is one editorial batch for continuity and QA purposes.

Finishing one title family is a checkpoint, **not a stopping condition**. After integrating a completed family, immediately identify the next base-title family and continue editorial work. Continue across title families for as many chapters as can be safely completed until the user explicitly asks to stop/pause, the corpus ends, or a genuine editorial blocker prevents safe progress.

Do not stop merely because one chapter, one PR, or one title-family batch has finished. If a title family is unusually large or a genuine blocker forces a split, document the exception and preserve a precise continuity handoff in `HANDOFF.md`.

## 2. Resolve the source container

Read `source/chinese/chapter-exceptions.tsv`.

- Normal chapter: use `source/chinese/chapters/NNN.txt`.
- Chapter 55: no standalone `055.txt`; use the documented 54/55 overlap in `054.txt`. E55 supplies only the missing opening/title boundary, while Chinese controls the surviving target-55 body.
- Combined chapter: use the shared Chinese container listed in the exception table. Do not require a physical raw split.

Record source paths in provenance and summarize unusual source status in the handoff.

## 3. Read Chinese before touching the English draft

For Chinese-backed chapters, read the complete relevant raw/container first. Establish scene order, title/title-family information, entities, terminology, explicit content, windows/lists, and chapter-ending transition. The recovered English MTL is not an authority when it conflicts with the Chinese.

The Chinese raw governs **what happens and what is said**. Canonical English rendering of established names, terms, locations, ranks, skills, monsters, organizations, and other proper nouns is handled separately through the English Fandom wiki.

## 4. Align the English MTL reference

The 493-chapter MTL numbering diverges from the 500-chapter target. Align by content, not by number, using:

- title/title-family sequence;
- first and last scene;
- distinctive entities, skills, monsters, or locations;
- scene ordering/transitions;
- neighboring continuity.

If alignment is uncertain, do not silently use a same-number chapter. Record the uncertainty and resolve it before acceptance. Put newly verified or changed alignment in `HANDOFF.md`; record nontrivial mappings in `source/chinese/chapter-exceptions.tsv` when appropriate.

## 5. Canonical English terminology check

Use the user-designated English Fandom wiki as the canonical English reference for names, terminology, locations, ranks, skills, monsters, organizations, titles, and other proper nouns:

https://revenge-of-the-ironblooded-sword-hound.fandom.com/wiki/Revenge_of_the_Iron-Blooded_Sword_Hound_Wiki

Use the wiki to choose the established English rendering **after the Chinese source identifies the underlying entity or term**. Do not use a wiki summary to override source dialogue, invent omitted events, alter characterization, or introduce future revelations before the chapter establishes them.

For consequential terms, record the page/entry or evidence summary, access limitation if any, competing forms, and decision. Consult `editorial/GLOSSARY.md` and neighboring accepted chapters for continuity. Namu Wiki and other supporting sources may be used for additional context and disambiguation.

Update `HANDOFF.md` with completed and pending canonical checks so the next agent does not repeat research unnecessarily.

## 6. Translate/edit

Create natural modern English that preserves the Chinese meaning, tone, explicitness, sequence, and level of detail. The MTL may provide a useful scaffold, but rewrite mistranslations, omissions, additions, awkward syntax, pronoun errors, terminology drift, and machine-like phrasing. Do not add explanatory material absent from the source.

**Do not sanitize.** Preserve violence, gore, profanity, anatomical language, degradation, sexual material, and other harsh or explicit content when present. Do not euphemize, generalize, omit, or soften it for palatability, and do not intensify beyond the evidence.

## 7. Combined-container chapter division

For a shared raw container:

1. determine the two English target chapter identities through title/content alignment;
2. locate the most defensible source-sequence boundary using paired English references and event continuity;
3. keep the original Chinese file intact unless the raw itself gives a reliable direct split marker;
4. produce separate translated chapter files;
5. QA the pair together for no untranslated gap and no duplicated overlap;
6. record the chosen division in provenance/review notes and `HANDOFF.md`.

The absence of a safe physical split is not permission to merge the English output.

## 8. Chapter QA gate

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

Chapter 55 additionally requires explicit boundary/neighbor review because its Chinese evidence is partial and embedded in `054.txt`; E55 may fill only the documented missing opening/title span.

## 9. Acceptance and batch continuation

Only after the QA gate:

1. write the accepted draft and QA/provenance evidence;
2. mark the chapter accepted in `editorial/chapter-tracker.json`;
3. update `editorial/reconstruction-status.json`, `PROJECT_STATE.md`, and `PROGRESS.md` at the appropriate batch checkpoint;
4. update `editorial/GLOSSARY.md` for newly accepted scoped terminology decisions;
5. update `HANDOFF.md` with the exact completed state and next action;
6. finish the rest of the current contiguous title family;
7. once that family is integrated, immediately determine the next title family and continue unless the user has asked to stop, the corpus has ended, or a genuine blocker exists.

A successful acceptance or PR merge is **not** itself a reason to stop processing.

## 10. End-of-session handoff gate

Before any session ends or work is handed to another agent, update `HANDOFF.md` even if no chapter was accepted.

The handoff must contain:

- timestamp/date and branch/PR state;
- accepted/staged counts and exact next chapter;
- active title family and verified range/boundary evidence;
- per-chapter in-progress status;
- source files reviewed;
- MTL mappings with alignment evidence;
- Fandom checks completed and pending;
- terminology/translation/continuity decisions;
- unresolved questions and blockers;
- changed/generated files;
- exact ordered next actions.

The next agent should be able to resume from this record without redoing completed analysis.

## Editorial-first checks

During ordinary chapter processing, prioritize translation/source comparison, terminology, continuity, provenance, and text QA. Use deterministic text/integrity checks when available and practical.

Do not require Playwright, browser screenshots, CSS measurements, viewport checks, or GitHub Actions for ordinary title-family editorial acceptance. Presentation/layout QA belongs to the complete-EPUB phase unless the user explicitly requests an earlier visual check.

GitHub-hosted runners are a last resort. Prefer direct repository/API work, deterministic reasoning, and static validation; batch unavoidable runner work at a larger release checkpoint.

## Post-500 completeness audit gate

When `HANDOFF.md` or the tracker marks a manuscript-completeness audit active:

1. Treat historical PASS/acceptance records as review evidence, not conclusive proof of full coverage.
2. Compare each audited draft against the complete Chinese source, including dialogue, narration, descriptions, transitions, windows, explicit details, and scene rhythm.
3. Reject summary-style condensation even when the major plot events are technically present.
4. Use byte/word-length anomalies only to prioritize review; never use them as an automatic pass/fail metric.
5. If one chapter in a title family is suspicious, audit the full contiguous family.
6. Rebuild stale QA/provenance/acceptance evidence whenever a chapter is corrected.
7. Do not enter EPUB assembly until current-state files formally close the completeness audit.

## Full sanitization + completeness audit cycle gate

When HANDOFF.md or the live tracker marks a full sanitization/completeness audit cycle active, it becomes the immediate editorial priority and complete-EPUB work is blocked.

The audit must use separate recorded gates for:

1. **sanitization fidelity** — no unsupported softening, euphemism, generalization, omission, or intensification of source harshness/explicitness;
2. **full completeness** — direct complete-source coverage of dialogue, narration, description, transitions, thoughts, windows, numbers/mechanics, scene order, and endings;
3. **boundary/alignment integrity** — chapter/family boundaries, combined raws, overlap containers, localized source gaps, shifted English mappings, and Side Stories.

During such a cycle:

- review every target chapter; historical acceptance and prior PASS artifacts are evidence, not an automatic pass;
- proceed in contiguous title-family order;
- do not use byte ratio, lexical overlap, or other diagnostics to skip direct review;
- record safety-limited passages explicitly while still verifying all surrounding ordinary source coverage;
- if one chapter fails either primary gate, review the complete family before repairs are accepted;
- re-run both primary gates after remediation;
- refresh chapter QA, provenance, acceptance, family QA/hash bindings, tracker acceptance SHAs, glossary entries, and source exceptions as applicable;
- run an independent residual/consistency sweep after remediation;
- validate all evidence/hash bindings before formally closing the cycle;
- do not unblock EPUB assembly until the live state files and audit record explicitly mark closure.

The active audit plan may define additional phase-specific evidence and checkpoint requirements. Keep those details in the live audit record rather than hard-coding a temporary chapter checkpoint here.

## Complete-EPUB presentation/release phase

At complete-EPUB assembly, apply and verify the preserved formatting requirements, including dialogue indentation, unindented narration, 1.65 line height, single-quote handling, information-window presentation, `◆◆◆` scene breaks, typography, CSS behavior, viewport/device rendering, EPUB packaging, and EPUBCheck.

## Working style

Use past-tense narration with intentional exceptions for general descriptions, direct thoughts, dialogue, and system/window text. Preserve rhetorical fragments where useful. Keep curly quotation marks; repair accidental point-of-view shifts. Normalize ellipses only where editorially reviewed.

Keep source-dependent terminology decisions documented in `editorial/GLOSSARY.md`. Canonical English wiki spellings should be preferred for identified entities, but do not flatten genuinely distinct source concepts merely because their translations look similar.

## Live state

Always derive the current checkpoint from `HANDOFF.md`, `PROJECT_STATE.md`, `editorial/chapter-tracker.json`, and accepted evidence. This workflow intentionally contains no fixed chapter/count checkpoint so it does not become stale as batches advance.
