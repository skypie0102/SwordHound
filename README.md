# Revenge of the Iron-Blooded Sword Hound

Recovered source and reference material for the English EPUB project after loss of access to `shadowmonarchbooks-cloud/SwordHound`.

## Repository contents

- `source/chapters/` — all 493 chapter XHTML files from the September source corpus, unchanged.
- `source/chapter-sha256.tsv` and `source/chapter-index.tsv` — original checksums and index.
- `archives/source-corpus.tar.xz` — the original downloaded source archive.
- `artifacts/SwordHound-Local-2026-07-29.epub` — complete local reference EPUB, unchanged.
- `epub/local-2026-07-29/` — all 524 extracted EPUB files, including cover, styles, navigation, and front matter.
- `editorial/Editorial-Audit.md` — original historical audit of a separate 500-chapter edition; 2,151 findings/candidates.
- `PROJECT_STATE.md` and `recovery/` — recovered production context, provenance, checksums, and limitations.

## Formatting decisions preserved

Prior project decisions include dialogue indentation, no narrative indentation, 1.65 line height, single-quote handling, styled information windows, `◆◆◆` scene breaks, Highbro/Middlebro/Lowbro, and separate side stories. See `editorial/Recovered-Editorial-Decisions.md`. These requirements are not a claim that every recovered version implements them.

## Recovery note

The former repository was reported complete through Chapter 372, with 373–374 validated on an unmerged branch and Chapter 375 next. **Those edited production files and their original Git history have not been recovered.** Do not mistake the source XHTML for that finished translation/QA work. See [the recovery checkpoint](PROJECT_STATE.md) and [recovery report](recovery/RECOVERY_REPORT.md).

## Working with the source

Run `python tools/verify_recovery.py` with Python 3 to verify source hashes, archive contents, EPUB snapshot hashes, XML parsing, and EPUB manifest/spine references. This does not certify translation quality or replace EPUBCheck.

Keep archived originals unchanged. The September chapter corpus is not a complete EPUB package; the July snapshot is a separate complete reference package. Do not combine them silently or assume the older audit has been applied.
