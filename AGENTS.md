# SwordHound Agent Instructions

These instructions govern reconstruction and editorial work in this repository.

## Source authority

Effective **2026-09-16**, source priority is:

1. **Chinese raw** in `source/chinese/chapters/` — primary authority for plot, meaning, sequence, names, terminology, titles, explicitness, and omissions/additions.
2. **Recovered English MTL** in `source/chapters/` — secondary reference for English phrasing and alignment. It may be heavily rewritten and must never override the Chinese raw.
3. **House style / recovered editorial decisions** — presentation and consistency only; never use style to alter source meaning.

The old Korean raw set is retired. Do not recreate, import, align against, or use Korean raws in the active workflow.

### Missing Chinese raws

When no Chinese raw exists, the English MTL becomes the sole text source. Currently this applies to **Chapter 55**. Such chapters still require a full line edit, continuity pass, terminology pass, and QA. Record the absence of the primary source explicitly.

### Combined Chinese raws

Some physical Chinese files contain two target chapters. See `source/chinese/chapter-exceptions.tsv`.

Do not split a source file merely to make filenames look sequential. Split the raw only when the boundary is directly defensible from the source itself. When the source boundary is not reliable, keep the raw file intact and treat it as a shared source container. The translated result must still produce **one output chapter per target chapter**, with the division established by source sequence plus verified title/content alignment to the English reference.

## Numbering and English alignment

The target edition has **500 chapters**. The recovered English MTL corpus has **493 chapters**, and its numbering is not globally one-to-one with the Chinese target edition.

Never infer `target N == MTL N` unless explicitly verified. Before using an English MTL chapter as a reference, align it by chapter title, neighboring title family, opening/closing events, named entities, and scene sequence. Store verified nontrivial mappings in `source/chinese/chapter-exceptions.tsv` or a future complete alignment table.

## Reconstruction workflow

Work in target-chapter order beginning at Chapter 1.

For every chapter:

1. Resolve the Chinese raw container and any source exception.
2. Read the complete Chinese source before editing.
3. Align any English MTL reference by title/content; do not trust the number alone.
4. Produce a faithful natural-English chapter. Preserve explicitness, tone, sequence, and information. Do not invent connective material to smooth over MTL problems.
5. Check proper nouns and recurring terminology against `editorial/GLOSSARY.md` and neighboring accepted chapters.
6. Run chapter QA: semantic fidelity; no dropped, duplicated, or invented material; names/terms consistency; title-family and chapter-boundary continuity; grammar and naturalness; project formatting; removal of machine-translation artifacts; and, for combined raws, documented split integrity with no gap or overlap.
7. Only then mark the chapter accepted.

For MTL-only Chapter 55, add a dedicated uncertainty pass: compare both neighboring chapters, resolve terminology from established context, and avoid speculative fixes that cannot be supported.

## Current checkpoint

The source-policy migration invalidated the previous Korean-assisted acceptance state. Reconstruction has now resumed under the Chinese-first policy.

- Accepted: **1 / 500**
- Staged: **0**
- Latest accepted: **Chapter 1 — Hellhound (1)**
- Next target: **Chapter 2 — Hellhound (2)**
- Current policy/state: `PROJECT_STATE.md`
- Detailed procedure: `editorial/WORKFLOW.md`
- Source exceptions: `source/chinese/chapter-exceptions.tsv`

Chapter 2 intentionally repeats part of the nursery/Cradle sequence from Chapter 1 from Vikir's internal perspective. Preserve this source-authentic overlap rather than treating it as accidental duplication.

## Repository hygiene

- Work on a dedicated branch; do not write source-policy migrations directly to `main`.
- Preserve user-supplied Chinese raws byte-for-byte unless a source-file repair is explicitly justified.
- Do not physically split the seven audited combined raws without new evidence of a reliable boundary.
- Keep generated draft/QA/provenance artifacts out of the accepted state until they pass the current Chinese-first workflow.
- Minimize unnecessary GitHub Actions runs.
- Update `PROGRESS.md`, `PROJECT_STATE.md`, `editorial/reconstruction-status.json`, and `editorial/chapter-tracker.json` when acceptance state changes.
