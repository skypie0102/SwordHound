# Sword Hound recovery report

Recovery date: 2026-09-13 (Asia/Manila).

## Verified materials

| Material | Provenance | Verification |
| --- | --- | --- |
| Chapters 001–493 | `source-corpus.tar.xz`, Sword Hound ChatGPT library, displayed modified Sep 9 | All original chapter SHA-256 values and byte counts match; original index retained |
| Complete local EPUB | Local `Revenge of the Iron-Blooded Sword Hound (Completed).epub` | ZIP CRC passes; 493 chapters, 524 total members; 521 XML-based files parse; internal date July 29 |
| Editorial audit | Original download from **Recovering GitHub Repository Data** | Original bytes retained; 2,151 findings for a separate older 500-chapter edition |
| Production reports | **Continue Chapter 54** and **Continue Production Batch Close** | Saved in `prior-production-records.json`; reports are context, not recovered Git objects |

The source hashes for Chapters 361–363 match the prefix/suffix fragments recorded in the earlier production report:

- 361: `ed42d798c4194736c7eeae58201633911a18ad73167133075264ad10fa0f3e81`
- 362: `f426c4abe072432f81952666b2fd14aa672bf1b3f64c455fbb97c38ad3e3077a`
- 363: `a50e35b9d420be4304d5935193e53d6ab1cdf19e9d16658ba5587fa4b39fe55d`

This supports the identity of the source corpus, not recovery of the edited production chapters.

## Historical checkpoint

The last report says PR #57 was merged and `main` was translated/QA-complete through Chapter 372. Chapters 373–374 were reported complete and validated on `production/chapters-0373-plus`, but suspension blocked PR creation/merge. Chapter 375 was next. An earlier Chapter 54 checkpoint was explicitly corrected and is not used here.

The local EPUB's internal modified date is July 29. A library display date of September 9 may indicate upload/save time, not manuscript revision. The audit concerns 500 chapters; the recovered corpus and local EPUB each contain 493. These versions must be mapped before applying editorial changes.

`source-vs-local-epub.json` records a comparison of whitespace-normalized XHTML body text, including headings and other body elements. All 493 chapter documents differ by this measure. The source corpus has therefore not been replaced by the older EPUB's chapter files.

## Commit history

The new repository started with README commit `dd63f4915a6aceaa0c92d942b355d4c97bee51ba`. Recovery retains it as an ancestor. No original historical commits have been fabricated.

The old repository's Git transport, repository API, forks endpoint, and known commit endpoint returned not found. A GitHub search including forks returned only the new repository; an exact web search found no old-repository result. Searches of likely workspaces, downloads, temporary files, and Git configuration paths across the user profile and relevant D: directories found no old SwordHound clone or Git bundle. This does not prove every possible backup is gone.

Historical full merge identifiers preserved as future recovery leads:

| PR | Chapters | Reported merge SHA |
| --- | --- | --- |
| 39 | 297–304 | `a0242eda1eaeb9515606a7b6153e1b88b6234850` |
| 40 | 305–311 | `02e05c3544797ae87ef6804f8d58c1e6923ad49d` |
| 41 | 312–318 | `8a5956067ae1644bf222b0aa0a26fbe804818099` |
| 43 | 324–328 | `fdaf1e9353237874c08fc00ba6a764efd8b008a0` |
| 44 | 329–330 | `f3fcedc280e37c041bedd7dac9a6a502b4afa7dd` |

SHA identifiers alone cannot recreate missing trees, blobs, parent links, or author information.

## Remaining leads and limitations

- **Recovering GitHub Repository Data** was still uploading objects to the new repository when inspected. Its blobs were not yet attached to a commit. Any resulting commit should be fetched and reconciled without overwriting either recovery.
- The library lists `SwordHound-MTL-Source-Corpus-001-493.tar.xz`, an archive checksum, two `Missing Raws` ZIPs, raw text files, and older formatting reports/EPUBs. A download of `Missing Raws(1).zip` failed.
- The library copy of the completed EPUB failed to download. The local complete EPUB is preserved separately with its own provenance.
- `SwordHound-Info-Windows-and-Grammar-Corrected.epub` is referenced in the earlier recovery task and is the audit's named source; it needs separate recovery and validation.
- Original edited chapter Markdown, per-chapter QA, continuity YAML, glossaries, `chapters.yml`, mappings, workflows, and the 373–374 branch remain absent as original files. Historical reports must not be used to mark them present.

All restored data is separate from the read-only synced project `sources/` directory. Artifact hashes are recorded in `artifact-checksums.json`; the verifier checks byte integrity, not translation quality.

## Remote verification

Recovery commit `0a403ca9b97e7f4a6aeae78ff205efa72b473de7` was pushed to both `main` and `recovery/2026-09-13` without force. A fresh clone of GitHub `main` passed the recovery verifier. A complete Git bundle of the available new-repository history was also created locally. That bundle backs up the recovered repository; it does not contain the unavailable old-account history.
