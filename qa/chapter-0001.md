# Chapter 1 QA — Chinese-first restart

**Status:** PASS  
**Target:** Chapter 1 — *Hellhound (1)*  
**Primary source:** `source/chinese/chapters/001.txt`  
**Secondary English reference:** `source/chapters/chapter-001.xhtml` — independently aligned to target Chapter 1 by title, opening/closing events, named entities, and scene sequence  
**Output:** `manuscript/drafts/chapter-0001.md`

## QA gate

| Check | Result | Notes |
| --- | --- | --- |
| Semantic fidelity | PASS | Full Chinese raw reviewed sequentially; Chinese meaning controls wherever the MTL differs. |
| Coverage | PASS | No narrative source segment intentionally omitted. Duplicate series/episode headers are normalized into the single English chapter heading. |
| No invention | PASS | Added English connective wording is stylistic only; no new plot facts or explanations were introduced. |
| Proper nouns / terminology | PASS | Vikir Van Baskerville, Hugo Le Baskerville, House Baskerville, River Styx, Demon Realm, and Cradle of Swords normalized consistently. |
| Explicitness / tone | PASS | Execution, illegitimacy, contempt, wounds, blood, and the utilitarian treatment of infants are retained without softening. |
| Natural English | PASS | MTL syntax, pronoun errors, literal artifacts, and incoherent lines were rewritten. |
| Chapter boundary | PASS | Chinese Chapter 2 intentionally revisits the nursery/Cradle events from Vikir’s perspective; the apparent overlap is source-authentic, not accidental duplication. |
| Formatting | PASS | `◆◆◆` scene break used; execution placard restored as an `info-window`; dialogue and thought punctuation normalized for later EPUB styling. |

## Material corrections versus the recovered English MTL

1. **Execution placard restored.** The MTL omits both `<Name: Vikir Van Baskerville>` and the charge for colluding with demons.
2. **Victory wording corrected.** Chinese says humanity’s victory was carved into stone; the MTL changes this to being written in books.
3. **Family-shadow description restored.** Vikir’s bloodstained work behind the scenes is rendered directly instead of the MTL’s broken syntax.
4. **Fate versus family corrected.** Chinese says fate abandoned Vikir after more than five hundred life-and-death ordeals; the MTL changes this to the family forsaking him.
5. **“Live again” restored.** The MTL drops the second part of Vikir’s final wish before the scene break.
6. **Birth-celebration sentence repaired.** The MTL’s “dozens of layers of slopes” is a machine-translation failure of the family receiving repeated happy news.
7. **Cradle explanation repaired.** Blade-maze mechanics, Styx entry condition, finite river power, and the mother’s-milk comparison are rendered from Chinese rather than inherited from broken MTL pronouns.
8. **Hugo’s major dialogue restored.** Chinese has Hugo asking how such children can fight the Demon Realm and when they will be strong enough to watch his back. The MTL replaces this with a different survival-of-the-fittest statement.
9. **Knight reactions repaired.** Chinese has cries/exclamations of shock, not “arguments.”
10. **Final exchange restored.** Hugo explicitly asks about the child, and the knights answer that the young master is drinking the water. The MTL misassigns “Sir” and loses the title.
11. **Final reaction corrected.** Chinese leaves Hugo staring with his mouth wide open; the MTL changes this into a grin.

## Source-specific decisions

### Hugo’s noble title

The Chinese raw uses `伯爵` at the nursery introduction, literally “Count.” The established English series terminology and the recovered English reference identify Hugo as **Marquis Hugo Le Baskerville**. The draft retains **Marquis** as a canonical title normalization rather than treating the Chinese localization’s rank word as a new rank change. This conflict remains documented rather than erased.

### Cradle of Swords

Chinese `刀刃摇篮` is literally closer to “Cradle of Blades.” The project term **Cradle of Swords** is retained as established terminology. The underlying mechanics are translated from the Chinese raw, so the terminology normalization does not alter the scene.

### Name particles

The Chinese transliterations corresponding to the Baskerville name particles are normalized to the established English forms `Van`, `Le`, and `Re` where applicable. This is a naming-system normalization, not a change to Vikir’s illegitimate status.

### Age wording inconsistency

The same Chinese chapter first says Vikir had **just reached one hundred days**, then later describes him as **not yet one hundred days old**. The draft preserves that source-level inconsistency instead of inventing an exact reconciliation. Chapter 2 likewise describes his body as roughly one hundred days old.

## Chapter 2 handoff

`source/chinese/chapters/002.txt` opens with Vikir checking his infant body, realizing he has returned to shortly after birth, then hearing Hugo’s nursery judgment and reliving the Cradle of Swords from his own perspective. This confirms that Chapter 1’s external-view ending at the Styx is complete and that the overlap at the start of Chapter 2 is intentional.

## Acceptance decision

**PASS.** Chapter 1 is suitable for acceptance under the Chinese-first workflow. No unresolved semantic, coverage, terminology, continuity, or formatting blocker remains. Future EPUB production still needs to apply the project CSS rules for dialogue indentation, narrative non-indentation, line height, and the styled information window.
