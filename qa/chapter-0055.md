# Chapter 55 QA — The Hunter and the Hunted (1)

**Chapter-level status:** PASS  
**Family acceptance:** contingent on `qa/families/hunter-hunted-0055-0060.md`

## Evidence

- Chinese overlap container: `source/chinese/chapters/054.txt` — `4e16871bc046c162978c419dc585f526b37d2dc4`
- Recovered English Chapter 55: `source/chapters/chapter-055.xhtml` — `b3d243ed6bdbd0268e0281d18589d0b4c308604e`
- Draft: `manuscript/drafts/chapter-0055.md` — `4cab7e75783208f932d9d868cbdc57b5b252f57b`

## Source-mode correction

Target 55 is **not English-only**. There is no standalone `055.txt`, but physical `054.txt` appends most of target 55 after the true target-54 endpoint. E55 supplies the missing target-55 opening/title boundary and directly overlaps the Chinese body from the hunting ceremony onward.

Source authority for this chapter is therefore hybrid:
- E55 controls the missing opening about Ballak martial culture/language and establishes the chapter boundary/title.
- Chinese `054.txt` controls semantics wherever the target-55 body overlaps.
- Recovered-English corruption does not override Chinese overlap.

## Fidelity checks

- PASS — Ballak martial/cultural-language opening is restored from E55 without importing unrelated later exposition.
- PASS — hunter gathering, charcoal rite, protective spiked collar, public-urination joke, wolf-riding lesson, Ahun challenge, quiver theft, beating, Aiyen's punishment, and final “Did it hurt?” all come from the Chinese overlap.
- PASS — Vikir's pickpocketing is tied to Age-of-Destruction survival experience.
- PASS — Aiyen's ownership-rule intervention is explicit: she punishes Vikir herself and threatens Ahun if he touches her slave privately again.
- PASS — body/toilet material is factual and non-erotic.
- PASS — Chapter 55 ends on Aiyen checking Vikir's injured face and asking whether it hurt; Chapter 56 begins with the same question while they travel on Bakira.

## Boundary repair

This QA supersedes the old “Chinese raw genuinely missing; E55 sole source” assumption. The corrected exception is recorded in `source/chinese/chapter-exceptions.tsv`.

## Cycle-2 Phase 4 remediation

**Resolved 2026-09-26.** Restored the Chinese-source shaman instruction: hunters must receive his blessing before departure or he will **ring the warning bell**. The unsupported curse wording has been removed.

## Phase-4 decision

**PASS at chapter level after Phase-4 remediation.** Final acceptance requires the refreshed Chapters 55–60 family QA.
