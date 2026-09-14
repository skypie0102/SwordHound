# Chapter 13 source comparison — 2026-09-14

Status: **source review complete; final generated-output/browser/repository validation pending; not QA accepted**. New Korean-plus-MTL reconstruction. Recovered MTL SHA-256: `2bef27c163e103c90c2af57bd7170d4ed16782b7035e8919b14513e30865be14`. Supplied Korean SHA-256: `f44e049710f465061adfd8416be5e490ff3e0be2e584ffc2ffd3e1745acb83c5`.

The chapter has 166 recovered MTL paragraph slots and 146 Korean physical lines. Korean lines 1–4 are repeated headings. Unlike the preceding bilingual chapters, the supplied Korean has a genuine missing passage: recovered MTL paragraphs **15–35** have no Korean body-line counterpart. The deterministic alignment records those 21 slots explicitly as MTL-only instead of reusing unrelated Korean lines.

## Beelzebub reveal and physical form

Chapter 13 opens by supplying the name withheld at the end of Chapter 12: only Baskerville blood can draw **Beelzebub**. Use the epithet **the Gluttonous Fly**.

The recovered MTL's `Devil's first name` wording is nonsense; the inscription contains the Baskerville family name and the **sword's name**. Vikir recognizes Beelzebub from an illustration in a myth book from his first life.

The weapon has a long awl/stinger-like blade, three rounded ruby-like nodes near the guard, and a rough greenish handle whose overall silhouette evokes a giant fly. The exact ornamental wording is smoothed, but the fly/stinger imagery remains.

## Declared MTL-only passage: paragraphs 15–35

The supplied Korean jumps directly from `one of those remnants was Beelzebub` to Vikir's prior-life fasting habits. MTL paragraphs 15–35 therefore have no Korean witness in the supplied file. They are not discarded: they remain part of the recovered chapter and are supported in their core claims by Fandom's Beelzebub, Demonic Creatures, Equipment, Dungeon and Vikir Synopsis pages.

The passage establishes, without importing later details:
- the Seven Great Families' founding heads each confronted one of the Seven Calamities/Demon Constellations;
- Baskerville's ancestral victory left Beelzebub's remains/weapon associated with the family;
- in Vikir's first timeline the forgotten weapon eventually fell into demon hands and appeared on later battlefields;
- in the current timeline Vikir claims it first;
- Beelzebub fuses into his **right hand/wrist** and can emerge as a concealed spare weapon;
- its demonic nature immediately imposes supernatural hunger on Vikir.

The generic alignment validator now permits an empty Korean mapping only when the paragraph is listed in `mtl_only_paragraphs` with a nonempty reason. Such a paragraph cannot simultaneously claim Korean line ownership, and exact Korean-line coverage remains mandatory. Existing accepted chapters gain no new provenance fields unless they actually use this feature.

## Hunger and first skill: Hellhound

Vikir is accustomed to extreme fasting from his previous life, so the sudden crippling hunger is clearly supernatural. Beelzebub draws him toward the earlier Hellhound corpse and drinks its blood and bodily fluids through its stinger/awl.

The first acquired skill is the Hellhound's bleeding ability. Supporting Fandom calls this **Hemorrhage**; the compact recovered window is rendered as `Bleeding`. The effect is that even shallow wounds bleed and continue bleeding much longer than normal.

Beelzebub's historical living form could steal broadly, but the artifact in Vikir's possession is limited to **three stored skills** at this point. Do not import later slot contents.

The first info window is:
- Slot 1: Bleeding — Hellhound (B+)
- Slot 2: None
- Slot 3: None

Recovered NBSP paragraphs surrounding the window remain provenance-accounted and are suppressed from reader-facing output.

## Cerberus feeding and shared pain

Still hungry, Beelzebub leads Vikir back to the assessment area and the Cerberus corpse. Vikir stops it from consuming too much because the corpse is evidence for the practical examination and must remain inspectable.

The recovered MTL loses an important Korean sentence after Vikir slaps the back of his own hand: because Beelzebub is fused with him, pain to Vikir is also pain to the weapon. MTL paragraph 117 therefore owns two adjacent Korean lines and reconstructs both ideas in one paragraph rather than omitting the explanation.

## Second skill window and replacement order

After tasting Cerberus, Beelzebub's slots reorder by stronger prey. The second window is reconstructed as:
- Slot 1: **Burn / Incinerate — Cerberus (A+)**
- Slot 2: **Bleeding / Hemorrhage — Hellhound (B+)**
- Slot 3: **Rapid Regeneration — Brown Rat Norvegicus (F)**

The MTL `Norbegicus the Rat` is corrected to the accepted **Brown Rat Norvegicus** terminology. The rat skill appears because remains of a rat previously eaten by Cerberus were beneath the corpse.

Vikir infers that stronger new abilities can displace older/weaker stored skills. Keep this as an inference at this point, not an exhaustive later-game ruleset.

Cerberus's skill is the severe burning effect associated with its hellfire/oil-flame nature. Avoid the MTL implication that the burn is literally impossible to heal under all circumstances; the source is emphasizing persistent, extreme burning pain.

## Current sword rank and the Tenth Form lead

After obtaining the available rewards on the mountain, Vikir assesses himself. He has accumulated magical power comparable to roughly four circles and can manifest three Baskerville fangs, perhaps approaching four. The wording around Expert/Graduator remains consistent with Chapters 4 and 11: he is at the upper end of **Sword Expert**, approaching **Sword Graduator**, but practical combat output is assessed conservatively.

In his first life Vikir's learned curriculum capped him at four fangs. Present Hugo can use seven; the future Hugo Vikir remembers could use nine. The Ninth Form is restricted to the direct family line and chosen successors/supporting sons.

The chapter then introduces the **Tenth Form / ten fangs** as a legendary, otherwise unreachable inheritance connected to the first Baskerville patriarch's ancient victory. Supporting Fandom's martial-skills page calls the relevant scripture **Lurking Embedded Teeth** and confirms that it contains Baskerville's true essence and the path toward the Tenth Fang. The current chapter itself does not import later technique details.

Vikir knows where the apparently worthless book containing that inheritance is kept. The endpoint is that **Hugo Le Baskerville himself will eventually hand it to Vikir without understanding its true value**.

Do not import Chapter 14's assessment aftermath or later study/training details.

## Alignment plan

Korean lines 1–4 are headings. Recovered MTL paragraphs 1–14 map to Korean lines 5–18. Recovered MTL paragraphs 15–35 are explicitly MTL-only. MTL paragraph 36 resumes at Korean line 19.

Explicit shared ownership after the gap:
- Korean line 61 -> p78–79 (NBSP spacer + first window title).
- Korean line 64 -> p82–83 (final first-window row + trailing NBSP spacer).
- Korean lines 98–99 -> p117 (self-slap pain + fused shared-pain explanation).
- Korean line 103 -> p121–122 (NBSP spacer + second window title).
- Korean line 106 -> p125–126 (final second-window row + trailing NBSP spacer).

With those declarations, all 146 physical Korean lines and all 166 recovered MTL slots are accounted for exactly.

## Historical audit triage

All three uniquely matched Chapter 13 findings are manually resolved:
- **ED-00108 p55 — grammar/conjunction:** rewrite the shared-hunger sentence as `The hunger Beelzebub shared with him was simply too intense.`
- **ED-00109 p75 — punctuation/spacing:** replace the corrupted artifact-limitation sentence with a complete statement that Beelzebub, as an artifact, no longer has its former near-limitless absorption power.
- **ED-00110 p155 — awkward fragment:** replace the transition into the Tenth Form reveal with the complete sentence `But now things were different.`

No historical audit suggestion automatically grants acceptance.

## Remaining gate

The full 166-slot English staging text, explicit 21-slot MTL-only witness gap, four structural spacer slots, and deterministic materializer are committed. The only unresolved QA item is final materialization/provenance generation, structured-window browser evidence, complete repository checks, and hash-bound batch acceptance together with Chapter 12. No independent human review is claimed.
