# Editorial Handoff

**Checkpoint:** 2026-09-20  
**Phase:** POST-500 MANUSCRIPT COMPLETENESS AUDIT  
**Manuscript files present:** 500 / 500  
**Current tracker state:** 496 accepted / 4 confirmed needs rework  
**Confirmed needs rework:** 97, 316, 319, 420  
**Completed audit family:** The Illiad (85–89) — rebuilt / PASS  
**Pending initial priority queue:** 44 chapters  
**Next target:** complete-family audit of **The Ghosts of the Ancestors (90–94)**

## Latest completed work — The Illiad (85–89)

Direct Chinese/raw review found that **all five historical drafts were materially compressed**, even though only 87–89 were caught by the initial <0.60 size-ratio detector. Chapters 85–86 therefore prove that length heuristics cannot certify completeness.

All five chapters were rebuilt from the Chinese primary source and rebound to fresh chapter QA, provenance, acceptance records, and family QA.

Key repairs:
- **85:** corrected Aiyen's bow from MTL-derived “five strings” to roughly **five people's draw strength / up to ten arrows**; restored full Ka'ah hunt, feast, and Silent Heel acquisition.
- **86:** restored Ah'Heman's full poison/medicine authority scheme, Leviathan/Bourgeois collaboration, clinical experiment motive, deliberate infection of Aheul, failed savior plan, and Akwilla confrontation.
- **87:** restored river-pouch trap, flour reveal, questioning, forged-letter/Chihuahua handwriting recollection, crowd response, denial strategy, and Akwilla's full honor trap.
- **88:** restored challenged-party timing rule, Vikir's anti-shaman contingency logic, Bakira exchange, Ah'Heman's outsider/abuse history and rise, and full pre-duel setup.
- **89:** restored spider-venom and jungle traps, Silent Heel/Incinerate combat, inner-thigh arrow, Rokoko corpse magic, and the **massive rear impact crushing Ah'Heman and the undead orangutans before the Oxbear reveal**.

Family evidence: `qa/families/illiad-0085-0089.md`.

## Audit state

Original priority queue: 47 ordinary one-target chapters below draft/raw byte ratio 0.60.

Completed from that queue: 87, 88, 89.

Remaining initial-priority chapters: **44**.

Confirmed separate needs-rework chapters remain 97, 316, 319, and 420 until their families are rebuilt.

All other retained acceptances remain provisional until the corpus-wide completeness pass closes.

## Source / alignment

- Illiad mapping remains **85→E84 through 89→E88**.
- Target90→E89 begins **The Ghosts of the Ancestors (1)**.
- Chapter55 remains hybrid: no standalone `055.txt`, but most target55 Chinese text survives appended in `054.txt`; E55 supplies only the missing opening/title boundary.

## Branch / PR state

- Working branch: `audit/illiad-85-89-completeness`.
- PR #127, **Rebuild The Illiad Chapters 85–89 for completeness**: OPEN.
- Prior corrective PR #126: merged.

## Files updated this batch

- `manuscript/drafts/chapter-0085.md` through `chapter-0089.md`
- `qa/chapter-0085.md` through `chapter-0089.md`
- `qa/families/illiad-0085-0089.md`
- `editorial/provenance/chapter-0085.json` through `chapter-0089.json`
- `qa/acceptance/chapter-0085.json` through `chapter-0089.json`
- `editorial/chapter-tracker.json`
- `editorial/reconstruction-status.json`
- `qa/manuscript-completeness-audit.md`
- `PROJECT_STATE.md`
- `PROGRESS.md`
- `HANDOFF.md`

## Exact next actions

1. Merge the Illiad completeness rebuild branch.
2. Create a new audit branch from updated `main`.
3. Audit the complete **The Ghosts of the Ancestors (90–94)** family against Chinese; flagged chapters are 92–94, but review 90–91 fully as well.
4. Rebuild every compressed chapter in the family, regenerate QA/provenance/acceptance, update tracker/audit state, merge, and continue directly to the next priority family.
