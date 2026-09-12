# Revenge of the Iron-Blooded Sword Hound

Recovered working repository for the English EPUB project **Revenge of the Iron-Blooded Sword Hound**.

## Repository contents

- `source/chapters/` — chapter XHTML source for chapters 001–493.
- `source/chapter-sha256.tsv` — checksums for the recovered chapter corpus.
- `archives/SwordHound-MTL-Source-Corpus-001-493.tar.xz` — the original recovered source archive.
- `artifacts/SwordHound-Completed.epub` — completed EPUB export recovered on 2026-09-09.
- `artifacts/SwordHound-Info-Windows-and-Grammar-Corrected.epub` — earlier corrected EPUB export.
- `editorial/Editorial-Audit.md` — editorial audit covering the recovered EPUB.

## Formatting decisions preserved

The recovered work uses dialogue indentation, no narrative indentation, 1.65 line height, single-quoted dialogue handling, styled information windows, `◆◆◆` scene breaks, corrected Baskerville triplet names (Highbro, Middlebro, Lowbro), and the side-story separation requested during editing.

## Recovery note

This repository was reconstructed after the original GitHub account became unavailable. The recovered archive and EPUB exports contain the usable project data, but the original Git commit history was not available.

## Working with the source

The XHTML files are the editable source. The `chapter-sha256.tsv` file can be used to verify that a chapter has not changed during editing. EPUB files in `artifacts/` are reference exports; future revisions should be generated from the chapter source and validated with an EPUB checker before release.
