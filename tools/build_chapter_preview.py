"""Render a standalone chapter layout from verified paragraph provenance."""
from pathlib import Path
import argparse
import html
import json

ROOT = Path(__file__).resolve().parents[1]


def render_preview(chapter):
    record = json.loads((ROOT / f'editorial/provenance/chapter-{chapter:04d}.json').read_text(encoding='utf-8'))
    title = (ROOT / f'manuscript/drafts/chapter-{chapter:04d}.md').read_text(encoding='utf-8').splitlines()[0][2:]
    body = []
    for row in record['paragraphs']:
        text = row['draft_text']
        content = html.escape(text)
        if text.startswith('‘') and text.endswith('’'):
            content = '<em>' + content + '</em>'
        elif 'thought, ‘' in text:
            start = content.index('‘')
            content = content[:start] + '<em>' + content[start:] + '</em>'
        kind = 'dialogue' if text.startswith('“') else 'narrative'
        body.append(f'<p id="p{row["paragraph"]:03d}" class="{kind}">{content}</p>')
        if row['paragraph'] in record['scene_breaks_after']:
            body.append('<div class="scene-break" role="separator" aria-label="Scene break">◆◆◆</div>')
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
@media(max-width: 480px) { body { font-size: 18px; } main { padding: 30px 22px 50px; } h1 { font-size: 28px; } }
@media print { body { background: white; } main { max-width: none; padding: 0; } p { orphans: 2; widows: 2; } }
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
