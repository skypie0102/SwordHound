"""Import or verify the user-supplied Korean 001-054 archive without changing bytes."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = 'archives/korean-raws-001-054.zip'
MANIFEST = 'recovery/korean-raws-manifest.json'
EXPECTED_SHA256 = 'e250131a9fe927c52b403258ca98696ac946b5b088106eba9909e01bbe3b9923'


def inspect_archive(data):
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        raise ValueError('Archive differs from the user-supplied 001-054.zip')
    outputs, members = {}, []
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        expected = [f'{n:03d}.txt' for n in range(1, 55)]
        if sorted(archive.namelist()) != expected or archive.testzip() is not None:
            raise ValueError('Expected exactly 001.txt through 054.txt with valid ZIP CRCs')
        for number, name in enumerate(expected, 1):
            raw = archive.read(name)
            text = raw.decode('utf-8-sig')
            first_line = next(line.strip() for line in text.splitlines() if line.strip())
            heading = re.match(r'#(\d+)(?!\d)', first_line)
            if not heading or int(heading.group(1)) != number:
                raise ValueError(f'Opening chapter number does not match filename: {name}')
            path = f'source/korean/chapters/{name}'
            outputs[path] = raw
            members.append({'chapter': number, 'archive_member': name, 'path': path,
                            'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
                            'encoding': 'utf-8', 'opening_heading': first_line,
                            'alignment': 'filename_and_opening_number_verified; full_passage_alignment_pending'})
    manifest = {'received_date': '2026-09-13', 'provenance': 'User supplied 001-054.zip as Korean raws for Chapters 1-54.',
                'archive': ARCHIVE, 'archive_bytes': len(data), 'archive_sha256': EXPECTED_SHA256,
                'chapter_count': 54, 'chapter_range': [1, 54],
                'notice': 'Original archive and member bytes preserved. Numbered coverage is verified, not translation accuracy or publisher provenance. User states Korean raws are unavailable from Chapter 55 onward; use MTL with supporting QA references there.',
                'members': members}
    outputs[ARCHIVE] = data
    outputs[MANIFEST] = (json.dumps(manifest, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    return outputs


def check_korean_raws(root=ROOT):
    outputs = inspect_archive((root / ARCHIVE).read_bytes())
    for name, expected in outputs.items():
        path = root / name
        if name == MANIFEST:
            if json.loads(path.read_text(encoding='utf-8')) != json.loads(expected):
                raise ValueError('Korean manifest differs from verified archive evidence')
        elif path.read_bytes() != expected:
            raise ValueError(f'Korean source byte mismatch: {name}')
    actual = {p.name for p in (root / 'source/korean/chapters').iterdir()}
    if actual != {f'{n:03d}.txt' for n in range(1, 55)}:
        raise ValueError('Unexpected or missing Korean chapter files')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive', nargs='?', type=Path, help='Original supplied ZIP; omit when verifying')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    if not args.check:
        if args.archive is None:
            parser.error('Provide the supplied ZIP path for import')
        outputs = inspect_archive(args.archive.read_bytes())
        for name, data in outputs.items():
            path = ROOT / name
            if path.exists() and path.read_bytes() != data:
                raise ValueError(f'Refusing to replace different existing evidence: {name}')
        for name, data in outputs.items():
            path = ROOT / name
            path.parent.mkdir(parents=True, exist_ok=True)
            if not path.exists():
                path.write_bytes(data)
    check_korean_raws()
    print('PASS: Korean ZIP checksum/CRC, all 54 chapter bytes, UTF-8 decoding, numbered headings, and manifest.')


if __name__ == '__main__':
    main()
