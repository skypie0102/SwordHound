#!/usr/bin/env python3
"""Rebuild the 500-chapter Chinese-first reconstruction tracker."""
from __future__ import annotations
import csv, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
EXCEPTIONS = ROOT / "source/chinese/chapter-exceptions.tsv"

def exceptions():
    with EXCEPTIONS.open(encoding="utf-8", newline="") as fh:
        return {int(r["target_chapter"]):r for r in csv.DictReader(fh, delimiter="\t")}

def build():
    ex=exceptions(); chapters=[]; accepted=[]; staged=[]
    for n in range(1,501):
        r=ex.get(n); status=r["raw_status"] if r else "single"; raw=None if status=="missing" else (r["raw_file"] if r and r["raw_file"] else f"{n:03d}.txt")
        draft=ROOT/f"manuscript/drafts/chapter-{n:04d}.md"; acc=ROOT/f"qa/acceptance/chapter-{n:04d}.json"; stage=ROOT/f"editorial/staging/chapter-{n:04d}-sources.json"
        state="unstarted"
        if draft.exists() or stage.exists(): state="draft"; staged.append(n)
        if acc.exists() and json.loads(acc.read_text(encoding="utf-8")).get("accepted") is True: state="qa_accepted"; accepted.append(n)
        m=int(r["verified_english_mtl_chapter"]) if r and r["verified_english_mtl_chapter"].strip() else None
        chapters.append({"chapter":n,"reconstruction_status":state,"primary_source":None if raw is None else f"source/chinese/chapters/{raw}","raw_status":status,"english_mtl_reference":f"source/chapters/chapter-{m:03d}.xhtml" if m else None,"english_mtl_alignment":"verified_exception_table" if m else "align_by_title_and_content_before_use","draft":f"manuscript/drafts/chapter-{n:04d}.md" if draft.exists() else None})
    next_ch=next((n for n in range(1,501) if n not in accepted),None)
    tracker={"notice":"Chinese-first tracker; prior Korean-assisted state superseded.","target_chapter_count":500,"accepted_count":len(accepted),"next_chapter":next_ch,"chapters":chapters}
    status={"checkpoint_policy":"chinese_primary_2026-09-16","target_chapters":500,"accepted_chapters":len(accepted),"accepted":accepted,"staged_or_draft":sorted(set(staged)-set(accepted)),"next_chapter":next_ch,"missing_chinese_raw_chapters":[55],"combined_raw_containers":{"075.txt":[75,76],"267.txt":[267,268],"284.txt":[284,285],"351.txt":[351,352],"353.txt":[353,354],"385.txt":[385,386],"495.txt":[495,496]}}
    return tracker,status

def main():
    t,s=build(); (ROOT/"editorial/chapter-tracker.json").write_text(json.dumps(t,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); (ROOT/"editorial/reconstruction-status.json").write_text(json.dumps(s,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(f"accepted={t['accepted_count']} next={t['next_chapter']}")
if __name__=="__main__": main()
