# Project State

**Checkpoint:** 2026-09-16  
**Target edition:** 500 chapters  
**Accepted:** 1  
**Staged:** 0  
**Next chapter:** 2

## Chinese-first reconstruction

The active reconstruction uses the user-supplied Chinese raws as the primary source of truth. The Korean raw path remains retired from the repository and workflow.

### Accepted under the current policy

- **Chapter 1 — Hellhound (1)**: rebuilt from `source/chinese/chapters/001.txt`, with English MTL Chapter 1 independently aligned by title/content and used only as a secondary reference. Full semantic, coverage, terminology, continuity, prose, explicitness, and formatting QA passed. See `qa/chapter-0001.md` and `editorial/provenance/chapter-0001.json`.

The prior Korean-assisted Chapter 1–13 acceptance and later staging state remain superseded. Their history is recoverable through Git but does not count toward current completion.

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

The combined raws remain intact because none exposes a sufficiently reliable second heading/boundary to justify destructive splitting from the raw alone. Translation outputs must still be split into individual target chapters.

## Missing Chapter 55

`055.txt` is genuinely absent between Chinese Chapters 54 and 56. The recovered English MTL Chapter 55 is the verified fallback source. Chapter 55 must receive the same full editing and QA as every other chapter, with additional uncertainty and neighboring-continuity review because no Chinese raw is available.

## Numbering warning

The Chinese target numbering and 493-chapter English MTL numbering diverge later. Same-number lookup is prohibited unless verified. Known exceptions are documented in `source/chinese/chapter-exceptions.tsv`; future mappings must be established by title/content alignment.

## Chapter 1 source decisions

The Chapter 1 QA records several material MTL corrections: the omitted execution placard, the missing “live again” line, the altered Hugo dialogue, the mistranslated final “young master” exchange, and the incorrect final grin. It also documents two terminology normalizations: **Marquis Hugo Le Baskerville** despite the Chinese localization’s `伯爵`, and **Cradle of Swords** for `刀刃摇篮`.

## Next work

Proceed to **Chapter 2 — Hellhound (2)** under `editorial/WORKFLOW.md`. Chapter 2 intentionally overlaps part of Chapter 1 from Vikir’s internal perspective; preserve that source-authentic structure rather than deduplicating it.
