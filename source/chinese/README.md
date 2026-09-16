# Chinese Raw Corpus

This directory is the primary source corpus for the 500-chapter reconstruction.

## Coverage audit

- Target chapters: **1–500**
- Physical `.txt` files: **492**
- Target chapters covered by Chinese text: **499**
- Confirmed missing raw: **Chapter 55**
- Combined two-chapter containers: **7**

`055.txt` is absent. The surrounding files are normal Chapter 54 and Chapter 56 sources, so Chapter 55 is treated as genuinely missing and uses the recovered English MTL Chapter 55 as fallback.

Combined containers:

| File | Covers |
| --- | --- |
| `075.txt` | 75 + 76 |
| `267.txt` | 267 + 268 |
| `284.txt` | 284 + 285 |
| `351.txt` | 351 + 352 |
| `353.txt` | 353 + 354 |
| `385.txt` | 385 + 386 |
| `495.txt` | 495 + 496 |

The combined files were inspected for an explicit second-chapter heading such as `第76话`, `第268话`, etc. No reliable second marker was found. They are therefore intentionally **not physically split**: an arbitrary cut would alter source structure without sufficient evidence.

The English reconstruction must still emit one translated chapter per target chapter. The boundary is established editorially using source sequence plus verified English title/content alignment, with no gap or overlap.

## English reference warning

The recovered English MTL has 493 chapters and its numbering diverges from this 500-chapter target. Do not use same-number lookup as a general rule. See `chapter-exceptions.tsv` and `editorial/SOURCES.md`.
