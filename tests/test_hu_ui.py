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

    def test_new_translation_coverage(self):
        self.assertEqual(translate("ElevenLabs - echte Dialektaussprache"),
                         "ElevenLabs – természetes magyar kiejtés")
        self.assertEqual(translate("Text kopieren"), "Szöveg másolása")
        self.assertEqual(translate("Auf Standard zurücksetzen"),
                         "Alapértelmezett szövegek visszaállítása")
        self.assertEqual(translate("Revolut-me támogatás"),
                         "Revolut-me támogatás")
        self.assertEqual(translate("Webserver beendet."),
                         "A helyi webszerver leállt.")

    def test_remaining_german_tour_and_voice_labels(self):
        self.assertEqual(translate("✓ Das hast du schon erledigt."),
                         "✓ Ezt már elvégezted.")
        self.assertEqual(translate("    noch keine"), "    Még nincs")

    def test_update_and_login_texts(self):
        cases = [
            ("Nachsehen, ob es eine neuere Fassung gibt", "Ellenőrzés, hogy elérhető-e újabb verzió."),
            ("Diese Fassung:", "Jelenlegi verzió:"),
            ("Die App fragt bei GitHub nach der neuesten Fassung. Dabei wird nichts über dich oder deinen Roboter übermittelt - aber wie bei jedem Seitenaufruf sieht die Gegenseite deine IP-Adresse. Deshalb ist die Abfrage ausgeschaltet, solange du sie nicht einschaltest.", "Az alkalmazás a GitHubon ellenőrzi, hogy elérhető-e újabb verzió. Ennek során sem rólad, sem a robotodról nem továbbít adatot, de mint minden webes kérésnél, a másik oldal látja az IP-címedet. Ezért ez az ellenőrzés ki van kapcsolva, amíg be nem kapcsolod."),
            ("Gefunden wird nichts von selbst installiert. Die App zeigt, was neu ist, und fragt. Erst dann lädt sie die neue Datei, prüft ihre Prüfsumme und ersetzt sich selbst - ohne Installation, ohne Administratorrechte. Dein Datenordner bleibt unberührt.", "A program semmit nem telepít automatikusan. Megmutatja, mi új, és rákérdez. Csak ezután tölti le az új fájlt, ellenőrzi az ellenőrzőösszegét, majd lecseréli saját magát – telepítés és rendszergazdai jogosultság nélkül. Az adatmappád érintetlen marad."),
            ("Die App meldet sich mit denselben Zugangsdaten an, die du in deiner Handy-App benutzt - Dreamehome, MOVA Home oder Trouver. Welche es ist, stellst du unten unter 'App' ein. Die Daten gehen ausschließlich an Dreame (MOVA und Trouver gehören dazu), nicht an Dritte. Ohne Anmeldung kennt die App weder dein Robotermodell noch kann sie ihm etwas schicken.", "Az alkalmazás ugyanazokkal a bejelentkezési adatokkal lép be, amelyeket a mobilalkalmazásban használsz – Dreamehome, MOVA Home vagy Trouver. Hogy melyiket használod, azt lent az „Alkalmazás” mezőnél állíthatod be. Az adatok kizárólag a Dreame-hez kerülnek (a MOVA és a Trouver is ide tartozik), harmadik félhez nem. Bejelentkezés nélkül az alkalmazás nem ismeri a robotod típusát, és nem tud neki semmit küldeni."),
            ("E-Mail und Passwort wie in deiner Hersteller-App.", "Ugyanaz az e-mail-cím és jelszó, mint a gyártó alkalmazásában."),
            ("zeigen", "mutat"),
            ("Europa (Deutschland, Österreich, Schweiz)", "Európa (Németország, Ausztria, Svájc)"),
        ]
        for source, expected in cases:
            with self.subTest(source=source[:50]):
                self.assertEqual(translate(source), expected)

    def test_hungarian_progress_logs(self):
        self.assertEqual(
            translate("Erzeuge Dialektpaket: Magyar – Vicces házimunkás"),
            "Magyar hangcsomag készítése: Magyar – Vicces házimunkás")
        self.assertEqual(
            translate("Spreche 181 von 181 Ansagen auf Magyar – Vicces házimunkás ..."),
            "181 / 181 bemondás generálása: Magyar – Vicces házimunkás…")
        self.assertIn("23 / 181",
            translate("Kontingent aufgebraucht nach 23 von 181 Ansagen."))
        self.assertEqual(
            translate("Warte bis zu 120 Sekunden auf den Download ..."),
            "Legfeljebb 120 másodpercig várok a robot letöltésére…")

    def test_machine_data_preserved_in_mixed_logs(self):
        self.assertIn(
            "Magyar_HU_Elison_2.tar.gz",
            translate("Paket:  Magyar_HU_Elison_2.tar.gz"))
        self.assertIn("eleven_flash_v2_5",
                      translate("eleven_flash_v2_5"))

    def test_unavailable_page_dialog_is_fully_hungarian(self):
        self.assertEqual(translate("Kész hangok geht noch nicht"),
                         "Kész hangok még nem használható")
        self.assertEqual(
            translate("Dafür muss die App erst wissen, welches Modell dein "
                      "Roboter ist. Melde dich auf der Startseite an."),
            "Először jelentkezz be a Kezdőlapon, hogy a program felismerje a robotod modelljét.")
        self.assertIn(
            "gyári hangcsomagja",
            translate("Dafür fehlt noch das offizielle Sprachpaket deines "
                      "Roboters. Es wird auf der Startseite einmalig geholt."))

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

    def test_windows_tk_widgets_translate_in_real_ui(self):
        """Exercise the actual tkinter constructors and live updates on CI."""
        import os
        if os.name != "nt":
            self.skipTest("Windows GUI runner required")
        import tkinter as tk
        from tkinter import ttk
        from dreamevoice.ui_hu import enable

        enable()
        enable()  # Installing the hooks twice must not stack wrappers.
        root = tk.Tk()
        root.withdraw()
        try:
            root.title("Dreame Sprachpaket-Manager")
            self.assertEqual(root.title(), "Dreame hangcsomag-kezelő")
            label = ttk.Label(root, text="Einstellungen")
            self.assertEqual(label.cget("text"), "Beállítások")
            button = ttk.Button(root, text="Fertige Stimmen")
            self.assertEqual(button.cget("text"), "Kész hangok")
            button.configure(text="Abbrechen")
            self.assertEqual(button.cget("text"), "Mégse")
        finally:
            root.destroy()

    def test_non_strings_untouched(self):
        self.assertIsNone(translate(None))
        self.assertEqual(translate(123), 123)


if __name__ == "__main__":
    unittest.main()
