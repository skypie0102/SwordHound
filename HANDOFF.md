# SwordHound Session Handoff

> **Mandatory:** Read this file before beginning editorial work. Update it after every meaningful checkpoint and always before ending or handing work to another agent. Hash-bound accepted evidence wins over this file if they ever conflict.

## Handoff metadata

- **Last updated:** 2026-09-18
- **Updated by:** ChatGPT — Red Death acceptance + 075 combined-source audit
- **Working branch:** `editorial/restart-red-death-family`
- **Base main checkpoint:** `20d0b84bc8c9a3326e625cb9f6bd4ddfb0ef01f4` (PR #26, Blood Relatives 68–71, merged)
- **Current PR:** #27 — `Rebuild The Red Death Chapters 72–74`
- **Pre-PR-stamp branch head:** `ceb51d3e044e586f13a49ecc08b23767d851a25f`
- **Blocking issue:** none

## Authoritative current checkpoint

- **Target:** 500 chapters
- **Accepted:** **74**
- **Staged:** **0**
- **Next:** **Chapter 75**
- **Latest accepted family:** **targets 72–74 — The Red Death (1)–(3)**
- **Latest family QA:** `qa/families/red-death-0072-0074.md` — **PASS** — `8899270579ac4a9d56a5497af6a70523e7c23669`
- **Next family:** **targets 75–77 — The Hound of the Night (1)–(3)**
- **Following family begins:** target 78 — **The Saintess (1)**

## Rules that must not be lost

- Chinese raw = semantic/narrative authority wherever present.
- English Fandom/project canonical register = canonical English terminology authority.
- Recovered English MTL/XHTML = aligned secondary witness unless an explicitly documented Chinese gap requires scoped restoration.
- Never assume target N == recovered-English N; verify content.
- Preserve source violence/coercion; do not reproduce sexual content involving under-18 characters.
- Disease mechanics in this fiction are source-world content, not real-world medical guidance.
- Protect reveal chronology.
- Process whole contiguous title families.
- Baskerville numbered techniques are **Fangs**, never Forms/Teeth.
- Every editorial session must update this file.

## Corpus status / exceptions

- Physical Chinese files: **492**
- Target chapters with at least partial Chinese coverage: **500/500**
- Localized Chinese gaps: **49 and 55**
- `054.txt` overlaps targets 54–55.
- `075.txt` combines targets 75–76 but is **not safely splittable**:
  - header declares 75+76;
  - no internal Chapter-76 heading/marker exists;
  - E74/E75 alignment exposes a cross-boundary splice/omission rather than a clean source seam.
  - keep physical `075.txt` intact and reconstruct target 75 / 76 separately by content.
- Other combined containers remain documented in `source/chinese/chapter-exceptions.tsv`.

## Accepted family — targets 72–74: The Red Death

### Resolved mapping

- **72 → E71**
- **73 → E72**
- **74 → E73**
- **75 → E74** begins next family

### Immutable evidence

| Ch. | Chinese SHA | English witness SHA | Draft SHA | QA SHA | Provenance SHA | Acceptance SHA |
|---|---|---|---|---|---|---|
| 72 | `8cf8c0385d0680afc3eb1148653abeac43ce12d9` | E71 `bbee450f38deaf7753263cc92cff28fc1d54e09e` | `194916079b9a805456013237aec4ef05f389b071` | `6015dc76bd76c542d457a58681f6faec677818ff` | `c5938752aa337cf97b188d6c2c34742955c14a79` | `04955b9aec18004377023adc563487d61043961c` |
| 73 | `9d3b6ccf88426b104e6e2577ae89fd4520bd685e` | E72 `15de32585922e667eeb7508af7c4b04e1c596f79` | `7ec4255821d6d640912a6848faf3394ef416ba2d` | `bf8efc732b0dac66c449b261357ec75c217950fa` | `739b2e54793a07ff76b0f5efab2da26d89f1946a` | `47dd866c3e02361fee8b64891b61adc2a52113ae` |
| 74 | `cc0e1e6b22601d136440825972a08cebcd429e8b` | E73 `db89bc3ca2cd63106daadf11e113fe3a50da3bef` | `7693e61cba97e5a84c8b2c864e91cdf7784d31f1` | `8590cd22276c47218e19c1a13a1b9db02a609f87` | `846d4e5f0dc6454e6f114cdd8e4e66286e55853c` | `3abad2669c4b91c49959e3d085e819fac4cab8f5` |

### Accepted decisions

- Target 72 prior-timeline Red Death history preserves Camus frontier flame barrier, Dolores Quovadis treatment, >40% native mortality, and Baskerville political/ecological benefit.
- Ballak demographic figures remain exact but clinical/nonsexual.
- Goblin contaminated-water / boiled-water experiments and prevention guidance remain fictional in-world mechanics.
- Target 72 endpoint: civil engineering / flood-control plan.
- Target 73 village is raised into trees at least 15 m high, with drainage and embankment redirection.
- **Mushuhushu** window: **A+ / 32 m / 8th Ridge / ‘Nation-Swallowing Snake’**.
- Recovered-English `Monsieur Hushu` / `Full-body Intestine Snake` rejected.
- Local individual **Ka'ah** escapes wounded.
- Target 74: Aheul is fourteen; illness is strictly medical.
- Ah'Heman insult means Ahun is useless like his **parents**, not `mother-in-law`.
- Ballak outsider exit conditions: >2 years residence + native family bond with at least three children.
- Aiyen bypasses Akwilla and authorizes Vikir's departure herself.
- Vikir takes Pomeranian and promises Aiyen he will return.

## Next family — targets 75–77: The Hound of the Night

Verified mapping:
- target 75 → **E74** *The Hound of the Night (1)* — `1bc968f310582423381420fc7e09e84aa4cf7e72`
- target 76 → **E75** *The Hound of the Night (2)* — `68c385dab862c292c4fbf2cc571beb1b6483e9c0`
- target 77 → **E76** *The Hound of the Night (3)* — `47f1a314662aacaf5d0117a6fd461d15258c8b14`
- target 78 → **E77** *The Saintess (1)* — `64c564988053d5a39bde90c0f81685055f2bf13f`

Chinese:
- combined target75–76 container `075.txt` — `e65af08f559f82f470687cc42c1d1420e1e55e15`
- target77 `077.txt` — `8800f5f079d10442f23e0d46f2674fcb3d8282ba`
- target78 `078.txt` — `155a238a81adfdc32ce7b97d9e28e05f4133c395`

### 075 split audit

Physical split rejected as unsafe:
- no `第76` / `第76话` / `夜之猎犬 (2)` marker exists;
- combined C075 starts with the target-75 Saint Mecca/oil-barrel infiltration and later passes seamlessly into target-76 slum/well/Quovadis-residence material;
- recovered E74 ends around the Underdog→Quovadis transition while E75 repeats/reframes Saint Mecca before the slum, so the boundary contains an omission/overlap rather than a byte-clean seam.

Use scoped hybrid alignment for 75/76; do **not** rewrite the source files.

## Exact next actions

1. Compare this branch against main.
2. Open/merge PR #27.
3. Branch from merged main for The Hound of the Night.
4. Read C075 + E74/E75, C077 + E76, and C078/E77 boundary completely.
5. Reconstruct target 75 and target 76 separately despite shared C075.
6. Reconstruct target 77 from C077.
7. QA/bind/promote/merge whole 75–77 family and continue into The Saintess.

