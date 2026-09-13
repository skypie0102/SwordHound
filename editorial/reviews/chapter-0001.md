# Chapter 1 source comparison and second English pass

Review date: 2026-09-13. Basis: `korean_plus_mtl`. **QA remains unaccepted: six issues resolved, three open.** This is a reconstruction decision record, not recovered historical QA or certification of the supplied Korean edition.

## Sources actually consulted

- Supplied Korean: [001.txt](../../source/korean/chapters/001.txt), all 116 physical lines, linked by checksum in [the alignment record](../korean-alignment/chapter-0001.json). `Knnn` below means its one-based decoded physical line number.
- Preserved MTL: [chapter-001.xhtml](../../source/chapters/chapter-001.xhtml), all 106 body paragraphs. Paragraph numbers below refer to this file, not the older audit edition.
- [Fandom: Hugo Le Baskerville](https://revenge-of-the-ironblooded-sword-hound.fandom.com/wiki/Hugo_Le_Baskerville), search-retrieved page content on the review date: supports the English name and Marquis title. Its introductory survival philosophy resembles the MTL speech, but does not prove the precise novel dialogue. The page mixes novel/manhwa material and contains inconsistent relationship wording; only the narrow, corroborated terminology was used.
- [Fandom: Vikir Van Baskerville](https://revenge-of-the-ironblooded-sword-hound.fandom.com/wiki/Vikir_Van_Baskerville), search-retrieved page content on the review date: supports the name spelling, 100-day rebirth, and Cradle of Swords terminology. No later abilities, river-immersion duration, or later-story events were inserted into Chapter 1.
- [Namu Wiki: series entry](https://namu.wiki/w/%EC%B2%A0%ED%98%88%EA%B2%80%EA%B0%80%20%EC%82%AC%EB%83%A5%EA%B0%9C%EC%9D%98%20%ED%9A%8C%EA%B7%80): direct opening failed; targeted search did not supply usable supporting Korean text. No Namu claim is marked verified.
- [Pindang Scans: Chapter 1](https://pindangscans.com/novel-chapter-1-revenge-of-the-iron-blooded-sword-hound/), search-retrieved content: closely resembles the preserved MTL, including its broken wording. It is a possible transmission lead, not independent evidence that resolves the Korean/MTL differences. No new chapter text was imported from it.

## Coverage and method

Compared the supplied Korean against all 106 MTL paragraphs, then read and edited the resulting English draft. There are now 89 edited paragraphs relative to the unchanged MTL; every replacement has a rationale. The remaining 17 paragraphs are still represented in the provenance record. Mapping a passage does not certify equivalence where a conflict is recorded.

All 116 Korean lines are accounted for. K001–K003 and K014 are edition/title headings represented by the Markdown chapter heading. K027 is restored as `◆◆◆` after paragraph 18. K008/K010 repeat the name and map to paragraph 5; K009/K023 express the charge and map to paragraph 16; K015/K016 map to Vikir's struggle in paragraph 9; K025/K026 restore the repeated wish to live in paragraph 18; K057/K058 restore thought attribution and content within paragraph 48. Other body lines map individually. The MTL's 106-paragraph structure is retained; the scene ornament is separate from body text.

## Resolved decisions

| Issue | Evidence | Decision and limits |
|---|---|---|
| CH001-02: names and rank | K008/K010/K036; K031 versus MTL22; Fandom character entries | Use Vikir Van Baskerville and Hugo Le Baskerville consistently. Keep Marquis, supported by MTL and the Hugo page, over K031's count title. Preserve Le/Re as the MTL's name elements without falsely defining the wider naming system. Retain MTL65's seven-swordsmen description as source wording; do not conflate it with a wiki classification or introduce a new formal rank. |
| CH001-03: family events and nannies | K030, K045 | Use a series of happy events and nannies standing behind Hugo. The prior audit's collateral-branches proposal is rejected. |
| CH001-04: age | K038/MTL29 versus K100/MTL90; Vikir entry | Explicit editorial harmonization to a hundred days at both locations. The detailed nursery introduction and supporting wiki agree on 100 days. This is a documented choice between contradictory witnesses, not a claim that K100 literally says the new wording. |
| CH001-05: ritual, thought, metaphor | K046/K050, K057–K061, Fandom Vikir entry | Standardize Cradle of Swords; restore Hugo as the thinker; use mother's milk. The finite shared resource and under-one-year restriction remain intact. |
| CH001-07: sounds and transition | K027/K028, K066/K067, K092–K095, K104/K105 and MTL94 | Restore the scene ornament, use consistent English infant cries, and localize blade contact contextually. Keep the MTL water-entry sound rather than the supplied Korean's anomalous food word. Sound spellings are editorial localizations, not certified phonetic translations. |
| CH001-08: final reaction | K116 versus MTL106 | Use an open-mouthed reaction from the explicit Korean phrase, rather than a grin. The English mirror repeats the MTL reading and does not independently settle the disagreement. |

## Partly repaired, still open

**CH001-01 — execution-era narration.** K007 supports a head above the gate, not a neck. K012 helps repair the blood/hand imagery while the MTL shadow metaphor is retained. K009 and K023 support a false demon-association/spy accusation; paragraph 16 now places Vikir facing execution, correcting the earlier draft's prematurely completed action. Two differences remain unresolved: paragraph 15 says the family forsook him while K022 assigns abandonment to fate; paragraph 17 has gritted teeth while K024 describes deep thought. These MTL details are retained provisionally. A near-identical English mirror is not independent confirmation.

**CH001-06 — speech and river terminology.** K065 plus MTL84 support the spiral blade layout; K073 directs Hugo's contempt at the babies; K084 identifies exclamations. Those repairs are applied. At paragraph 66, the supplied Korean has two questions about fighting demons and training the children to support Hugo; the MTL instead states a survival principle. The wiki's general maxim is insufficient to identify the exact novel utterance. Paragraph 68's mana/aura terminology also differs from K078's more generic magical power/technique description. Both MTL passages remain provisional pending a reasoned resolution with better evidence or an explicit editorial adjudication.

**CH001-09 — acceptance.** The full comparison and second English pass are complete. Resolve the two conflict groups above, then perform a final whole-chapter reading and publication-format review. No accepted chapter or EPUB release is declared by this batch.

## Other notable treatments

- The opening remains the MTL's retrospective end-of-bloodshed narration; K004's dried-river image and K006's stone inscription are alternate renderings, not new facts silently inserted into the English.
- K067 distinguishes groups of infant reactions and explicitly places some children lying down; paragraph 57 now preserves those distinctions. K075 supports Hugo's reputation, without independently establishing the MTL's number seven.
- Preserve the MTL blades rather than K095's anomalous wings; the adjacent Korean lines and the entire trial establish blades. Use concrete blade language where needles/thorns are metaphors for the same obstacle, without inventing another obstacle course.
- The final knights' exclamation follows K114 while retaining the compatible alarm from the MTL. The chapter still ends with drinking river water; later wiki events remain outside this chapter.

## Validation scope

The builder checks both source hashes, all 106 paragraph mappings, all 116 Korean line dispositions, quoted-line hashes, and scene-break placement. Resolved issues require written decisions and existing evidence files. Recovery checks continue to protect all original MTL/Korean files, archives, the audit, and the EPUB. These structural checks do not settle the open translation conflicts.
