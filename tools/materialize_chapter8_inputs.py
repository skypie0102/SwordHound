"""Materialize reviewed Chapter 8 editorial inputs without changing recovered sources."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = 8
MTL = ROOT / "source/chapters/chapter-008.xhtml"
KOREAN = ROOT / "source/korean/chapters/008.txt"
STAGING = ROOT / "editorial/staging/chapter-0008-final-text.txt"
MTL_SHA = "d0174210fffb9ee884a456e0c70d31f6c5de6620de3da01193210fcdd288d26f"
KOREAN_SHA = "04c2b50afb454f6d6068492e080b813870afd8a042abd2d538259b0e6edb839f"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def dump(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    if sha(MTL.read_bytes()) != MTL_SHA:
        raise ValueError("Chapter 8 MTL source hash changed")
    korean_bytes = KOREAN.read_bytes()
    if sha(korean_bytes) != KOREAN_SHA:
        raise ValueError("Chapter 8 Korean source hash changed")

    texts = STAGING.read_text(encoding="utf-8").splitlines()
    if len(texts) != 104:
        raise ValueError(f"Expected 104 staged paragraphs, got {len(texts)}")

    # Remove three accidental internal spaces in pure-ellipsis dialogue lines.
    for paragraph in (80, 81, 82):
        if texts[paragraph - 1] == "“… ”":
            texts[paragraph - 1] = "“…”"
    if any(text == "“… ”" for text in texts):
        raise ValueError("Unnormalized ellipsis dialogue remains")

    key_reasons = {
        2: "Restore the distinction between strict academics and the near-lethal practical examination.",
        8: "Restore the demonic-creature corpse desensitization detail from Korean.",
        12: "Use the Korean meat/chicken-bone-broth preparation rather than the MTL fish corruption.",
        15: "Restore the salting/drying sequence that turns haggis into field jerky.",
        17: "Standardize the setting as Le Rouge et Le Noir Mountain.",
        20: "Use Guide Hounds for the Guardian Knights supervising the restricted survival area.",
        22: "Restore the two objectives: survive and, if possible, hunt powerful demonic creatures.",
        27: "Restore the 10-point survival threshold.",
        28: "Restore 30 points for surviving without serious injury.",
        29: "Restore 50 points for outlasting the other children and surviving.",
        30: "Restore 70 points for hunting a demonic creature and surviving.",
        31: "Restore the 90-point combined high-performance condition.",
        36: "Preserve the dog-death idiom while clarifying its pointless-death meaning.",
        45: "Restore the secured-area warning and unexplored forbidden regions.",
        49: "Resolve historical audit ED-00076 and standardize Le Rouge et Le Noir Mountain.",
        56: "Standardize the exterior danger region as the Forbidden Zone.",
        63: "Follow Korean: the Cradle inside the ridge is especially familiar to Vikir.",
        69: "Use Korean's distressed reaction rather than claiming all eight-year-olds cried.",
        75: "Restore the seven-minute River Styx rumor.",
        76: "Restore the two-venomous-snakes rumor.",
        83: "Carry the triplets' broken fighting spirit forward from Chapter 7.",
        86: "Restore the Korean threat to smash Vikir's head with a rock.",
        93: "Use Korean's 'pathetic' insult rather than flattening it to merely weak.",
        95: "Repair the corrupted MTL boast to the Korean taunt 'Just you wait.'",
        97: "Restore the threat's subject correctly: the speaker does not care if Vikir dies.",
        98: "Resolve the provocation contradiction: the children immediately take the bait.",
        100: "Anchor the old-hound metaphor to regression-veteran Vikir.",
        103: "Identify Pavlov Van Baskerville as Guardian Knight, instructor and Guide Hound.",
        104: "Preserve the exact endpoint: the practical examination begins."
    }

    edits = []
    for paragraph, text in enumerate(texts, 1):
        reason = key_reasons.get(
            paragraph,
            f"Compared Korean line {paragraph + 4} with MTL paragraph {paragraph}; repair English grammar, tense, punctuation or phrasing while preserving event and speaker."
        )
        edits.append([paragraph, text, reason])

    spec = {
        "chapter": CHAPTER,
        "source": "source/chapters/chapter-008.xhtml",
        "source_sha256": MTL_SHA,
        "expected_paragraphs": 104,
        "notice": "New reconstruction, not recovered production. Explicit source adjudications and limitations are recorded in editorial/reviews/chapter-0008.md.",
        "korean_alignment": "editorial/korean-alignment/chapter-0008.json",
        "scene_breaks_after": [],
        "edits": edits,
    }

    korean_lines = korean_bytes.decode("utf-8-sig").splitlines()
    if len(korean_lines) != 108:
        raise ValueError(f"Expected 108 Korean physical lines, got {len(korean_lines)}")

    paragraphs = []
    for paragraph in range(1, 105):
        line_number = paragraph + 4
        line = korean_lines[line_number - 1]
        paragraphs.append({
            "mtl_paragraph": paragraph,
            "korean_lines": [line_number],
            "line_text_sha256": [sha(line.encode("utf-8"))],
            "comparison": key_reasons.get(paragraph, "Compared corresponding meaning, event and speaker; source decisions in editorial/reviews/chapter-0008.md."),
        })

    alignment = {
        "chapter": CHAPTER,
        "korean_source": "source/korean/chapters/008.txt",
        "korean_sha256": KOREAN_SHA,
        "mtl_source": "source/chapters/chapter-008.xhtml",
        "mtl_sha256": MTL_SHA,
        "line_numbering": "One-based physical UTF-8 splitlines; original bytes unchanged.",
        "line_count": 108,
        "paragraphs": paragraphs,
        "non_body_lines": [
            {"line": 1, "disposition": "Repeated title/edition heading."},
            {"line": 2, "disposition": "Repeated title/edition heading."},
            {"line": 3, "disposition": "Repeated title/edition heading."},
            {"line": 4, "disposition": "Repeated title/edition heading."},
        ],
        "shared_lines": [],
    }

    dump(ROOT / "editorial/edits/chapter-0008.json", spec)
    dump(ROOT / "editorial/korean-alignment/chapter-0008.json", alignment)
    print("Chapter 8 editorial edit/alignment inputs materialized.")


if __name__ == "__main__":
    main()
