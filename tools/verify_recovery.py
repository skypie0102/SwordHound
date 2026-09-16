"""Verify recovered files against their preserved evidence; no dependencies."""
from pathlib import Path
import csv
import hashlib
import json
import tarfile
import xml.etree.ElementTree as ET
import zipfile
from import_korean_raws import check_korean_raws

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    supplemental = check_korean_raws(ROOT)
    for item in json.loads((ROOT / 'recovery/artifact-checksums.json').read_text(encoding='utf-8')):
        data = (ROOT / item['path']).read_bytes()
        require(len(data) == item['bytes'] and sha(data) == item['sha256'], 'Artifact checksum mismatch: '+item['path'])
    manifest = json.loads((ROOT / 'recovery/source-corpus-manifest.json').read_text(encoding='utf-8'))
    archive = ROOT / manifest['archive']
    require(sha(archive.read_bytes()) == manifest['sha256'], 'Source archive checksum mismatch')
    with (ROOT / 'source/chapter-sha256.tsv').open(encoding='utf-8', newline='') as stream:
        rows = list(csv.DictReader(stream, delimiter='\t'))
    require(sorted(int(r['chapter']) for r in rows) == list(range(1, 494)), 'Chapter coverage mismatch')
    require(len(list((ROOT / 'source/chapters').glob('*.xhtml'))) == 493, 'Unexpected chapter count')
    with tarfile.open(archive) as tf:
        for member in tf.getmembers():
            if member.isfile():
                target = ROOT / 'source' / member.name
                require(target.read_bytes() == tf.extractfile(member).read(), f'Archive mismatch: {member.name}')
    for row in rows:
        data = (ROOT / 'source/chapters' / row['repo_file']).read_bytes()
        require(len(data) == int(row['bytes']) and sha(data) == row['sha256'], f'Chapter checksum mismatch: {row["chapter"]}')
        ET.fromstring(data)
    local = json.loads((ROOT / 'recovery/local-epub-manifest.json').read_text(encoding='utf-8'))
    epub = ROOT / local['artifact']
    require(sha(epub.read_bytes()) == local['artifact_sha256'], 'Local EPUB checksum mismatch')
    with zipfile.ZipFile(epub) as z:
        require(z.testzip() is None, 'EPUB ZIP integrity failure')
        require(z.namelist()[0] == 'mimetype' and z.getinfo('mimetype').compress_type == 0, 'Invalid EPUB mimetype placement')
        require(z.read('mimetype') == b'application/epub+zip', 'Invalid EPUB mimetype')
        for item in local['members']:
            p = ROOT / item['path']
            data = p.read_bytes()
            require(sha(data) == item['sha256'] and len(data) == item['bytes'], f'Snapshot checksum mismatch: {p}')
            member = p.relative_to(ROOT / 'epub/local-2026-07-29').as_posix()
            require(data == z.read(member), f'Snapshot differs from EPUB: {member}')
            if p.suffix in {'.xhtml', '.xml', '.opf', '.ncx'}:
                ET.fromstring(data)
        ns = {'opf': 'http://www.idpf.org/2007/opf'}
        package = ET.fromstring(z.read('EPUB/package.opf'))
        items = {x.attrib['id']: x for x in package.findall('opf:manifest/opf:item', ns)}
        for item in items.values():
            require('EPUB/' + item.attrib['href'] in z.namelist(), 'Missing package resource: '+item.attrib['href'])
        for ref in package.findall('opf:spine/opf:itemref', ns):
            require(ref.attrib['idref'] in items, 'Unresolved spine reference')
    total_korean = 54 + supplemental['chapter_count']
    print(f"PASS: preserved Korean 001-054 archive plus {supplemental['chapter_count']} supplemental raws ({total_korean} Korean chapters total); artifact hashes (including original audit), 493 MTL source hashes, archive members, 524 EPUB snapshot members, XML parsing, EPUB manifest and spine.")


if __name__ == '__main__':
    main()
