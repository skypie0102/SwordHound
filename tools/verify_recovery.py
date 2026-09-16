#!/usr/bin/env python3
"""Verify the active Chinese-first source baseline; not translation-quality certification."""
from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parents[1]; CHINESE=ROOT/"source/chinese/chapters"; EX=ROOT/"source/chinese/chapter-exceptions.tsv"; EN=ROOT/"source/chapters"
COMBINED={75:"075.txt",76:"075.txt",267:"267.txt",268:"267.txt",284:"284.txt",285:"284.txt",351:"351.txt",352:"351.txt",353:"353.txt",354:"353.txt",385:"385.txt",386:"385.txt",495:"495.txt",496:"495.txt"}
def fail(m): raise SystemExit("ERROR: "+m)
def main():
    actual={p.name for p in CHINESE.glob("*.txt")}
    if len(actual)!=492: fail(f"expected 492 Chinese files, found {len(actual)}")
    expected={f"{n:03d}.txt" for n in range(1,501)}; expected.discard("055.txt")
    for n,f in COMBINED.items():
        if n!=int(f[:3]): expected.discard(f"{n:03d}.txt")
    if actual!=expected: fail(f"Chinese corpus mismatch; missing={sorted(expected-actual)} extra={sorted(actual-expected)}")
    with EX.open(encoding="utf-8",newline="") as fh: rows={int(r["target_chapter"]):r for r in csv.DictReader(fh,delimiter="\t")}
    if rows.get(55,{}).get("raw_status")!="missing": fail("Chapter 55 missing declaration absent")
    for n,f in COMBINED.items():
        r=rows.get(n)
        if not r or r["raw_status"]!="combined" or r["raw_file"]!=f: fail(f"bad combined mapping for {n}")
    if len(list(EN.glob("chapter-*.xhtml")))!=493: fail("expected 493 English MTL chapter files")
    forbidden=[ROOT/"source/korean",ROOT/"archives/korean-raws-001-054.zip",ROOT/"recovery/korean-raws-manifest.json",ROOT/"editorial/korean-alignment",ROOT/"tools/import_korean_raws.py"]
    present=[str(p.relative_to(ROOT)) for p in forbidden if p.exists()]
    if present: fail(f"retired Korean artifacts still present: {present}")
    for n in range(1,501):
        if n==55:
            if not (EN/"chapter-055.xhtml").is_file(): fail("Chapter 55 English fallback missing")
        elif not (CHINESE/COMBINED.get(n,f"{n:03d}.txt")).is_file(): fail(f"target {n} has no Chinese container")
    print("Chinese-first source baseline: OK")
    print("500 targets; 499 Chinese-backed; Chapter 55 MTL-only; 7 combined containers.")
if __name__=="__main__": main()
