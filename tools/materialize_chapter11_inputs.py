"""Materialize reviewed Chapter 11 editorial inputs without changing recovered sources."""
from pathlib import Path
import hashlib
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = 11
MTL = ROOT / "source/chapters/chapter-011.xhtml"
KOREAN = ROOT / "source/korean/chapters/011.txt"
STAGING = ROOT / "editorial/staging/chapter-0011-final-text.txt"
MTL_SHA = "3e33fad1699136e0baf0506c349abfd068ac7411893aeb6199753c77b90b8268"
KOREAN_SHA = "24988d46d5a1a48115fcb42eab2ea7e99e2702f4e253aa26b3b12391994ed7a1"
NS = {'h': 'http://www.w3.org/1999/xhtml'}
SUPPRESSED = {2, 8, 34, 42, 151}
MARKERS = {
    2: "[[SOURCE-NBSP]]",
    8: "[[SOURCE-NBSP]]",
    34: "[[SOURCE-NBSP]]",
    42: "[[SOURCE-NBSP]]",
    151: "[[UNSUPPORTED-MTL-FRAGMENT]]",
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def dump(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def korean_refs(paragraph: int):
    if paragraph == 1:
        return [5]
    if paragraph in (2, 3):
        return [6]
    if 4 <= paragraph <= 6:
        return [paragraph + 3]
    if paragraph in (7, 8):
        return [10]
    if 9 <= paragraph <= 33:
        return [paragraph + 2]
    if paragraph in (34, 35):
        return [36]
    if 36 <= paragraph <= 40:
        return [paragraph + 1]
    if paragraph in (41, 42):
        return [42]
    if 43 <= paragraph <= 142:
        return [paragraph]
    if paragraph in (143, 144):
        return [143]
    if 145 <= paragraph <= 149:
        return [paragraph - 1]
    if paragraph in (150, 151):
        return [149]
    if 152 <= paragraph <= 201:
        return [paragraph - 2]
    raise ValueError(f"No Korean mapping for paragraph {paragraph}")


def main() -> None:
    mtl_bytes = MTL.read_bytes()
    korean_bytes = KOREAN.read_bytes()
    if sha(mtl_bytes) != MTL_SHA:
        raise ValueError("Chapter 11 MTL source hash changed")
    if sha(korean_bytes) != KOREAN_SHA:
        raise ValueError("Chapter 11 Korean source hash changed")

    doc = ET.fromstring(mtl_bytes)
    body = doc.find('.//h:div[@class="chapter-content"]', NS)
    source_paragraphs = [''.join(node.itertext()) for node in body.findall('.//h:p', NS)]
    if len(source_paragraphs) != 201:
        raise ValueError(f"Expected 201 MTL paragraph slots, got {len(source_paragraphs)}")

    staged = STAGING.read_text(encoding="utf-8").splitlines()
    if len(staged) != 201:
        raise ValueError(f"Expected 201 staged lines, got {len(staged)}")
    for number, marker in MARKERS.items():
        if staged[number - 1] != marker:
            raise ValueError(f"Missing structural marker at p{number}")
    for number in (2, 8, 34, 42):
        if source_paragraphs[number - 1].replace('\xa0', '').strip():
            raise ValueError(f"Source p{number} is no longer an NBSP spacer")

    key_reasons = {
        3: "Keep the repeated Cerberus entry as a structured info-window title.",
        6: "Standardize Cerberus discovery location as Le Rouge et Le Noir Mountain, Seventh Ridge.",
        7: "Keep the Cerberus AKA inside its info window.",
        16: "Use the established Camus Morgue spelling/title context rather than the corrupted Korean/MTL royal epithet.",
        20: "Restore Vikir's question about a Seventh-Ridge Cerberus descending this far.",
        22: "Place the encounter in the lowlands around the First Ridge rather than flattening the mountain geography.",
        30: "Use Guide Hound Guardian Knights consistently and clarify why Vikir may reveal his strength.",
        33: "State gaseous aura as the hallmark of an Advanced Sword Expert.",
        35: "Normalize the sword/mage equivalence window starting with Low Sword Expert.",
        37: "Use Advanced Sword Expert consistently with the accepted Chapter 4 rank terminology.",
        41: "Retain Sword Master = 7th-Circle Mage as the final comparison row.",
        43: "Repair the MTL's 'martial law' error into a rank-equivalence statement.",
        46: "Clarify that Vikir did not reach this stage in his prior life until around age twenty.",
        50: "Normalize Baskerville Style, Third Form and the three-fang description.",
        51: "Restore prior mastery through the Fourth Form and four fangs.",
        52: "Restore the prior-life Advanced Sword Graduator comparison rather than the corrupted 'Duator'.",
        57: "Remove the MTL's nonsense 'organ' insertion while preserving the missing fourth fang due to a child's reach.",
        60: "Make the apparent mismatch explicit: current-child Vikir should not normally contend with Cerberus at his former difficulty.",
        65: "Restore the caved-in rib area as evidence Cerberus is already injured.",
        67: "Preserve arrow wounds as the clue to outside attackers.",
        71: "Clarify long-standing conflict between mountain tribes and both Baskerville/Morgue rather than reversing actor roles.",
        78: "Carry the Highbro/Middlebro/Lowbro continuity into Vikir's familiarity with three-headed attack patterns.",
        89: "Explain that Vikir's post-destruction Baskerville Style is subtly different from the orthodox form.",
        91: "Restore the Age-of-Destruction stripping-away of unnecessary swordsmanship flourishes.",
        94: "Preserve the beef/chicken/jerky analogy as an intentional comparison of increasingly stripped-down swordsmanship.",
        97: "Repair the MTL profanity corruption; Korean supplies an impact sound, not an expletive.",
        103: "Render the bone-for-flesh exchange as a combat maxim rather than broken first-person grammar.",
        104: "Avoid implying Vikir's spine literally snaps; the following Korean establishes broken ribs rather than a severed back.",
        105: "Keep River Styx durability finite: Cerberus's claw is survived once, not rendered harmless.",
        108: "Restore several broken ribs, directly confirming Chapter 10's resistance was not invulnerability.",
        114: "Restore the Thirty-Six Stratagems retreat maxim from Korean.",
        116: "Translate 走爲上策 by meaning: retreat/run away is the best policy when all else fails.",
        120: "Resolve historical audit ED-00084 by repairing malformed roar brackets.",
        122: "Repair the MTL water-disaster homonym as the sea of trees and retain gratitude to the unknown tribe.",
        124: "Use Guide Hounds consistently at the boundary.",
        135: "Restore the straw-disguised pit trap set up in Chapter 9.",
        143: "Resolve historical audit ED-00085: complete the stake-penetration sentence.",
        144: "Preserve the second half of the Korean wound line in its separate recovered source slot.",
        146: "Use Korean's deliberate trap pun 'Cradle of Needles', distinct from the Cradle of Swords ritual.",
        150: "Restore the unexpected usefulness/harvest of a trap originally meant only to slow pursuers.",
        151: "Suppress the unsupported MTL-only fragment 'But that's it'; no Korean body line corresponds to it.",
        155: "Continue Bloody Bean terminology from Chapters 7–10.",
        156: "Restore the boiled-Bloody-Bean infusion applied to the wooden stakes.",
        157: "Explain chocolate compounds entering Cerberus directly through the stake wounds.",
        162: "Resolve historical audit ED-00088 by replacing duplicated/fused bean sounds with a clean rattle sequence.",
        164: "Preserve that almost all thrown beans enter Cerberus's three open mouths after the stakes slow it.",
        170: "Preserve Vikir's silent calculation before Cerberus's final leap.",
        174: "Restore the hunter-thrown spear/stake action leading to the hidden venom payoff.",
        183: "Keep the first recovery step after Cerberus loses balance.",
        188: "Preserve the seven-step countdown that foreshadows the venom clue.",
        194: "Restore the meaning that Vikir's hidden preparation finally paid off.",
        198: "Place the two small sharp thorns on the thrown spear tip.",
        200: "Tie the venom clue to being unable to make even seven steps.",
        201: "Preserve the exact endpoint: Bloody Mamba venom still lingers on the hidden thorns."
    }

    edits = []
    for number, replacement in enumerate(staged, 1):
        if number in SUPPRESSED:
            continue
        original = source_paragraphs[number - 1]
        if replacement == original:
            continue
        reason = key_reasons.get(
            number,
            f"Compared Korean source mapping with MTL paragraph {number}; repair English grammar, tense, punctuation or phrasing while preserving event and speaker."
        )
        edits.append([number, replacement, reason])

    suppression_reasons = {
        "2": "Recovered XHTML NBSP spacer before the opening Cerberus info window; retain provenance but suppress reader-facing blank output.",
        "8": "Recovered XHTML NBSP spacer after the opening Cerberus info window; retain provenance but suppress reader-facing blank output.",
        "34": "Recovered XHTML NBSP spacer before the sword/mage rank comparison window; retain provenance but suppress reader-facing blank output.",
        "42": "Recovered XHTML NBSP spacer after the sword/mage rank comparison window; retain provenance but suppress reader-facing blank output.",
        "151": "MTL-only sentence fragment with no Korean body-line witness between the unexpected-trap payoff and Cerberus's trembling; retain the source slot in provenance but suppress it from reader-facing text."
    }

    spec = {
        "chapter": CHAPTER,
        "source": "source/chapters/chapter-011.xhtml",
        "source_sha256": MTL_SHA,
        "expected_paragraphs": 201,
        "notice": "New reconstruction, not recovered production. Explicit source adjudications and structural exceptions are recorded in editorial/reviews/chapter-0011.md.",
        "korean_alignment": "editorial/korean-alignment/chapter-0011.json",
        "scene_breaks_after": [],
        "suppressed_paragraphs": sorted(SUPPRESSED),
        "suppression_reasons": suppression_reasons,
        "edits": edits,
    }

    korean_lines = korean_bytes.decode("utf-8-sig").splitlines()
    if len(korean_lines) != 199:
        raise ValueError(f"Expected 199 Korean physical lines, got {len(korean_lines)}")

    paragraphs = []
    for number in range(1, 202):
        refs = korean_refs(number)
        paragraphs.append({
            "mtl_paragraph": number,
            "korean_lines": refs,
            "line_text_sha256": [sha(korean_lines[line - 1].encode("utf-8")) for line in refs],
            "comparison": key_reasons.get(number, "Compared corresponding meaning, event and speaker; source decisions in editorial/reviews/chapter-0011.md."),
        })

    alignment = {
        "chapter": CHAPTER,
        "korean_source": "source/korean/chapters/011.txt",
        "korean_sha256": KOREAN_SHA,
        "mtl_source": "source/chapters/chapter-011.xhtml",
        "mtl_sha256": MTL_SHA,
        "line_numbering": "One-based physical UTF-8 splitlines; original bytes unchanged.",
        "line_count": 199,
        "paragraphs": paragraphs,
        "non_body_lines": [
            {"line": 1, "disposition": "Repeated title/edition heading."},
            {"line": 2, "disposition": "Repeated title/edition heading."},
            {"line": 3, "disposition": "Repeated title/edition heading."},
            {"line": 4, "disposition": "Repeated title/edition heading."},
        ],
        "shared_lines": [
            {"line": 6, "mtl_paragraphs": [2, 3], "reason": "Recovered XHTML inserts an NBSP spacer immediately before the Cerberus title."},
            {"line": 10, "mtl_paragraphs": [7, 8], "reason": "Recovered XHTML inserts an NBSP spacer immediately after the Cerberus AKA row."},
            {"line": 36, "mtl_paragraphs": [34, 35], "reason": "Recovered XHTML inserts an NBSP spacer immediately before the first sword/mage equivalence row."},
            {"line": 42, "mtl_paragraphs": [41, 42], "reason": "Recovered XHTML inserts an NBSP spacer immediately after the final sword/mage equivalence row."},
            {"line": 143, "mtl_paragraphs": [143, 144], "reason": "Recovered MTL splits one Korean sentence about stakes piercing Cerberus and leaving serious wounds across two paragraph slots."},
            {"line": 149, "mtl_paragraphs": [150, 151], "reason": "Recovered MTL adds an unsupported fragment after the Korean unexpected-harvest line; p151 remains provenance-accounted but is suppressed."
        ],
    }

    dump(ROOT / "editorial/edits/chapter-0011.json", spec)
    dump(ROOT / "editorial/korean-alignment/chapter-0011.json", alignment)
    print(f"Chapter 11 editorial inputs materialized: {len(edits)} changed paragraph slots; {len(SUPPRESSED)} structural slots suppressed.")


if __name__ == "__main__":
    main()
