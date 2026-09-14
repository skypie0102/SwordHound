# Chapter 7 repository validation — 2026-09-14

The Chapter 7 acceptance workflow reached finalization only after the reviewed candidate was regenerated with its final prose refinements and passed all of the following on a complete GitHub checkout:

- Chromium rendering at 1100×900 and 390×844, including committed layout measurements and screenshots;
- `python tools/verify_recovery.py`;
- `python tools/build_editorial_draft.py 7 --check`;
- `python tools/build_chapter_preview.py 7 --check`;
- `python tools/rebuild_editorial_tracking.py --check`;
- `python -m unittest discover -s tests -v`;
- `git diff --check`.

These checks establish preserved-source integrity, deterministic materialization, exact Korean-line accounting, browser-rendered layout invariants, tracker consistency and test compatibility. They do not authenticate the supplied Korean as a publisher witness or constitute whole-EPUB release QA.
