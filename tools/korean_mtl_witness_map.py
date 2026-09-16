"""Map canonical Korean/source chapters to the recovered MTL corpus.

Canonical chapter identity follows the original Korean/source chapter number.  The
recovered MTL corpus is only a translation witness and has a chapter-boundary defect:
its Chapter 59 folds source Chapters 59 and 60 together.  Therefore recovered MTL
numbering is one chapter behind the source from source Chapter 61 onward.

Supplemental ``075.txt`` is another packaging oddity: one physical file explicitly
contains source Chapters 75 and 76.  Packaging does not change either source chapter's
identity.
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


def korean_witnesses_for_source(chapter: int, root: Path = ROOT) -> list[dict]:
    """Return Korean witness material for one canonical source chapter.

    Chapter 55 is intentionally detected dynamically.  The user reports possessing a
    055 raw, but that file is not present in the currently committed repository tree;
    if it is added later, it becomes available automatically rather than requiring a
    policy rewrite.
    """
    if chapter < 1 or chapter > 493:
        raise ValueError(f'Chapter outside source corpus: {chapter}')
    if chapter <= 54:
        return [witness(chapter, [chapter])]
    if chapter == 55:
        path = root / 'source/korean/chapters/055.txt'
        return [witness(55, [55])] if path.is_file() else []
    if 56 <= chapter <= 74:
        return [witness(chapter, [chapter])]
    if chapter == 75:
        return [witness(75, [75], 'bundled_file_segment_1')]
    if chapter == 76:
        return [witness(75, [76], 'bundled_file_segment_2')]
    if 77 <= chapter <= 125:
        return [witness(chapter, [chapter])]
    return []


def mtl_witnesses_for_source(chapter: int) -> list[dict]:
    """Return recovered MTL chapter(s) containing a canonical source chapter."""
    if chapter < 1 or chapter > 493:
        raise ValueError(f'Chapter outside source corpus: {chapter}')
    if chapter <= 58:
        return [{'mtl_chapter': chapter, 'role': 'single'}]
    if chapter == 59:
        return [{'mtl_chapter': 59, 'role': 'composite_part_1'}]
    if chapter == 60:
        return [{'mtl_chapter': 59, 'role': 'composite_part_2'}]
    if 61 <= chapter <= 493:
        return [{'mtl_chapter': chapter - 1, 'role': 'single'}]
    return []


def witnesses_for_mtl(chapter: int, root: Path = ROOT) -> list[dict]:
    """Reverse lookup retained for legacy tools whose primary index is MTL numbering."""
    if chapter < 1 or chapter > 493:
        raise ValueError(f'Chapter outside recovered corpus: {chapter}')
    if chapter <= 54:
        return [witness(chapter, [chapter])]
    if chapter == 55:
        return korean_witnesses_for_source(55, root)
    if 56 <= chapter <= 58:
        return [witness(chapter, [chapter])]
    if chapter == 59:
        return [
            witness(59, [59], 'composite_part_1'),
            witness(60, [60], 'composite_part_2'),
        ]
    # From recovered MTL 60 onward, the corresponding canonical source chapter is +1.
    source = chapter + 1
    return korean_witnesses_for_source(source, root)


def verify_mapping_files(root: Path = ROOT, through_source: int = 125) -> None:
    """Verify every declared Korean witness for canonical source chapters through N."""
    for chapter in range(1, through_source + 1):
        for item in korean_witnesses_for_source(chapter, root):
            path = root / item['path']
            if not path.is_file():
                raise ValueError(f'Missing mapped Korean witness for source {chapter}: {item["path"]}')


def source_gaps(through: int = 125, root: Path = ROOT) -> list[int]:
    return [chapter for chapter in range(1, through + 1) if not korean_witnesses_for_source(chapter, root)]


def mtl_gaps(through: int = 125, root: Path = ROOT) -> list[int]:
    """Legacy diagnostic: recovered MTL chapters with no Korean witness.

    Do not use this to define canonical source coverage.  In particular, recovered MTL
    Chapter 125 aligns to source Chapter 126; that does not make source Chapter 125
    missing.
    """
    return [chapter for chapter in range(1, through + 1) if not witnesses_for_mtl(chapter, root)]


if __name__ == '__main__':
    verify_mapping_files()
    print('Canonical source chapters without committed Korean witness through 125:', source_gaps())
    print('Legacy MTL chapters without Korean witness through 125:', mtl_gaps())
