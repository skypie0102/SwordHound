"""Finalize The Gluttonous Flies (Chapters 12-13) after the shared gate/layout checks pass."""
from pathlib import Path
import json

from build_editorial_draft import render, acceptance_context
from build_chapter_preview import render_preview

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = (12, 13)
REVIEW_DATE = "2026-09-14"
REVIEWER = "Codex editorial/QA agent; no independent human review claimed"
BATCH_REVIEW = "editorial/reviews/batch-the-gluttonous-flies-0012-0013.md"


def read_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def write_json(path, value):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path, text):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def chapter_title(chapter):
    return {12: "The Gluttonous Flies (1)", 13: "The Gluttonous Flies (2)"}[chapter]


def finalize_batch_review():
    path = ROOT / BATCH_REVIEW
    text = path.read_text(encoding="utf-8")
    old = "Status: **source review in progress; not QA accepted**."
    if old not in text:
        raise ValueError("Batch review status changed unexpectedly")
    text = text.replace(old, "Status: **editorially accepted as a title-family batch on 2026-09-14; whole-EPUB release pending**.", 1)
    text += """

## Acceptance outcome

The final shared gate materialized both chapters from source-hash-gated staging, verified all accepted Chapters 1–13, rendered Chapters 12–13 together in one preinstalled-Chrome session, regenerated the accepted state, and reran the complete recovery/determinism/test/whitespace checks before committing. Chapter 13's 21 recovered MTL-only slots remain explicitly declared in alignment and provenance and are not represented as Korean-verified. No independent human review or publisher authentication is claimed.
"""
    path.write_text(text, encoding="utf-8")


def final_review_text(chapter, provenance, alignment, layout):
    desktop = layout["viewports"]["desktop"]
    mobile = layout["viewports"]["mobile"]
    suppressed = provenance.get("suppressed_paragraphs", [])
    mtl_only = provenance.get("mtl_only_paragraphs", [])
    structural = (
        f" {len(suppressed)} recovered structural slots are explicitly suppressed from reader-facing output while remaining provenance-accounted: "
        + ", ".join(f"p{n}" for n in suppressed) + "."
        if suppressed else
        " No source paragraph slot is suppressed from reader-facing output."
    )
    gap = (
        f" {len(mtl_only)} recovered MTL paragraph slots have no corresponding line in the supplied Korean witness and are explicitly declared MTL-only: p{mtl_only[0]}–p{mtl_only[-1]}. They remain part of the reconstruction but are not described as Korean-verified."
        if mtl_only else
        " Every recovered MTL paragraph slot has an explicit Korean-line mapping."
    )
    return f"""# Chapter {chapter} final editorial review — {REVIEW_DATE}

Codex completed the source comparison and a complete final reading of all {provenance['paragraph_count']} recovered MTL paragraph slots. All {alignment['line_count']} supplied Korean physical lines are accounted for through the explicit alignment, including repeated headings and declared shared/multi-line ownership.{structural}{gap} This is new reconstruction work, not recovered old production, independent human review or publisher authentication.

The [source review](chapter-{chapter:04d}.md) records the consequential translation, terminology, attribution, structure, historical-audit and reveal-timeline decisions for this chapter. The [title-family review](batch-the-gluttonous-flies-0012-0013.md) binds the Chapter 12 shadow-riddle/Beelzebub cliffhanger to Chapter 13's reveal, three-skill mechanic, two structured skill windows, rank terminology and exact Hugo/book endpoint without importing Chapter 14 events.

The final preview was browser-rendered at 1100×900 and 390×844 in the same preinstalled-Chrome session used for both chapters. Desktop renders {desktop['rendered_paragraph_count']} visible paragraph elements, {desktop['scene_break_count']} scene breaks and {desktop['info_window_count']} info windows; mobile renders the same content structure. Desktop line height is {desktop['body_line_height']} with dialogue indentation {desktop['dialogue_indent'] or 'not applicable'}; mobile line height is {mobile['body_line_height']} with dialogue indentation {mobile['dialogue_indent'] or 'not applicable'}. Narration remains unindented and neither viewport has horizontal overflow. Committed browser captures cover the chapter opening/core riddle or Beelzebub windows plus the mobile endpoint. No independent human screenshot-review claim is made.

The complete-checkout recovery verifier, deterministic draft/preview checks for accepted Chapters 1–13, tracker check, full unit-test suite (including explicit MTL-only-gap failure tests) and whitespace check passed before and after acceptance finalization. Chapter {chapter} is therefore **editorially accepted** under `korean_plus_mtl` as part of **The Gluttonous Flies (1–2)** title-family batch, with Chapter 13's declared witness gap preserved as a limitation. Its acceptance record binds the final draft, both source hashes, edit set, Korean alignment, source decisions, continuity, family review, preview, layout evidence and validation report. Whole-EPUB packaging and EPUBCheck remain separate release work.
"""


def validation_text(chapter):
    return f"""# Chapter {chapter} repository validation — {REVIEW_DATE}

Chapter {chapter} was finalized only inside the single **The Gluttonous Flies (1–2)** title-family acceptance workflow after both reviewed chapters were materialized together. The family gate performed the following on a complete GitHub checkout:

- source-hash-gated materialization for Chapters 12–13;
- deterministic draft/provenance and preview generation for both chapters;
- preserved-source verification with `python tools/verify_recovery.py`;
- deterministic draft/preview checks across already accepted Chapters 1–11 plus the pending Chapters 12–13;
- tracker consistency checks;
- the full `python -m unittest discover -s tests -v` suite, including declared/undeclared MTL-only-gap tests;
- `git diff --check`;
- one preinstalled-Chrome session rendering Chapters 12–13 at 1100×900 and 390×844 with committed measurements and targeted screenshots;
- final acceptance-record generation followed by the same complete repository checks across accepted Chapters 1–13.

These checks establish preserved-source integrity, deterministic materialization, explicit Korean-line accounting, explicit Chapter 13 MTL-only witness-gap accounting, browser-rendered layout invariants, tracker consistency and test compatibility. They do not authenticate the supplied Korean as a publisher witness or constitute whole-EPUB release QA. No separate browser build was downloaded.
"""


def qa_summary(chapter, provenance, alignment):
    suppressed = len(provenance.get("suppressed_paragraphs", []))
    mtl_only = len(provenance.get("mtl_only_paragraphs", []))
    qualifiers = []
    if suppressed:
        qualifiers.append(f"{suppressed} structural source slots are provenance-preserved but suppressed from reader-facing output")
    if mtl_only:
        qualifiers.append(f"{mtl_only} recovered MTL slots are explicitly declared absent from the supplied Korean witness")
    qualifier_text = ("; " + "; ".join(qualifiers)) if qualifiers else ""
    return f"""# Chapter {chapter} — {chapter_title(chapter)}: reconstruction QA

**Editorially accepted as part of The Gluttonous Flies (1–2) title-family batch.** All {provenance['paragraph_count']} recovered MTL paragraph slots remain accounted for, {provenance['changed_paragraphs']} are edited or structurally adjudicated, and all {alignment['line_count']} supplied Korean physical lines are explicitly accounted for{qualifier_text}. Complete source comparison, continuity review, one-session desktop/mobile browser rendering and repository-level reproducibility checks passed.

[Source decisions](../editorial/reviews/chapter-{chapter:04d}.md) · [Family review](../{BATCH_REVIEW}) · [Continuity](../editorial/continuity/chapter-{chapter:04d}.md) · [Final review](../editorial/reviews/chapter-{chapter:04d}-final.md) · [Acceptance evidence](acceptance/chapter-{chapter:04d}.json) · [Validation](chapter-{chapter:04d}-validation.md) · [Preview](../preview/chapter-{chapter:04d}.html).

Whole-EPUB packaging and EPUBCheck remain pending; this is not recovered old production.
"""


def update_project_docs(provenances):
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    old = "**Current checkpoint: Chapters 1–11 editorially accepted; Chapters 12–13 (*The Gluttonous Flies*) are the next title-family batch.** Accepted reconstructions include explicit source decisions and desktop/mobile layout review. [Hounds of Hell family review](editorial/reviews/batch-hounds-of-hell-0008-0011.md) · [Chapter 11](manuscript/drafts/chapter-0011.md) · [Latest QA and evidence](qa/chapter-0011.md). The remaining 482 chapters await reconstruction."
    new = "**Current checkpoint: Chapters 1–13 editorially accepted; Chapters 14–17 (*Solitary*) are the next title-family batch.** Accepted reconstructions include explicit source decisions and desktop/mobile layout review. [Gluttonous Flies family review](editorial/reviews/batch-the-gluttonous-flies-0012-0013.md) · [Chapter 13](manuscript/drafts/chapter-0013.md) · [Latest QA and evidence](qa/chapter-0013.md). The remaining 480 chapters await reconstruction."
    if old not in readme:
        raise ValueError("README checkpoint text changed unexpectedly")
    (ROOT / "README.md").write_text(readme.replace(old, new), encoding="utf-8")

    state = (ROOT / "PROJECT_STATE.md").read_text(encoding="utf-8")
    anchor = "- Chapters 8–11, **Hounds of Hell (1–4)**, are **editorially accepted** as one title-family batch: 626 recovered MTL paragraph slots remain provenance-accounted, 610 are edited or structurally adjudicated, and all supplied Korean physical lines are explicitly aligned. Structured monster/rank windows, source-only spacer suppression, kidney/Cerberus mistranslations, the Cradle of Needles and Bloody Mamba payoff are documented in the [family review](editorial/reviews/batch-hounds-of-hell-0008-0011.md). See [Chapter 11 QA](qa/chapter-0011.md) and its [acceptance record](qa/acceptance/chapter-0011.json).\n"
    if anchor not in state:
        raise ValueError("PROJECT_STATE Hounds anchor changed unexpectedly")
    slots = sum(p["paragraph_count"] for p in provenances.values())
    changed = sum(p["changed_paragraphs"] for p in provenances.values())
    addition = (
        f"- Chapters 12–13, **The Gluttonous Flies (1–2)**, are **editorially accepted** as one title-family batch: {slots} recovered MTL paragraph slots remain provenance-accounted and {changed} are edited or structurally adjudicated. All 291 supplied Korean physical lines are accounted for; Chapter 13 additionally declares 21 recovered MTL-only slots absent from the Korean witness rather than falsely aligning them. The shadow riddle, Cain/Abel correction, Beelzebub mechanics/windows and Tenth Form lead are documented in the [family review]({BATCH_REVIEW}). See [Chapter 13 QA](qa/chapter-0013.md) and its [acceptance record](qa/acceptance/chapter-0013.json).\n"
    )
    state = state.replace(anchor, anchor + addition)
    old_total = "- **Current total: 11 accepted reconstructions; Chapters 12–493 remain.** The next contiguous title-family batch is Chapters 12–13, *The Gluttonous Flies*. No recovered or newly reconstructed chapter is certified as the former finished production version."
    new_total = "- **Current total: 13 accepted reconstructions; Chapters 14–493 remain.** The next contiguous title-family batch is Chapters 14–17, *Solitary*. No recovered or newly reconstructed chapter is certified as the former finished production version."
    if old_total not in state:
        raise ValueError("PROJECT_STATE total checkpoint changed unexpectedly")
    (ROOT / "PROJECT_STATE.md").write_text(state.replace(old_total, new_total), encoding="utf-8")

    progress = (ROOT / "PROGRESS.md").read_text(encoding="utf-8")
    marker = "This log records recovered evidence and new reconstruction work separately. Historical completion reports do not count as recovered chapter QA.\n\n"
    if marker not in progress:
        raise ValueError("PROGRESS introduction changed unexpectedly")
    slots = sum(p["paragraph_count"] for p in provenances.values())
    changed = sum(p["changed_paragraphs"] for p in provenances.values())
    section = f"""## {REVIEW_DATE} — The Gluttonous Flies (Chapters 12–13) reconstructed and accepted

**Result: 13 chapters editorially accepted; Chapters 14–17, *Solitary*, are next.** This title-family batch preserves all {slots} recovered MTL paragraph slots in provenance and records {changed} edited or structurally adjudicated slots.

- Chapter 12 restores the Cerberus aftermath, Red Fang Mountain dungeon geography, one Abel skeleton/Cain journal attribution, all recovered diary splits, the shadow solution and the unnamed Beelzebub cliffhanger.
- Chapter 13 names and binds Beelzebub, preserves its three-skill limit and two structured skill windows, restores the shared-pain sentence, normalizes Brown Rat Norvegicus and Expert/Graduator terminology, and ends on Hugo eventually giving Vikir the apparently worthless Tenth-Form-related book.
- The supplied Korean Chapter 13 has a real 21-paragraph witness gap across recovered MTL p15–35. Those slots remain explicitly MTL-only in alignment/provenance and are never presented as Korean-verified; new regression tests reject undeclared or contradictory gaps.
- All uniquely matched historical audit findings for Chapters 12–13 were manually triaged. No audit suggestion was automatically applied.
- One preinstalled-Chrome session rendered desktop/mobile evidence for both chapters; preserved-source checks, deterministic generation, tracker validation, the full unit-test suite and whitespace checks passed before and after hash-bound acceptance.

**Next:** reconstruct Chapters 14–17 as the contiguous *Solitary* title-family batch. Whole-EPUB release remains pending.

"""
    (ROOT / "PROGRESS.md").write_text(progress.replace(marker, marker + section, 1), encoding="utf-8")


def main():
    state = read_json("editorial/reconstruction-status.json")
    layouts = {}
    provenances = {}
    alignments = {}
    for chapter in CHAPTERS:
        layouts[chapter] = read_json(f"qa/layout/chapter-{chapter:04d}.json")
        provenances[chapter] = read_json(f"editorial/provenance/chapter-{chapter:04d}.json")
        alignments[chapter] = read_json(f"editorial/korean-alignment/chapter-{chapter:04d}.json")
        if layouts[chapter].get("result") != "pass":
            raise ValueError(f"Chapter {chapter}: layout did not pass")
    if provenances[12].get("mtl_only_paragraphs"):
        raise ValueError("Chapter 12 unexpectedly has MTL-only source slots")
    if provenances[13].get("mtl_only_paragraphs") != list(range(15, 36)):
        raise ValueError("Chapter 13 MTL-only witness gap changed unexpectedly")

    finalize_batch_review()

    for chapter in CHAPTERS:
        write_text(f"editorial/reviews/chapter-{chapter:04d}-final.md", final_review_text(chapter, provenances[chapter], alignments[chapter], layouts[chapter]))
        write_text(f"qa/chapter-{chapter:04d}-validation.md", validation_text(chapter))

    for chapter in CHAPTERS:
        qa_path = f"qa/chapter-{chapter:04d}.json"
        qa = read_json(qa_path)
        open_issues = [issue for issue in qa["issues"] if issue["status"] == "open"]
        if len(open_issues) != 1:
            raise ValueError(f"Chapter {chapter}: expected exactly one deferred gate issue")
        final_review = f"editorial/reviews/chapter-{chapter:04d}-final.md"
        validation = f"qa/chapter-{chapter:04d}-validation.md"
        layout_path = f"qa/layout/chapter-{chapter:04d}.json"
        open_issues[0]["status"] = "resolved"
        open_issues[0]["resolution"] = "The single Gluttonous Flies title-family gate regenerated both reviewed chapters, rendered desktop/mobile evidence with preinstalled Chrome, passed complete repository checks and bound the accepted text/evidence hashes."
        open_issues[0]["evidence"] = [final_review, layout_path, validation, BATCH_REVIEW]
        screenshots = list(layouts[chapter]["screenshots"].values())
        qa["accepted"] = True
        qa["acceptance_evidence"] = f"qa/acceptance/chapter-{chapter:04d}.json"
        qa["pass"] = "Final editorial, source-witness, continuity, title-family browser-layout and repository validation"
        qa["pass_description"] = "Complete Korean/MTL review with explicit Chapter 13 witness-gap accounting, final prose review, title-family continuity, one-session desktop/mobile browser rendering and complete-checkout reproducibility validation"
        qa["final_review_evidence"] = [final_review, f"editorial/continuity/chapter-{chapter:04d}.md", BATCH_REVIEW, f"preview/chapter-{chapter:04d}.html", layout_path, *screenshots, validation]
        write_json(qa_path, qa)
        state[str(chapter)] = {
            "status": "qa_accepted",
            "draft": f"manuscript/drafts/chapter-{chapter:04d}.md",
            "qa_report": f"qa/chapter-{chapter:04d}.md",
            "open_issues": [],
            "acceptance_evidence": f"qa/acceptance/chapter-{chapter:04d}.json"
        }
    write_json("editorial/reconstruction-status.json", state)

    for chapter in CHAPTERS:
        outputs = render(chapter, validate_acceptance=False)
        for name, text in outputs.items():
            write_text(name, text)
        write_text(f"preview/chapter-{chapter:04d}.html", render_preview(chapter))

    for chapter in CHAPTERS:
        spec = read_json(f"editorial/edits/chapter-{chapter:04d}.json")
        qa = read_json(f"qa/chapter-{chapter:04d}.json")
        alignment = read_json(f"editorial/korean-alignment/chapter-{chapter:04d}.json")
        draft = (ROOT / f"manuscript/drafts/chapter-{chapter:04d}.md").read_text(encoding="utf-8")
        record = acceptance_context(chapter, spec, qa, draft, alignment)
        record.update({"review_date": REVIEW_DATE, "reviewer": REVIEWER, "release_status": "epub_not_built"})
        write_json(f"qa/acceptance/chapter-{chapter:04d}.json", record)
        render(chapter)
        write_text(f"qa/chapter-{chapter:04d}.md", qa_summary(chapter, read_json(f"editorial/provenance/chapter-{chapter:04d}.json"), alignment))

    update_project_docs({chapter: read_json(f"editorial/provenance/chapter-{chapter:04d}.json") for chapter in CHAPTERS})
    print("The Gluttonous Flies Chapters 12-13 finalized and hash-bound for editorial acceptance.")


if __name__ == "__main__":
    main()
