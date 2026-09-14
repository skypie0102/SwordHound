"""Apply the final Chapter 7 prose refinements and regenerate reviewed outputs."""
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import build_editorial_draft as bed


def write(path, text):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding='utf-8', newline='\n')


def main():
    path = ROOT / 'editorial/edits/chapter-0007.json'
    spec = json.loads(path.read_text(encoding='utf-8'))
    replacements = {
        43: ('‘I always thought only the eldest son could inherit the family. So even an eldest son could be made after the fact.’', 'Smooth the eldest-son realization after the complete prose read without changing the source decision.'),
        100: ('It was a task easily handled with mana, but there was nothing strange about the old butler tending to it by hand.', 'Smooth the lantern/mana contrast after the complete prose read while preserving the Korean action.'),
        133: ('The flavor hit his mouth at once.', 'Sharpen the immediate taste reaction after the complete prose read without changing meaning.')
    }
    found=set()
    for edit in spec['edits']:
        if edit[0] in replacements:
            edit[1], edit[2] = replacements[edit[0]]
            found.add(edit[0])
    if found != set(replacements):
        raise SystemExit(f'Missing expected Chapter 7 edit entries: {sorted(set(replacements)-found)}')
    write('editorial/edits/chapter-0007.json', json.dumps(spec, ensure_ascii=False, indent=2) + '\n')
    outputs = bed.render(7, validate_acceptance=False)
    for name, text in outputs.items():
        write(name, text)
    subprocess.run([sys.executable, str(ROOT / 'tools/build_chapter_preview.py'), '7'], check=True)
    print('Chapter 7 final prose refinements applied and outputs regenerated.')


if __name__ == '__main__':
    main()
