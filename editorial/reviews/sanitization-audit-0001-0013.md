# Sanitization audit — Chapters 1–13

Date: 2026-09-16

Scope: every currently accepted reconstructed chapter, Chapters 1–13, checked specifically for wording that was softened, generalized, euphemized, or omitted relative to the supplied Korean witness. This is a narrow fidelity audit, not permission to make the prose more graphic than the source.

## Policy

Sanitization is an editorial error. Violence, gore, profanity, anatomical language, degradation, and other harsh material should retain the force and specificity actually present in the source. Conversely, an accepted line should not be intensified when the Korean does not support the stronger wording.

## Findings

The accepted reconstruction is not systematically sanitized. Chapters 3–7, 9, and 12 showed no sanitation requiring correction in this pass. Their existing text already preserves the relevant harsh or graphic material. Localized softenings were found in Chapters 1, 2, 8, 10, 11, and 13.

### Chapter 1

**Paragraph 75**

Current:
> What could have startled the family’s normally unshakable guardian knights?

Corrected:
> What could have made the family’s normally unshakable guardian knights tremble in fear?

Basis: Korean `도대체 무엇이 이 가문의 수호기사들을 그토록 공포에 떨게 만든 것일까?` explicitly describes the knights trembling in fear. “Startled” weakens the reaction.

**Paragraph 88**

Current:
> His knees were bruised, and his soft palms were already bloody.

Corrected:
> His knees were covered in scrapes, and his small hands were already covered in blood.

Basis: Korean `무릎은 온통 긁힌 상처투성이였고 ... 손은 이미 피범벅이 되어 있었다` specifies knees covered in abrasions/scrapes and hands covered in blood. “Bruised” is inaccurate and “bloody” is less specific than the source image.

### Chapter 2

**Paragraph 4**

Current:
> Not a trace remained of the aura he had built up through countless battles.

Corrected:
> Not a trace remained of the aura he had built up while repeatedly hovering at death’s door and coughing up blood.

Basis: Korean `수없이 죽음의 문턱을 넘나들며 피를 토해내면서 축적해 온 ...` explicitly includes repeatedly crossing death’s threshold and coughing/spitting up blood. “Through countless battles” drops both details.

### Chapter 8

**Paragraph 12**

Current:
> Tough, sinewy cuts of meat were simmered in broth made from chicken bones until everything softened into a thick mash.

Corrected:
> Various kinds of tough, sinewy offal were simmered in chicken-bone broth until everything softened into a thick mash.

Basis: Korean `질기고 근육이 많은 여러 종류의 내장` explicitly says various kinds of offal/internal organs. Generic “cuts of meat” removes that visceral specificity.

### Chapter 10

**Paragraph 24**

Current:
> Its heart hammered as though it might burst, and the blood vessels in its eyes swelled red.

Corrected:
> Its heart hammered as though it might burst, and its bloodshot eyes looked ready to burst as well.

Basis: Korean `심장은 터질 듯이 뛰었고, 눈은 핏발이 서려 터질 듯했다` applies the “about to burst” image to both the heart and the bloodshot eyes. The accepted English drops the latter half of that image.

### Chapter 11

**Paragraph 144**

Current:
> They drove into its body and opened serious wounds.

Corrected:
> They drove into its body and opened grievous, potentially fatal wounds.

Basis: Korean `몸을 꿰뚫어 치명적인 상처를 입혔다` describes the stakes piercing its body and causing `치명적인` wounds. “Serious” is too mild; “potentially fatal” preserves the source force without falsely implying Cerberus dies at that exact instant.

### Chapter 13

**Paragraph 67**

Current:
> Blood and bodily fluids flowed through Beelzebub’s hollow stinger and into Vikir.

Corrected:
> Blood and fluids from its organs flowed through Beelzebub’s hollow stinger and into Vikir.

Basis: Korean `피와 내장액` specifically says blood and organ/internal-organ fluids. “Bodily fluids” generalizes the anatomical detail.

**Paragraph 68**

Current:
> The gnawing hunger inside him eased, his cramped stomach gradually settling.

Corrected:
> His starving intestines filled, and the organs twisted by hunger gradually settled back into place.

Basis: Korean `그의 허기진 창자는 가득 찼다. 뒤틀렸던 내장들은 점차 원래 위치로 돌아왔다.` explicitly refers to the intestines filling and twisted internal organs returning to position. The accepted line abstracts both details into a settling stomach.

**Paragraph 74**

Current:
> When Beelzebub had been alive, the scope of that absorption had been nearly limitless, leaving countless victims stripped of achievements they had spent their entire lives building.

Corrected:
> When Beelzebub had been alive, the scope of that absorption had been nearly limitless, leaving countless victims stripped of abilities they had spent their entire lives building, powerless and disabled.

Basis: Korean says `수많은 사람들이 평생의 노력을 도둑맞아 무능하고 불구가 되었습니다.` The accepted line omits the stated consequence that victims were left powerless/incapacitated and disabled.

**Paragraph 109**

Current:
> Then Beelzebub drove its stinger into Cerberus’s corpse and began greedily drinking from its flesh and organs.

Corrected:
> Then Beelzebub drove its stinger into Cerberus’s corpse and began voraciously devouring its flesh and entrails.

Basis: Korean `필사적으로 살점과 내장을 게걸스럽게 먹어치우기 시작했다` uses deliberately visceral language: flesh, entrails/internal organs, and voracious devouring. “Drinking from” noticeably weakens the action.

## Chapters with no sanitation correction in this pass

- Chapter 3: retains the snakes’ broken necks, bulging eyes/tongues, evacuation of bowels and bladder, venom, and the punishment of the night-shift nannies.
- Chapter 4: retains the bullying injuries and crude insult register; no source harshness was removed for palatability.
- Chapter 5: retains suffocation, the bitten-off finger, shattered teeth, dislocated jaw, torn flesh, blood/saliva/snot, and fear-induced urination.
- Chapter 6: retains severed/broken injuries, the triplets being psychologically broken, and fear-induced urination.
- Chapter 7: retains fratricide, family extermination, revenge language, and explicit offal in the diet description.
- Chapter 9: retains participant injuries/deaths, gutting the Norvegicus, burning excrement, and the Hellhound’s lethal description.
- Chapter 12: retains Cerberus’s saliva/excrement/anus wording, the hacked skeleton, old blood, fratricide, and the journal’s descent into madness.

## Acceptance handling

These corrections change accepted prose and therefore invalidate the existing per-chapter accepted hashes for the affected chapters. They must be applied through the normal edit-source/regeneration workflow and the affected chapters must be reopened and re-accepted rather than silently patching generated `manuscript/drafts/` files.

A machine-readable replacement manifest accompanies this review at `editorial/reviews/sanitization-corrections-0001-0013.json`.
