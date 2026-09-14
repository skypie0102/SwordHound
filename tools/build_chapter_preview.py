"""Render a standalone chapter layout from verified paragraph provenance."""
from pathlib import Path
import argparse
import html
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = {'h': 'http://www.w3.org/1999/xhtml'}


def source_paragraph_metadata(source_rel):
    """Return source structural metadata without changing recovered XHTML."""
    doc = ET.fromstring((ROOT / source_rel).read_bytes())
    body = doc.find('.//h:div[@class="chapter-content"]', NS)
    rows = []

    def walk(node, in_info_window=False):
        for child in list(node):
            local = child.tag.rsplit('}', 1)[-1]
            cls = child.attrib.get('class', '')
            child_info = in_info_window or (local == 'div' and 'info-window' in cls.split())
            if local == 'p':
                rows.append({
                    'info_window': in_info_window,
                    'source_class': cls,
                    'source_text': ''.join(child.itertext()),
                })
            else:
                walk(child, child_info)

    walk(body)
    return rows


def render_preview(chapter):
    record = json.loads((ROOT / f'editorial/provenance/chapter-{chapter:04d}.json').read_text(encoding='utf-8'))
    title = (ROOT / f'manuscript/drafts/chapter-{chapter:04d}.md').read_text(encoding='utf-8').splitlines()[0][2:]
    source_meta = source_paragraph_metadata(record['source'])
    if len(source_meta) != len(record['paragraphs']):
        raise ValueError('Source structure no longer matches paragraph provenance')

    body = []
    info_open = False
    for row, meta in zip(record['paragraphs'], source_meta):
        text = row['draft_text']
        source_classes = meta['source_class'].split()
        is_formatting_blank = not text.replace('\xa0', '').strip()
        is_source_divider = 'scene-break' in source_classes and text.strip() in {'◆', '◆◆◆', '* * *'}

        if row.get('suppressed'):
            if not meta['info_window'] and info_open:
                body.append('</div>')
                info_open = False
            if row['paragraph'] in record['scene_breaks_after']:
                body.append('<div class="scene-break" role="separator" aria-label="Scene break">◆◆◆</div>')
            continue

        if is_source_divider:
            if info_open:
                body.append('</div>')
                info_open = False
            body.append('<div class="scene-break" role="separator" aria-label="Scene break">◆◆◆</div>')
        else:
            if meta['info_window'] and not info_open:
                body.append('<div class="info-window">')
                info_open = True
            elif not meta['info_window'] and info_open:
                body.append('</div>')
                info_open = False

            if not is_formatting_blank:
                content = html.escape(text)
                if meta['info_window']:
                    info_class = 'info-window-title' if 'info-window-title' in source_classes else 'info-window-row'
                    body.append(f'<p id="p{row["paragraph"]:03d}" class="{info_class}">{content}</p>')
                else:
                    if text.startswith('‘') and text.endswith('’'):
                        content = '<em>' + content + '</em>'
                    elif 'thought, ‘' in text:
                        start = content.index('‘')
                        content = content[:start] + '<em>' + content[start:] + '</em>'
                    kind = 'dialogue' if text.startswith('“') else 'narrative'
                    body.append(f'<p id="p{row["paragraph"]:03d}" class="{kind}">{content}</p>')

        if row['paragraph'] in record['scene_breaks_after']:
            if info_open:
                body.append('</div>')
                info_open = False
            body.append('<div class="scene-break" role="separator" aria-label="Scene break">◆◆◆</div>')

    if info_open:
        body.append('</div>')

    return '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>''' + html.escape(title) + '''</title>
<style>
* { box-sizing: border-box; }
body { margin: 0; background: #f7f4ed; color: #262421; font: 19px/1.65 Georgia, 'Times New Roman', serif; }
main { max-width: 720px; margin: 0 auto; padding: 52px 28px 72px; }
.edition-note { font: 12px/1.5 Arial,sans-serif; letter-spacing: .08em; text-transform: uppercase; color: #68625a; }
h1 { font-size: 32px; font-weight: normal; line-height: 1.25; margin: 22px 0 38px; }
p { margin: 0 0 .85em; text-indent: 0; overflow-wrap: break-word; }
p.dialogue { text-indent: 1.5em; }
.scene-break { text-align: center; letter-spacing: .45em; margin: 2.5em 0; font-size: 13px; }
.info-window { border: 1px solid #8f887e; margin: 1.55em 0; padding: .8em 1em .65em; background: rgba(255,255,255,.34); }
.info-window p { margin: 0 0 .28em; text-indent: 0; }
.info-window p:last-child { margin-bottom: 0; }
.info-window-title { font-weight: bold; text-align: center; margin-bottom: .55em !important; }
@media(max-width: 480px) { body { font-size: 18px; } main { padding: 30px 22px 50px; } h1 { font-size: 28px; } .info-window { padding: .72em .8em .58em; } }
@media print { body { background: white; } main { max-width: none; padding: 0; } p { orphans: 2; widows: 2; } .info-window { break-inside: avoid; } }
</style></head><body><main><div class="edition-note">Chapter layout preview · EPUB packaging pending</div><h1>''' + html.escape(title) + '</h1>\n' + '\n'.join(body) + '\n</main></body></html>\n'


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('chapter',type=int)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    path=ROOT / f'preview/chapter-{args.chapter:04d}.html'
    text=render_preview(args.chapter)
    if args.check:
        if path.read_text(encoding='utf-8') != text:
            raise ValueError('Chapter preview is stale')
    else:
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(text,encoding='utf-8')
    print(f'Chapter {args.chapter}: layout preview {"verified" if args.check else "generated"}.')
