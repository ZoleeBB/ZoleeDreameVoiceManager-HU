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

    def test_static_widget_text_coverage_report(self):
        """Report untranslated static German labels without touching runtime data."""
        import ast
        from pathlib import Path
        root = Path(__file__).resolve().parents[1] / "dreamevoice" / "ui"
        detected = []
        for file in root.glob("*.py"):
            tree = ast.parse(file.read_text(encoding="utf-8-sig"), filename=str(file))
            for node in ast.walk(tree):
                if not isinstance(node, ast.Call):
                    continue
                values = []
                for kw in node.keywords:
                    if kw.arg in ("text", "title", "message"):
                        values.append(kw.value)
                if isinstance(node.func, ast.Name) and node.func.id == "Card":
                    values.extend(node.args[2:4])
                for expr in values:
                    try:
                        value = ast.literal_eval(expr)
                    except (ValueError, TypeError, SyntaxError, MemoryError):
                        continue
                    if isinstance(value, str) and len(value) > 3 and value.strip():
                        translated = translate(value)
                        if translated == value and any(w in value.lower() for w in
                            ("stimme", "paket", "ansage", "herunter", "deine ", "die app",
                             "roboter", "werden", "kannst", "bitte", "klick", "deutsch",
                             "nicht", "gleich", "wieder", "unter ", "sprache")):
                            detected.append((file.name, expr.lineno, value))
        print("UNCOVERED STATIC GERMAN UI TEXTS:", len(detected))
        for name, line, value in detected[:85]:
            print(f"  {name}:{line}: {value[:160]!r}")
        self.assertTrue(root.is_dir())

    def test_non_strings_untouched(self):
        self.assertIsNone(translate(None))
        self.assertEqual(translate(123), 123)


if __name__ == "__main__":
    unittest.main()
