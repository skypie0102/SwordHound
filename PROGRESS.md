# Reconstruction Progress

## 2026-09-16 — Full restart from Chapter 1 with mandatory handoff

**Current state:** 0 / 500 accepted; 0 staged; next Chapter 1.

The project was restarted from the beginning again after recovering established workflow rules that had been unintentionally dropped during the Chinese-source migration.

Restored rules:

- Chinese raws are the semantic/narrative authority.
- The English Fandom wiki is the canonical English reference for established names, terms, locations, ranks, skills, monsters, organizations, titles, and other proper nouns.
- Chapters are processed as complete contiguous title-family batches.
- Finishing a chapter, title family, or PR is a checkpoint, **not** a reason to stop; work continues across subsequent title families until the user pauses it, the corpus ends, or a genuine blocker prevents safe progress.
- Source explicitness is not sanitized.
- Editorial/source QA comes before final EPUB presentation QA.
- GitHub-hosted runners remain a last resort.

The previous Chinese-first Chapter 1 acceptance was invalidated because it was completed before these restored rules were fully active. Its draft, QA, provenance, and acceptance files were removed from the active tree; the work remains in Git history only and may be consulted as a non-authoritative lead during the new review.

A new root-level `HANDOFF.md` is now the mandatory cross-session operational record. Every session must read it first and update it before ending or handing off work.

**Next:** determine the complete title-family boundary beginning at Chapter 1, verify English-MTL alignment and applicable Fandom canonical terminology, then reconstruct that entire family from the Chinese raws before continuing directly to the next family.

## 2026-09-16 — Chinese-source migration

The active reconstruction was originally reset to Chapter 1 after the user supplied the Chinese raws from which the previously used Korean raws had been translated.

Corpus audit retained from that migration:

- 492 physical Chinese chapter files cover 499 target chapters.
- Chapter 55 is the only confirmed missing Chinese raw and uses the recovered English MTL Chapter 55 as its fallback text source.
- Seven Chinese files are combined two-chapter containers: 075→75–76, 267→267–268, 284→284–285, 351→351–352, 353→353–354, 385→385–386, and 495→495–496.
- Those seven combined raws remain intact because no defensible second-chapter marker was found in the raw alone; translated output must still be split by target chapter.
- English MTL numbering is not globally aligned with the Chinese 500-chapter target. Every secondary-source lookup must be aligned by title/content rather than chapter number alone.

See `HANDOFF.md`, `PROJECT_STATE.md`, `AGENTS.md`, `editorial/SOURCES.md`, `editorial/WORKFLOW.md`, and `source/chinese/chapter-exceptions.tsv`.
