"""Prepare canonical source inventories and prior-review baselines for Chapters 14-125."""
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import re
import subprocess

from korean_mtl_witness_map import (
    korean_witnesses_for_source,
    mtl_witnesses_for_source,
    source_gaps,
    verify_mapping_files,
)
from manage_supplemental_korean_raws import write_manifest

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'editorial' / 'reprocessing'


def file_info(path: Path):
    if not path.is_file():
        return None
    data = path.read_bytes()
    return {
        'path': path.relative_to(ROOT).as_posix(),
        'bytes': len(data),
        'sha256': hashlib.sha256(data).hexdigest(),
    }


def production_refs() -> list[str]:
    return subprocess.check_output(
        ['git', 'for-each-ref', '--format=%(refname:short)', 'refs/remotes/origin/production/'],
        cwd=ROOT,
        text=True,
    ).splitlines()


def build_inventory() -> dict:
    """Build the inventory by original/Korean chapter number, never MTL filename number."""
    OUT.mkdir(parents=True, exist_ok=True)
    verify_mapping_files(ROOT, 125)
    rows = []
    for source_chapter in range(1, 126):
        korean = []
        for item in korean_witnesses_for_source(source_chapter, ROOT):
            info = file_info(ROOT / item['path'])
            if info is None:
                raise ValueError(f'Mapped Korean witness missing: source {source_chapter} -> {item["path"]}')
            korean.append({**item, **info})

        mtl = []
        for item in mtl_witnesses_for_source(source_chapter):
            path = ROOT / f"source/chapters/chapter-{item['mtl_chapter']:03d}.xhtml"
            info = file_info(path)
            if info is None:
                raise ValueError(f'Mapped MTL witness missing: source {source_chapter} -> {path}')
            mtl.append({**item, **info})

        rows.append({
            'canonical_source_chapter': source_chapter,
            'basis': 'korean_plus_mtl' if korean else 'mtl_with_supporting_references',
            'korean_witnesses': korean,
            'recovered_mtl_witnesses': mtl,
        })

    missing_korean = [r['canonical_source_chapter'] for r in rows if not r['korean_witnesses']]
    if 125 in missing_korean:
        raise ValueError('Canonical source Chapter 125 must use source/korean/chapters/125.txt')

    doc = {
        'canonical_numbering': 'original Korean/source chapter number',
        'range': [1, 125],
        'korean_source_present_count': sum(bool(r['korean_witnesses']) for r in rows),
        'korean_source_files_missing_from_repo': missing_korean,
        'user_reported_external_or_local_raws_not_yet_found_in_repo': [55] if 55 in missing_korean else [],
        'special_alignments': {
            'source_59': 'Canonical source Chapter 59 is the first segment of recovered MTL Chapter 59.',
            'source_60': 'Canonical source Chapter 60 is the second segment of recovered MTL Chapter 59. The MTL merge must not renumber the source corpus.',
            'source_61_125': 'Canonical source Chapters 61-125 align to recovered MTL chapter number -1, subject to passage-level verification.',
            'source_75_76': 'Physical raw file 075.txt explicitly bundles canonical source Chapters 75 and 76; the chapters retain their own identities.',
            'source_125': 'Canonical source Chapter 125 is present in 125.txt and aligns to recovered MTL Chapter 124. Recovered MTL Chapter 125 corresponds to later source material and is outside the Korean-through-125 audit scope.',
        },
        'chapters': rows,
    }
    (OUT / 'source-inventory-001-125.json').write_text(
        json.dumps(doc, ensure_ascii=False, indent=2) + '\n', encoding='utf-8'
    )

    md = [
        '# Reprocessing source inventory — canonical Chapters 1–125',
        '',
        '**Canonical numbering is the original Korean/source chapter number.** Recovered MTL numbering is only an auxiliary witness and must never redefine chapter identity.',
        '',
        f"- Canonical chapters with a committed Korean witness: **{doc['korean_source_present_count']}/125**",
        '- Korean source chapters currently absent from the repository: ' + (', '.join(map(str, missing_korean)) if missing_korean else 'none'),
        '- User reports that Chapter 55 raw exists; no `source/korean/chapters/055.txt` is currently committed in the accessible repository tree. If it is added, the inventory will adopt it automatically.',
        '- Chapter 125 **is Korean-backed** by `source/korean/chapters/125.txt`.',
        '',
        '## MTL boundary/alignment notes',
        '',
        '- Source Chapters 1–58 align to the same recovered MTL chapter number.',
        '- Recovered MTL Chapter 59 contains both canonical source Chapters 59 and 60. Reconstruction must split that material back across two canonical chapters.',
        '- Canonical source Chapters 61–125 align to recovered MTL chapter number minus one, with passage-level checks rather than blind filename matching.',
        '- `source/korean/chapters/075.txt` physically bundles source Chapters 75 and 76; this is a packaging detail, not a chapter renumbering.',
        '- Canonical source Chapter 125 uses Korean `125.txt` and recovered MTL Chapter 124. Recovered MTL Chapter 125 is not a reason to call source Chapter 125 MTL-only.',
        '',
        'Where a Korean raw is genuinely unavailable in the repository, MTL fallback is permitted under the user’s instruction, but the limitation must be recorded explicitly.',
    ]
    (OUT / 'SOURCE-INVENTORY.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    return doc


def branch_claims(refs: list[str]) -> dict[int, list[str]]:
    """Index legacy production branches by their recovered-MTL chapter numbering."""
    claims: dict[int, list[str]] = {}
    for ref in refs:
        name = ref.split('origin/', 1)[-1]
        nums = [int(x) for x in re.findall(r'(?<!\d)(\d{4})(?!\d)', name)]
        if len(nums) >= 2:
            lo, hi = nums[-2], nums[-1]
        elif len(nums) == 1:
            lo = hi = nums[0]
        else:
            continue
        if lo > hi:
            lo, hi = hi, lo
        for chapter in range(lo, hi + 1):
            claims.setdefault(chapter, []).append(name)
    return claims


def build_production_baselines() -> dict:
    """Carry prior review records forward, translating legacy MTL IDs to source IDs."""
    refs = production_refs()
    claims = branch_claims(refs)
    prior_dir = OUT / 'prior-reviews'
    prior_dir.mkdir(parents=True, exist_ok=True)
    rows = []

    for source_chapter in range(14, 126):
        legacy_mtl = [x['mtl_chapter'] for x in mtl_witnesses_for_source(source_chapter)]
        records = []
        copied_review = None
        for mtl_chapter in legacy_mtl:
            for branch in claims.get(mtl_chapter, []):
                ref = f'origin/{branch}'
                paths = {
                    'draft': f'manuscript/drafts/chapter-{mtl_chapter:04d}.md',
                    'edit_set': f'editorial/edits/chapter-{mtl_chapter:04d}.json',
                    'qa_json': f'qa/chapter-{mtl_chapter:04d}.json',
                    'review': f'editorial/reviews/chapter-{mtl_chapter:04d}.md',
                    'final_review': f'editorial/reviews/chapter-{mtl_chapter:04d}-final.md',
                }
                present = {}
                for kind, path in paths.items():
                    probe = subprocess.run(['git', 'cat-file', '-e', f'{ref}:{path}'], cwd=ROOT, capture_output=True)
                    present[kind] = path if probe.returncode == 0 else None
                if copied_review is None and present['review']:
                    body = subprocess.check_output(['git', 'show', f"{ref}:{present['review']}"], cwd=ROOT, text=True)
                    target = prior_dir / f'chapter-{source_chapter:04d}.md'
                    preface = (
                        f'<!-- Canonical source Chapter {source_chapter}; imported from legacy recovered-MTL '
                        f'Chapter {mtl_chapter}. Prior review is evidence, not automatic acceptance. -->\n\n'
                    )
                    target.write_text(preface + body.rstrip() + '\n', encoding='utf-8')
                    copied_review = {
                        'source_branch': branch,
                        'legacy_mtl_chapter': mtl_chapter,
                        'source_path': present['review'],
                        'copied_to': target.relative_to(ROOT).as_posix(),
                    }
                records.append({'legacy_mtl_chapter': mtl_chapter, 'branch': branch, 'files': present})

        rows.append({
            'canonical_source_chapter': source_chapter,
            'legacy_mtl_chapters': legacy_mtl,
            'claimed_branches': records,
            'has_production_baseline': any(r['files']['draft'] or r['files']['edit_set'] for r in records),
            'prior_review': copied_review,
        })

    doc = {
        'canonical_range': [14, 125],
        'note': 'Production branch names use the recovered MTL numbering. Rows are re-keyed here to canonical Korean/source chapter numbers.',
        'production_branches_scanned': refs,
        'chapters': rows,
    }
    (OUT / 'production-baselines-0014-0125.json').write_text(
        json.dumps(doc, ensure_ascii=False, indent=2) + '\n', encoding='utf-8'
    )
    return doc


def replace_required(text: str, old: str, new: str, label: str) -> str:
    if old in text:
        return text.replace(old, new)
    if new in text:
        return text
    raise RuntimeError(f'Policy anchor changed: {label}')


def update_policy() -> None:
    path = ROOT / 'editorial/WORKFLOW.md'
    text = path.read_text(encoding='utf-8')
    old = 'The recovered 493-chapter English MTL corpus is the working narrative base. Edition-aware Korean witnesses are currently available for recovered MTL Chapters 1–54 and 56–124; recovered MTL Chapters 55 and 125 are MTL-only with the currently supplied raw set. Korean source numbering diverges from recovered MTL numbering after the Chapter 59 merge, so use `editorial/reprocessing/source-inventory-001-125.json` rather than matching filenames by number. Chapters 126–493 remain MTL-based unless additional Korean evidence is supplied. Use the Fandom and Namu Wiki references for QA, with additional web research as needed. Follow [SOURCES.md](SOURCES.md) for evidence rules and review modes.'
    new = 'Canonical chapter identity follows the original Korean/source chapter number. The recovered 493-chapter English MTL corpus is a working translation witness, not the authority for chapter numbering. Its Chapter 59 merges canonical source Chapters 59 and 60, so recovered MTL numbering runs one chapter behind the source from canonical Chapter 61 onward in the currently mapped range. Korean source Chapter 125 is present in `source/korean/chapters/125.txt` and aligns to recovered MTL Chapter 124. Use `editorial/reprocessing/source-inventory-001-125.json` for the source-to-MTL map. The user reports possessing a Chapter 55 Korean raw, but no `055.txt` is currently committed in the accessible repository tree; use MTL fallback only while that raw is unavailable. Use the Fandom and Namu Wiki references for QA, with additional web research as needed. Follow [SOURCES.md](SOURCES.md) for evidence rules and review modes.'
    text = replace_required(text, old, new, 'WORKFLOW source coverage')

    old = '3. For every recovered MTL chapter with one or more Korean witnesses recorded in the current source inventory, compare the mapped Korean witness material and MTL passage by passage. Composite and bundled witnesses must be aligned by content, not filename. For MTL-only Chapters 55 and 125, and for chapters beyond the currently supplied Korean range, review the MTL against context, continuity, and supporting references; missing Korean is not a prerequisite for acceptance when the limitation is explicit. Consult the two designated wikis for applicable names, terms, and locations, and seek other web support when needed. Record specific evidence, access dates, decisions, and conflicts. Label the review basis as `korean_plus_mtl` or `mtl_with_supporting_references`.'
    new = '3. Work by canonical Korean/source chapter number. For every canonical chapter with a Korean witness in the inventory, compare that Korean material against its mapped recovered-MTL passage(s) line by line. Treat the MTL Chapter 59 merge as a boundary defect to repair: canonical Chapters 59 and 60 remain separate chapters. Physical bundles such as Korean `075.txt` likewise do not collapse canonical Chapters 75 and 76. If a canonical Korean raw is genuinely unavailable in the repository, use the recovered MTL plus context, continuity, and supporting references under an explicit `mtl_with_supporting_references` limitation. Consult the designated wikis where relevant, record evidence and conflicts, and never describe MTL-only fallback as bilingual verification.'
    text = replace_required(text, old, new, 'WORKFLOW review mode')
    path.write_text(text, encoding='utf-8')

    path = ROOT / 'editorial/SOURCES.md'
    text = path.read_text(encoding='utf-8')
    old_table = '''| Recovered MTL chapters | Working material | Required review mode |
|---|---|---|
| 1–54 | Preserved Korean raws from the original ZIP plus recovered English MTL | Compare Korean and MTL passage by passage. |
| 55 | No aligned Korean witness in the supplied set; recovered English MTL remains available | MTL-only reconstruction with contextual, continuity, and supporting-reference QA; record the limitation explicitly. |
| 56–58 | Same-number supplemental Korean raw plus recovered English MTL | Compare Korean and MTL passage by passage. |
| 59 | Korean source Chapters 59+60 plus recovered English MTL Chapter 59 | Treat as a composite Korean witness and align both source chapters against the single recovered MTL chapter. |
| 60–73 | Korean source chapter number +1 plus recovered English MTL | Compare mapped Korean and MTL passage by passage. |
| 74–75 | Bundled `source/korean/chapters/075.txt`, which declares source Chapters 75+76, plus recovered English MTL | Split/alignment by passage: source 75 → MTL 74; source 76 → MTL 75. |
| 76–124 | Korean source chapter number +1 plus recovered English MTL | Compare mapped Korean and MTL passage by passage. |
| 125 | Would require Korean source Chapter 126, not present in the supplied set | MTL-only reconstruction with contextual, continuity, and supporting-reference QA. |
| 126–493 | Recovered English MTL; no Korean witness currently registered | MTL-only reconstruction unless more Korean evidence is supplied later. |'''
    new_table = '''| Canonical source chapters | Korean/source witness | Recovered MTL witness | Required review mode |
|---|---|---|---|
| 1–54 | Preserved raws from the original ZIP | Same chapter number | Korean-first passage comparison. |
| 55 | User reports a Korean raw exists, but `055.txt` is not currently committed in the accessible repo | MTL 55 | Use MTL fallback only while the raw is unavailable; import/use the Korean raw if it lands before acceptance. |
| 56–58 | `056.txt`–`058.txt` | Same chapter number | Korean-first passage comparison. |
| 59 | `059.txt` | First portion of MTL 59 | Keep canonical Chapter 59 separate. |
| 60 | `060.txt` | Second portion of MTL 59 | Split the merged MTL chapter and restore canonical Chapter 60. |
| 61–74 | Same-number Korean raw | MTL source chapter − 1 | Korean-first passage comparison. |
| 75 | First chapter segment in bundled `075.txt` | MTL 74 | Preserve canonical Chapter 75. |
| 76 | Second chapter segment in bundled `075.txt` | MTL 75 | Preserve canonical Chapter 76. |
| 77–125 | Same-number Korean raw, including `125.txt` | MTL source chapter − 1 | Korean-first passage comparison. |
| >125 | Not currently registered for this reprocessing pass | Align recovered MTL by content before use | MTL fallback unless further Korean raws are supplied. |'''
    text = replace_required(text, old_table, new_table, 'SOURCES coverage table')

    old = 'The original ZIP remains the Korean comparison source for MTL Chapters 1–54. Supplemental raw files are separately hash-bound in `recovery/korean-supplemental-raws-manifest.json`; the edition-aware mapping into recovered MTL Chapters 56–124 is recorded in `editorial/reprocessing/source-inventory-001-125.json`. Their publisher/edition provenance is not independently established.'
    new = 'The original ZIP remains the Korean comparison source for canonical Chapters 1–54. Supplemental raw files are separately hash-bound in `recovery/korean-supplemental-raws-manifest.json`. Canonical source identity comes from the Korean/source chapter heading, while recovered MTL correspondence is recorded separately in `editorial/reprocessing/source-inventory-001-125.json`. In particular, `125.txt` is canonical Chapter 125 even though its parallel recovered MTL passage is numbered 124. Their publisher/edition provenance is not independently established.'
    text = replace_required(text, old, new, 'SOURCES evidence paragraph')

    old = '- Use mapped Korean witness text, MTL context, and wiki evidence together wherever the inventory records a Korean witness. Do not infer correspondence from filenames alone. For MTL-only Chapters 55 and 125 and chapters beyond current Korean coverage, use the MTL as the narrative basis and consult supporting references where relevant. Do not invent Korean wording or describe an MTL-only chapter as bilingually verified.'
    new = '- Use canonical Korean/source chapter identity first, then align the recovered MTL by content. Do not let a shifted MTL filename renumber the Korean source. Chapter 125 is Korean-backed. For Chapter 55, the user reports a raw exists but the file is not currently committed; use MTL fallback only while that raw cannot be accessed. Do not invent Korean wording or describe fallback-only review as bilingual verification.'
    text = replace_required(text, old, new, 'SOURCES evidence use')

    old = '- Missing aligned Korean for recovered MTL Chapters 55 and 125, and beyond the currently mapped raw range, is a declared source limitation, not itself an unresolved QA issue. Actual unresolved story-changing ambiguities still need explicit treatment before editorial acceptance. Acceptance must identify its basis as `korean_plus_mtl` or `mtl_with_supporting_references`.'
    new = '- A missing committed Korean file is a repository/source-access limitation, not permission to renumber chapters. At present the accessible tree lacks `055.txt`, while `125.txt` is present and must be used for canonical Chapter 125. Actual story-changing ambiguities still require explicit treatment before editorial acceptance. Acceptance must identify its basis as `korean_plus_mtl` or `mtl_with_supporting_references`.'
    text = replace_required(text, old, new, 'SOURCES missing Korean')
    path.write_text(text, encoding='utf-8')


def main() -> None:
    inventory = build_inventory()
    build_production_baselines()
    supplemental = write_manifest(ROOT)
    update_policy()
    print(json.dumps({
        'canonical_korean_present_1_125': inventory['korean_source_present_count'],
        'canonical_korean_files_missing_from_repo': inventory['korean_source_files_missing_from_repo'],
        'supplemental_files': supplemental['file_count'],
        'supplemental_source_chapters_declared': supplemental['source_chapter_count_declared'],
        'source_125_korean_backed': 125 not in source_gaps(125, ROOT),
    }))


if __name__ == '__main__':
    main()
