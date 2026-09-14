# Chapter 8 repository validation — 2026-09-14

Chapter 8 was finalized only inside the single **Hounds of Hell (1–4)** title-family acceptance workflow after all four reviewed chapters were materialized together. The family gate performed the following on a complete GitHub checkout:

- source-hash-gated materialization for Chapters 8–11;
- deterministic draft/provenance and preview generation for all four chapters;
- preserved-source verification with `python tools/verify_recovery.py`;
- deterministic draft/preview checks and tracker consistency checks;
- the full `python -m unittest discover -s tests -v` suite;
- `git diff --check`;
- one Chromium installation/session rendering all four chapters at 1100×900 and 390×844, including committed measurements and targeted screenshots;
- final acceptance-record generation followed by the same repository checks across accepted Chapters 1–11.

These checks establish preserved-source integrity, deterministic materialization, explicit Korean-line accounting, browser-rendered layout invariants, tracker consistency and test compatibility. They do not authenticate the supplied Korean as a publisher witness or constitute whole-EPUB release QA. The single family-level browser run was used deliberately to comply with the repository's GitHub-runner minimization policy.
