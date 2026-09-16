"""Declared Korean witness mapping for recovered MTL Chapters 1-125.

This mapping is edition-aware. Supplemental Korean source numbering diverges from the
recovered MTL after English Chapter 59 because the MTL folds Korean source Chapters
59 and 60 into one chapter. Supplemental 075.txt explicitly bundles Korean source
Chapters 75 and 76, which align to MTL Chapters 74 and 75 respectively.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def witness(path_chapter: int, source_chapters: list[int], role: str = 'single') -> dict:
    return {
        'path': f'source/korean/chapters/{path_chapter:03d}.txt',
        'source_chapters': source_chapters,
        'role': role,
    }


def witnesses_for_mtl(chapter: int) -> list[dict]:
    if chapter < 1 or chapter > 493:
        raise ValueError(f'Chapter outside recovered corpus: {chapter}')
    if chapter <= 54:
        return [witness(chapter, [chapter])]
    if chapter == 55:
        return []
    if 56 <= chapter <= 58:
        return [witness(chapter, [chapter])]
    if chapter == 59:
        return [
            witness(59, [59], 'composite_part_1'),
            witness(60, [60], 'composite_part_2'),
        ]
    if 60 <= chapter <= 73:
        return [witness(chapter + 1, [chapter + 1])]
    if chapter == 74:
        return [witness(75, [75], 'bundled_file_segment_1')]
    if chapter == 75:
        return [witness(75, [76], 'bundled_file_segment_2')]
    if 76 <= chapter <= 124:
        return [witness(chapter + 1, [chapter + 1])]
    # Korean source supplied only through source Chapter 125. Due the edition offset,
    # MTL Chapter 125 would require Korean source Chapter 126.
    if chapter == 125:
        return []
    return []


def verify_mapping_files(root: Path = ROOT, through: int = 125) -> None:
    for chapter in range(1, through + 1):
        for item in witnesses_for_mtl(chapter):
            path = root / item['path']
            if not path.is_file():
                raise ValueError(f'Missing mapped Korean witness for MTL {chapter}: {item["path"]}')


def mtl_gaps(through: int = 125) -> list[int]:
    return [chapter for chapter in range(1, through + 1) if not witnesses_for_mtl(chapter)]


if __name__ == '__main__':
    verify_mapping_files()
    print('MTL chapters without Korean witness through 125:', mtl_gaps())
