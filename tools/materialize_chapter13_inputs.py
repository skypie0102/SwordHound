"""Materialize reviewed Chapter 13 editorial inputs without changing recovered sources."""
from pathlib import Path
import hashlib
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = 13
MTL = ROOT / "source/chapters/chapter-013.xhtml"
KOREAN = ROOT / "source/korean/chapters/013.txt"
STAGING = ROOT / "editorial/staging/chapter-0013-final-text.txt"
MTL_SHA = "2bef27c163e103c90c2af57bd7170d4ed16782b7035e8919b14513e30865be14"
KOREAN_SHA = "f44e049710f465061adfd8416be5e490ff3e0be2e584ffc2ffd3e1745acb83c5"
NS = {'h': 'http://www.w3.org/1999/xhtml'}
SPACER_SLOTS = {78, 83, 121, 126}
MARKER = "[[SOURCE-NBSP]]"
MTL_ONLY = set(range(15, 36))
SHARED_GROUPS = [
    (61, [78, 79], "Recovered XHTML inserts an NBSP spacer immediately before the first Beelzebub skill-window title."),
    (64, [82, 83], "Recovered XHTML inserts an NBSP spacer immediately after the first Beelzebub window's final row."),
    (103, [121, 122], "Recovered XHTML inserts an NBSP spacer immediately before the second Beelzebub skill-window title."),
    (106, [125, 126], "Recovered XHTML inserts an NBSP spacer immediately after the second Beelzebub window's final row."),
]
MULTI_LINE = {117: 2}
MTL_ONLY_REASON = (
    "The supplied Korean witness jumps from Beelzebub's mythic origin directly to Vikir's prior-life fasting habits. "
    "Recovered MTL paragraphs 15-35 preserve an intervening passage about the Seven Great Families, the weapon's future loss, "
    "right-hand fusion and the first supernatural hunger; supporting references corroborate its core continuity, but no Korean line is falsely assigned."
)


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
    for paragraph in range(1, 167):
        if paragraph in MTL_ONLY:
            mapping[paragraph] = []
            continue
        if paragraph in owners:
            expected, paragraphs = owners[paragraph]
            if paragraph == paragraphs[0]:
                if current != expected:
                    raise ValueError(f"Chapter 13 shared-line map drifted at p{paragraph}: {current} != {expected}")
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
    if current != 147 or len(mapping) != 166:
        raise ValueError("Chapter 13 Korean/MTL-only mapping does not conserve all source slots/lines")
    return mapping


def main() -> None:
    mtl_bytes = MTL.read_bytes()
    korean_bytes = KOREAN.read_bytes()
    if sha(mtl_bytes) != MTL_SHA:
        raise ValueError("Chapter 13 MTL source hash changed")
    if sha(korean_bytes) != KOREAN_SHA:
        raise ValueError("Chapter 13 Korean source hash changed")

    doc = ET.fromstring(mtl_bytes)
    body = doc.find('.//h:div[@class="chapter-content"]', NS)
    source_paragraphs = [''.join(node.itertext()) for node in body.findall('.//h:p', NS)]
    if len(source_paragraphs) != 166:
        raise ValueError(f"Expected 166 MTL paragraph slots, got {len(source_paragraphs)}")

    staged = STAGING.read_text(encoding="utf-8").splitlines()
    if len(staged) != 166:
        raise ValueError(f"Expected 166 staged lines, got {len(staged)}")
    for number in SPACER_SLOTS:
        if staged[number - 1] != MARKER:
            raise ValueError(f"Missing Chapter 13 spacer marker at p{number}")
        if source_paragraphs[number - 1].replace('\xa0', '').strip():
            raise ValueError(f"Source p{number} is no longer an NBSP spacer")

    key_reasons = {
        1: "Name the Chapter 12 cliffhanger artifact as Beelzebub while preserving the Baskerville-blood inscription.",
        2: "Repair the MTL's 'Devil's first name' corruption: the inscription contains the sword's name.",
        5: "Restore Beelzebub's awl/stinger blade and three ruby-like guard nodes.",
        9: "Use the established epithet Beelzebub, the Gluttonous Fly.",
        12: "Normalize the ancient invaders as the Seven Calamities/demon constellations without importing later individual identities.",
        13: "Clarify that the defeated beings left remnants retaining only part of their former power.",
        15: "MTL-only witness-gap passage: retain the seven-family victory background with explicit provenance rather than fabricate Korean support.",
        16: "MTL-only witness-gap passage: retain Beelzebub's Baskerville custody and monster-attracting demonic aura.",
        17: "MTL-only witness-gap passage: preserve Vikir's first-timeline knowledge that the artifact later fell to demons.",
        25: "MTL-only witness-gap passage: preserve Beelzebub fusing into Vikir's palm/right hand.",
        28: "MTL-only witness-gap passage: preserve its concealed-spare-weapon behavior.",
        33: "MTL-only witness-gap passage: make the supernatural hunger onset explicit.",
        55: "Resolve historical audit ED-00108 and state naturally that Vikir and Beelzebub share the same intense hunger.",
        57: "Restore the drying/shriveling effect around Beelzebub's feeding point.",
        58: "Preserve Vikir's speculation that Beelzebub's hunger may explain the mountain's dead, parched landscape.",
        67: "Restore blood and bodily fluids passing through Beelzebub's hollow stinger into Vikir.",
        73: "State Beelzebub's living-form ability to steal distinctive traits/skills through consumed blood.",
        75: "Resolve historical audit ED-00109: as an artifact, Beelzebub no longer has its former near-limitless absorption scope.",
        76: "Preserve the current three-skill storage limit.",
        79: "Keep the first Beelzebub skill display as a structured info-window title.",
        80: "Normalize the first slot as Bleeding/Hemorrhage from Hellhound (B+).",
        85: "Describe the Hellhound-derived bleeding effect without universalizing it beyond the displayed mechanic.",
        97: "Continue the accepted Cradle terminology for the practical-assessment area.",
        100: "Use Guide Hounds consistently for the practical-assessment supervisors.",
        111: "Preserve Cerberus as practical-test evidence that must remain inspectable.",
        117: "Restore the Korean-only shared-pain explanation: pain to Vikir's fused hand is pain to Beelzebub as well.",
        122: "Keep the second Beelzebub skill display as a structured info-window title.",
        123: "Normalize Cerberus's acquired skill as Burn/Incinerate (A+).",
        124: "Keep Hellhound Bleeding/Hemorrhage in Slot 2 after the stronger Cerberus skill arrives.",
        125: "Correct Norbegicus to Brown Rat Norvegicus and normalize Rapid Regeneration (F).",
        132: "Frame skill replacement as Vikir's current inference rather than a later exhaustive ruleset.",
        135: "Preserve Cerberus's Burn/Incinerate as the chapter's major new combat gain.",
        136: "Avoid the MTL's absolute natural-healing claim while preserving the persistent hellfire-like burning effect.",
        145: "Describe Vikir's mana as roughly Fourth-Circle-equivalent rather than falsely recasting him as a wizard.",
        147: "Keep rank terminology consistent: upper Sword Expert approaching Sword Graduator.",
        148: "Clarify the conservative/generous Expert-versus-Low-Graduator self-assessment.",
        151: "Preserve current Hugo at seven fangs and Vikir's remembered future Hugo at nine.",
        153: "Clarify that the Ninth Form belongs to the direct succession line and chosen supporting sons.",
        155: "Resolve historical audit ED-00110 with a complete transition into the newly known Tenth Form lead.",
        156: "Correct the MTL's '10 meals' corruption to Tenth Form.",
        157: "State Baskerville Style, Tenth Form as ten fangs.",
        159: "Preserve the legendary first-patriarch secret text without importing later technique details.",
        162: "Clarify that the hidden inheritance is decaying among seemingly ordinary miscellaneous books.",
        164: "Use the established name Hugo Le Baskerville.",
        166: "Preserve the exact endpoint: Hugo will hand over the apparently worthless book without knowing its true value."
    }

    suppression_reasons = {
        str(number): "Recovered XHTML NBSP spacer around a Beelzebub info window; retain the source slot in provenance but suppress reader-facing blank output."
        for number in sorted(SPACER_SLOTS)
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
            ("Recovered MTL-only passage absent from the supplied Korean witness; preserve and polish the source text with explicit gap provenance."
             if number in MTL_ONLY else
             f"Compared the corresponding Korean witness with MTL paragraph {number}; repair English grammar, punctuation, register or attribution while preserving event and source slot.")
        )
        edits.append([number, replacement, reason])

    spec = {
        "chapter": CHAPTER,
        "source": "source/chapters/chapter-013.xhtml",
        "source_sha256": MTL_SHA,
        "expected_paragraphs": 166,
        "notice": "New reconstruction, not recovered production. The declared Korean witness gap and source adjudications are recorded in editorial/reviews/chapter-0013.md.",
        "korean_alignment": "editorial/korean-alignment/chapter-0013.json",
        "scene_breaks_after": [],
        "suppressed_paragraphs": sorted(SPACER_SLOTS),
        "suppression_reasons": suppression_reasons,
        "edits": edits,
    }

    korean_lines = korean_bytes.decode("utf-8-sig").splitlines()
    if len(korean_lines) != 146:
        raise ValueError(f"Expected 146 Korean physical lines, got {len(korean_lines)}")
    mapping = build_mapping()

    paragraphs = []
    for number in range(1, 167):
        refs = mapping[number]
        paragraphs.append({
            "mtl_paragraph": number,
            "korean_lines": refs,
            "line_text_sha256": [sha(korean_lines[line - 1].encode("utf-8")) for line in refs],
            "comparison": (
                MTL_ONLY_REASON if number in MTL_ONLY else
                key_reasons.get(number, "Compared corresponding Korean meaning, event and speaker; consequential decisions are documented in editorial/reviews/chapter-0013.md.")
            ),
        })

    alignment = {
        "chapter": CHAPTER,
        "korean_source": "source/korean/chapters/013.txt",
        "korean_sha256": KOREAN_SHA,
        "mtl_source": "source/chapters/chapter-013.xhtml",
        "mtl_sha256": MTL_SHA,
        "line_numbering": "One-based physical UTF-8 splitlines; original bytes unchanged.",
        "line_count": 146,
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
        "mtl_only_paragraphs": [
            {"mtl_paragraph": number, "reason": MTL_ONLY_REASON}
            for number in sorted(MTL_ONLY)
        ],
    }

    dump(ROOT / "editorial/edits/chapter-0013.json", spec)
    dump(ROOT / "editorial/korean-alignment/chapter-0013.json", alignment)
    print(f"Chapter 13 editorial inputs materialized: {len(edits)} changed slots; {len(MTL_ONLY)} explicit MTL-only slots; {len(SPACER_SLOTS)} structural slots suppressed.")


if __name__ == "__main__":
    main()
