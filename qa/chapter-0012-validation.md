# Chapter 12 repository validation — 2026-09-14

Chapter 12 was finalized only inside the single **The Gluttonous Flies (1–2)** title-family acceptance workflow after both reviewed chapters were materialized together. The family gate performed the following on a complete GitHub checkout:

- source-hash-gated materialization for Chapters 12–13;
- deterministic draft/provenance and preview generation for both chapters;
- preserved-source verification with `python tools/verify_recovery.py`;
- deterministic draft/preview checks across already accepted Chapters 1–11 plus the pending Chapters 12–13;
- tracker consistency checks;
- the full `python -m unittest discover -s tests -v` suite, including declared/undeclared MTL-only-gap tests;
- `git diff --check`;
- one preinstalled-Chrome session rendering Chapters 12–13 at 1100×900 and 390×844 with committed measurements and targeted screenshots;
- final acceptance-record generation followed by the same complete repository checks across accepted Chapters 1–13.

These checks establish preserved-source integrity, deterministic materialization, explicit Korean-line accounting, explicit Chapter 13 MTL-only witness-gap accounting, browser-rendered layout invariants, tracker consistency and test compatibility. They do not authenticate the supplied Korean as a publisher witness or constitute whole-EPUB release QA. No separate browser build was downloaded.
