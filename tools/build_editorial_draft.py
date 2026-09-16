#!/usr/bin/env python3
"""Resolve Chinese-first chapter sources and build an editorial scaffold.

This tool intentionally never assumes that target chapter N equals English MTL
chapter N. An English reference is used only when verified in the exception table
or explicitly supplied by the editor.
"""
from __future__ import annotations
import argparse, csv, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHINESE = ROOT / "source/chinese/chapters"
EXCEPTIONS = ROOT / "source/chinese/chapter-exceptions.tsv"
MTL = ROOT / "source/chapters"

def load_exceptions():
    with EXCEPTIONS.open(encoding="utf-8", newline="") as fh:
        return {int(r["target_chapter"]): r for r in csv.DictReader(fh, delimiter="\t")}

def resolve_sources(chapter: int, explicit_mtl_chapter: int | None = None):
    if not 1 <= chapter <= 500:
        raise ValueError("Target chapter must be in 1..500")
    row = load_exceptions().get(chapter)
    raw_status = row["raw_status"] if row else "single"
    if raw_status == "missing":
        chinese = None
    else:
        raw_file = row["raw_file"] if row and row["raw_file"] else f"{chapter:03d}.txt"
        chinese = CHINESE / raw_file
        if not chinese.is_file():
            raise FileNotFoundError(chinese)
    verified = int(row["verified_english_mtl_chapter"]) if row and row["verified_english_mtl_chapter"].strip() else None
    if explicit_mtl_chapter is not None:
        if not 1 <= explicit_mtl_chapter <= 493:
            raise ValueError("English MTL chapter must be in 1..493")
        mtl_number, alignment = explicit_mtl_chapter, "editor_supplied"
    elif verified is not None:
        mtl_number, alignment = verified, "verified_exception_table"
    else:
        mtl_number, alignment = None, "unresolved_align_by_title_and_content"
    english = MTL / f"chapter-{mtl_number:03d}.xhtml" if mtl_number else None
    if english and not english.is_file():
        raise FileNotFoundError(english)
    if chinese is None and english is None:
        raise ValueError("Missing Chinese raw requires a verified/explicit English fallback")
    return {
        "target_chapter": chapter,
        "source_mode": "mtl_only" if chinese is None else "chinese_primary",
        "raw_status": raw_status,
        "chinese_source": str(chinese.relative_to(ROOT)) if chinese else None,
        "english_mtl_reference": str(english.relative_to(ROOT)) if english else None,
        "english_mtl_chapter": mtl_number,
        "english_alignment": alignment,
        "notes": row["notes"] if row else "",
    }

def render(chapter: int, explicit_mtl_chapter: int | None = None):
    src = resolve_sources(chapter, explicit_mtl_chapter)
    n = f"{chapter:04d}"
    packet = {"policy":"chinese_primary_2026-09-16", **src,
              "qa_required":["semantic_fidelity","coverage","terminology","continuity","natural_english","formatting","source_provenance"]}
    lines = [f"# Chapter {chapter}", "", "> Chinese-first reconstruction scaffold; not accepted until full QA passes.", "",
             "## Sources", f"- Chinese: `{src['chinese_source'] or 'MISSING'}`",
             f"- English MTL: `{src['english_mtl_reference'] or 'UNRESOLVED — align by title/content first'}`",
             f"- Raw status: `{src['raw_status']}`", "", "## Draft", "",
             "<!-- Read the complete Chinese source container before translating/editing. -->", "", "## QA notes", "",
             "- [ ] Semantic fidelity", "- [ ] No omissions / duplication / inventions", "- [ ] Names and terminology",
             "- [ ] Neighbor/title-family continuity", "- [ ] Grammar and natural English", "- [ ] Formatting/windows/scene breaks"]
    if src["raw_status"] == "combined":
        lines.append("- [ ] Shared-container split documented; paired outputs have no gap/overlap")
    if src["source_mode"] == "mtl_only":
        lines.append("- [ ] MTL-only uncertainty and neighboring-context review")
    return {f"editorial/staging/chapter-{n}-sources.json": json.dumps(packet, ensure_ascii=False, indent=2)+"\n",
            f"manuscript/drafts/chapter-{n}.md": "\n".join(lines)+"\n"}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("chapter", type=int); ap.add_argument("--mtl-chapter", type=int); ap.add_argument("--write", action="store_true")
    a = ap.parse_args(); outputs = render(a.chapter, a.mtl_chapter)
    if a.write:
        for rel, content in outputs.items():
            p = ROOT / rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(content, encoding="utf-8"); print(rel)
    else:
        print(json.dumps(resolve_sources(a.chapter, a.mtl_chapter), ensure_ascii=False, indent=2))
if __name__ == "__main__": main()
