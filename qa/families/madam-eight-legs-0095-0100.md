# Title-Family QA — Madam Eight-Legs (1)–(6)

**Family status:** PASS — COMPLETENESS REBUILD  
**Target range:** Chapters 95–100  
**Completeness-audit review:** 2026-09-20  
**Following family:** target Chapter 101 begins *Nostalgia (1)*.

## Audit result

The historical family PASS is superseded by this completeness review.

Direct Chinese/draft comparison found material completeness problems across the entire six-part family.

- Chapters 96–99 were already in the initial low-ratio priority queue.
- Chapter 97 had been directly confirmed as a summary-compression failure before this family audit.
- Chapter 95 was above the alert threshold but still compressed and also contains a newly verified localized Chinese-source omission.
- Chapter 100 was not merely compressed: its historical draft crossed the source boundary and imported a large section of target Chapter 101.

All six drafts have now been rebuilt against the Chinese primary source, with only the explicitly documented Chapter95 gap restored from E94.

## Evidence / mapping

| Target | Chinese source | Chinese SHA | Recovered-English witness | English SHA | Rebuilt draft SHA | Rebuilt QA SHA |
|---|---|---|---|---|---|---|
| 95 | `095.txt` + localized E94 bridge | `891ba63cdf585a6d5cb456cf55ac0c2a8a64dedc` | **E94** | `88b0d59eb7cc73e684a1d56c7db610c53cd92413` | `3bc9dacf572ec377d28579bcfb62a7f512b1aed2` | `d8390b1dca303ef7a3ff77535901ab4f699b5b0e` |
| 96 | `096.txt` | `a44930a8cfb09a245054bb64c5b4fad7c53de2e6` | **E95** | `3e1933668787f9f0138e808d722d9fc5e578bda5` | `786e708638bc941f68bbb7fea84e6b36c0dd4537` | `8284518284093b2fe864ecac0b3eebeb20168de8` |
| 97 | `097.txt` | `0ee54bd429913b5081a5728c70d46712dbda7319` | **E96** | `1b5f9ec23397fb15b25db1650fb0860234694548` | `9e7f4a942cdc5aa5bb6726990519f914213c7869` | `ae68eededc1fcce032da54ab177e0efea16b031e` |
| 98 | `098.txt` | `3e81774dab8c9a8cc7fff79812a1184a1377a6dc` | **E97** | `5c1a936e89692aa380e6aa1b21fd719672a1f09d` | `3aab83e12530126204a15cea8b7ad27e41fa7a7a` | `852a01b16c051392c9a72bff958a097a576e2986` |
| 99 | `099.txt` | `9de78fd15855a19f0e67ef0f02752c7d3a0893bc` | **E98** | `df6f149514287d5fadb6e8e249651cbec0aa8102` | `075a8d997fdf1ef2e4b94cd7da177711fd4755dc` | `47495d207066b7bd3223fd42613892191465a480` |
| 100 | `100.txt` | `0290a265ebc69a85eac8480030fe60e71e21b006` | **E99** | `6f7bbdba6b24537df925820e137906b98d46a655` | `90b4331e30a3aa835a2c6fc5a12fed0e649f128f` | `6769ba303173de3d5ddf97db984f185845029dd5` |
| boundary | `101.txt` — *Nostalgia (1)* | `efce896878033b37c07d419a5533ea538fa601bf` | **E100** | `fd40f3fd52afa198ff059e4295e47630b294360e` | next family | next family |

Verified shifted mapping remains **95→E94 through 100→E99; 101→E100**.

## Source / boundary corrections

### Target95 localized Chinese gap

C095 visibly jumps from the dead-guard/casualty paragraph to Vikir already patting **Aheul** on the back, with no introduction.

E94 aligns exactly on both sides of the gap and preserves the missing bridge:
- Vikir examines Madam's giant drag/leg tracks under the water;
- he identifies poisonous slime, black hair/flesh, and damaged wood;
- Aheul emerges from hiding inside a spice jar and reaches Vikir.

Only that span is restored from E94. The exception is recorded in `source/chinese/chapter-exceptions.tsv`.

### Target100 / 101 boundary

Chinese C100 and E99 both end with Vikir falling toward the gas-bloated Bog Salamander prepared as a landing cushion.

Chinese C101 and E100 both begin with the impact.

The historical target100 draft incorrectly continued across that boundary through:
- the landing and full-body injuries;
- Madam's post-fall condition and death;
- Beelzebub's S-rank Venom acquisition;
- Vikir's exhaustion/dream sequence;
- Bakira/Aiyen finding him.

All of that material has been removed from target100. It belongs to target101, which will be reviewed in the following **Nostalgia** family.

## Source-coverage findings

### Chapter 95
- Restored full village-destruction evidence, altar lure mechanism, relatively low casualty explanation, Ballak cleanup, Ahun's regret, and Vikir's full Baskerville-policy responsibility/debt-to-Ballak reasoning.
- Restored only the verified localized E94 bridge.
- Removed the old draft's partial/cherry-picked use of the gap evidence by making the restoration complete and explicitly scoped.

### Chapter 96
- Restored Ballak's collective opposition to confronting Madam, Akwilla's post-Adonai wounds, Bakira's shattered poisoned hind leg, and Akwilla's wounded-but-chief-first response.
- Restored Vikir's full strategic motives for hunting Madam and Aiyen's complete wolf/hound metaphor and promise scene.

### Chapter 97
- Resolved prior confirmed needs-rework state.
- Restored full tracking ecology, isolated-cliff reasoning, Bog Salamander bait plan, Bone-Sucking Mosquito mechanics, smoke dispersal, and the still-living boneless salamander landing preparation.

### Chapter 98
- Restored the complete dangerous ascent, slime-flooded rest-cave traps, dozens of skeletons, fingernail/fingerprint damage, summit carrion terrain, named Ballak dead, mourning ritual, and full declaration-of-war sequence.

### Chapter 99
- Restored Madam's full Chinese-primary window and Rokoko monster-compendium context.
- Restored summit-wave mechanics, lightning timing, deliberate left-side blind zone, Sixth Fang/silk-sac attack, doubled-leg regeneration reveal, catastrophic counterstrike, and Vikir's Bog Salamander recovery.

### Chapter 100
- Restored complete regeneration/Incinerate mechanics, egg-eating/pregnancy explanation, deliberate limb-multiplication center-of-gravity strategy, poison-vs-regeneration distinction, breastplate push, weak-joint cuts, cliff fall, failed web escape, and prepared landing setup.
- Corrected the target100/101 boundary.

## Continuity

- 94→95: target94 ends on Ah'Heman's village warning; target95 reveals Madam's attack.
- 95→96: Vikir declares he will confront Madam; target96 begins with the tribe opposing that decision.
- 96→97: Vikir leaves alone; target97 tracks Madam and prepares his resources.
- 97→98: preparation complete; target98 climbs to the nest.
- 98→99: Madam emerges; target99 begins the direct fight.
- 99→100: Madam reveals doubled regeneration; target100 opens by formalizing Vikir's Bog Salamander regeneration slot and continues the strategy.
- 100→101: target100 ends above the prepared Bog Salamander cushion; target101 begins at impact.

## Verdict

**PASS.** Chapters 95–100 have been rebuilt for complete source coverage and corrected boundary integrity. Chapter97's prior confirmed needs-rework status is resolved. The completeness audit advances to **Nostalgia (101–104)**.
