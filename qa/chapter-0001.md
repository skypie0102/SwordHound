# Chapter 1 QA — Restarted Hellhound family

**Chapter-level status:** PASS  
**Family acceptance:** contingent on `qa/families/hellhound-0001-0003.md`  
**Target:** Chapter 1 — *Hellhound (1)*  
**Primary source:** `source/chinese/chapters/001.txt` (`fa9dfcf2f15c575d3a5971a93b9951d1ae0d0431`)  
**Aligned English reference:** `source/chapters/chapter-001.xhtml` (`93188cc599feec0ec8bbfc1e326fe3b70d2be0eb`)  
**Draft:** `manuscript/drafts/chapter-0001.md`

## Alignment

Target Chapter 1 → English MTL Chapter 1 is verified by:

- title family: *Hellhound (1)*;
- opening: end of the human/demon war and Vikir’s execution;
- Vikir/Hugo/Baskerville entities;
- Cradle of Swords and River Styx sequence;
- ending: the infant remains underwater and is discovered drinking Styx water.

The match is based on content, not chapter number alone.

## Canonical English evidence

Checked 2026-09-16 against the user-designated English Fandom wiki:

- `https://revenge-of-the-ironblooded-sword-hound.fandom.com/wiki/Vikir_Van_Baskerville` — **Vikir Van Baskerville**; novel first appearance *Ch. 1 - Hellhound (1)*; Van status/background.
- `https://revenge-of-the-ironblooded-sword-hound.fandom.com/wiki/Hugo_Le_Baskerville` — **Hugo Le Baskerville**; Patriarch; explicit noble title **Marquis**; novel first appearance *Ch. 1 - Hellhound (1)*.
- `https://revenge-of-the-ironblooded-sword-hound.fandom.com/wiki/Baskerville_Clan` — **Baskerville Clan**, alias **Iron-Blooded Sword Clan**; name-system distinction records Le/La for the main family and Van for secondary/illegitimate lines.
- `https://revenge-of-the-ironblooded-sword-hound.fandom.com/wiki/Grand_Mansion_of_the_Baskerville_Clan` — **Cradle of Swords** and **River Styx**.

The wiki is used only for canonical English naming. Chinese remains controlling for what happens and what is said.

## QA gate

| Check | Result | Notes |
| --- | --- | --- |
| Semantic fidelity | PASS | Complete Chinese raw reviewed in order; Chinese controls every narrative conflict with MTL/wiki. |
| Coverage | PASS | Execution placard, pre-execution wish, Cradle mechanics, infant injuries, Hugo dialogue, and final Styx exchange all retained. Wrapper/site headings are normalized into the chapter heading. |
| No invention | PASS | No MTL-only plot event or wiki-summary detail inserted. |
| No sanitization | PASS | Beheading display, illegitimacy, blood, infant wounds, contempt, and trial cruelty remain explicit. |
| Canonical terminology | PASS | Current Fandom evidence applied to Vikir, Hugo, Marquis, Baskerville Clan, Iron-Blooded Sword Clan, Cradle of Swords, River Styx, and Le/La/Van naming distinction. |
| Reveal chronology | PASS | No later family identities, ranks, abilities, or plot revelations imported. |
| Natural English | PASS | MTL grammar/pronoun failures rewritten without changing source content. |
| Scene/window semantics | PASS | Execution placard retained as `info-window`; source `* * *` retained as `◆◆◆`. |
| Boundary continuity | PASS | Ending correctly hands into Chapter 2’s intentional internal-perspective replay. |

## Material corrections versus the recovered English MTL

1. **Execution placard restored.** Chinese explicitly provides Vikir’s name and the charge of collusion with demons; the MTL omits the window.
2. **Victory wording restored.** Humanity’s victory is carved into stone, not merely “written in the books.”
3. **Shadow-work sentence repaired.** Chinese says Vikir’s hands were stained with blood working behind/in the shadows of the clan; MTL syntax is broken.
4. **Fate restored as the final abandoner.** Chinese says fate abandoned him after 500+ life-and-death ordeals; MTL shifts the agent.
5. **“Live again” restored.** Chinese explicitly gives a second wish line before the scene break.
6. **Birth-celebration sentence repaired.** MTL’s “dozens of layers of slopes” is a machine-translation failure.
7. **Cradle mechanics rebuilt from Chinese.** Blade maze, Styx-entry condition, finite shared power, and mother’s-milk comparison follow the raw.
8. **Hugo’s dialogue restored.** Chinese asks how the children can fight the Demon Realm and when he can raise them to guard his back. The MTL substitutes different survival-of-the-fittest dialogue.
9. **Knight reaction restored as astonishment/alarm**, not “arguments.”
10. **Final exchange restored.** Hugo asks what happened to the child; the knights answer that the young master is drinking the water.
11. **Final reaction corrected.** Hugo’s mouth hangs open in shock; the MTL changes this into a grin.

## Documented source/canonical conflicts

### Hugo’s title

Chinese Chapter 1 uses `伯爵` (“Count”) at the nursery introduction. The designated Fandom character page explicitly identifies Hugo Le Baskerville as a **Marquis**. Under the project’s split authority, the Chinese rank-word conflict is preserved here while the final English uses the canonical English title **Marquis**.

### Name particles

Chinese transliterations around Vikir’s main-line siblings do not cleanly map to the established English system. The Fandom Baskerville page explicitly records **Le/La** for the main family and **Van** for secondary/illegitimate lines. The draft uses that canonical English distinction while retaining the Chinese semantic point: Vikir’s name marks him as an outsider.

### Vikir’s age

The Chinese chapter first says Vikir had **just reached one hundred days**, then later calls him **not yet one hundred days old**. Both ideas remain represented in context. No unsupported exact-age reconciliation is invented.

## Chapter-level decision

**PASS.** No unresolved Chapter 1 semantic, coverage, explicitness, canonical-name, chronology, or prose blocker remains. Final acceptance is recorded only after the complete Hellhound (1)–(3) family QA passes.
