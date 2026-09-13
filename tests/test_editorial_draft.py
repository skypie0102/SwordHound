"""Failure and conservation checks using the current reconstruction batch."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('draft_builder', ROOT / 'tools/build_editorial_draft.py')
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


class DraftChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('source/chapters/chapter-001.xhtml', 'editorial/edits/chapter-0001.json',
                     'qa/chapter-0001.json', 'editorial/reconstruction-status.json',
                     'source/korean/chapters/001.txt', 'editorial/korean-alignment/chapter-0001.json',
                     'editorial/reviews/chapter-0001.md'):
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)
        self.root_patch = patch.object(builder, 'ROOT', self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)

    def change_json(self, name, mutate):
        path = self.root / name
        data = json.loads(path.read_text(encoding='utf-8'))
        mutate(data)
        path.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')

    def test_conserves_paragraphs_and_disputed_passages(self):
        source = self.root / 'source/chapters/chapter-001.xhtml'
        before = source.read_bytes()
        outputs = builder.render(1)
        record = json.loads(outputs['editorial/provenance/chapter-0001.json'])
        self.assertEqual([p['paragraph'] for p in record['paragraphs']], list(range(1, 107)))
        self.assertEqual(record['paragraphs'][16]['source_text'], record['paragraphs'][16]['draft_text'])
        self.assertIn('CH001-01', record['paragraphs'][16]['open_issues'])
        self.assertIn('CH001-06', record['paragraphs'][65]['open_issues'])
        self.assertEqual(record['scene_breaks_after'], [18])
        self.assertIn('QA not accepted', outputs['manuscript/drafts/chapter-0001.md'])
        self.assertEqual(source.read_bytes(), before)

    def test_rejects_changed_source(self):
        path = self.root / 'source/chapters/chapter-001.xhtml'
        path.write_bytes(path.read_bytes() + b'\n')
        with self.assertRaisesRegex(ValueError, 'original source'):
            builder.render(1)

    def test_rejects_duplicate_edit(self):
        self.change_json('editorial/edits/chapter-0001.json', lambda d: d['edits'].append(d['edits'][0]))
        with self.assertRaisesRegex(ValueError, 'Duplicate or invalid paragraph'):
            builder.render(1)

    def test_rejects_deleted_paragraph(self):
        self.change_json('editorial/edits/chapter-0001.json', lambda d: d['edits'][0].__setitem__(1, ''))
        with self.assertRaisesRegex(ValueError, 'Invalid replacement'):
            builder.render(1)

    def test_rejects_acceptance_with_open_questions(self):
        self.change_json('qa/chapter-0001.json', lambda d: d.update(accepted=True, acceptance_evidence='unsupported assertion'))
        with self.assertRaisesRegex(ValueError, 'QA acceptance requires'):
            builder.render(1)

    def test_rejects_tracker_hiding_open_questions(self):
        self.change_json('editorial/reconstruction-status.json', lambda d: d['1'].update(open_issues=[]))
        with self.assertRaisesRegex(ValueError, 'disagrees with QA'):
            builder.render(1)

    def test_rejects_changed_korean_source(self):
        path = self.root / 'source/korean/chapters/001.txt'
        path.write_bytes(path.read_bytes() + b'\n')
        with self.assertRaisesRegex(ValueError, 'alignment source mismatch'):
            builder.render(1)

    def test_rejects_omitted_korean_line(self):
        self.change_json('editorial/korean-alignment/chapter-0001.json', lambda d: d['non_body_lines'].pop())
        with self.assertRaisesRegex(ValueError, 'coverage omits or duplicates'):
            builder.render(1)

    def test_rejects_resolution_without_evidence(self):
        self.change_json('qa/chapter-0001.json', lambda d: next(i for i in d['issues'] if i['status']=='resolved').update(evidence=[]))
        with self.assertRaisesRegex(ValueError, 'requires a decision and evidence'):
            builder.render(1)


if __name__ == '__main__':
    unittest.main()
