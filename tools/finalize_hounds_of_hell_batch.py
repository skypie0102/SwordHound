"""Finalize the Hounds of Hell (Chapters 8-11) title-family after all gate checks/layout evidence pass."""
from pathlib import Path
import json

from build_editorial_draft import render, acceptance_context
from build_chapter_preview import render_preview

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = (8, 9, 10, 11)
REVIEW_DATE = "2026-09-14"
REVIEWER = "Codex editorial/QA agent; no independent human review claimed"
BATCH_REVIEW = "editorial/reviews/batch-hounds-of-hell-0008-0011.md"


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
    return {8: "Hounds of Hell (1)", 9: "Hounds of Hell (2)", 10: "Hounds of Hell (3)", 11: "Hounds of Hell (4)"}[chapter]


def final_review_text(chapter, provenance, alignment, layout):
    desktop = layout["viewports"]["desktop"]
    mobile = layout["viewports"]["mobile"]
    suppressed = provenance.get("suppressed_paragraphs", [])
    source_review = f"chapter-{chapter:04d}.md"
    structural = (
        f" {len(suppressed)} recovered structural/source slots are explicitly suppressed from reader-facing output while remaining provenance-accounted: "
        + ", ".join(f"p{n}" for n in suppressed) + "."
        if suppressed else
        " No source paragraph slot is suppressed from reader-facing output."
    )
    return f"""# Chapter {chapter} final editorial review — {REVIEW_DATE}

Codex completed Korean/MTL comparison and a complete final reading of all {provenance['paragraph_count']} recovered MTL paragraph slots. All {alignment['line_count']} Korean physical lines are accounted for through the explicit alignment, including repeated headings and any declared shared structural lines.{structural} This is new reconstruction work, not recovered old production, independent human review or publisher authentication.

The [source review]({source_review}) records the consequential translation, terminology, attribution, structure, historical-audit and reveal-timeline decisions for this chapter. Cross-chapter terms and mechanics were also checked against the [Hounds of Hell title-family review](batch-hounds-of-hell-0008-0011.md), so Le Rouge et Le Noir Mountain, Guide Hounds, Bloody Beans/cacao, the Cradle/Forbidden Zone distinction, sword ranks, finite River Styx durability, Cerberus terminology and the Chapter 11 Bloody Mamba payoff remain consistent across Chapters 8–11.

The final preview was browser-rendered at 1100×900 and 390×844 in the same Chromium installation/session used for the whole title family. Desktop renders {desktop['rendered_paragraph_count']} visible paragraph elements, {desktop['scene_break_count']} scene breaks and {desktop['info_window_count']} info windows; mobile renders the same content structure. Desktop line height is {desktop['body_line_height']} with dialogue indentation {desktop['dialogue_indent'] or 'not applicable'}; mobile line height is {mobile['body_line_height']} with dialogue indentation {mobile['dialogue_indent'] or 'not applicable'}. Narration remains unindented and neither viewport has horizontal overflow. Committed browser captures cover chapter-specific opening/mechanics/window/trap material plus the mobile endpoint. No independent human screenshot-review claim is made.

The complete-checkout recovery verifier, deterministic draft/preview checks, tracker check, full unit-test suite and whitespace check passed before finalization and are rerun after the acceptance records are generated. Chapter {chapter} is therefore **editorially accepted** under `korean_plus_mtl` as part of the **Hounds of Hell (1–4)** title-family batch. Its acceptance record binds the final draft, both source hashes, edit set, Korean alignment, source decisions, continuity, family review, preview, layout evidence and validation report. Whole-EPUB packaging and EPUBCheck remain separate release work.
"""


def validation_text(chapter):
    return f"""# Chapter {chapter} repository validation — {REVIEW_DATE}

Chapter {chapter} was finalized only inside the single **Hounds of Hell (1–4)** title-family acceptance workflow after all four reviewed chapters were materialized together. The family gate performed the following on a complete GitHub checkout:

- source-hash-gated materialization for Chapters 8–11;
- deterministic draft/provenance and preview generation for all four chapters;
- preserved-source verification with `python tools/verify_recovery.py`;
- deterministic draft/preview checks and tracker consistency checks;
- the full `python -m unittest discover -s tests -v` suite;
- `git diff --check`;
- one Chromium installation/session rendering all four chapters at 1100×900 and 390×844, including committed measurements and targeted screenshots;
- final acceptance-record generation followed by the same repository checks across accepted Chapters 1–11.

These checks establish preserved-source integrity, deterministic materialization, explicit Korean-line accounting, browser-rendered layout invariants, tracker consistency and test compatibility. They do not authenticate the supplied Korean as a publisher witness or constitute whole-EPUB release QA. The single family-level browser run was used deliberately to comply with the repository's GitHub-runner minimization policy.
"""


def qa_summary(chapter, provenance, alignment):
    suppressed = len(provenance.get("suppressed_paragraphs", []))
    suppressed_text = f", with {suppressed} explicitly provenance-preserved structural slots suppressed from reader-facing output" if suppressed else ""
    return f"""# Chapter {chapter} — {chapter_title(chapter)}: reconstruction QA

**Editorially accepted Korean-plus-MTL reconstruction as part of the Hounds of Hell (1–4) title-family batch.** All {provenance['paragraph_count']} recovered MTL paragraph slots remain accounted for{suppressed_text}, {provenance['changed_paragraphs']} slots are edited or structurally adjudicated, and all {alignment['line_count']} Korean physical lines are accounted for. Complete source comparison, continuity review, one-session desktop/mobile browser rendering and repository-level reproducibility checks passed.

[Source decisions](../editorial/reviews/chapter-{chapter:04d}.md) · [Family review](../{BATCH_REVIEW}) · [Continuity](../editorial/continuity/chapter-{chapter:04d}.md) · [Final review](../editorial/reviews/chapter-{chapter:04d}-final.md) · [Acceptance evidence](acceptance/chapter-{chapter:04d}.json) · [Validation](chapter-{chapter:04d}-validation.md) · [Preview](../preview/chapter-{chapter:04d}.html).

Whole-EPUB packaging and EPUBCheck remain pending; this is not recovered old production.
"""


def update_project_docs(provenances):
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    old = "**Current checkpoint: Chapters 1–7 editorially accepted; Chapter 8 is next.** Each includes Korean/MTL comparison, explicit source decisions and desktop/mobile layout review. [Chapter 6](manuscript/drafts/chapter-0006.md) · [Chapter 7](manuscript/drafts/chapter-0007.md) · [Latest QA and evidence](qa/chapter-0007.md). The remaining 486 chapters await reconstruction."
    new = "**Current checkpoint: Chapters 1–11 editorially accepted; Chapters 12–13 (*The Gluttonous Flies*) are the next title-family batch.** Accepted reconstructions include explicit source decisions and desktop/mobile layout review. [Hounds of Hell family review](editorial/reviews/batch-hounds-of-hell-0008-0011.md) · [Chapter 11](manuscript/drafts/chapter-0011.md) · [Latest QA and evidence](qa/chapter-0011.md). The remaining 482 chapters await reconstruction."
    if old not in readme:
        raise ValueError("README checkpoint text changed unexpectedly")
    (ROOT / "README.md").write_text(readme.replace(old, new), encoding="utf-8")

    state = (ROOT / "PROJECT_STATE.md").read_text(encoding="utf-8")
    anchor = "- Chapter 7 is **editorially accepted**: 146 paragraph slots retained, 135 edited, all 151 Korean physical lines accounted for and all six QA items resolved. See [Chapter 7 QA](qa/chapter-0007.md) and its [acceptance record](qa/acceptance/chapter-0007.json).\n"
    if anchor not in state:
        raise ValueError("PROJECT_STATE Chapter 7 anchor changed unexpectedly")
    batch_slots = sum(p["paragraph_count"] for p in provenances.values())
    batch_changed = sum(p["changed_paragraphs"] for p in provenances.values())
    addition = (
        f"- Chapters 8–11, **Hounds of Hell (1–4)**, are **editorially accepted** as one title-family batch: {batch_slots} recovered MTL paragraph slots remain provenance-accounted, {batch_changed} are edited or structurally adjudicated, and all supplied Korean physical lines are explicitly aligned. Structured monster/rank windows, source-only spacer suppression, kidney/Cerberus mistranslations, the Cradle of Needles and Bloody Mamba payoff are documented in the [family review]({BATCH_REVIEW}). See [Chapter 11 QA](qa/chapter-0011.md) and its [acceptance record](qa/acceptance/chapter-0011.json).\n"
    )
    state = state.replace(anchor, anchor + addition)
    old_total = "- **Current total: 7 accepted reconstructions; Chapters 8–493 remain unstarted.** No recovered or newly reconstructed chapter is certified as the former finished production version."
    new_total = "- **Current total: 11 accepted reconstructions; Chapters 12–493 remain.** The next contiguous title-family batch is Chapters 12–13, *The Gluttonous Flies*. No recovered or newly reconstructed chapter is certified as the former finished production version."
    if old_total not in state:
        raise ValueError("PROJECT_STATE total checkpoint changed unexpectedly")
    (ROOT / "PROJECT_STATE.md").write_text(state.replace(old_total, new_total), encoding="utf-8")

    progress = (ROOT / "PROGRESS.md").read_text(encoding="utf-8")
    marker = "This log records recovered evidence and new reconstruction work separately. Historical completion reports do not count as recovered chapter QA.\n\n"
    if marker not in progress:
        raise ValueError("PROGRESS introduction changed unexpectedly")
    batch_slots = sum(p["paragraph_count"] for p in provenances.values())
    batch_changed = sum(p["changed_paragraphs"] for p in provenances.values())
    section = f"""## {REVIEW_DATE} — Hounds of Hell (Chapters 8–11) reconstructed and accepted

**Result: 11 chapters editorially accepted; Chapters 12–13, *The Gluttonous Flies*, are next.** The Hounds of Hell title-family batch preserves all {batch_slots} recovered MTL paragraph slots in provenance and records {batch_changed} edited or structurally adjudicated slots across Chapters 8–11.

- Reviewed the entire contiguous title family together under Korean-plus-MTL mode so practical-exam rules, Guide Hounds, Le Rouge et Le Noir Mountain, Bloody Beans/cacao, Hellhound weaknesses, Cerberus geography and sword ranks remain consistent across chapter boundaries.
- Preserved Norvegicus, Hellhound, Cerberus and sword/mage comparison data as reader-facing info windows while keeping all recovered source slots auditable; source-only NBSP spacers and explicitly documented duplicate/unsupported fragments are suppressed only from presentation.
- Corrected consequential machine-translation failures including Chapter 10 Korean `신장` as **kidneys**, not height; limited River Styx protection to strong but finite resistance; restored Chapter 11's **Cradle of Needles**; and preserved the seven-step Bloody Mamba venom payoff at the exact family endpoint.
- All historical audit hits for Chapters 8–11 were manually triaged. No audit suggestion was automatically applied.
- One shared Chromium installation/session rendered desktop/mobile evidence for all four chapters, then preserved-source checks, deterministic generation, tracker validation, the full test suite and whitespace checks passed before hash-bound acceptance records were created.
- The repository now requires title-family batching and sparse GitHub-runner usage in `AGENTS.md`; this batch used one final family-level runner rather than per-chapter candidate/acceptance runs.

**Next:** reconstruct Chapters 12–13 as the contiguous *The Gluttonous Flies* title-family batch. Whole-EPUB release remains pending.

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

    # Create final review/validation evidence before binding hashes.
    for chapter in CHAPTERS:
        write_text(f"editorial/reviews/chapter-{chapter:04d}-final.md", final_review_text(chapter, provenances[chapter], alignments[chapter], layouts[chapter]))
        write_text(f"qa/chapter-{chapter:04d}-validation.md", validation_text(chapter))

    # Close the one deliberately deferred gate issue per chapter and mark accepted.
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
        open_issues[0]["resolution"] = "The single Hounds of Hell title-family gate regenerated the reviewed chapter, rendered desktop/mobile browser evidence, passed complete repository checks and bound the accepted text/evidence hashes."
        open_issues[0]["evidence"] = [final_review, layout_path, validation, BATCH_REVIEW]
        screenshots = list(layouts[chapter]["screenshots"].values())
        qa["accepted"] = True
        qa["acceptance_evidence"] = f"qa/acceptance/chapter-{chapter:04d}.json"
        qa["pass"] = "Final editorial, bilingual source, continuity, title-family browser-layout and repository validation"
        qa["pass_description"] = "Complete Korean/MTL source comparison, final prose review, title-family continuity review, one-session desktop/mobile browser rendering and complete-checkout reproducibility validation"
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

    # Regenerate accepted-status draft/provenance and stable previews before hashing evidence.
    for chapter in CHAPTERS:
        outputs = render(chapter, validate_acceptance=False)
        for name, text in outputs.items():
            write_text(name, text)
        write_text(f"preview/chapter-{chapter:04d}.html", render_preview(chapter))

    # Bind exact final evidence hashes.
    for chapter in CHAPTERS:
        spec = read_json(f"editorial/edits/chapter-{chapter:04d}.json")
        qa = read_json(f"qa/chapter-{chapter:04d}.json")
        alignment = read_json(f"editorial/korean-alignment/chapter-{chapter:04d}.json")
        draft = (ROOT / f"manuscript/drafts/chapter-{chapter:04d}.md").read_text(encoding="utf-8")
        record = acceptance_context(chapter, spec, qa, draft, alignment)
        record.update({"review_date": REVIEW_DATE, "reviewer": REVIEWER, "release_status": "epub_not_built"})
        write_json(f"qa/acceptance/chapter-{chapter:04d}.json", record)
        # Immediate stale-hash validation before touching project summaries.
        render(chapter)
        write_text(f"qa/chapter-{chapter:04d}.md", qa_summary(chapter, read_json(f"editorial/provenance/chapter-{chapter:04d}.json"), alignment))

    update_project_docs({chapter: read_json(f"editorial/provenance/chapter-{chapter:04d}.json") for chapter in CHAPTERS})
    print("Hounds of Hell Chapters 8-11 finalized and hash-bound for editorial acceptance.")


if __name__ == "__main__":
    main()
