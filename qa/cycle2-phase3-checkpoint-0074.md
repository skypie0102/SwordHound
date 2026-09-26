# Cycle 2 Phase 3 Checkpoint — Chapters 1–74

**Date:** 2026-09-26  
**Phase:** 3 — corpus boundary/alignment/exception integrity  
**Reviewed:** 74 / 500 targets  
**Ordinary PASS:** 53  
**FAIL:** 0  
**EXCEPTION-DOCUMENTED:** 21  
**Families reviewed:** 21 / 118  
**Family PASS:** 14  
**Family EXCEPTION-DOCUMENTED:** 7  
**New source-exception rows during Phase 3:** 18  
**Manuscript edits during Phase 3:** 0  
**Next family:** Chapters 75–77 — *The Hound of the Night*

## New structural finding

The recovered English corpus develops a one-chapter offset after target Chapter 56:

- target 57 has no clean standalone English witness; E56 only partially overlaps its later setup;
- target 58 → E57;
- target 59 → E58;
- target 60 → E59;
- targets 61–74 continue as target N → E(N−1).

The tracker/provenance already carried these mappings, but `source/chinese/chapter-exceptions.tsv` did not. Phase 3 added machine-readable rows for targets 57–74 so the exception table now matches the established alignment evidence.

## Existing exceptions revalidated

- target 49: localized Chinese raw gap restored only from aligned E49;
- target 54: physical `054.txt` is a combined 54–55 overlap container and E54 supplies the missing target-54 closing exchange;
- target 55: no standalone 055 raw; most target-55 body survives in `054.txt`, while E55 supplies the missing opening/title boundary.

## Next action

Audit the combined `075.txt` container for targets 75–76, then continue in contiguous family order. Keep the 273-chapter remediation queue frozen and do not edit manuscripts during Phase 3.
