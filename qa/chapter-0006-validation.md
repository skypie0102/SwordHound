# Chapter 6 repository validation — 2026-09-14

The Chapter 6 acceptance workflow reached finalization only after these checks completed successfully on a complete GitHub checkout of the reviewed candidate:

- final punctuation fixes regenerated the explicit edit set, draft, provenance and preview;
- Chromium rendered the final preview at 1100×900 and 390×844 and regenerated the committed layout measurements/screenshots;
- `python tools/verify_recovery.py`;
- `python tools/build_editorial_draft.py 6 --check`;
- `python tools/build_chapter_preview.py 6 --check`;
- `python tools/rebuild_editorial_tracking.py --check`;
- `python -m unittest discover -s tests -v`;
- `git diff --check`.

These checks establish preserved-source integrity, deterministic materialization, complete Korean-line accounting, browser-rendered layout invariants, tracker consistency and test compatibility. They do not authenticate the supplied Korean as a publisher witness or constitute whole-EPUB release QA.
