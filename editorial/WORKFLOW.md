# Chinese-First Reconstruction Workflow

## Goal

Produce one polished English chapter for each target Chapter 1–500, using the Chinese raw as the semantic authority wherever available and applying a full editorial/QA pass to every chapter.

## 1. Resolve the source container

Read `source/chinese/chapter-exceptions.tsv`.

- Normal chapter: use `source/chinese/chapters/NNN.txt`.
- Missing Chapter 55: use verified English MTL Chapter 55 as the sole source.
- Combined chapter: use the shared Chinese container listed in the exception table. Do not require a physical raw split.

Record the source path(s) in provenance.

## 2. Read Chinese before touching the English draft

For Chinese-backed chapters, read the complete relevant raw/container first. Establish scene order, title/title-family information, names, terminology, explicit content, windows/lists, and chapter-ending transition. The recovered English MTL is not an authority when it conflicts with the Chinese.

## 3. Align the English MTL reference

The 493-chapter MTL numbering diverges from the 500-chapter target. Align by content, not by number: title/title-family sequence; first and last scene; distinctive proper nouns/skills/monsters; scene ordering/transitions; and neighboring continuity.

If alignment is uncertain, do not silently use a same-number chapter. Record the uncertainty and resolve it before acceptance.

## 4. Translate/edit

Create natural modern English that preserves the Chinese meaning, tone, explicitness, sequence, and level of detail. The MTL may provide a useful scaffold, but rewrite mistranslations, omissions, additions, awkward syntax, pronoun errors, terminology drift, and machine-like phrasing. Do not add explanatory material absent from the source.

## 5. Combined-container chapter division

For a shared raw container:

1. Determine the two English target chapter identities through title/content alignment.
2. Locate the most defensible source-sequence boundary using the paired English references and event continuity.
3. Keep the original Chinese file intact unless the raw itself gives a reliable direct split marker.
4. Produce two separate translated chapter files.
5. QA the pair together and verify that the shared source has no untranslated gap and no duplicated overlap.
6. Record the chosen division in provenance/review notes.

The absence of a safe physical split is not permission to merge the English output.

## 6. Chapter QA gate

Every chapter must pass: semantic fidelity; full coverage with no dropped/duplicated/invented material; terminology/proper-noun consistency; neighboring/title-family continuity; polished grammar and natural English; correct project formatting; source provenance; and, where applicable, combined-pair split integrity.

Chapter 55 additionally requires explicit neighboring-context and uncertainty review because Chinese source evidence is unavailable.

## 7. Acceptance/state update

Only after the QA gate: write the accepted draft and QA/provenance evidence; mark the chapter accepted in `editorial/chapter-tracker.json`; update `editorial/reconstruction-status.json`, `PROJECT_STATE.md`, and `PROGRESS.md`.

## Reset state

The 2026-09-16 source migration supersedes all earlier Korean-assisted draft/acceptance state. Restart from Chapter 1. Historical files remain retrievable from Git history but do not count toward current completion.
