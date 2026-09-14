"""Apply the final Chapter 6 punctuation fixes and regenerate reviewed outputs."""
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
    path = ROOT / 'editorial/edits/chapter-0006.json'
    spec = json.loads(path.read_text(encoding='utf-8'))
    targets = {99, 122}
    found = set()
    for edit in spec['edits']:
        if edit[0] in targets:
            edit[1] = '“…”'
            edit[2] = 'Normalize the silent-response ellipsis after the complete bilingual prose read; remove the accidental interior space.'
            found.add(edit[0])
    if found != targets:
        raise SystemExit(f'Expected edit entries 99 and 122, found {sorted(found)}')
    write('editorial/edits/chapter-0006.json', json.dumps(spec, ensure_ascii=False, indent=2) + '\n')
    outputs = bed.render(6, validate_acceptance=False)
    for name, text in outputs.items():
        write(name, text)
    subprocess.run([sys.executable, str(ROOT / 'tools/build_chapter_preview.py'), '6'], check=True)
    print('Chapter 6 final punctuation fixes applied and outputs regenerated.')


if __name__ == '__main__':
    main()
