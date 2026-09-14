# Chapter 13 source comparison — 2026-09-14

Status: **source review in progress; not QA accepted**. New Korean-plus-MTL reconstruction. Recovered MTL SHA-256: `2bef27c163e103c90c2af57bd7170d4ed16782b7035e8919b14513e30865be14`. Supplied Korean SHA-256: `f44e049710f465061adfd8416be5e490ff3e0be2e584ffc2ffd3e1745acb83c5`.

The chapter has 166 recovered MTL paragraph slots and 146 Korean physical lines. Korean lines 1–4 are repeated headings. Unlike the preceding bilingual chapters, the supplied Korean has a genuine missing passage: recovered MTL paragraphs **15–35** have no Korean body-line counterpart. That gap must be represented explicitly as MTL-only provenance rather than by reusing unrelated Korean lines.

## Beelzebub reveal and physical form

Chapter 13 opens by supplying the name withheld at the end of Chapter 12: only Baskerville blood can draw **Beelzebub**. Use the epithet **the Gluttonous Fly**.

The recovered MTL's `Devil's first name` wording is nonsense; the inscription contains the Baskerville family name and the **sword's name**. Vikir recognizes Beelzebub from an illustration in a myth book from his first life.

The weapon has a long awl/stinger-like blade, three rounded ruby-like nodes near the guard, and a rough greenish handle whose overall silhouette evokes a giant fly. The exact ornamental wording can be smoothed, but the fly/stinger imagery should remain.

## Declared MTL-only passage: paragraphs 15–35

The supplied Korean jumps directly from `one of those remnants was Beelzebub` to Vikir's prior-life fasting habits. MTL paragraphs 15–35 therefore have no Korean witness in the supplied file. They are not discarded: they remain part of the recovered chapter and are supported in their core claims by Fandom's Beelzebub, Demonic Creatures, Equipment, Dungeon and Vikir Synopsis pages.

The passage establishes, without importing later details:
- the Seven Great Families' heads each confronted one of the Seven Calamities/Demon Constellations;
- Baskerville's ancestral victory left Beelzebub's remains/weapon associated with the family;
- in Vikir's first timeline the forgotten weapon eventually fell into demon hands and appeared on later battlefields;
- in the current timeline Vikir claims it first;
- Beelzebub fuses into his **right hand/wrist** and can emerge as a concealed spare weapon;
- its demonic nature immediately imposes supernatural hunger on Vikir.

These paragraphs require a new explicit `mtl_only_paragraphs` declaration in the alignment/validator. They must not be marked as Korean-verified.

## Hunger and first skill: Hellhound

Vikir is accustomed to extreme fasting from his previous life, so the sudden crippling hunger is clearly supernatural. Beelzebub draws him toward the earlier Hellhound corpse and drinks its blood and bodily fluids through its stinger/awl.

The first acquired skill is the Hellhound's bleeding ability. Supporting Fandom calls this **Hemorrhage**; the compact window may retain `Bleeding` if that is the recovered chapter's displayed label. The effect is that even shallow wounds bleed and continue bleeding much longer than normal.

Beelzebub's historical living form could steal broadly, but the artifact in Vikir's possession is limited to **three stored skills** at this point. Do not import later slot contents.

The first info window is:
- Slot 1: Bleeding / Hemorrhage — Hellhound (B+)
- Slot 2: None
- Slot 3: None

Recovered NBSP paragraphs surrounding the window remain provenance-accounted and are suppressed from reader-facing output.

## Cerberus feeding and shared pain

Still hungry, Beelzebub leads Vikir back to the assessment area and the Cerberus corpse. Vikir stops it from consuming too much because the corpse is evidence for the practical examination and must remain inspectable.

The recovered MTL loses an important Korean line after Vikir slaps the back of his own hand: because Beelzebub is fused with him, pain to Vikir is also pain to the weapon. The alignment must preserve both Korean lines under the appropriate recovered MTL slot rather than silently omit the explanation.

## Second skill window and replacement order

After tasting Cerberus, Beelzebub's slots reorder by stronger prey. The second window is reconstructed as:
- Slot 1: **Burn / Incinerate — Cerberus (A+)**
- Slot 2: **Bleeding / Hemorrhage — Hellhound (B+)**
- Slot 3: **Rapid Regeneration — Brown Rat Norvegicus (F)**

The MTL `Norbegicus the Rat` is corrected to the accepted **Brown Rat Norvegicus** terminology. The rat skill appears because remains of a rat previously eaten by Cerberus were beneath the corpse.

Vikir infers that stronger new abilities can displace older/weaker stored skills. Keep this as an inference at this point, not an exhaustive later-game ruleset.

Cerberus's skill is the severe burning effect associated with its hellfire/oil-flame nature. Avoid the MTL implication that the burn is literally impossible to heal under all circumstances; the source is emphasizing persistent, extreme burning pain.

## Current sword rank and the Tenth Form lead

After obtaining the available rewards on the mountain, Vikir assesses himself. He has accumulated magical power comparable to roughly four circles and can manifest three Baskerville fangs, perhaps approaching four. The wording around Expert/Graduator must remain consistent with Chapters 4 and 11: he is at the upper end of **Sword Expert**, approaching **Sword Graduator**, but practical combat output is assessed conservatively.

In his first life Vikir's learned curriculum capped him at four fangs. Present Hugo can use seven; the future Hugo Vikir remembers could use nine. The Ninth Form is restricted to the direct family line and chosen successors/supporting sons.

The chapter then introduces the **Tenth Form / ten fangs** as a legendary, otherwise unreachable inheritance connected to the first Baskerville patriarch's ancient victory. Supporting Fandom's martial-skills page calls the relevant scripture **Lurking Embedded Teeth** and confirms that it contains Baskerville's true essence and the path toward the Tenth Fang. The current chapter itself does not yet require importing every later technique name.

Vikir knows where the apparently worthless book containing that inheritance is kept. The key endpoint is that **Hugo Le Baskerville himself will eventually hand it to Vikir without understanding its true value**.

Do not import Chapter 14's assessment aftermath or later study/training details.

## Alignment plan

Korean lines 1–4 are headings. Recovered MTL paragraphs 1–14 map to Korean lines 5–18. Recovered MTL paragraphs 15–35 are explicitly MTL-only because the supplied Korean has no corresponding passage. MTL paragraph 36 resumes at Korean line 19.

The first info-window spacer/title pair shares the Korean title line, as does the first window's trailing spacer with its final row. The same pattern repeats for the second info window.

One Korean-only explanatory sentence around the self-slap/shared-pain moment must be attached to the adjacent MTL paragraph so the full Korean witness is retained. After accounting for that two-line ownership and the four NBSP spacer slots, the remaining post-gap body lines align sequentially.

## Historical audit

The tracker reports uniquely matched historical findings `ED-00108`, `ED-00109`, and `ED-00110`. They remain pending explicit paragraph-level triage before QA acceptance. No historical suggestion is automatically applied.
