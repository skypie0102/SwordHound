# Project progress

This log records recovered evidence and new reconstruction work separately. Historical completion reports do not count as recovered chapter QA.

## 2026-09-13 — Korean sources and wiki QA policy restored

The user supplied `001-054.zip` and clarified that Korean raws are unavailable after Chapter 54. The current policy supersedes any earlier plan that would wait for Korean throughout the project.

- Preserved the original 285,286-byte ZIP and all 54 text files without changes. No missing or duplicate numbered files; strict UTF-8 decoding and each opening chapter number checked. Full passage alignment remains part of per-chapter QA.
- Added the archive/member checksum manifest and incorporated its verification into `tools/verify_recovery.py`.
- Registered the user-designated Fandom and Namu Wiki URLs in [SOURCES.md](editorial/SOURCES.md) for canonical names, terms, locations, and series context. Additional web research remains allowed. Direct opening failed in this batch, so no wiki content or term is falsely marked verified.
- Updated the 493-chapter tracker: 54 chapters use `korean_plus_mtl`, and 439 use `mtl_with_supporting_references`. Each available Korean source has a path and checksum.
- Added repository `AGENTS.md` and updated workflow, README, project state, and Chapter 1 review records so other agents receive the same source instructions.
- Chapter 1's full Korean file is now present. Existing nine QA items remain open; this source import makes no manuscript changes or new QA-acceptance claims.
- Validation passed: both source archives and chapter sets, unchanged EPUB/audit evidence, existing Chapter 1 draft/provenance, tracker regeneration, all six editorial tests, all Korean tracker links, and the Chapter 54/55 review-mode boundary.

**Next:** review Chapter 1 against its complete Korean file and specific wiki evidence, then proceed with assigned chapter batches. For Chapters 55 onward, complete MTL-based editorial QA under the declared source limitation rather than waiting for unavailable Korean. Preserve actual unresolved semantic issues and avoid introducing later wiki revelations into earlier chapters.

## 2026-09-13 — First reconstruction checkpoint

**Result:** the project now has an auditable editing workflow, a full chapter tracker, and a first Chapter 1 draft. **Newly QA-accepted chapters: 0.**

| Work | Completed result |
|---|---|
| Chapter inventory | 493 source chapters indexed with source hashes, original-file recovery status, historical status, and current reconstruction state. |
| Historical audit mapping | All 2,151 findings retained: 266 unique exact text/title matches, 40 ambiguous matches, 1,845 unmatched. No suggestion automatically applied. |
| Chapter 1 English pass | 41 paragraph edits; all 106 paragraphs retained in order. Every paragraph has original/draft text and hashes; every edit has a rationale. |
| Chapter 1 audit triage | ED-00001–ED-00037 reviewed as historical suggestions; duplicate suggestions identified and unresolved semantic changes held. |
| Source comparison | Selected Korean library-preview excerpts documented with provenance and reliability limits. The original raw-file download remains incomplete. |
| QA | Nine open Chapter 1 items covering meaning, terminology, chronology, sounds, and the remaining whole-chapter review. |
| Editorial foundation | Workflow, terminology register, explicit edit sets, reproducible draft builder, status overlay, generated tracker, and six conservation/failure tests. |

### Validation at this checkpoint

- Recovery verifier passed: preserved artifact hashes, all 493 source hashes, source archive membership, all 524 EPUB snapshot members, XML parsing, manifest and spine references.
- Chapter 1 draft/provenance regeneration check passed. Source identity and paragraph count match; unresolved key passages remain unchanged.
- Tracker/alignment regeneration check passed with the counts above.
- Six tests passed, covering paragraph conservation, altered source rejection, duplicate edits, paragraph deletion, unsupported QA acceptance, and hidden open issues.
- Generated draft and provenance files use fixed LF line endings so their hashes survive Windows checkouts.
- Published implementation commit `e97b254` to `main` and `reconstruction/first-batch` without rewriting history. A fresh clone from GitHub at that commit passed all recovery, draft, tracker, and six test checks, with a clean working tree.
- Created and verified the local backup `SwordHound-reconstruction-20260913.bundle` beside the checkout, containing all available repository history through this implementation checkpoint. The bundle is local and is not stored in GitHub.

These checks establish integrity and reproducibility. They do not certify translation quality or a new EPUB release.

### Next work

1. Seek an attributable Korean witness or recovered production/QA evidence for Chapter 1's disputed passages. The current library preview has conflicting names, titles, ages, speech, and reactions; it cannot settle those questions by itself.
2. Resolve [Chapter 1's issue list](qa/chapter-0001.md), complete full bilingual/continuity review, and do a final English reading before acceptance. Keep an explicit evidence trail for each decision.
3. Begin Chapter 2 with the same source-hash and paragraph-provenance procedure. Grammar work can continue while specific source questions remain open; unresolved chapters must stay visibly unaccepted.
4. Build and inspect a new EPUB only from editorially accepted material, preserving recovered formatting decisions and separating it from the unchanged July reference EPUB.
5. Continue checking concrete recovery leads if additional library exports, local backups, or the other recovery task produce original files. Import genuine old Git objects/history without rewriting existing commits.

## 2026-09-13 — Recovery foundation

Recovery commits: `0a403ca`, `8d58a98`, and `138e68f`, following the new repository's initial commit `dd63f49`.

- Preserved the original September corpus (493 XHTML chapters), its archive, and checksums.
- Preserved the July 29 local EPUB and all 524 extracted members.
- Recovered the unchanged older 500-chapter editorial audit containing 2,151 findings.
- Preserved prior production summaries and a 55-entry library inventory as recovery leads.
- Compared the two recovered chapter witnesses: all 493 whitespace-normalized chapter bodies differ. They are not interchangeable copies of the lost finished manuscript.
- Verified a fresh clone of the recovered repository. Created verified local Git bundles of the available new-repository history.

**Still unrecovered:** the former edited production Markdown chapters, original per-chapter QA, original continuity/glossary files and workflows, and old Git commit objects. Earlier reports described merged production through 372 and validated but unmerged 373–374. Those reports survive as context; the files do not yet.

See [the recovery report](recovery/RECOVERY_REPORT.md) and [current project state](PROJECT_STATE.md) for provenance and limitations.
