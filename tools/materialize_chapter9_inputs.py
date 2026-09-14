"""Materialize reviewed Chapter 9 editorial inputs without changing recovered sources."""
from pathlib import Path
import hashlib
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = 9
MTL = ROOT / "source/chapters/chapter-009.xhtml"
KOREAN = ROOT / "source/korean/chapters/009.txt"
STAGING = ROOT / "editorial/staging/chapter-0009-final-text.txt"
MTL_SHA = "bde389754e2c64cc279949fd5a6e260768af2a294a3135f826879c7f167454b7"
KOREAN_SHA = "c138ca1813382e341b1b9a0a330a7761e9a9f16ebb8e3516023a73fe4ae9c1e0"
NS = {'h': 'http://www.w3.org/1999/xhtml'}
SPACER_SLOTS = {66, 72, 136, 142}
MARKER = "[[SOURCE-NBSP]]"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def dump(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def korean_refs(paragraph: int):
    if 1 <= paragraph <= 65:
        return [paragraph + 4]
    if paragraph in (66, 67):
        return [70]
    if 68 <= paragraph <= 70:
        return [paragraph + 3]
    if paragraph in (71, 72):
        return [74]
    if 73 <= paragraph <= 112:
        return [paragraph + 2]
    if paragraph == 113:
        return [115, 116]
    if 114 <= paragraph <= 135:
        return [paragraph + 3]
    if paragraph in (136, 137):
        return [139]
    if 138 <= paragraph <= 140:
        return [paragraph + 2]
    if paragraph in (141, 142):
        return [143]
    if 143 <= paragraph <= 183:
        return [paragraph + 1]
    raise ValueError(f"No Korean mapping for paragraph {paragraph}")


def main() -> None:
    mtl_bytes = MTL.read_bytes()
    korean_bytes = KOREAN.read_bytes()
    if sha(mtl_bytes) != MTL_SHA:
        raise ValueError("Chapter 9 MTL source hash changed")
    if sha(korean_bytes) != KOREAN_SHA:
        raise ValueError("Chapter 9 Korean source hash changed")

    doc = ET.fromstring(mtl_bytes)
    body = doc.find('.//h:div[@class="chapter-content"]', NS)
    source_paragraphs = [''.join(node.itertext()) for node in body.findall('.//h:p', NS)]
    if len(source_paragraphs) != 183:
        raise ValueError(f"Expected 183 MTL paragraph slots, got {len(source_paragraphs)}")

    staged = STAGING.read_text(encoding="utf-8").splitlines()
    if len(staged) != 183:
        raise ValueError(f"Expected 183 staged lines, got {len(staged)}")
    for number in SPACER_SLOTS:
        if staged[number - 1] != MARKER:
            raise ValueError(f"Missing spacer marker at p{number}")
        if source_paragraphs[number - 1].replace('\xa0', '').strip():
            raise ValueError(f"Source p{number} is no longer an NBSP spacer")
    if any(text == MARKER for i, text in enumerate(staged, 1) if i not in SPACER_SLOTS):
        raise ValueError("Unexpected spacer marker")

    key_reasons = {
        16: "Resolve historical audits ED-00077/ED-00078 using the Korean-supported triplet dialogue.",
        24: "Restore the issued blunted short swords and natural English action sequence.",
        28: "Restore the heavy point penalty for directly killing another participant.",
        29: "Preserve the exception for absorbing the penalty or avoiding Guide Hound detection.",
        30: "Use Guide Hounds consistently and clarify concealed deaths/accidents during the test.",
        34: "Place Vikir's chosen wasteland near the secured boundary beside the Forbidden Zone.",
        54: "Normalize the recovered source scene-divider slot to ◆◆◆.",
        60: "Follow Korean: Vikir catches snakes or earthworms for food.",
        67: "Preserve the Norvegicus title inside the info window.",
        68: "Normalize the Norvegicus Danger Level row.",
        70: "Keep the Norvegicus discovery location as one complete info-window row.",
        71: "Keep the Norvegicus demonic-energy description inside the info window.",
        73: "Fix the historical grammar defect 'A adult Norvegicus' while preserving the supplied description.",
        79: "Restore Vikir's Age-of-Destruction hunter reflection.",
        82: "Preserve the hunter-killed-by-hound metaphor leading into Hugo's old maxim.",
        84: "Restore Hugo's master/hound preparedness maxim from Korean.",
        90: "Continue established Bloody Bean/cacao terminology from Chapter 7.",
        93: "Use cacao rather than coca and preserve the field-cooking odor-removal detail.",
        103: "Restore the wooden-stake trap rather than generic spear wording.",
        110: "Standardize the Forbidden Zone and Le Rouge et Le Noir Mountain terminology.",
        112: "Restore the spoken line that Vikir has used up his wood.",
        113: "Preserve both adjacent Korean wood-exhaustion lines under the MTL's collapsed paragraph slot.",
        118: "Normalize the second recovered source scene-divider slot to ◆◆◆.",
        137: "Preserve the Hellhound title inside the info window.",
        138: "Normalize the Hellhound Danger Level row to B+.",
        140: "Standardize the Hellhound discovery location as Le Rouge et Le Noir Mountain, Second Ridge.",
        141: "Keep the Hellhound AKA inside the same info window.",
        153: "Restore the sidestep that exploits the Hellhound's straight-line charge.",
        156: "State the straight-line movement weakness naturally.",
        163: "Restore the two-days-of-dew water line used to block the Hellhound.",
        166: "Preserve the Hellhound's refusal to cross water.",
        170: "Preserve regression knowledge about the future Demon Realm Gate without importing later events.",
        173: "Restore the intermediate Expert-rank one-on-one difficulty.",
        174: "Restore Vikir's old-life age benchmark of roughly eighteen.",
        175: "Resolve historical audit ED-00079 by replacing the fragment 'But.' with a complete transition.",
        177: "Restore the canine open-mouth-running weakness.",
        182: "Continue Bloody Bean terminology.",
        183: "Preserve the exact chapter endpoint: the secret weapon is chocolate.",
    }

    edits = []
    for number, replacement in enumerate(staged, 1):
        if number in SPACER_SLOTS:
            continue
        original = source_paragraphs[number - 1]
        if replacement == original:
            continue
        reason = key_reasons.get(
            number,
            f"Compared Korean source mapping with MTL paragraph {number}; repair English grammar, tense, punctuation or phrasing while preserving event and speaker."
        )
        edits.append([number, replacement, reason])

    spec = {
        "chapter": CHAPTER,
        "source": "source/chapters/chapter-009.xhtml",
        "source_sha256": MTL_SHA,
        "expected_paragraphs": 183,
        "notice": "New reconstruction, not recovered production. Explicit source adjudications and structural exceptions are recorded in editorial/reviews/chapter-0009.md.",
        "korean_alignment": "editorial/korean-alignment/chapter-0009.json",
        "scene_breaks_after": [],
        "edits": edits,
    }

    korean_lines = korean_bytes.decode("utf-8-sig").splitlines()
    if len(korean_lines) != 184:
        raise ValueError(f"Expected 184 Korean physical lines, got {len(korean_lines)}")

    paragraphs = []
    for number in range(1, 184):
        refs = korean_refs(number)
        paragraphs.append({
            "mtl_paragraph": number,
            "korean_lines": refs,
            "line_text_sha256": [sha(korean_lines[line - 1].encode("utf-8")) for line in refs],
            "comparison": key_reasons.get(number, "Compared corresponding meaning, event and speaker; source decisions in editorial/reviews/chapter-0009.md."),
        })

    alignment = {
        "chapter": CHAPTER,
        "korean_source": "source/korean/chapters/009.txt",
        "korean_sha256": KOREAN_SHA,
        "mtl_source": "source/chapters/chapter-009.xhtml",
        "mtl_sha256": MTL_SHA,
        "line_numbering": "One-based physical UTF-8 splitlines; original bytes unchanged.",
        "line_count": 184,
        "paragraphs": paragraphs,
        "non_body_lines": [
            {"line": 1, "disposition": "Repeated title/edition heading."},
            {"line": 2, "disposition": "Repeated title/edition heading."},
            {"line": 3, "disposition": "Repeated title/edition heading."},
            {"line": 4, "disposition": "Repeated title/edition heading."},
        ],
        "shared_lines": [
            {"line": 70, "mtl_paragraphs": [66, 67], "reason": "Recovered XHTML inserts an NBSP spacer immediately before the Norvegicus title; both slots point to the same Korean title line so every MTL paragraph remains represented."},
            {"line": 74, "mtl_paragraphs": [71, 72], "reason": "Recovered XHTML inserts an NBSP spacer immediately after the Norvegicus description; the spacer shares the final window-description line."},
            {"line": 139, "mtl_paragraphs": [136, 137], "reason": "Recovered XHTML inserts an NBSP spacer immediately before the Hellhound title; both slots point to the same Korean title line."},
            {"line": 143, "mtl_paragraphs": [141, 142], "reason": "Recovered XHTML inserts an NBSP spacer immediately after the Hellhound AKA row; the spacer shares that final window line."}
        ],
    }

    dump(ROOT / "editorial/edits/chapter-0009.json", spec)
    dump(ROOT / "editorial/korean-alignment/chapter-0009.json", alignment)
    print(f"Chapter 9 editorial inputs materialized: {len(edits)} changed paragraph slots.")


if __name__ == "__main__":
    main()
