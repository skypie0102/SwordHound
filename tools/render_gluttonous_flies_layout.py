"""Render browser layout evidence for The Gluttonous Flies title-family batch."""
from pathlib import Path
import json
import shutil
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
REVIEW_DATE = "2026-09-14"
CONFIG = {
    12: [("desktop-opening", 1), ("desktop-skeleton", 46), ("desktop-riddle", 74), ("mobile-ending", 150)],
    13: [("desktop-beelzebub", 1), ("desktop-first-window", 79), ("desktop-second-window", 122), ("mobile-ending", 166)],
}
EXPECTED_WINDOWS = {12: 0, 13: 2}
EXPECTED_SCENES = {12: 0, 13: 0}
EXPECTED_MTL_ONLY = {12: 0, 13: 21}


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


def find_system_chrome():
    for executable in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        path = shutil.which(executable)
        if path:
            return path
    raise RuntimeError("No preinstalled Chrome/Chromium executable found; do not download a browser implicitly")


def main():
    chrome = find_system_chrome()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path=chrome)
        page = browser.new_page()
        for chapter, captures in CONFIG.items():
            provenance = json.loads((ROOT / f"editorial/provenance/chapter-{chapter:04d}.json").read_text(encoding="utf-8"))
            mtl_only = provenance.get("mtl_only_paragraphs", [])
            if len(mtl_only) != EXPECTED_MTL_ONLY[chapter]:
                raise ValueError(f"Chapter {chapter}: unexpected MTL-only provenance count {len(mtl_only)}")
            preview = ROOT / f"preview/chapter-{chapter:04d}.html"

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
                screenshots[label.replace("-", "_")] = screenshot_at(page, chapter, label, paragraph, mobile=label.startswith("mobile-"))

            layout = {
                "chapter": chapter,
                "review_date": REVIEW_DATE,
                "preview": preview.relative_to(ROOT).as_posix(),
                "source_paragraph_slots": provenance["paragraph_count"],
                "suppressed_source_slots": provenance.get("suppressed_paragraphs", []),
                "mtl_only_source_slots": mtl_only,
                "browser_executable": Path(chrome).name,
                "viewports": viewports,
                "screenshots": screenshots,
                "result": "pass",
                "notes": [
                    "Every recovered MTL paragraph slot remains provenance-accounted; declared structural spacers are omitted only from reader-facing output.",
                    "Chapter 13's 21 MTL-only slots remain explicitly marked as absent from the supplied Korean witness and are still rendered as recovered source content.",
                    "Dialogue is indented; narration and info-window rows are unindented; no horizontal overflow occurs at either viewport.",
                    "Both chapters were rendered in one session using the runner's preinstalled Chrome without downloading a separate browser build."
                ]
            }
            out = ROOT / f"qa/layout/chapter-{chapter:04d}.json"
            out.write_text(json.dumps(layout, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        browser.close()
    print("The Gluttonous Flies layout evidence rendered for Chapters 12-13 using preinstalled Chrome.")


if __name__ == "__main__":
    main()
