# Project State

**Checkpoint:** 2026-09-20  
**Target edition:** 500 chapters  
**Manuscript files present:** 500 / 500  
**Historical acceptance before post-run audit:** 500 / 500  
**Current retained accepted status:** 496 / 500, provisional  
**Needs rework (confirmed):** 97, 316, 319, 420  
**Project completion:** REOPENED — manuscript completeness audit active  
**Next audit family:** The Illiad (85–89)

The production run reached all 500 target manuscript files and final PR #125 was merged. A post-run integrity check then confirmed that multiple previously accepted drafts are summary-compressed relative to their Chinese raws. The repository therefore must not be treated as EPUB-ready yet.

Primary audit record: `qa/manuscript-completeness-audit.md`.

A 48-chapter priority queue was generated from unusually low draft/raw byte ratios (<0.60, excluding shared raw containers). This ratio is only a triage heuristic; direct source comparison determines pass/fail, and the remaining corpus still requires a completeness pass.

Chapter 55 source status is hybrid rather than English-only: there is no standalone `055.txt`, but most target-55 Chinese text survives appended in `054.txt`; E55 supplies the missing opening/title boundary.

Next phase: family-by-family completeness repair, then whole-corpus verification, then complete-EPUB assembly.
