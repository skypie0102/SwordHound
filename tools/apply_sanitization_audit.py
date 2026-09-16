"""Reopen, correct, regenerate, and re-accept sanitation fixes for accepted chapters."""
from __future__ import annotations

from pathlib import Path
import argparse
import json
import subprocess

from tools.build_editorial_draft import acceptance_context, render

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-16"
REVIEWER = "Codex editorial/QA agent; sanitation fidelity re-review; no independent human review claimed"
AUDIT_MD = "editorial/reviews/sanitization-audit-0001-0013.md"
AUDIT_JSON = "editorial/reviews/sanitization-corrections-0001-0013.json"

CORRECTIONS = {
    1: {
        75: (
            "What could have startled the family’s normally unshakable guardian knights?",
            "What could have made the family’s normally unshakable guardian knights tremble in fear?",
            "Sanitization re-review: Korean explicitly describes the guardian knights trembling in fear; restore the full reaction instead of the softened 'startled'.",
        ),
        88: (
            "His knees were bruised, and his soft palms were already bloody.",
            "His knees were covered in scrapes, and his small hands were already covered in blood.",
            "Sanitization re-review: Korean specifies abrasion-covered knees and hands already covered in blood; restore the injury type and source intensity.",
        ),
    },
    2: {
        4: (
            "Not a trace remained of the aura he had built up through countless battles.",
            "Not a trace remained of the aura he had built up while repeatedly hovering at death’s door and coughing up blood.",
            "Sanitization re-review: restore the Korean's explicit repeated near-death ordeals and coughing/spitting up blood.",
        ),
    },
    8: {
        12: (
            "Tough, sinewy cuts of meat were simmered in broth made from chicken bones until everything softened into a thick mash.",
            "Various kinds of tough, sinewy offal were simmered in chicken-bone broth until everything softened into a thick mash.",
            "Sanitization re-review: Korean explicitly says various kinds of offal/internal organs; do not generalize this to ordinary cuts of meat.",
        ),
    },
    10: {
        24: (
            "Its heart hammered as though it might burst, and the blood vessels in its eyes swelled red.",
            "Its heart hammered as though it might burst, and its bloodshot eyes looked ready to burst as well.",
            "Sanitization re-review: Korean applies the bursting image to the bloodshot eyes as well as the heart.",
        ),
    },
    11: {
        144: (
            "They drove into its body and opened serious wounds.",
            "They drove into its body and opened grievous, potentially fatal wounds.",
            "Sanitization re-review: Korean uses 치명적인; restore the potentially fatal severity without falsely claiming Cerberus dies at this instant.",
        ),
    },
    13: {
        67: (
            "Blood and bodily fluids flowed through Beelzebub’s hollow stinger and into Vikir.",
            "Blood and fluids from its organs flowed through Beelzebub’s hollow stinger and into Vikir.",
            "Sanitization re-review: Korean specifically says blood and organ/internal-organ fluids.",
        ),
        68: (
            "The gnawing hunger inside him eased, his cramped stomach gradually settling.",
            "His starving intestines filled, and the organs twisted by hunger gradually settled back into place.",
            "Sanitization re-review: restore the explicit Korean description of filling intestines and twisted internal organs returning to position.",
        ),
        74: (
            "When Beelzebub had been alive, the scope of that absorption had been nearly limitless, leaving countless victims stripped of achievements they had spent their entire lives building.",
            "When Beelzebub had been alive, the scope of that absorption had been nearly limitless, leaving countless victims stripped of abilities they had spent their entire lives building, powerless and disabled.",
            "Sanitization re-review: restore the Korean consequence that victims were left powerless/incapacitated and disabled.",
        ),
        109: (
            "Then Beelzebub drove its stinger into Cerberus’s corpse and began greedily drinking from its flesh and organs.",
            "Then Beelzebub drove its stinger into Cerberus’s corpse and began voraciously devouring its flesh and entrails.",
            "Sanitization re-review: restore the source's deliberately visceral flesh/entrails wording and voracious-devouring action.",
        ),
    },
}


def load(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def save(path: str, value):
    (ROOT / path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def issue_id(chapter: int) -> str:
    return f"CH{chapter:03d}-SANITIZATION"


def current_paragraph(spec, chapter: int, paragraph: int) -> str:
    edits = {n: replacement for n, replacement, _ in spec["edits"]}
    if paragraph in edits:
        return edits[paragraph]
    # Use the already accepted draft for unchanged source paragraphs.
    draft = (ROOT / f"manuscript/drafts/chapter-{chapter:04d}.md").read_text(encoding="utf-8")
    marker = f"<!-- source-p:{paragraph:03d} -->\n"
    tail = draft.split(marker, 1)[1]
    return tail.split("\n\n", 1)[0]


def ensure_policy_text():
    agents = ROOT / "AGENTS.md"
    text = agents.read_text(encoding="utf-8")
    needle = "- **Editorial work comes first.** During chapter processing, prioritize translation fidelity, grammar, awkward wording, mistranslations, names/terms, speaker attribution, continuity, chronology, information-window content/structure, scene-break semantics, source alignment, paragraph provenance, historical-audit triage, and readable final prose.\n"
    addition = needle + "- **Do not sanitize the source.** Preserve the source's actual force and specificity, including violence, gore, profanity, anatomical language, degradation, sexual material, and other harsh content when present. Do not euphemize, generalize, omit, or soften it for palatability; equally, do not intensify beyond the evidence.\n"
    if "**Do not sanitize the source.**" not in text:
        if needle not in text:
            raise RuntimeError("AGENTS editorial-policy anchor changed")
        agents.write_text(text.replace(needle, addition, 1), encoding="utf-8")

    workflow = ROOT / "editorial/WORKFLOW.md"
    text = workflow.read_text(encoding="utf-8")
    needle = "2. Read the entire chapter. Make explicit English edits and record the reason for each. Prioritize translation fidelity, grammar, awkward wording, mistranslations, names/terms, speaker attribution, chronology, information-window content/structure, scene-break meaning, and natural prose.\n"
    replacement = needle + "   - Preserve the source's actual intensity and specificity. Do not sanitize violence, gore, profanity, anatomical language, degradation, sexual material, or other harsh content; do not euphemize or omit it for palatability, and do not intensify beyond what the evidence supports.\n"
    if "Preserve the source's actual intensity and specificity" not in text:
        if needle not in text:
            raise RuntimeError("WORKFLOW procedure anchor changed")
        workflow.write_text(text.replace(needle, replacement, 1), encoding="utf-8")


def reopen():
    state = load("editorial/reconstruction-status.json")
    for chapter, corrections in CORRECTIONS.items():
        qa_path = f"qa/chapter-{chapter:04d}.json"
        qa = load(qa_path)
        if not qa.get("accepted"):
            raise RuntimeError(f"Chapter {chapter} was not accepted before reopening")
        iid = issue_id(chapter)
        if any(issue["id"] == iid for issue in qa["issues"]):
            raise RuntimeError(f"Chapter {chapter} already has sanitation issue")
        qa["accepted"] = False
        qa["review_date"] = DATE
        qa["pass"] = "Reopened for sanitation/fidelity re-review against the supplied Korean witness"
        qa["issues"].append({
            "id": iid,
            "status": "open",
            "paragraphs": sorted(corrections),
            "question": "Sanitization / source-intensity fidelity re-review",
            "required_evidence": "Compare the accepted English against the supplied Korean and restore any softened, generalized, euphemized, or omitted source detail without gratuitous intensification.",
        })
        save(qa_path, qa)
        state[str(chapter)]["status"] = "qa_pending"
        state[str(chapter)]["open_issues"] = [iid]
    save("editorial/reconstruction-status.json", state)
    print("Reopened chapters:", ", ".join(map(str, CORRECTIONS)))


def apply_corrections():
    state = load("editorial/reconstruction-status.json")

    # First modify the authoritative edit sets and resolve the reopened QA issue.
    for chapter, corrections in CORRECTIONS.items():
        spec_path = f"editorial/edits/chapter-{chapter:04d}.json"
        spec = load(spec_path)
        edit_index = {row[0]: i for i, row in enumerate(spec["edits"])}
        for paragraph, (expected, replacement, reason) in corrections.items():
            actual = current_paragraph(spec, chapter, paragraph)
            if actual != expected:
                raise RuntimeError(f"Chapter {chapter} paragraph {paragraph} changed unexpectedly:\nEXPECTED {expected!r}\nACTUAL   {actual!r}")
            row = [paragraph, replacement, reason]
            if paragraph in edit_index:
                spec["edits"][edit_index[paragraph]] = row
            else:
                spec["edits"].append(row)
        spec["edits"].sort(key=lambda row: row[0])
        save(spec_path, spec)

        qa_path = f"qa/chapter-{chapter:04d}.json"
        qa = load(qa_path)
        iid = issue_id(chapter)
        issue = next(issue for issue in qa["issues"] if issue["id"] == iid)
        issue["status"] = "resolved"
        issue["resolution"] = "Restored every sanitation/fidelity softening identified in the accepted text for this chapter against the supplied Korean witness. The replacement wording preserves source force and specificity without adding unsupported intensity."
        issue["evidence"] = [AUDIT_MD, AUDIT_JSON, f"editorial/korean-alignment/chapter-{chapter:04d}.json"]
        qa["pass"] = "Sanitization/fidelity re-review, corrected edit-source regeneration, complete deterministic QA, and editorial re-acceptance"
        qa["final_review_evidence"] = list(dict.fromkeys(qa.get("final_review_evidence", []) + [AUDIT_MD, AUDIT_JSON]))
        save(qa_path, qa)
        state[str(chapter)]["open_issues"] = []
    save("editorial/reconstruction-status.json", state)

    ensure_policy_text()

    # Regenerate once while QA is reopened, proving the manuscript derives from edit sources.
    for chapter in CORRECTIONS:
        outputs = render(chapter, validate_acceptance=False)
        for name, text in outputs.items():
            path = ROOT / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")

    # Re-accept, calculate new hash-bound evidence from the exact final accepted bytes,
    # then regenerate once more with acceptance validation enabled.
    for chapter in CORRECTIONS:
        qa_path = f"qa/chapter-{chapter:04d}.json"
        qa = load(qa_path)
        qa["accepted"] = True
        qa["review_date"] = DATE
        save(qa_path, qa)
        state[str(chapter)]["status"] = "qa_accepted"
    save("editorial/reconstruction-status.json", state)

    for chapter in CORRECTIONS:
        spec = load(f"editorial/edits/chapter-{chapter:04d}.json")
        qa = load(f"qa/chapter-{chapter:04d}.json")
        alignment = load(spec["korean_alignment"]) if spec.get("korean_alignment") else None
        outputs = render(chapter, validate_acceptance=False)
        draft_path = f"manuscript/drafts/chapter-{chapter:04d}.md"
        text = outputs[draft_path]
        record = acceptance_context(chapter, spec, qa, text, alignment)
        record.update({
            "review_date": DATE,
            "reviewer": REVIEWER,
            "release_status": qa.get("release_status", "epub_not_built"),
        })
        save(f"qa/acceptance/chapter-{chapter:04d}.json", record)

        outputs = render(chapter, validate_acceptance=True)
        for name, rendered in outputs.items():
            path = ROOT / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(rendered, encoding="utf-8")

    # Record the new acceptance checkpoint.
    progress = ROOT / "PROGRESS.md"
    text = progress.read_text(encoding="utf-8")
    heading = "## 2026-09-16 — Sanitization fidelity re-review and re-acceptance\n"
    if heading not in text:
        block = f"""{heading}\n**Result: Chapters 1, 2, 8, 10, 11, and 13 were formally reopened, corrected at the authoritative edit-source layer, regenerated, and re-accepted. The accepted chapter count remains 13; Chapters 14–17 remain editorially staged.**\n\n- Restored 10 localized source-intensity/fidelity details identified by the sanitation audit, including Chapter 2's near-death/blood imagery, Chapter 8's offal, Chapter 11's potentially fatal stake wounds, and Chapter 13's anatomical/Beelzebub feeding details.\n- Added a permanent no-sanitization rule to `AGENTS.md` and `editorial/WORKFLOW.md`: preserve source force and specificity without euphemizing, generalizing, omitting, or gratuitously intensifying harsh material.\n- Reopened the six accepted chapters before changing their edit sets, recorded a dedicated resolved QA issue in each chapter, regenerated manuscript/provenance from the edit specifications, and replaced stale acceptance records with new hash-bound evidence dated {DATE}.\n- The audit scope of Chapters 1–13 refers only to the chapters formally accepted by the newer reconstruction pipeline. The recovered repository still contains the full 493-chapter MTL corpus and older EPUB/editorial artifacts; those are separate from the current reconstruction-acceptance count.\n\n"""
        text = text.replace("# Project progress\n\n", "# Project progress\n\n" + block, 1)
        progress.write_text(text, encoding="utf-8")

    subprocess.run(["python", "tools/rebuild_editorial_tracking.py"], cwd=ROOT, check=True)
    print("Applied and re-accepted chapters:", ", ".join(map(str, CORRECTIONS)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=("reopen", "apply"))
    args = parser.parse_args()
    if args.phase == "reopen":
        reopen()
    else:
        apply_corrections()


if __name__ == "__main__":
    main()
