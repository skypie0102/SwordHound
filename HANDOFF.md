# Editorial Handoff

**Checkpoint:** 2026-09-20  
**Phase:** POST-500 MANUSCRIPT COMPLETENESS AUDIT  
**Manuscript files present:** 500 / 500  
**Current tracker state:** 496 accepted / 4 confirmed needs rework  
**Confirmed needs rework:** 97, 316, 319, 420  
**Completed audit families:** The Illiad (85–89), The Ghosts of the Ancestors (90–94) — rebuilt / PASS  
**Pending initial priority queue:** 41 chapters  
**Next target:** complete-family audit of **Madam Eight-Legs (95–100)**

## Latest completed work — The Ghosts of the Ancestors (90–94)

Direct Chinese review found **all five historical drafts materially compressed**. Only 92–94 were in the initial <0.60 queue; 90–91 were above the threshold and still failed full-coverage review.

All five chapters were rebuilt and rebound to fresh QA, provenance, acceptance, and family QA.

Key repairs:
- **90:** full Oxbear window/territory trap, second lower-body strike, cub/mother exit, complete crowd judgment, Ah'Heman self-comparison, Ahun exchange, explicit abandonment of Ballak identity, Rokoko spell reaching Tomb of the Brave.
- **91:** full undead/nature-contract explanation, Death Knight window/mechanics, seven intelligent cases, burial shrouds, salt response, Ballak restraint around ancestors, Ah'Heman life/soul cost, quality-over-quantity escalation, full Adonai reveal.
- **92:** full master-aura mechanics, Vikir's injuries/mana pressure, Madam Eight-Legs bow origin/poison, River Styx/Beelzebub factors, Kilogram Hammer, Aiyen rescue, ten-arrow catch/crush, Akwilla barehanded interception.
- **93:** complete Akwilla–Adonai technical duel, storm-return arrows, repeated penetration, final front/back headshot, prime-Adonai caveat, ancestor-blood hostage tactic, salt-river dam release.
- **94:** complete saltwater purification, post-flood environment, Adonai bow recovery, Ah'Heman sorcery assessment, Thorn-Tree Punishment, Ahun's decision, explicit burning death, final village warning.

Family evidence: `qa/families/ghosts-ancestors-0090-0094.md`.

## Audit state

Original priority queue: 47 ordinary one-target chapters below ratio 0.60.

Completed from that queue: 87–89, 92–94.

Remaining initial-priority chapters: **41**.

Confirmed needs-rework chapters still open: **97, 316, 319, 420**.

The first two audited families also proved four above-threshold chapters incomplete: 85–86 and 90–91. Therefore after the priority queue, a whole-corpus direct review remains mandatory.

## Source / alignment

Ghosts mapping remains **90→E89 through 94→E93**. Target95→E94 begins **Madam Eight-Legs (1)**.

## Branch / PR state

- Working branch: `audit/ghosts-90-94-completeness`.
- PR: not yet opened at this handoff write.
- Illiad completeness PR #127: merged.

## Files updated this batch

- `manuscript/drafts/chapter-0090.md` through `chapter-0094.md`
- `qa/chapter-0090.md` through `chapter-0094.md`
- `qa/families/ghosts-ancestors-0090-0094.md`
- `editorial/provenance/chapter-0090.json` through `chapter-0094.json`
- `qa/acceptance/chapter-0090.json` through `chapter-0094.json`
- tracker, reconstruction status, audit record, project state, progress, handoff

## Exact next actions

1. Merge the Ghosts completeness rebuild branch.
2. Create a fresh branch from updated `main`.
3. Audit **Madam Eight-Legs (95–100)** in full, including unflagged 95 and 100. Chapter97 is already confirmed compressed; 96–99 are initial-priority chapters.
4. Rebuild every compressed chapter, regenerate all evidence, resolve Chapter97's `needs_rework` status, update counts/state, merge, and continue immediately to **Nostalgia (101–104)**.
