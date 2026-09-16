"""Prepare source policy, inventories, and prior-review baselines for Chapters 14-125."""
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import re
import subprocess

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
    rows = []
    for chapter in range(1, 126):
        ko = file_info(ROOT / f'source/korean/chapters/{chapter:03d}.txt')
        mtl = file_info(ROOT / f'source/chapters/chapter-{chapter:03d}.xhtml')
        rows.append({'chapter': chapter, 'basis': 'korean_plus_mtl' if ko else 'mtl_only', 'korean': ko, 'mtl': mtl})
    missing_korean = [r['chapter'] for r in rows if r['korean'] is None]
    missing_mtl = [r['chapter'] for r in rows if r['mtl'] is None]
    doc = {
        'range': [1, 125],
        'korean_present_count': sum(r['korean'] is not None for r in rows),
        'korean_missing': missing_korean,
        'mtl_missing': missing_mtl,
        'chapters': rows,
    }
    (OUT / 'source-inventory-001-125.json').write_text(json.dumps(doc, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    md = [
        '# Reprocessing source inventory — Chapters 1–125', '',
        f"- Korean raws present: **{doc['korean_present_count']}/125**",
        '- Missing Korean raws: ' + (', '.join(map(str, missing_korean)) if missing_korean else 'none'),
        '- Missing MTL chapters: ' + (', '.join(map(str, missing_mtl)) if missing_mtl else 'none'), '',
        'Chapters without a Korean raw must be reviewed from the recovered MTL only and explicitly marked `mtl_only`; no Korean evidence may be claimed for them.',
    ]
    (OUT / 'SOURCE-INVENTORY.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    if missing_korean != [55, 76]:
        raise ValueError(f'Expected current Korean gaps [55, 76], got {missing_korean}')
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
    text = replace_required(
        text,
        'The recovered 493-chapter English MTL corpus is the working narrative base. User-supplied Korean raws are available for Chapters 1–54; from Chapter 55 onward the user has no Korean raws and authorizes MTL-based reconstruction. Use the Fandom and Namu Wiki references for QA, with additional web research as needed. Follow [SOURCES.md](SOURCES.md) for exact paths, links, evidence rules, and review modes.',
        'The recovered 493-chapter English MTL corpus is the working narrative base. Korean raws are currently available for Chapters 1–125 except the unrecoverable Chapters 55 and 76. Chapters 55 and 76, and currently Chapters 126–493, use MTL-based reconstruction unless additional Korean evidence is later supplied. Use the Fandom and Namu Wiki references for QA, with additional web research as needed. Follow [SOURCES.md](SOURCES.md) and `editorial/reprocessing/source-inventory-001-125.json` for exact paths, live coverage, evidence rules, and review modes.',
        'WORKFLOW source coverage',
    )
    text = replace_required(
        text,
        '3. For Chapters 1–54, compare the supplied Korean and MTL passages. For Chapters 55–493, review the MTL against context, continuity, and supporting references; Korean availability is not a prerequisite. Consult the two designated wikis for applicable names, terms, and locations, and seek other web support when needed. Record specific evidence, access dates, decisions, and conflicts. Label the review basis as `korean_plus_mtl` or `mtl_with_supporting_references`.',
        '3. For every chapter with a Korean raw recorded in the current source inventory, compare Korean and MTL passage by passage. For Chapters 55 and 76, and for chapters beyond the currently supplied Korean range, review the MTL against context, continuity, and supporting references; missing Korean is not a prerequisite for MTL-only acceptance when the limitation is explicit. Consult the two designated wikis for applicable names, terms, and locations, and seek other web support when needed. Record specific evidence, access dates, decisions, and conflicts. Label the review basis as `korean_plus_mtl` or `mtl_with_supporting_references`.',
        'WORKFLOW review mode',
    )
    path.write_text(text, encoding='utf-8')

    path = ROOT / 'editorial/SOURCES.md'
    text = path.read_text(encoding='utf-8')
    text = replace_required(
        text,
        "Updated 2026-09-13 from the user's supplied archive and explicit source instructions.",
        "Updated 2026-09-16 from the user's preserved 1–54 archive, supplemental repository raws, and explicit source instructions.",
        'SOURCES date',
    )
    old_table = '''| Chapters | Working material | Required review mode |
|---|---|---|
| 1–54 | User-supplied Korean raws in `source/korean/chapters/001.txt` through `054.txt`, plus recovered English MTL in `source/chapters/` | Compare Korean and MTL passage by passage. Use the wiki references for canonical names, terms, and locations; document conflicting evidence. |
| 55–493 | Recovered English MTL in `source/chapters/`; the user has no Korean raws for this range | Reconstruct from MTL with contextual, continuity, and wiki-supported QA. Do not make Korean retrieval a prerequisite for starting or completing this review mode. |'''
    new_table = '''| Chapters | Working material | Required review mode |
|---|---|---|
| 1–54 | Preserved user-supplied Korean raws from the original ZIP, plus recovered English MTL | Compare Korean and MTL passage by passage. |
| 55 | Korean raw unrecoverable; recovered English MTL remains available | MTL-only reconstruction with contextual, continuity, and supporting-reference QA; record the source limitation explicitly. |
| 56–75 | Supplemental Korean raws plus recovered English MTL | Compare Korean and MTL passage by passage. |
| 76 | Korean raw unrecoverable; recovered English MTL remains available | MTL-only reconstruction with contextual, continuity, and supporting-reference QA; record the source limitation explicitly. |
| 77–125 | Supplemental Korean raws plus recovered English MTL | Compare Korean and MTL passage by passage. |
| 126–493 | Recovered English MTL; no Korean raw currently registered | MTL-only reconstruction with contextual, continuity, and supporting-reference QA unless more Korean evidence is supplied later. |'''
    text = replace_required(text, old_table, new_table, 'SOURCES coverage table')
    text = replace_required(
        text,
        'The supplied files are the Korean comparison source for 1–54. Their publisher/edition provenance is not independently established.',
        'The original ZIP files remain the Korean comparison source for 1–54. Supplemental raws for 56–75 and 77–125 are separately hash-bound in `recovery/korean-supplemental-raws-manifest.json`; Chapters 55 and 76 are explicitly unrecoverable. Their publisher/edition provenance is not independently established.',
        'SOURCES evidence paragraph',
    )
    text = replace_required(
        text,
        '- Use Korean text, MTL context, and wiki evidence together for 1–54. For 55 onward, use the MTL as the narrative basis and consult both wiki sources where relevant. Do not invent Korean wording or describe an MTL-only chapter as bilingually verified.',
        '- Use Korean text, MTL context, and wiki evidence together whenever a Korean raw is registered. For Chapters 55 and 76, and chapters beyond the currently supplied Korean range, use the MTL as the narrative basis and consult supporting references where relevant. Do not invent Korean wording or describe an MTL-only chapter as bilingually verified.',
        'SOURCES evidence use',
    )
    text = replace_required(
        text,
        '- Missing Korean from Chapter 55 onward is a declared source limitation, not itself an unresolved QA issue.',
        '- Missing Korean for Chapters 55 and 76, and beyond the currently supplied raw range, is a declared source limitation, not itself an unresolved QA issue.',
        'SOURCES missing Korean',
    )
    path.write_text(text, encoding='utf-8')


def main() -> None:
    inventory = build_inventory()
    build_production_baselines()
    supplemental = write_manifest(ROOT)
    update_policy()
    print(json.dumps({
        'korean_present_1_125': inventory['korean_present_count'],
        'korean_missing_1_125': inventory['korean_missing'],
        'supplemental_raws': supplemental['chapter_count'],
    }))


if __name__ == '__main__':
    main()
