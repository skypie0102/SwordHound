"""Prepare source policy, inventories, and prior-review baselines for Chapters 14-125."""
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import re
import subprocess

from korean_mtl_witness_map import mtl_gaps, verify_mapping_files, witnesses_for_mtl
from manage_supplemental_korean_raws import write_manifest

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'editorial' / 'reprocessing'


def file_info(path: Path):
    if not path.is_file():
        return None
    data = path.read_bytes()
    return {'path': path.relative_to(ROOT).as_posix(), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def production_refs() -> list[str]:
    return subprocess.check_output(
        ['git', 'for-each-ref', '--format=%(refname:short)', 'refs/remotes/origin/production/'],
        cwd=ROOT, text=True,
    ).splitlines()


def build_inventory() -> dict:
    OUT.mkdir(parents=True, exist_ok=True)
    verify_mapping_files(ROOT, 125)
    rows = []
    for chapter in range(1, 126):
        witnesses = []
        for item in witnesses_for_mtl(chapter):
            info = file_info(ROOT / item['path'])
            if info is None:
                raise ValueError(f'Mapped Korean witness missing: MTL {chapter} -> {item["path"]}')
            witnesses.append({**item, **info})
        mtl = file_info(ROOT / f'source/chapters/chapter-{chapter:03d}.xhtml')
        rows.append({
            'chapter': chapter,
            'basis': 'korean_plus_mtl' if witnesses else 'mtl_only',
            'korean_witnesses': witnesses,
            'mtl': mtl,
        })
    missing_korean = [r['chapter'] for r in rows if not r['korean_witnesses']]
    missing_mtl = [r['chapter'] for r in rows if r['mtl'] is None]
    doc = {
        'range': [1, 125],
        'alignment_basis': 'edition-aware Korean-to-recovered-MTL title-family and passage alignment; filename number is not assumed to equal MTL chapter number',
        'korean_witness_present_count': sum(bool(r['korean_witnesses']) for r in rows),
        'mtl_chapters_without_korean_witness': missing_korean,
        'missing_mtl': missing_mtl,
        'special_alignments': {
            '59': 'Recovered MTL Chapter 59 combines Korean source Chapters 59 and 60.',
            '74_75': 'Supplemental 075.txt declares Korean source Chapters 75+76 and covers recovered MTL Chapters 74 and 75 in sequence.',
            '60_124': 'Except the special 74/75 bundle handling, recovered MTL Chapters 60-124 align to Korean source chapter number +1.',
        },
        'chapters': rows,
    }
    (OUT / 'source-inventory-001-125.json').write_text(json.dumps(doc, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    md = [
        '# Reprocessing source inventory — recovered MTL Chapters 1–125', '',
        f"- Recovered MTL chapters with a Korean witness: **{doc['korean_witness_present_count']}/125**",
        '- MTL-only chapters after edition alignment: ' + (', '.join(map(str, missing_korean)) if missing_korean else 'none'),
        '- Missing MTL chapters: ' + (', '.join(map(str, missing_mtl)) if missing_mtl else 'none'), '',
        '## Edition-alignment notes', '',
        '- Korean and recovered MTL numbering are identical through Chapter 58, except that Korean 55 is absent.',
        '- Recovered MTL Chapter 59 combines Korean source Chapters 59 and 60.',
        '- Recovered MTL Chapters 60–73 align to Korean source chapter number +1.',
        '- `source/korean/chapters/075.txt` explicitly bundles source Chapters 75+76 and covers recovered MTL Chapters 74+75.',
        '- Recovered MTL Chapters 76–124 align to Korean source chapter number +1.',
        '- Recovered MTL Chapter 125 would require Korean source Chapter 126, which is not in the supplied raw set, so Chapter 125 is MTL-only.', '',
        'MTL-only chapters must never be described as bilingually verified. Missing Korean is a declared source limitation, not by itself an acceptance blocker.',
    ]
    (OUT / 'SOURCE-INVENTORY.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    if missing_korean != [55, 125] or mtl_gaps(125) != [55, 125]:
        raise ValueError(f'Expected edition-aligned MTL Korean gaps [55, 125], got {missing_korean}')
    if missing_mtl:
        raise ValueError(f'MTL coverage unexpectedly incomplete: {missing_mtl}')
    return doc


def branch_claims(refs: list[str]) -> dict[int, list[str]]:
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
        for chapter in range(max(14, lo), min(125, hi) + 1):
            claims.setdefault(chapter, []).append(name)
    return claims


def build_production_baselines() -> dict:
    refs = production_refs()
    claims = branch_claims(refs)
    prior_dir = OUT / 'prior-reviews'
    prior_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for chapter in range(14, 126):
        records = []
        copied_review = None
        for branch in claims.get(chapter, []):
            ref = f'origin/{branch}'
            paths = {
                'draft': f'manuscript/drafts/chapter-{chapter:04d}.md',
                'edit_set': f'editorial/edits/chapter-{chapter:04d}.json',
                'qa_json': f'qa/chapter-{chapter:04d}.json',
                'review': f'editorial/reviews/chapter-{chapter:04d}.md',
                'final_review': f'editorial/reviews/chapter-{chapter:04d}-final.md',
            }
            present = {}
            for kind, path in paths.items():
                probe = subprocess.run(['git', 'cat-file', '-e', f'{ref}:{path}'], cwd=ROOT, capture_output=True)
                present[kind] = path if probe.returncode == 0 else None
            if copied_review is None and present['review']:
                body = subprocess.check_output(['git', 'show', f"{ref}:{present['review']}"], cwd=ROOT, text=True)
                target = prior_dir / f'chapter-{chapter:04d}.md'
                target.write_text(body.rstrip() + '\n', encoding='utf-8')
                copied_review = {'source_branch': branch, 'source_path': present['review'], 'copied_to': target.relative_to(ROOT).as_posix()}
            records.append({'branch': branch, 'files': present})
        rows.append({
            'chapter': chapter,
            'claimed_branches': records,
            'has_production_baseline': any(r['files']['draft'] or r['files']['edit_set'] for r in records),
            'prior_review': copied_review,
        })
    doc = {'range': [14, 125], 'production_branches_scanned': refs, 'chapters': rows}
    (OUT / 'production-baselines-0014-0125.json').write_text(json.dumps(doc, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
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
    old = 'The recovered 493-chapter English MTL corpus is the working narrative base. User-supplied Korean raws are available for Chapters 1–54; from Chapter 55 onward the user has no Korean raws and authorizes MTL-based reconstruction. Use the Fandom and Namu Wiki references for QA, with additional web research as needed. Follow [SOURCES.md](SOURCES.md) for exact paths, links, evidence rules, and review modes.'
    new = 'The recovered 493-chapter English MTL corpus is the working narrative base. Edition-aware Korean witnesses are currently available for recovered MTL Chapters 1–54 and 56–124; recovered MTL Chapters 55 and 125 are MTL-only with the currently supplied raw set. Korean source numbering diverges from recovered MTL numbering after the Chapter 59 merge, so use `editorial/reprocessing/source-inventory-001-125.json` rather than matching filenames by number. Chapters 126–493 remain MTL-based unless additional Korean evidence is supplied. Use the Fandom and Namu Wiki references for QA, with additional web research as needed. Follow [SOURCES.md](SOURCES.md) for evidence rules and review modes.'
    text = replace_required(text, old, new, 'WORKFLOW source coverage')
    old = '3. For Chapters 1–54, compare the supplied Korean and MTL passages. For Chapters 55–493, review the MTL against context, continuity, and supporting references; Korean availability is not a prerequisite. Consult the two designated wikis for applicable names, terms, and locations, and seek other web support when needed. Record specific evidence, access dates, decisions, and conflicts. Label the review basis as `korean_plus_mtl` or `mtl_with_supporting_references`.'
    new = '3. For every recovered MTL chapter with one or more Korean witnesses recorded in the current source inventory, compare the mapped Korean witness material and MTL passage by passage. Composite and bundled witnesses must be aligned by content, not filename. For MTL-only Chapters 55 and 125, and for chapters beyond the currently supplied Korean range, review the MTL against context, continuity, and supporting references; missing Korean is not a prerequisite for acceptance when the limitation is explicit. Consult the two designated wikis for applicable names, terms, and locations, and seek other web support when needed. Record specific evidence, access dates, decisions, and conflicts. Label the review basis as `korean_plus_mtl` or `mtl_with_supporting_references`.'
    text = replace_required(text, old, new, 'WORKFLOW review mode')
    path.write_text(text, encoding='utf-8')

    path = ROOT / 'editorial/SOURCES.md'
    text = path.read_text(encoding='utf-8')
    text = replace_required(text, "Updated 2026-09-13 from the user's supplied archive and explicit source instructions.", "Updated 2026-09-16 from the user's preserved 1–54 archive, supplemental repository raws, and explicit source instructions.", 'SOURCES date')
    old_table = '''| Chapters | Working material | Required review mode |
|---|---|---|
| 1–54 | User-supplied Korean raws in `source/korean/chapters/001.txt` through `054.txt`, plus recovered English MTL in `source/chapters/` | Compare Korean and MTL passage by passage. Use the wiki references for canonical names, terms, and locations; document conflicting evidence. |
| 55–493 | Recovered English MTL in `source/chapters/`; the user has no Korean raws for this range | Reconstruct from MTL with contextual, continuity, and wiki-supported QA. Do not make Korean retrieval a prerequisite for starting or completing this review mode. |'''
    new_table = '''| Recovered MTL chapters | Working material | Required review mode |
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
    text = replace_required(text, old_table, new_table, 'SOURCES coverage table')
    old = 'The supplied files are the Korean comparison source for 1–54. Their publisher/edition provenance is not independently established.'
    new = 'The original ZIP remains the Korean comparison source for MTL Chapters 1–54. Supplemental raw files are separately hash-bound in `recovery/korean-supplemental-raws-manifest.json`; the edition-aware mapping into recovered MTL Chapters 56–124 is recorded in `editorial/reprocessing/source-inventory-001-125.json`. Their publisher/edition provenance is not independently established.'
    text = replace_required(text, old, new, 'SOURCES evidence paragraph')
    old = '- Use Korean text, MTL context, and wiki evidence together for 1–54. For 55 onward, use the MTL as the narrative basis and consult both wiki sources where relevant. Do not invent Korean wording or describe an MTL-only chapter as bilingually verified.'
    new = '- Use mapped Korean witness text, MTL context, and wiki evidence together wherever the inventory records a Korean witness. Do not infer correspondence from filenames alone. For MTL-only Chapters 55 and 125 and chapters beyond current Korean coverage, use the MTL as the narrative basis and consult supporting references where relevant. Do not invent Korean wording or describe an MTL-only chapter as bilingually verified.'
    text = replace_required(text, old, new, 'SOURCES evidence use')
    old = '- Missing Korean from Chapter 55 onward is a declared source limitation, not itself an unresolved QA issue.'
    new = '- Missing aligned Korean for recovered MTL Chapters 55 and 125, and beyond the currently mapped raw range, is a declared source limitation, not itself an unresolved QA issue.'
    text = replace_required(text, old, new, 'SOURCES missing Korean')
    path.write_text(text, encoding='utf-8')


def main() -> None:
    inventory = build_inventory()
    build_production_baselines()
    supplemental = write_manifest(ROOT)
    update_policy()
    print(json.dumps({
        'korean_witness_present_1_125': inventory['korean_witness_present_count'],
        'mtl_only_1_125': inventory['mtl_chapters_without_korean_witness'],
        'supplemental_files': supplemental['file_count'],
        'supplemental_source_chapters_declared': supplemental['source_chapter_count_declared'],
    }))


if __name__ == '__main__':
    main()
