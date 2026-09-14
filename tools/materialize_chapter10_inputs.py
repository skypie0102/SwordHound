"""Materialize reviewed Chapter 10 editorial inputs without changing recovered sources."""
from pathlib import Path
import hashlib
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = 10
MTL = ROOT / "source/chapters/chapter-010.xhtml"
KOREAN = ROOT / "source/korean/chapters/010.txt"
STAGING = ROOT / "editorial/staging/chapter-0010-final-text.txt"
MTL_SHA = "67ab38d1c1e0fe7543833696b5147599cfaa5f796e2726bdabc22fbbe6131f20"
KOREAN_SHA = "72d8f7f1c9ca55c2c4904d9df5ecb0cae5262ce625e02b529e6f25cb1ecc5586"
NS = {'h': 'http://www.w3.org/1999/xhtml'}
SUPPRESSED = {128, 134, 135}
MARKERS = {
    128: "[[SOURCE-NBSP]]",
    134: "[[SOURCE-NBSP]]",
    135: "[[MOVED-INTO-INFO-WINDOW]]",
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def dump(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def korean_refs(paragraph: int):
    if 1 <= paragraph <= 16:
        return [paragraph + 4]
    if paragraph == 17:
        return [21, 22]
    if 18 <= paragraph <= 127:
        return [paragraph + 5]
    if paragraph in (128, 129):
        return [133]
    if paragraph == 130:
        return [134]
    if paragraph == 131:
        return [135]
    if paragraph in (132, 133):
        return [136]
    if paragraph in (134, 135):
        return [137]
    if paragraph == 136:
        return [138]
    if paragraph == 137:
        return [139]
    if paragraph == 138:
        return [140]
    raise ValueError(f"No Korean mapping for paragraph {paragraph}")


def main() -> None:
    mtl_bytes = MTL.read_bytes()
    korean_bytes = KOREAN.read_bytes()
    if sha(mtl_bytes) != MTL_SHA:
        raise ValueError("Chapter 10 MTL source hash changed")
    if sha(korean_bytes) != KOREAN_SHA:
        raise ValueError("Chapter 10 Korean source hash changed")

    doc = ET.fromstring(mtl_bytes)
    body = doc.find('.//h:div[@class="chapter-content"]', NS)
    source_paragraphs = [''.join(node.itertext()) for node in body.findall('.//h:p', NS)]
    if len(source_paragraphs) != 138:
        raise ValueError(f"Expected 138 MTL paragraph slots, got {len(source_paragraphs)}")

    staged = STAGING.read_text(encoding="utf-8").splitlines()
    if len(staged) != 138:
        raise ValueError(f"Expected 138 staged lines, got {len(staged)}")
    for number, marker in MARKERS.items():
        if staged[number - 1] != marker:
            raise ValueError(f"Missing structural marker at p{number}")
    for number in (128, 134):
        if source_paragraphs[number - 1].replace('\xa0', '').strip():
            raise ValueError(f"Source p{number} is no longer an NBSP spacer")
    if not source_paragraphs[134].lstrip().startswith('-Aka'):
        raise ValueError("Source p135 is no longer the Cerberus AKA line")

    key_reasons = {
        8: "Continue Chapter 7 cacao/Bloody Bean terminology rather than MTL chocolate-bean wording.",
        9: "Restore the western-front Bloody Bean explanation consistently with Chapter 7.",
        12: "Carry forward the Chapter 9 water weakness and charging Hellhound state.",
        14: "Preserve the hound metaphor applied to regression-veteran Vikir.",
        17: "The MTL collapses Korean 'Then.' plus the immediate-reaction line; preserve both in one natural sentence.",
        20: "Follow Korean: the swallowed bean immediately triggers convulsions rather than generic staggering.",
        23: "Restore the Korean diarrhea/body-convulsion symptom detail.",
        28: "State the established mechanic that canine demonic creatures are vulnerable to chocolate.",
        29: "Use cacao terminology and describe the dog-toxic compounds without overstating a real-world chemical name absent from the source.",
        33: "Repair the Korean/Machine-translation confusion between a sea of trees and a water disaster.",
        38: "Correct the Korean homonym mistranslation: 신장 here means kidneys, not height.",
        39: "Explain the kidney target from anatomy and chocolate-toxin stress.",
        43: "Resolve historical audits ED-00080/ED-00081 with complete natural English describing kidney damage and worsening toxicity.",
        44: "Resolve historical audit ED-00082 and restore the Korean collapse/burning-waste/tongue detail.",
        48: "Restore Hugo-style extinguished-fire maxim from Korean rather than the generic MTL line.",
        56: "Normalize the source's duplicated karma wording into the four distinct labels supplied by Korean.",
        60: "Reject the MTL's universal imperviousness; Korean supports very high resistance to toxins, magic and physical force.",
        68: "Keep the established sword-rank terminology: Advanced Sword Expert.",
        74: "Use Guide Hounds consistently for the supervising Guardian Knights and assign boundary blame correctly.",
        75: "Preserve the B+ feat and Forbidden Zone context without inflating it beyond the supplied witnesses.",
        80: "Resolve historical audit ED-00083 by giving the corpse-weight sentence a complete causal construction.",
        83: "Restore the Korean thorny uphill road/flower-strewn-road contrast.",
        88: "Repair the corrupted stop/look-around line as Vikir sensing several nearby presences before the pack reveal.",
        95: "Restore the pack-hunter fact that Vikir had momentarily forgotten.",
        103: "Preserve the source's dog-recognizes-dog rhetorical metaphor.",
        105: "Carry forward Bloody Mamba/Cradle continuity without introducing later knowledge.",
        111: "Normalize the retreat sound as a Hellhound whine.",
        117: "Clarify that Vikir's current eight-year-old body cannot by killing intent alone drive off eleven Hellhounds.",
        123: "Identify the approaching Cerberus as the territorial presence that frightened the Hellhounds.",
        126: "Preserve Vikir's surprise at encountering Cerberus here.",
        129: "Keep the Cerberus title inside the recovered info window.",
        130: "Normalize the Cerberus Danger Level row to A+.",
        132: "Repair the split discovery-location row as Le Rouge et Le Noir Mountain, Seventh Ridge.",
        133: "Move the Cerberus AKA into the final row of the info window.",
        136: "Restore Cerberus's role tearing apart souls that try to escape hell.",
        137: "Describe Cerberus as a pinnacle hell-type canine demonic creature without importing later combat mechanics.",
        138: "Preserve the exact endpoint: the three-headed dog symbolizing hell has appeared."
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
        "128": "Recovered XHTML NBSP spacer before the Cerberus info window; retain the source slot in provenance but suppress reader-facing blank output.",
        "134": "Recovered XHTML NBSP spacer after the Cerberus info window; retain the source slot in provenance but suppress reader-facing blank output.",
        "135": "Recovered XHTML places the Cerberus AKA outside the info window; its content is moved into reviewed paragraph 133 and this duplicate structural slot is suppressed."
    }

    spec = {
        "chapter": CHAPTER,
        "source": "source/chapters/chapter-010.xhtml",
        "source_sha256": MTL_SHA,
        "expected_paragraphs": 138,
        "notice": "New reconstruction, not recovered production. Explicit source adjudications and structural exceptions are recorded in editorial/reviews/chapter-0010.md.",
        "korean_alignment": "editorial/korean-alignment/chapter-0010.json",
        "scene_breaks_after": [],
        "suppressed_paragraphs": sorted(SUPPRESSED),
        "suppression_reasons": suppression_reasons,
        "edits": edits,
    }

    korean_lines = korean_bytes.decode("utf-8-sig").splitlines()
    if len(korean_lines) != 140:
        raise ValueError(f"Expected 140 Korean physical lines, got {len(korean_lines)}")

    paragraphs = []
    for number in range(1, 139):
        refs = korean_refs(number)
        paragraphs.append({
            "mtl_paragraph": number,
            "korean_lines": refs,
            "line_text_sha256": [sha(korean_lines[line - 1].encode("utf-8")) for line in refs],
            "comparison": key_reasons.get(number, "Compared corresponding meaning, event and speaker; source decisions in editorial/reviews/chapter-0010.md."),
        })

    alignment = {
        "chapter": CHAPTER,
        "korean_source": "source/korean/chapters/010.txt",
        "korean_sha256": KOREAN_SHA,
        "mtl_source": "source/chapters/chapter-010.xhtml",
        "mtl_sha256": MTL_SHA,
        "line_numbering": "One-based physical UTF-8 splitlines; original bytes unchanged.",
        "line_count": 140,
        "paragraphs": paragraphs,
        "non_body_lines": [
            {"line": 1, "disposition": "Repeated title/edition heading."},
            {"line": 2, "disposition": "Repeated title/edition heading."},
            {"line": 3, "disposition": "Repeated title/edition heading."},
            {"line": 4, "disposition": "Repeated title/edition heading."},
        ],
        "shared_lines": [
            {"line": 133, "mtl_paragraphs": [128, 129], "reason": "Recovered XHTML inserts an NBSP spacer immediately before the Cerberus title; both source slots correspond to the same Korean title line."},
            {"line": 136, "mtl_paragraphs": [132, 133], "reason": "Recovered XHTML splits the Korean Cerberus discovery-location line into separate '7th' and 'Ridge' paragraphs; the reviewed window consolidates it into one row and reuses the second source slot for the AKA row."},
            {"line": 137, "mtl_paragraphs": [134, 135], "reason": "Recovered XHTML inserts an NBSP spacer before an AKA paragraph outside the window; the AKA content is moved into the window while both source slots remain accounted for."}
        ],
    }

    dump(ROOT / "editorial/edits/chapter-0010.json", spec)
    dump(ROOT / "editorial/korean-alignment/chapter-0010.json", alignment)
    print(f"Chapter 10 editorial inputs materialized: {len(edits)} changed paragraph slots; {len(SUPPRESSED)} structural slots suppressed.")


if __name__ == "__main__":
    main()
