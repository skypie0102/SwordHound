# Project State

**Checkpoint:** 2026-09-16  
**Target edition:** 500 chapters  
**Accepted:** 0  
**Staged:** 0  
**Next chapter:** 1

## Full editorial restart

The active reconstruction has been restarted from **Chapter 1** after restoring two project rules that were unintentionally lost during the Chinese-source migration:

1. chapters must be processed as complete contiguous **title-family batches**, and work must continue across subsequent title families for as long as safe work can be completed; and
2. the user-designated English Fandom wiki is the canonical English authority for established names, terms, locations, ranks, skills, monsters, organizations, titles, and other proper nouns, while the Chinese raw remains the semantic/narrative authority.

The earlier Chinese-first Chapter 1 acceptance is therefore **superseded**. Its draft, QA, acceptance, and provenance records have been removed from the active tree and remain available in Git history for reference only. No part of that former acceptance may be treated as current evidence without re-review under the complete workflow.

## Mandatory continuation record

`HANDOFF.md` is the operational handoff file for every work session.

Every agent/session must:

- read `HANDOFF.md` before beginning editorial work;
- reconcile it with this file, `PROGRESS.md`, and `editorial/chapter-tracker.json`;
- update it after meaningful progress and **always before ending a session or handing work to another agent**;
- record the exact next chapter/title-family action, in-progress work, source alignment, canonical-wiki checks, decisions, blockers, branch/PR state, and files created or changed.

If `HANDOFF.md` disagrees with accepted tracker/provenance evidence, correct the handoff immediately; accepted evidence remains authoritative for completed chapters.

## Active source baseline

### Semantic / narrative authority

Chinese is primary for the 500-chapter target edition.

- Physical Chinese files: **492**
- Target chapters covered by Chinese: **499 / 500**
- Confirmed missing Chinese chapter: **55**
- Combined two-chapter source containers: **7**
- Recovered English MTL/XHTML corpus: **493 chapters**, secondary/reference source only except Chapter 55

### Canonical English terminology authority

The English *Revenge of the Iron-Blooded Sword Hound* Fandom wiki is the canonical English reference for identified names, terms, locations, ranks, skills, monsters, organizations, titles, and other proper nouns. It does not override Chinese narrative meaning or reveal chronology.

Combined containers:

| Raw file | Target chapters |
| --- | --- |
| `075.txt` | 75–76 |
| `267.txt` | 267–268 |
| `284.txt` | 284–285 |
| `351.txt` | 351–352 |
| `353.txt` | 353–354 |
| `385.txt` | 385–386 |
| `495.txt` | 495–496 |

The combined raws remain intact because none exposes a sufficiently reliable second heading/boundary to justify destructive splitting from the raw alone. Translation outputs must still be split into individual target chapters.

## Missing Chapter 55

`055.txt` is genuinely absent between Chinese Chapters 54 and 56. The recovered English MTL Chapter 55 is the verified fallback source. It still requires full editing, canonical terminology verification, neighboring-continuity review, uncertainty review, and normal QA.

## Numbering warning

The Chinese target numbering and 493-chapter English MTL numbering diverge later. Same-number lookup is prohibited unless verified by title/content. Known nontrivial mappings are documented in `source/chinese/chapter-exceptions.tsv`.

## Current work

- **Accepted:** none under the restarted workflow.
- **Current target:** Chapter 1.
- **Active title family:** determine the full contiguous family beginning with Chapter 1 before accepting any chapter.
- **Next action:** follow `HANDOFF.md` and `editorial/WORKFLOW.md`; verify the title-family boundary, English-MTL alignment, and applicable Fandom canonical terms, then reconstruct the whole batch.
