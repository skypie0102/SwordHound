"""Materialize reviewed Chapter 12 editorial inputs without changing recovered sources."""
from pathlib import Path
import hashlib
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = 12
MTL = ROOT / "source/chapters/chapter-012.xhtml"
KOREAN = ROOT / "source/korean/chapters/012.txt"
STAGING = ROOT / "editorial/staging/chapter-0012-final-text.txt"
MTL_SHA = "2f04dc2121d6667bab974b49dcbc49c623a9c41ae77c5f0330d55b8263db3b22"
KOREAN_SHA = "38d0e42019a9aba00b809e4fc8685ff49f99b40357407961360b05a43a401305"
NS = {'h': 'http://www.w3.org/1999/xhtml'}

SHARED_GROUPS = [
    (58, [53, 54], "Recovered MTL splits one Korean journal sentence across two paragraph slots."),
    (64, [60, 61, 62], "Recovered MTL splits the journal's dungeon-arrival sentence across three paragraph slots."),
    (67, [65, 66], "Recovered MTL splits the inference that the writer and skeleton were twin brothers."),
    (69, [68, 69], "Recovered MTL splits the final-task/three-year statement across two paragraph slots."),
    (78, [78, 79], "Recovered MTL splits one Korean diary sentence about the Baskerville legend."),
    (81, [82, 83], "Recovered MTL splits the womb/birth sentence across two paragraph slots."),
    (83, [85, 86], "Recovered MTL splits the literal impossibility of becoming one and the killing conclusion."),
    (85, [88, 89], "Recovered MTL splits the brothers' fight and Abel's death across two paragraph slots."),
    (99, [103, 104], "Recovered MTL splits the transition to Cain's later, neater handwriting."),
    (101, [106, 107], "Recovered MTL splits Cain's warning to future descendants."),
]
MULTI_LINE = {2: 2, 136: 2}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def dump(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build_mapping():
    owners = {}
    for line, paragraphs, _ in SHARED_GROUPS:
        for paragraph in paragraphs:
            owners[paragraph] = (line, paragraphs)
    mapping = {}
    current = 5
    for paragraph in range(1, 151):
        if paragraph in owners:
            expected, paragraphs = owners[paragraph]
            if paragraph == paragraphs[0]:
                if current != expected:
                    raise ValueError(f"Chapter 12 shared-line map drifted at p{paragraph}: {current} != {expected}")
                for owner in paragraphs:
                    mapping[owner] = [current]
                current += 1
            continue
        if paragraph in MULTI_LINE:
            count = MULTI_LINE[paragraph]
            mapping[paragraph] = list(range(current, current + count))
            current += count
        else:
            mapping[paragraph] = [current]
            current += 1
    if current != 146 or len(mapping) != 150:
        raise ValueError("Chapter 12 Korean mapping does not conserve all source slots/lines")
    return mapping


def main() -> None:
    mtl_bytes = MTL.read_bytes()
    korean_bytes = KOREAN.read_bytes()
    if sha(mtl_bytes) != MTL_SHA:
        raise ValueError("Chapter 12 MTL source hash changed")
    if sha(korean_bytes) != KOREAN_SHA:
        raise ValueError("Chapter 12 Korean source hash changed")

    doc = ET.fromstring(mtl_bytes)
    body = doc.find('.//h:div[@class="chapter-content"]', NS)
    source_paragraphs = [''.join(node.itertext()) for node in body.findall('.//h:p', NS)]
    if len(source_paragraphs) != 150:
        raise ValueError(f"Expected 150 MTL paragraph slots, got {len(source_paragraphs)}")

    staged = STAGING.read_text(encoding="utf-8").splitlines()
    if len(staged) != 150:
        raise ValueError(f"Expected 150 staged lines, got {len(staged)}")

    key_reasons = {
        2: "Restore Korean's oily saliva and excrement detail while preserving the simultaneous transition.",
        9: "Keep assessment continuity: Guide Hounds witnessed Vikir preparing the wooden-spear trap.",
        15: "Restore Cerberus's gatekeeper logic and Vikir's inference that a dungeon lies nearby.",
        21: "Restore that Cerberus scent/filth drives lesser monsters away.",
        28: "Preserve the ten-years-later first-life discovery timeline.",
        36: "Standardize the dungeon connection as Red Fang Mountain, a branch of Le Rouge et Le Noir Mountain.",
        46: "Correct the MTL's two-skeleton error: the supplied Korean and continuity support one skeleton, Abel's remains.",
        51: "Correct MTL 'Gain' to Cain and resolve historical audit ED-00089 in the journal opening.",
        53: "Resolve ED-00090 while retaining the recovered split journal sentence.",
        60: "Resolve ED-00092 and preserve the ancient Baskerville-dungeon journal voice.",
        61: "Resolve ED-00093 without collapsing the recovered paragraph slot.",
        65: "Resolve ED-00094 and preserve the one-skeleton/twin-brother inference.",
        68: "Resolve ED-00095 in the final-task statement.",
        74: "Restore the wall riddle by meaning: one enters, two are present inside, one leaves.",
        77: "Resolve ED-00096 in Cain's explanation of the riddle.",
        78: "Resolve ED-00097 while preserving the shared Korean sentence.",
        82: "Resolve ED-00098 in the twins' womb/birth explanation.",
        85: "Resolve ED-00099 in the mistaken become-one interpretation.",
        88: "Resolve ED-00101 while preserving the brothers' fight across the recovered split.",
        93: "Keep the chamber's remains singular; Vikir is looking at Abel's lone skeleton.",
        96: "Resolve ED-00102 and state plainly that Cain killed his brother and remained alone.",
        100: "Resolve ED-00103 in the maddened journal passage.",
        103: "Resolve ED-00104 in the transition back to Cain's later handwriting.",
        106: "Resolve ED-00105 in Cain's warning to descendants.",
        108: "Resolve ED-00106 and restore the imperative to leave the dungeon.",
        109: "Resolve ED-00107 and close Cain's journal warning cleanly.",
        114: "Restore Vikir's decisive observation that he is not a twin.",
        118: "Correct the MTL actor: Vikir, not 'Baskerville', looks back toward the cave.",
        122: "Identify the second presence as Vikir's shadow.",
        129: "Replace the MTL's stray 'OK.' with the causal transition into the mechanism activating.",
        136: "State the riddle answer explicitly as shadow while owning both adjacent Korean lines.",
        142: "Preserve that Cain and Abel had already cleared the dungeon's monsters long ago.",
        147: "Restore the inscription without prematurely printing the weapon's name in the Chapter 12 cliffhanger.",
        148: "Clarify that the inscription contains Baskerville's name and the weapon's name.",
        150: "Preserve the exact cliffhanger: Vikir recognizes the artifact but Chapter 13 supplies its name."
    }

    edits = []
    for number, replacement in enumerate(staged, 1):
        original = source_paragraphs[number - 1]
        if replacement == original:
            continue
        reason = key_reasons.get(
            number,
            f"Compared the corresponding Korean witness with MTL paragraph {number}; repair English grammar, punctuation, register or attribution while preserving event and source slot."
        )
        edits.append([number, replacement, reason])

    spec = {
        "chapter": CHAPTER,
        "source": "source/chapters/chapter-012.xhtml",
        "source_sha256": MTL_SHA,
        "expected_paragraphs": 150,
        "notice": "New reconstruction, not recovered production. Explicit source adjudications are recorded in editorial/reviews/chapter-0012.md.",
        "korean_alignment": "editorial/korean-alignment/chapter-0012.json",
        "scene_breaks_after": [],
        "edits": edits,
    }

    korean_lines = korean_bytes.decode("utf-8-sig").splitlines()
    if len(korean_lines) != 145:
        raise ValueError(f"Expected 145 Korean physical lines, got {len(korean_lines)}")
    mapping = build_mapping()

    paragraphs = []
    for number in range(1, 151):
        refs = mapping[number]
        paragraphs.append({
            "mtl_paragraph": number,
            "korean_lines": refs,
            "line_text_sha256": [sha(korean_lines[line - 1].encode("utf-8")) for line in refs],
            "comparison": key_reasons.get(number, "Compared corresponding Korean meaning, event and speaker; consequential decisions are documented in editorial/reviews/chapter-0012.md."),
        })

    alignment = {
        "chapter": CHAPTER,
        "korean_source": "source/korean/chapters/012.txt",
        "korean_sha256": KOREAN_SHA,
        "mtl_source": "source/chapters/chapter-012.xhtml",
        "mtl_sha256": MTL_SHA,
        "line_numbering": "One-based physical UTF-8 splitlines; original bytes unchanged.",
        "line_count": 145,
        "paragraphs": paragraphs,
        "non_body_lines": [
            {"line": 1, "disposition": "Repeated title/edition heading."},
            {"line": 2, "disposition": "Repeated title/edition heading."},
            {"line": 3, "disposition": "Repeated title/edition heading."},
            {"line": 4, "disposition": "Repeated title/edition heading."},
        ],
        "shared_lines": [
            {"line": line, "mtl_paragraphs": paragraphs_, "reason": reason}
            for line, paragraphs_, reason in SHARED_GROUPS
        ],
    }

    dump(ROOT / "editorial/edits/chapter-0012.json", spec)
    dump(ROOT / "editorial/korean-alignment/chapter-0012.json", alignment)
    print(f"Chapter 12 editorial inputs materialized: {len(edits)} changed paragraph slots.")


if __name__ == "__main__":
    main()
