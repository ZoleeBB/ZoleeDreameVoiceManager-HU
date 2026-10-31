"""Semantic release version regression for the HU fork (v1.5.0, v1.5.1)."""
import tempfile
import unittest
from pathlib import Path
from scripts.set_release_version import set_version


class ReleaseVersionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "dreamevoice").mkdir()
        (self.root / "dreamevoice" / "__init__.py").write_text(
            '__version__ = "1.4.0"\n', encoding="utf-8")
        (self.root / "version_info.txt").write_text(
            "filevers=(1, 4, 0, 0)\n"
            "prodvers=(1, 4, 0, 0)\n"
            "StringStruct('FileVersion', '1.4.0.0'),\n"
            "StringStruct('ProductVersion', '1.4.0.0'),\n",
            encoding="utf-8")
        (self.root / "RELEASE.md").write_text(
            "## v1.4.0 – Eredeti upstream changelog\n",
            encoding="utf-8")

    def test_new_semver_is_synchronized_in_app_exe_and_notes(self):
        self.assertEqual(set_version("v1.5.0", self.root), "1.5.0")
        package = (self.root / "dreamevoice" / "__init__.py").read_text(
            encoding="utf-8")
        meta = (self.root / "version_info.txt").read_text(encoding="utf-8")
        notes = (self.root / "RELEASE.md").read_text(encoding="utf-8")
        self.assertIn('__version__ = "1.5.0"', package)
        self.assertIn("filevers=(1, 5, 0, 0)", meta)
        self.assertIn("prodvers=(1, 5, 0, 0)", meta)
        self.assertEqual(meta.count("'1.5.0.0'"), 2)
        self.assertTrue(notes.startswith("## v1.5.0"))
        self.assertIn("## v1.4.0", notes)

    def test_patch_release_after_minor_release(self):
        set_version("v1.5.0", self.root)
        set_version("v1.5.1", self.root)
        self.assertIn('__version__ = "1.5.1"',
                      (self.root / "dreamevoice" / "__init__.py").read_text(
                          encoding="utf-8"))
        notes = (self.root / "RELEASE.md").read_text(encoding="utf-8")
        self.assertTrue(notes.startswith("## v1.5.1"))
        self.assertIn("## v1.5.0", notes)
        self.assertIn("## v1.4.0", notes)

    def test_repeating_version_does_not_duplicate_release_notes(self):
        set_version("v1.5.0", self.root)
        set_version("v1.5.0", self.root)
        self.assertEqual(
            (self.root / "RELEASE.md").read_text(encoding="utf-8")
            .count("## v1.5.0"), 1)

    def test_reject_old_custom_suffix_and_malformed_versions(self):
        for invalid in ("v1.4.0-hu.8", "1.5.0", "v1.5", "v1.5.0-pre",
                        "v1.5.0; echo foo"):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                set_version(invalid, self.root)

    def test_hungarian_auto_update_points_to_own_build(self):
        import inspect
        from dreamevoice import aktualisierung
        self.assertEqual(
            inspect.signature(aktualisierung.pruefen)
                   .parameters["projekt_url"].default,
            "https://github.com/ZoleeBB/ZoleeDreameVoiceManager-HU")
        self.assertEqual(aktualisierung.EXE_NAME, "DreameSprachpaket-HU.exe")
        self.assertIn("EXE_NAME.lower()", inspect.getsource(aktualisierung.pruefen))
        self.assertNotIn("return None  # Release updates only through private GitHub Actions.",
                         inspect.getsource(aktualisierung.pruefen))
        # The original author credit remains unchanged.
        from dreamevoice import PROJEKT_URL
        self.assertIn("Anon365-Project", PROJEKT_URL)

    def test_support_section_stays_in_shared_app_header(self):
        source = (Path(__file__).resolve().parents[1] / "dreamevoice"
                  / "ui" / "app.py").read_text(encoding="utf-8-sig")
        self.assertIn('text="Támogatás"', source)
        self.assertIn('text="Ko-fi támogatás"', source)
        self.assertIn('text="Revolut-me támogatás"', source)
        self.assertIn("https://ko-fi.com/E1H8299KGN", source)
        self.assertIn("https://revolut.me/zoleebb", source)
        self.assertLess(source.index('text="Támogatás"'),
                        source.index("self.shell = NavShell(self, self.theme)"))


if __name__ == "__main__":
    unittest.main()
