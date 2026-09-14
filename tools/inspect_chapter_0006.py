"""Render and measure Chapter 6 desktop/mobile preview with Playwright."""
from pathlib import Path
import json
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PREVIEW = (ROOT / 'preview/chapter-0006.html').resolve().as_uri()
OUT = ROOT / 'qa/layout'
OUT.mkdir(parents=True, exist_ok=True)


def metrics(page):
    return page.evaluate("""() => {
      const ps = [...document.querySelectorAll('p')];
      const d = ps.find(p => p.classList.contains('dialogue'));
      const n = ps.find(p => p.classList.contains('narrative'));
      const body = getComputedStyle(document.body);
      return {
        paragraph_count: ps.length,
        scene_break_count: document.querySelectorAll('.scene-break').length,
        italic_count: document.querySelectorAll('p em').length,
        dialogue_count: document.querySelectorAll('p.dialogue').length,
        narrative_count: document.querySelectorAll('p.narrative').length,
        body_line_height: body.lineHeight,
        dialogue_indent: d ? getComputedStyle(d).textIndent : null,
        narrative_indent: n ? getComputedStyle(n).textIndent : null,
        scroll_width: document.documentElement.scrollWidth,
        client_width: document.documentElement.clientWidth,
        horizontal_overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
        document_height: document.documentElement.scrollHeight
      };
    }""")


def shot(page, selector, path):
    page.locator(selector).scroll_into_view_if_needed()
    page.screenshot(path=str(path), full_page=False)


def main():
    result = {'chapter': 6, 'review_date': '2026-09-14', 'preview': 'preview/chapter-0006.html', 'viewports': {}, 'screenshots': {}, 'result': 'pass'}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for name, width, height in [('desktop', 1100, 900), ('mobile', 390, 844)]:
            page = browser.new_page(viewport={'width': width, 'height': height})
            page.goto(PREVIEW)
            page.wait_for_load_state('load')
            result['viewports'][name] = {'width': width, 'height': height, **metrics(page)}
            if name == 'desktop':
                opening = OUT / 'chapter-0006-desktop-opening.png'
                page.screenshot(path=str(opening), full_page=False)
                omen = OUT / 'chapter-0006-desktop-omen.png'
                shot(page, '#p034', omen)
                father = OUT / 'chapter-0006-desktop-father.png'
                shot(page, '#p092', father)
                result['screenshots'].update(desktop_opening=str(opening.relative_to(ROOT)).replace('\\','/'), desktop_omen=str(omen.relative_to(ROOT)).replace('\\','/'), desktop_father=str(father.relative_to(ROOT)).replace('\\','/'))
            else:
                ending = OUT / 'chapter-0006-mobile-ending.png'
                shot(page, '#p124', ending)
                result['screenshots']['mobile_ending'] = str(ending.relative_to(ROOT)).replace('\\','/')
            page.close()
        browser.close()
    d, m = result['viewports']['desktop'], result['viewports']['mobile']
    checks = [d['paragraph_count'] == 124, m['paragraph_count'] == 124, d['scene_break_count'] == 1, m['scene_break_count'] == 1, d['italic_count'] == 3, m['italic_count'] == 3, not d['horizontal_overflow'], not m['horizontal_overflow'], d['narrative_indent'] == '0px', m['narrative_indent'] == '0px']
    if not all(checks):
        result['result'] = 'fail'
        (OUT/'chapter-0006.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
        raise SystemExit('Chapter 6 layout metrics failed')
    result['notes'] = ['All 124 paragraphs rendered with one restored scene break.', 'Dialogue is indented; narration is unindented.', 'Three full-paragraph thoughts are italicized.', 'No horizontal overflow at desktop or mobile widths.']
    (OUT/'chapter-0006.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result['viewports'], indent=2))

if __name__ == '__main__':
    main()
