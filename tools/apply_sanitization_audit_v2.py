"""Run the sanitation reacceptance while binding evidence to existing chapter review fixtures."""
from __future__ import annotations

from pathlib import Path
import argparse
import json
import subprocess

from tools import apply_sanitization_audit as base
from tools.build_editorial_draft import acceptance_context, render

ROOT = base.ROOT


def load(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def save(path: str, value):
    (ROOT / path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def chapter_review_path(chapter: int, qa: dict) -> str:
    preferred = f"editorial/reviews/chapter-{chapter:04d}-final.md"
    if (ROOT / preferred).is_file():
        return preferred
    candidates = [
        p for p in qa.get("final_review_evidence", [])
        if p.startswith("editorial/reviews/") and p.endswith(".md") and (ROOT / p).is_file()
    ]
    if not candidates:
        raise RuntimeError(f"Chapter {chapter} has no existing final review evidence file")
    return candidates[0]


def append_review_addendum(chapter: int, review_path: str):
    path = ROOT / review_path
    text = path.read_text(encoding="utf-8")
    marker = "## 2026-09-16 sanitation fidelity re-review"
    if marker in text:
        return
    paragraphs = ", ".join(str(n) for n in sorted(base.CORRECTIONS[chapter]))
    addition = f"""

{marker}

The previously accepted English was rechecked specifically for source sanitization against the supplied Korean witness. Paragraph(s) {paragraphs} contained localized softening, generalization, or omission of source intensity/specificity. The authoritative edit set was corrected, the chapter was regenerated from source, the QA record was formally reopened and resolved, and new acceptance hashes were calculated. The correction standard is fidelity rather than gratuitous intensification: preserve the source's actual force and anatomical/violent specificity, but do not make it harsher than the evidence supports.

See `editorial/reviews/sanitization-audit-0001-0013.md` for the cross-chapter audit and `editorial/reviews/sanitization-corrections-0001-0013.json` for the exact replacements.
"""
    path.write_text(text.rstrip() + addition + "\n", encoding="utf-8")


def finalize_evidence_and_acceptance():
    for chapter in base.CORRECTIONS:
        qa_path = f"qa/chapter-{chapter:04d}.json"
        qa = load(qa_path)
        review_path = chapter_review_path(chapter, qa)
        append_review_addendum(chapter, review_path)

        iid = base.issue_id(chapter)
        issue = next(i for i in qa["issues"] if i["id"] == iid)
        issue["evidence"] = [
            review_path,
            f"editorial/korean-alignment/chapter-{chapter:04d}.json",
        ]
        qa["final_review_evidence"] = [
            p for p in qa.get("final_review_evidence", [])
            if p not in (base.AUDIT_MD, base.AUDIT_JSON)
        ]
        save(qa_path, qa)

    # Rebind acceptance hashes after the evidence paths and chapter review addenda change.
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
    base.apply_corrections()
    finalize_evidence_and_acceptance()
    print("Sanitization corrections finalized with chapter-local QA evidence.")


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
