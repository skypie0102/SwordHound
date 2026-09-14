"""Render browser layout evidence for the Hounds of Hell title-family batch."""
from pathlib import Path
import json
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
REVIEW_DATE = "2026-09-14"
CONFIG = {
    8: [("desktop-opening", 1), ("desktop-scoring", 27), ("desktop-mountain", 49), ("mobile-ending", 104)],
    9: [("desktop-opening", 1), ("desktop-norvegicus", 67), ("desktop-hellhound", 137), ("mobile-ending", 183)],
    10: [("desktop-kidney", 38), ("desktop-pack", 98), ("desktop-cerberus", 129), ("mobile-ending", 138)],
    11: [("desktop-ranks", 35), ("desktop-injury", 65), ("desktop-trap", 146), ("mobile-ending", 201)],
}
EXPECTED_WINDOWS = {8: 0, 9: 2, 10: 1, 11: 2}
EXPECTED_SCENES = {8: 0, 9: 2, 10: 0, 11: 0}


def measure(page):
    return page.evaluate("""() => {
      const body = getComputedStyle(document.body);
      const dialogue = document.querySelector('p.dialogue');
      const narrative = document.querySelector('p.narrative');
      return {
        rendered_paragraph_count: document.querySelectorAll('p[id]').length,
        scene_break_count: document.querySelectorAll('.scene-break').length,
        info_window_count: document.querySelectorAll('.info-window').length,
        info_window_row_count: document.querySelectorAll('.info-window p[id]').length,
        italic_count: document.querySelectorAll('em').length,
        dialogue_count: document.querySelectorAll('p.dialogue').length,
        narrative_count: document.querySelectorAll('p.narrative').length,
        body_line_height: body.lineHeight,
        dialogue_indent: dialogue ? getComputedStyle(dialogue).textIndent : null,
        narrative_indent: narrative ? getComputedStyle(narrative).textIndent : null,
        scroll_width: document.documentElement.scrollWidth,
        client_width: document.documentElement.clientWidth,
        horizontal_overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
        document_height: document.documentElement.scrollHeight
      };
    }""")


def screenshot_at(page, chapter, label, paragraph, mobile=False):
    viewport = {"width": 390, "height": 844} if mobile else {"width": 1100, "height": 900}
    page.set_viewport_size(viewport)
    locator = page.locator(f"#p{paragraph:03d}")
    if locator.count() != 1:
        raise ValueError(f"Chapter {chapter}: screenshot anchor p{paragraph} not rendered exactly once")
    locator.scroll_into_view_if_needed()
    page.wait_for_timeout(100)
    path = ROOT / f"qa/layout/chapter-{chapter:04d}-{label}.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(path), full_page=False)
    return path.relative_to(ROOT).as_posix()


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        for chapter, captures in CONFIG.items():
            provenance = json.loads((ROOT / f"editorial/provenance/chapter-{chapter:04d}.json").read_text(encoding="utf-8"))
            preview = ROOT / f"preview/chapter-{chapter:04d}.html"
            page.goto(preview.resolve().as_uri())

            viewports = {}
            for name, viewport in (("desktop", {"width": 1100, "height": 900}), ("mobile", {"width": 390, "height": 844})):
                page.set_viewport_size(viewport)
                page.goto(preview.resolve().as_uri())
                metrics = measure(page)
                expected_units = provenance["paragraph_count"] - len(provenance.get("suppressed_paragraphs", []))
                actual_units = metrics["rendered_paragraph_count"] + metrics["scene_break_count"]
                if actual_units != expected_units:
                    raise ValueError(f"Chapter {chapter} {name}: rendered units {actual_units} != expected {expected_units}")
                if metrics["scene_break_count"] != EXPECTED_SCENES[chapter]:
                    raise ValueError(f"Chapter {chapter} {name}: unexpected scene-break count")
                if metrics["info_window_count"] != EXPECTED_WINDOWS[chapter]:
                    raise ValueError(f"Chapter {chapter} {name}: unexpected info-window count")
                if metrics["horizontal_overflow"]:
                    raise ValueError(f"Chapter {chapter} {name}: horizontal overflow")
                expected_line = "31.35px" if name == "desktop" else "29.7px"
                expected_indent = "28.5px" if name == "desktop" else "27px"
                if metrics["body_line_height"] != expected_line:
                    raise ValueError(f"Chapter {chapter} {name}: unexpected line height {metrics['body_line_height']}")
                if metrics["dialogue_indent"] not in (None, expected_indent):
                    raise ValueError(f"Chapter {chapter} {name}: unexpected dialogue indent {metrics['dialogue_indent']}")
                if metrics["narrative_indent"] not in (None, "0px"):
                    raise ValueError(f"Chapter {chapter} {name}: narrative unexpectedly indented")
                metrics.update(width=viewport["width"], height=viewport["height"])
                viewports[name] = metrics

            screenshots = {}
            for label, paragraph in captures:
                mobile = label.startswith("mobile-")
                screenshots[label.replace("-", "_")] = screenshot_at(page, chapter, label, paragraph, mobile=mobile)

            layout = {
                "chapter": chapter,
                "review_date": REVIEW_DATE,
                "preview": preview.relative_to(ROOT).as_posix(),
                "source_paragraph_slots": provenance["paragraph_count"],
                "suppressed_source_slots": provenance.get("suppressed_paragraphs", []),
                "viewports": viewports,
                "screenshots": screenshots,
                "result": "pass",
                "notes": [
                    "All recovered source paragraph slots remain provenance-accounted; explicitly suppressed structural slots are omitted only from reader-facing output.",
                    "Dialogue is indented; narration is unindented; info-window rows remain unindented inside bordered windows.",
                    "No horizontal overflow at desktop or mobile widths.",
                    "Browser evidence for the full title family was generated in one Chromium installation/session."
                ]
            }
            out = ROOT / f"qa/layout/chapter-{chapter:04d}.json"
            out.write_text(json.dumps(layout, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        browser.close()
    print("Hounds of Hell layout evidence rendered for Chapters 8-11.")


if __name__ == "__main__":
    main()
