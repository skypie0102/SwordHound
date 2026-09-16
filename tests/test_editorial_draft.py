"""Tests for Chinese-first source resolution."""
import importlib.util, shutil, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("draft_builder",ROOT/"tools/build_editorial_draft.py"); builder=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(builder)
class SourceResolutionTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup); self.root=Path(self.temp.name)
        for rel in ["source/chinese/chapter-exceptions.tsv","source/chinese/chapters/001.txt","source/chinese/chapters/075.txt","source/chinese/chapters/267.txt","source/chapters/chapter-001.xhtml","source/chapters/chapter-055.xhtml","source/chapters/chapter-074.xhtml","source/chapters/chapter-075.xhtml","source/chapters/chapter-265.xhtml","source/chapters/chapter-266.xhtml"]:
            dst=self.root/rel; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(ROOT/rel,dst)
        self.p=patch.object(builder,"ROOT",self.root); self.p.start(); self.addCleanup(self.p.stop); builder.CHINESE=self.root/"source/chinese/chapters"; builder.EXCEPTIONS=self.root/"source/chinese/chapter-exceptions.tsv"; builder.MTL=self.root/"source/chapters"
    def test_normal_chapter_does_not_assume_same_number_mtl(self):
        r=builder.resolve_sources(1); self.assertEqual(r["chinese_source"],"source/chinese/chapters/001.txt"); self.assertIsNone(r["english_mtl_reference"])
    def test_chapter_55_uses_verified_mtl_only_fallback(self):
        r=builder.resolve_sources(55); self.assertIsNone(r["chinese_source"]); self.assertEqual(r["english_mtl_chapter"],55); self.assertEqual(r["source_mode"],"mtl_only")
    def test_combined_75_76_share_raw_and_map_separately(self):
        a=builder.resolve_sources(75); b=builder.resolve_sources(76); self.assertEqual(a["chinese_source"],b["chinese_source"]); self.assertEqual((a["english_mtl_chapter"],b["english_mtl_chapter"]),(74,75)); self.assertEqual(a["raw_status"],"combined")
    def test_verified_numbering_divergence_at_267(self):
        self.assertEqual(builder.resolve_sources(267)["english_mtl_chapter"],265); self.assertEqual(builder.resolve_sources(268)["english_mtl_chapter"],266)
    def test_explicit_alignment(self):
        self.assertEqual(builder.resolve_sources(1,1)["english_alignment"],"editor_supplied")
    def test_target_range(self):
        with self.assertRaises(ValueError): builder.resolve_sources(0)
        with self.assertRaises(ValueError): builder.resolve_sources(501)
if __name__=="__main__": unittest.main()
