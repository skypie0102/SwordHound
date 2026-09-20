# Editorial Handoff

**Checkpoint:** 2026-09-20  
**Phase:** POST-500 MANUSCRIPT COMPLETENESS AUDIT  
**Manuscript files present:** 500 / 500  
**Current tracker state:** 497 accepted / 3 confirmed needs rework  
**Confirmed needs rework:** 316, 319, 420  
**Resolved confirmed failure:** 97  
**Completed audit families:** The Illiad (85–89), The Ghosts of the Ancestors (90–94), Madam Eight-Legs (95–100) — rebuilt / PASS  
**Pending initial priority queue:** 37 chapters  
**Next target:** complete-family audit of **Nostalgia (101–104)**

## Latest completed work — Madam Eight-Legs (95–100)

All six historical drafts had source-coverage or boundary-integrity problems and were rebuilt.

### Chapter95 localized raw gap

C095 visibly jumps from the dead-guard/casualty paragraph to Vikir already patting **Aheul** on the back. E94 aligns exactly on both sides and preserves the missing bridge:
- Vikir inspects Madam's giant tracks beneath the floodwater;
- poisonous slime, black hair/flesh, and damaged wood narrow the identification;
- Aheul emerges from hiding inside a spice jar and reaches Vikir.

Only that missing span is restored from E94. The exception is now recorded in `source/chinese/chapter-exceptions.tsv`.

### Chapter100 / 101 boundary correction

Chinese100 and E99 end with Vikir falling toward the prepared gas-bloated Bog Salamander cushion.

Chinese101 and E100 begin at the impact.

The historical target100 draft incorrectly imported target101 material: landing injuries, Madam's death, S-rank Venom acquisition, exhaustion/dream sequence, and Bakira/Aiyen rescue. Target100 now ends at the cushion; target101 will be rebuilt next under **Nostalgia (1)**.

### Other family restorations

- **95:** complete village destruction/altar lure/casualty mitigation/Baskerville responsibility and Vikir debt-to-Ballak reasoning.
- **96:** full tribal opposition, Akwilla/Bakira injuries, Vikir strategic motives, and Aiyen's complete wolf/hound promise scene.
- **97:** prior confirmed failure resolved; full Madam tracking, Bog Salamander and Bone-Sucking Mosquito ecology/mechanics, and prepared landing resource restored.
- **98:** full cliff ascent, slime-cave traps, skeletons, summit carrion terrain, named Ballak dead, mourning, and declaration of war.
- **99:** full Madam window/Rokoko compendium, lightning-blind-zone tactic, Sixth Fang/silk-sac attack, doubled-leg regeneration reveal, catastrophic counterstrike, and Vikir regeneration.
- **100:** full regeneration/Incinerate/egg-eating/limb-multiplication/center-of-gravity strategy and corrected cliff-fall endpoint.

Family evidence: `qa/families/madam-eight-legs-0095-0100.md`.

## Audit state

Original priority queue: 47 ordinary one-target chapters below ratio 0.60.

Completed from that queue: 87–89, 92–94, 96–99.

Remaining initial-priority chapters: **37**.

Current unresolved confirmed failures: **316, 319, 420**.

Resolved confirmed failure: **97**.

Above-threshold failures found so far include 85–86, 90–91, 95, and 100, reinforcing that the whole-corpus pass remains mandatory.

## Source / alignment

- Madam mapping remains **95→E94 through 100→E99**.
- Target101→E100 begins **Nostalgia (1)** and owns the landing/kill/Venom/rescue material previously misplaced in target100.
- Chapter95 localized E94 restoration is documented in `source/chinese/chapter-exceptions.tsv`.

## Branch / PR state

- Working branch: `audit/madam-eight-legs-95-100-completeness`.
- PR #129, **Rebuild Madam Eight-Legs Chapters 95–100 for completeness**: OPEN.
- Ghosts completeness PR #128: merged.

## Exact next actions

1. Merge the Madam Eight-Legs completeness branch.
2. Create a fresh branch from updated `main`.
3. Audit **Nostalgia (101–104)** in full. All four chapters are in the initial priority queue.
4. Pay special attention to target101 because the historical target100 draft imported a large target101 span; ensure target101 now contains the full Chinese101/E100 content exactly once.
5. Rebuild all compressed chapters, regenerate QA/provenance/acceptance, update the audit state, merge, and continue immediately to the next priority family.
