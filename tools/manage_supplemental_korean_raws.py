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


def opening_chapter_numbers(first_line: str) -> list[int]:
    """Return source chapter numbers explicitly declared by the opening heading."""
    match = re.match(r'#(\d+)(?!\d)', first_line)
    if match:
        return [int(match.group(1))]
    match = re.match(r'제\s*(\d+)\s*(?:장|화)(?:\s*:)?', first_line)
    if match:
        return [int(match.group(1))]
    # Supplemental 075.txt explicitly packages two source chapters as
    # "75장+76장 ... (1+2)". Keep that packaging fact in the manifest.
    match = re.match(r'(\d+)\s*장\s*\+\s*(\d+)\s*장', first_line)
    if match:
        return [int(match.group(1)), int(match.group(2))]
    return []


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
        opening_numbers = opening_chapter_numbers(first_line)
        if chapter not in opening_numbers:
            raise ValueError(
                f'Opening chapter number does not include filename chapter: {path.name}; '
                f'opening={first_line!r}, parsed={opening_numbers!r}'
            )
        members.append({
            'chapter': chapter,
            'source_chapters_declared': opening_numbers,
            'path': path.relative_to(root).as_posix(),
            'bytes': len(raw),
            'sha256': sha256(raw),
            'encoding': 'utf-8',
            'opening_heading': first_line,
            'alignment': 'filename_and_opening_number_verified; edition_to_mtl_passage_alignment_pending',
        })
    source_chapters = sorted({n for member in members for n in member['source_chapters_declared']})
    return {
        'received_date': '2026-09-16',
        'provenance': 'User added supplemental Korean raws directly to the repository after the preserved Chapters 1-54 archive. Files are preserved byte-for-byte and independently hash-bound here.',
        'file_count': len(members),
        'source_chapter_count_declared': len(source_chapters),
        'source_chapters_declared': source_chapters,
        'files': [m['chapter'] for m in members],
        'missing_filenames_within_055_125': [55, 76],
        'notice': 'This supplemental manifest does not modify the original 001-054 ZIP or its historical manifest. Korean source numbering is not assumed to equal recovered MTL numbering; 075.txt explicitly bundles source Chapters 75 and 76. Passage-level edition alignment is a separate editorial step.',
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
    print(
        f"PASS: {manifest['file_count']} supplemental Korean raw files verified; "
        f"{manifest['source_chapter_count_declared']} source chapter numbers declared."
    )


if __name__ == '__main__':
    main()
