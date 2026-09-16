# Project State

**Checkpoint:** 2026-09-16  
**Target edition:** 500 chapters  
**Accepted:** 0  
**Staged:** 0  
**Next chapter:** 1

## Source-policy reset

The reconstruction has been reset to Chapter 1 because the newly supplied Chinese raws are a better source than the previously used Korean raw set. The Korean files were translations from the Chinese material, so they have been removed from the active repository and workflow.

The prior Chapter 1–13 accepted state and Chapter 14–17 staging state are superseded. Their history remains recoverable through Git, but none of those artifacts count as accepted under the new policy.

## Active source baseline

Chinese is the primary source for the 500-chapter target edition.

- Physical Chinese files: **492**
- Target chapters covered by Chinese: **499 / 500**
- Confirmed missing Chinese chapter: **55**
- Combined two-chapter source containers: **7**
- Recovered English MTL/XHTML corpus: **493 chapters**, secondary/reference source only except Chapter 55

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

The combined raws were audited for explicit second-chapter markers. None exposes a sufficiently reliable second heading/boundary to justify destructive splitting from the raw alone, so they remain intact. Translation outputs must still be split into individual target chapters.

## Missing Chapter 55

`055.txt` is genuinely absent between the Chinese Chapter 54 and Chapter 56 files. The recovered English MTL Chapter 55 is the verified fallback source. Chapter 55 must receive the same full editing and QA as every other chapter, with additional uncertainty and neighboring-continuity review because no Chinese raw is available.

## Numbering warning

The Chinese target numbering and 493-chapter English MTL numbering diverge later. Same-number lookup is prohibited unless verified. Known examples are documented in `source/chinese/chapter-exceptions.tsv`; future mappings must be established by title/content alignment.

## Next work

Restart at Chapter 1 under `editorial/WORKFLOW.md`. No chapter is accepted until it has been rebuilt and QA'd against the Chinese-first policy.
