# Editorial Handoff

**Checkpoint:** 2026-09-20  
**Phase:** POST-500 MANUSCRIPT COMPLETENESS AUDIT  
**Manuscript files present:** 500 / 500  
**Historical acceptance before audit:** 500 / 500  
**Currently retained accepted status:** 496 / 500, provisional pending corpus-wide completeness review  
**Confirmed needs rework:** 4 — Chapters 97, 316, 319, 420  
**Next target:** complete-family audit beginning with **The Illiad (85–89)**

## Why reconstruction was reopened

PR #125, **Complete reconstruction Chapters 494–500**, was merged into `main` on 2026-09-20. The run therefore did reach the end of the 500-target manuscript set.

However, a post-run manuscript-length audit found severe compression outliers. Direct Chinese-raw comparison confirms Chapters **97, 316, 319, and 420** are condensed summaries rather than full translations: broad plot survives, but substantial dialogue, narration, detail, and transitions are omitted.

The earlier “500 / 500 accepted; reconstruction complete” state is therefore no longer a safe quality claim. File coverage is 500 / 500; source-faithful editorial completeness is being revalidated.

See: `qa/manuscript-completeness-audit.md`.

## Triage evidence

For ordinary one-target Chinese containers, the corpus median `draft bytes / raw bytes` is about **0.85**.

Initial priority-review threshold: **< 0.60** (triage only, never an automatic fail).

- 48 chapters fall below 0.60.
- 22 chapters fall below 0.50.
- Confirmed by direct raw/draft reading:
  - Ch. 97 — ratio ~0.389
  - Ch. 316 — ratio ~0.319
  - Ch. 319 — ratio ~0.332
  - Ch. 420 — ratio ~0.348

Do not assume chapters above the threshold are complete; after the priority queue, perform a whole-corpus coverage pass.

## Source-policy correction recovered from accepted evidence

The old “Chapter 55 has no Chinese raw and is English-only” wording is stale.

There is no standalone `055.txt`, but accepted Chapter 54/55 boundary QA and provenance prove that `054.txt` is an overlapping 54–55 container:
- target54 ends before the appended hunting-ceremony material;
- target55's opening/title boundary is missing from Chinese and restored from E55;
- most of target55's body survives in `054.txt` and remains Chinese-primary where it overlaps.

`source/chinese/chapter-exceptions.tsv` already records this correctly. Source-policy docs are being reconciled to it.

## Branch / PR state

- Final reconstruction PR #125: **MERGED**.
- Active audit branch: `audit/post500-manuscript-completeness`.
- Audit evidence: `qa/manuscript-completeness-audit.md`.

## Exact next actions

1. Audit the complete **The Illiad (85–89)** family against Chinese, beginning with flagged 87–89; rebuild any compressed chapters rather than merely expanding prose.
2. Continue family-by-family through the priority queue in `qa/manuscript-completeness-audit.md`, preserving target order.
3. For every rebuilt chapter, regenerate chapter QA, provenance, acceptance evidence, and tracker state.
4. After all priority families pass, run a whole-corpus completeness pass so the byte heuristic is not treated as proof of safety.
5. Only after the completeness audit closes should the project return to complete-EPUB assembly and final presentation/epubcheck QA.
