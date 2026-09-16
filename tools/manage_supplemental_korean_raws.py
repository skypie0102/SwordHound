"""Build or verify Korean raw files added after the preserved 001-054 archive."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = 'recovery/korean-supplemental-raws-manifest.json'
ORIGINAL_CHAPTERS = set(range(1, 55))


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def opening_chapter_number(first_line: str) -> int | None:
    """Accept the preserved archive's #NN heading or supplemental 제NN장 heading."""
    for pattern in (r'#(\d+)(?!\d)', r'제\s*(\d+)\s*장(?:\s*:)?'):
        match = re.match(pattern, first_line)
        if match:
            return int(match.group(1))
    return None


def inspect_supplemental(root: Path = ROOT) -> dict:
    members = []
    chapter_dir = root / 'source/korean/chapters'
    for path in sorted(chapter_dir.glob('*.txt')):
        if not path.stem.isdigit():
            raise ValueError(f'Unexpected Korean raw filename: {path.name}')
        chapter = int(path.stem)
        if chapter in ORIGINAL_CHAPTERS:
            continue
        if chapter < 1 or chapter > 493:
            raise ValueError(f'Korean raw chapter is outside recovered corpus range: {path.name}')
        raw = path.read_bytes()
        text = raw.decode('utf-8-sig')
        first_line = next((line.strip() for line in text.splitlines() if line.strip()), '')
        opening_number = opening_chapter_number(first_line)
        if opening_number != chapter:
            raise ValueError(
                f'Opening chapter number does not match filename: {path.name}; '
                f'opening={first_line!r}, parsed={opening_number!r}'
            )
        members.append({
            'chapter': chapter,
            'path': path.relative_to(root).as_posix(),
            'bytes': len(raw),
            'sha256': sha256(raw),
            'encoding': 'utf-8',
            'opening_heading': first_line,
            'alignment': 'filename_and_opening_number_verified; full_passage_alignment_pending',
        })
    return {
        'received_date': '2026-09-16',
        'provenance': 'User added supplemental Korean raws directly to the repository after the preserved Chapters 1-54 archive. Files are preserved byte-for-byte and independently hash-bound here.',
        'chapter_count': len(members),
        'chapters': [m['chapter'] for m in members],
        'known_unrecoverable_within_001_125': [55, 76],
        'notice': 'This supplemental manifest does not modify the original 001-054 ZIP or its historical manifest. Numbered coverage and bytes are verified; translation accuracy and publisher provenance still require chapter review.',
        'members': members,
    }


def check_supplemental_raws(root: Path = ROOT) -> dict:
    manifest_path = root / MANIFEST
    if not manifest_path.is_file():
        raise ValueError(f'Missing supplemental Korean raw manifest: {MANIFEST}')
    expected = json.loads(manifest_path.read_text(encoding='utf-8'))
    actual = inspect_supplemental(root)
    if expected != actual:
        raise ValueError('Supplemental Korean raw manifest is stale or source bytes changed')
    return expected


def write_manifest(root: Path = ROOT) -> dict:
    manifest = inspect_supplemental(root)
    path = root / MANIFEST
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='Write the manifest from the current supplemental raw files.')
    args = parser.parse_args()
    manifest = write_manifest() if args.write else check_supplemental_raws()
    print(f"PASS: {manifest['chapter_count']} supplemental Korean raws verified: " + ', '.join(map(str, manifest['chapters'])))


if __name__ == '__main__':
    main()
