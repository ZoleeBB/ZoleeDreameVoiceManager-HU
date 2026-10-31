"""Complete-coverage HU translation prompt and safe import regression tests."""
import tempfile
import unittest
from pathlib import Path

from dreamevoice.hu_translation import (
    MISSING, UNVERIFIED, export_prompt, parse_missing, uncovered_ids,
)
from dreamevoice.sounds import Sound, SoundCatalog


class MissingVoicePromptTests(unittest.TestCase):
    def setUp(self):
        self.catalog = SoundCatalog([
            Sound(id=1, de="Netzwerkfehler", en="Network error", group="Netzwerk"),
            Sound(id=2, de="Akku schwach", en="Battery low", group="Akku & Laden"),
            Sound(id=3, de="", en="", group="Sonstiges"),
            Sound(id=4, de="Wasser fehlt", en="Water missing", group="Basisstation"),
            Sound(id=5, de="", en="Dust bag full", group="Fehler & Wartung"),
        ])

    def test_includes_every_missing_official_id_not_every_catalog_id(self):
        official = [1, 2, 3, 5, 100]
        covered = {1: "Nem érem el a hálózatot", 100: "100 százalék"}
        self.assertEqual(uncovered_ids(official, covered), [2, 3, 5])

    def test_export_all_with_german_english_and_unknown_markers(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "missing.txt"
            p, missing, unknown = export_prompt(
                [1, 2, 3, 5], {1: "Már magyar"}, self.catalog, target
            )
            self.assertEqual((missing, unknown), (3, 1))
            text = p.read_text(encoding="utf-8")
            self.assertIn("2 | Akku & Laden; DE: Akku schwach; EN: Battery low | " + MISSING, text)
            self.assertIn("3 | NINCS ADAT", text)
            self.assertIn(UNVERIFIED, text)
            self.assertIn("5 | Fehler & Wartung; DE: -; EN: Dust bag full | ", text)
            self.assertNotIn("1 |", text)
            self.assertIn("# FELADAT AZ AI SZÁMÁRA", text)

    def test_export_never_overwrites_previous_ai_work(self):
        with tempfile.TemporaryDirectory() as temp:
            dest = Path(temp) / "edited.txt"
            dest.write_text("felhasználói fordítás", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                export_prompt([2], {}, self.catalog, dest)
            self.assertEqual(dest.read_text(encoding="utf-8"), "felhasználói fordítás")

    def test_import_only_missing_non_placeholder_real_ids(self):
        text = """\
# Translation
2 | Battery low | Merül az akkumulátorom.
3 | No description | [HANGMINTA ELLENŐRZÉSE SZÜKSÉGES]
4 | No | Vízhiány. Kérlek, ellenőrizd a tartályt!
5 | Dust bag full | Tele a porzsák. Cseréld ki!
6 | Extra | Nem létező hang.
1 | Old | Az eredeti magyar mondatot nem írhatod felül.
"""
        result = parse_missing(text, [1, 2, 3, 4, 5], {1: "Régi vicces magyar"})
        self.assertEqual(set(result.new), {2, 4, 5})
        self.assertEqual(result.skipped_existing, [1])
        self.assertEqual(result.skipped_unknown, [6])
        self.assertEqual(result.skipped_placeholder, [3])

    def test_import_rejects_duplicate_ids(self):
        text = "2 | Low | Merülök.\n2 | Low | Még mindig merülök.\n"
        with self.assertRaisesRegex(ValueError, "Ismétlődő"):
            parse_missing(text, [2], {})

    def test_import_keeps_embedded_pipe_in_spoken_text(self):
        parsed = parse_missing("4 | label | Takarítok | már megint.", [4], {})
        self.assertEqual(parsed.new[4], "Takarítok | már megint.")

    def test_import_rejects_overlong_generated_content(self):
        with self.assertRaisesRegex(ValueError, "túl hosszú"):
            parse_missing("3 | unknown | " + "a" * 601, [3], {})

    def test_all_ids_no_missing(self):
        with tempfile.TemporaryDirectory() as temp:
            path, missing, unknown = export_prompt(
                [1, 2], {1: "A", 2: "B"}, self.catalog,
                Path(temp) / "finished.txt"
            )
            self.assertEqual((missing, unknown), (0, 0))
            self.assertNotIn("1 |", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
