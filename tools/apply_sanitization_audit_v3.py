"""Final sanitation reacceptance wrapper with normalized review file endings."""
from __future__ import annotations

import argparse
import json
import subprocess

from tools import apply_sanitization_audit as base
from tools import apply_sanitization_audit_v2 as v2
from tools.build_editorial_draft import acceptance_context, render

ROOT = base.ROOT


def load(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def save(path: str, value):
    (ROOT / path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def normalize_and_rebind():
    for chapter in base.CORRECTIONS:
        qa = load(f"qa/chapter-{chapter:04d}.json")
        review_path = v2.chapter_review_path(chapter, qa)
        path = ROOT / review_path
        path.write_text(path.read_text(encoding="utf-8").rstrip() + "\n", encoding="utf-8")

    for chapter in base.CORRECTIONS:
        spec = load(f"editorial/edits/chapter-{chapter:04d}.json")
        qa = load(f"qa/chapter-{chapter:04d}.json")
        alignment = load(spec["korean_alignment"]) if spec.get("korean_alignment") else None
        outputs = render(chapter, validate_acceptance=False)
        draft_path = f"manuscript/drafts/chapter-{chapter:04d}.md"
        text = outputs[draft_path]
        record = acceptance_context(chapter, spec, qa, text, alignment)
        record.update({
            "review_date": base.DATE,
            "reviewer": base.REVIEWER,
            "release_status": qa.get("release_status", "epub_not_built"),
        })
        save(f"qa/acceptance/chapter-{chapter:04d}.json", record)
        outputs = render(chapter, validate_acceptance=True)
        for name, rendered in outputs.items():
            path = ROOT / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(rendered, encoding="utf-8")

    subprocess.run(["python", "tools/rebuild_editorial_tracking.py"], cwd=ROOT, check=True)


def apply():
    v2.apply()
    normalize_and_rebind()
    print("Sanitization corrections finalized with normalized review evidence.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=("reopen", "apply"))
    args = parser.parse_args()
    if args.phase == "reopen":
        base.reopen()
    else:
        apply()


if __name__ == "__main__":
    main()
