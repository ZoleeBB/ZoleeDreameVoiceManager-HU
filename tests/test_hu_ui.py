"""Hungarian-only presentation layer: never rewrite machine data."""
import unittest
from dreamevoice.ui_hu import translate


class HungarianUiTests(unittest.TestCase):
    def test_navigation_translated(self):
        self.assertEqual(translate("Fertige Stimmen"), "Kész hangok")
        self.assertEqual(translate("Aufnahmen einlesen"), "Hangfelvételek importálása")
        self.assertEqual(translate("Einstellungen"), "Beállítások")
        self.assertEqual(translate("Erweitert"), "Haladó")

    def test_dialogs_translated(self):
        self.assertEqual(translate("Nicht verbunden"), "Nincs kapcsolat")
        self.assertEqual(translate("Schließen"), "Bezárás")

    def test_long_help_paragraph_translated(self):
        self.assertIn("gyári", translate("Das offizielle Sprachpaket wird geholt"))

    def test_system_values_untouched(self):
        for s in ("eleven_flash_v2_5", "Jp9AlKVTDRYwWCf6uKqK",
                  "dreame.vacuum.r2532h", "http://192.168.2.1:9090/",
                  "Magyar – Vicces házimunkás"):
            self.assertEqual(translate(s), s)

    def test_translate_idempotent(self):
        for s in ("Anmelden", "Fertige Stimmen", "Wirklich löschen?"):
            self.assertEqual(translate(translate(s)), translate(s))

    def test_non_strings_untouched(self):
        self.assertIsNone(translate(None))
        self.assertEqual(translate(123), 123)


if __name__ == "__main__":
    unittest.main()
