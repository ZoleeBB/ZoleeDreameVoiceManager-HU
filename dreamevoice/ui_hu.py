"""Hungarian UI translations for Dreame Voice Manager (v1.4.0 overlay).

This module translates Tkinter presentation-bound text only. It does not
modify settings, credentials, device IDs, or voice package data.
"""
from __future__ import annotations

import functools
import re

_TRANSLATIONS = {
  "Dreame Sprachpaket-Manager": "Dreame hangcsomag-kezelő",
  "Fertige Stimmen": "Kész hangok",
  "Aufnahmen einlesen": "Hangfelvételek importálása",
  "Dialekt erzeugen": "Hangcsomag készítése",
  "Einstellungen": "Beállítások",
  "Start": "Kezdőlap",
  "Verbindung": "Kapcsolat",
  "Hilfe": "Súgó",
  "Über": "Névjegy",
  "Schließen": "Bezárás",
  "Abbrechen": "Mégse",
  "Weiter": "Tovább",
  "Zurück": "Vissza",
  "Fertig": "Kész",
  "Öffnen": "Megnyitás",
  "Anmelden": "Bejelentkezés",
  "Abmelden": "Kijelentkezés",
  "Speichern": "Mentés",
  "Löschen": "Törlés",
  "Umbenennen": "Átnevezés",
  "Übernehmen": "Alkalmazás",
  "Erneut versuchen": "Újrapróbálás",
  "Jetzt herunterladen": "Letöltés most",
  "Noch nicht verbunden": "Még nincs kapcsolat",
  "Beim Hersteller-Konto anmelden": "Bejelentkezés a gyártói fiókba",
  "Anmelden und Roboter suchen": "Bejelentkezés és robot keresése",
  "Mit anderem Konto anmelden": "Bejelentkezés másik fiókkal",
  "Welcher Roboter?": "Melyik robot?",
  "Einen Moment": "Egy pillanat",
  "Auf dem Roboter": "A roboton",
  "Nachsehen, was er spricht": "Aktuális hang ellenőrzése",
  "Andere Stimme wählen": "Másik hang kiválasztása",
  "Originalstimme wiederherstellen": "Gyári hang visszaállítása",
  "Willkommen": "Üdvözlünk!",
  "Kein Roboter gefunden": "Nem található robot",
  "Fast geschafft": "Mindjárt kész",
  "Anmeldung fehlgeschlagen": "Sikertelen bejelentkezés",
  "Angaben fehlen": "Hiányzó adatok",
  "Nicht verbunden": "Nincs kapcsolat",
  "Nicht wiederhergestellt": "Nem sikerült a visszaállítás",
  "Originalpaket nicht geladen": "A gyári hangcsomag nincs betöltve",
  "Abfrage fehlgeschlagen": "Sikertelen lekérdezés",
  "Noch nichts Eigenes aufgespielt": "Még nincs saját hangcsomag telepítve",
  "Deutsch": "Német",
  "Angemeldet": "Bejelentkezve",
  "Region": "Régió",
  "selbst erkennen": "Automatikus felismerés",
  "Passwort auf diesem PC merken": "Jelszó megjegyzése ezen a gépen",
  "E-Mail": "E-mail",
  "Passwort": "Jelszó",
  "App": "Alkalmazás",
  "Name": "Név",
  "Modell": "Modell",
  "Geräte-ID": "Eszközazonosító",
  "Geräte-ID (did)": "Eszközazonosító (did)",
  "Aktive Stimme": "Aktív hang",
  "Dunkles Design": "Sötét megjelenés",
  "Diese App": "Az alkalmazás",
  "Herstellerkonto": "Gyártói fiók",
  "Gefundene Roboter": "Talált robotok",
  "Ausgewählter Roboter": "Kiválasztott robot",
  "Netzwerk fürs Aufspielen": "Hálózat a hangcsomag telepítéséhez",
  "PC-Adresse": "Számítógép címe",
  "Port": "Port",
  "Eigene URL": "Egyéni URL",
  "leer = automatisch ermitteln": "Üresen hagyva automatikus felismerés",
  "leer = freien Port wählen": "Üresen hagyva szabad port választása",
  "Dreame-Hilfeseite öffnen": "Dreame súgó megnyitása",
  "App weitergeben": "Alkalmazás továbbadása",
  "Persönliche Daten entfernen ...": "Személyes adatok törlése…",
  "Nicht angemeldet": "Nincs bejelentkezve",
  "Melde an ...": "Bejelentkezés…",
  "Zuletzt gespeicherter Roboter geladen": "A korábban mentett robot betöltve",
  "Angemeldet, aber kein Saugroboter gefunden": "Bejelentkezve, de nem található robotporszívó",
  "wird abgefragt ...": "Lekérdezés folyamatban…",
  "nicht abfragbar (Roboter im Standby?)": "Nem olvasható ki (a robot készenléti állapotban van?)",
  "Erledigt": "Elkészült",
  "Port unzulässig": "Érvénytelen port",
  "Adresse unvollständig": "Hiányos cím",
  "Noch keine Roboter geladen - melde dich oben an.": "Még nem töltöttünk be robotokat. Előbb jelentkezz be!",
  "Die App selbst, dein Konto, der Roboter und das Netz.": "Az alkalmazás, a fiókod, a robot és a hálózat beállításai.",
  "Datenordner öffnen": "Adatmappa megnyitása",
  "hier liegen Einstellungen, Pakete und Aufnahmen": "Itt találhatók a beállítások, hangcsomagok és felvételek",
  "Erste Schritte - die Tour noch einmal ansehen": "Első lépések – bemutató újraindítása",
  "So funktioniert es": "Így működik",
  "Ausführlich nachlesen": "Részletes útmutató",
  "Projektseite öffnen": "Projektoldal megnyitása",
  "Projektseite": "Projektoldal",
  "Trinkgeld dalassen (freiwillig)": "Fejlesztés támogatása (önkéntes)",
  "Ordner nicht geöffnet": "Nem sikerült megnyitni a mappát",
  "Aufräumen alter Fassungen fehlgeschlagen": "A régi verziók takarítása sikertelen",
  "Beim Beenden bricht das ab.": "Kilépéskor a művelet megszakad.",
  "Trotzdem beenden?": "Biztosan kilépsz?",
  "Technische Details:": "Technikai részletek:",
  "Technische Details": "Technikai részletek",
  "Welche Stimme?": "Melyik hang?",
  "Welche Stimme": "Melyik hang",
  "Keine Stimme gewählt": "Nincs hang kiválasztva",
  "Aussuchen, anhören, aufspielen": "Kiválasztás, meghallgatás és telepítés",
  "▶ Anhören": "▶ Meghallgatás",
  "■ Stopp": "■ Leállítás",
  "Anhören": "Meghallgatás",
  "Aufspielen": "Telepítés a robotra",
  "Aufspielen?": "Telepíted a robotra?",
  "Auf den Roboter bringen": "Telepítés a robotra",
  "Abbruch angefordert ...": "Megszakítás kérése…",
  "Abgebrochen": "Megszakítva",
  "Nicht aufgespielt": "Nem sikerült a telepítés",
  "Erfolgreich aufgespielt": "Sikeresen telepítve",
  "Übertragen, nicht bestätigt": "Átmásolva, de nincs visszaigazolás",
  "Probe fehlgeschlagen": "Sikertelen hangpróba",
  "Probe abgebrochen.": "Hangpróba megszakítva.",
  "Es steht noch keine fertige Stimme bereit.": "Még nincs elérhető kész hang.",
  "Du willst eine eigene Stimme?": "Saját hangot szeretnél?",
  "Eigene Stimme": "Saját hang",
  "fertiges Paket": "Kész hangcsomag",
  "noch keine": "Még nincs",
  "Grundlage": "Alapcsomag",
  "Größe": "Méret",
  "Sprache": "Nyelv",
  "Prüfung": "Ellenőrzés",
  "Nicht gefunden": "Nem található",
  "Fortschritt": "Folyamat",
  "Protokoll anzeigen": "Napló megjelenítése",
  "Protokoll ausblenden": "Napló elrejtése",
  "Protokoll": "Napló",
  "Einzelne Ansagen": "Egyedi bemondások",
  "Eigene oder heruntergeladene Aufnahmen einlesen": "Saját vagy letöltött felvételek importálása",
  "Aufnahmen oder Paket einlesen ...": "Hangfelvételek vagy csomag importálása…",
  "Ansagen einzeln austauschen ...": "Bemondások egyenkénti cseréje…",
  "Originalpaket als Grundlage:": "Gyári csomag alapként:",
  "Originalpaket fehlt": "Hiányzik a gyári hangcsomag",
  "Originalstimme": "Gyári hang",
  "wechseln": "Módosítás",
  "ffmpeg automatisch einrichten": "FFmpeg automatikus beállítása",
  "ffmpeg einrichten": "FFmpeg beállítása",
  "ffmpeg eingerichtet": "Az FFmpeg beállítva",
  "ffmpeg-Einrichtung fehlgeschlagen": "Az FFmpeg beállítása sikertelen",
  "Welcher Dialekt?": "Melyik beszédstílus?",
  "Dialekt": "Beszédstílus",
  "Eigene Textsammlung anlegen ...": "Saját szövegcsomag létrehozása…",
  "Texte ansehen und ändern": "Szövegek megtekintése és szerkesztése",
  "Paket erzeugen": "Hangcsomag létrehozása",
  "Kostprobe anhören": "Hangminta meghallgatása",
  "Kostprobe:": "Hangminta:",
  "Kostprobe": "Hangminta",
  "Texte als Dateien ausgeben": "Szövegek exportálása fájlba",
  "Texte aus Datei einlesen": "Szövegek importálása fájlból",
  "Ordner öffnen": "Mappa megnyitása",
  "Zwischenstand verwerfen": "Elkészült rész törlése",
  "Zwischenstand: noch nichts gesprochen.": "Állapot: még nincs elkészült felvétel.",
  "Keine Aufnahme": "Nincs hangfelvétel",
  "Noch nichts zugewiesen": "Még nincs hozzárendelt felvétel",
  "Ansagen einzeln austauschen": "Bemondások egyenkénti cseréje",
  "Original anhören": "Gyári hang meghallgatása",
  "Durchsuchen ...": "Tallózás…",
  "Suche": "Keresés",
  "Bereich": "Kategória",
  "nur die wichtigsten": "Csak a fontos bemondások",
  "nur bereits zugewiesene": "Csak a hozzárendelt felvételek",
  "Alle Zuweisungen löschen": "Összes hozzárendelés törlése",
  "Weitere anzeigen": "Továbbiak megjelenítése",
  "Paket aus diesen Ansagen bauen": "Csomag készítése a bemondásokból",
  "Vorlagenordner anlegen ...": "Mintamappa létrehozása…",
  "Keine Hörprobe": "Nincs hangminta",
  "Wiedergabe nicht möglich": "Nem sikerült lejátszani",
  "Diese Datei existiert nicht (mehr).": "Ez a fájl már nem létezik.",
  "Zu diesen Filtern gibt es keine Ansagen.": "Nincs a szűrőknek megfelelő bemondás.",
  "Alle Zuweisungen löschen?": "Törlöd az összes hozzárendelést?",
  "Wo soll der Vorlagenordner entstehen?": "Hová kerüljön a mintamappa?",
  "Vorlagenordner nicht angelegt": "Nem sikerült létrehozni a mintamappát",
  "Aktualisierung": "Frissítés",
  "Nach Aktualisierung suchen": "Frissítések keresése",
  "Jetzt nach Aktualisierung suchen": "Frissítés ellenőrzése most",
  "Beim Start nachsehen, ob es eine neuere Fassung gibt": "Új verzió keresése indításkor",
  "Sehe nach ...": "Ellenőrzés…",
  "Suche fehlgeschlagen": "A keresés sikertelen",
  "Lade ...": "Letöltés…",
  "Lade herunter ...": "Letöltés…",
  "Download abbrechen": "Letöltés megszakítása",
  "Bitte von Hand nachhelfen": "Kézi beavatkozás szükséges",
  "Nicht aktualisiert": "Nem sikerült frissíteni",
  "Neustart": "Újraindítás",
  "Setze die neue Fassung ein ...": "Az új verzió telepítése…",
  "Tour beenden": "Bemutató befejezése",
  "Schritt": "Lépés",
  "Zurück zur Übersicht": "Vissza az áttekintéshez",
  "Fehler": "Hiba",
  "Warnung": "Figyelmeztetés",
  "Information": "Információ",
  "Bereit": "Készen áll",
  "Verbunden": "Csatlakoztatva",
  "Erfolgreich": "Sikeres",
  "Spreche die Kostprobe ...": "A hangminta generálása…",
  "Kostprobe fertig": "Hangminta elkészült",
  "Bitte warten": "Kérlek, várj",
  "Keine Sprache gewählt": "Nem választottál nyelvet",
  "Kein Roboter gewählt": "Nem választottál robotot",
  "Nicht gespeichert": "Sikertelen mentés",
  "Neuer Name:": "Új név:",
  "Kein eigenes Paket": "Nincs saját hangcsomag",
  "Einlesen": "Importálás",
  "Erzeugen": "Létrehozás",
  "Keine kompatible Stimme": "Nincs megfelelő hang",
  "Wer spricht?": "Ki beszéljen?",
  "Windows-Sprachausgabe": "Windows felolvasás",
  "ElevenLabs": "ElevenLabs",
  "Zugangsschlüssel": "API-kulcs",
  "Verbinden und Stimmen laden": "Csatlakozás és hanglista betöltése",
  "Schlüssel holen": "API-kulcs létrehozása",
  "Schlüssel vergessen": "API-kulcs elfelejtése",
  "Klang der Stimme übernehmen": "A hang saját beállításainak használata",
  "Gleichmäßigkeit": "Stabilitás",
  "Ausdruck": "Kifejezőerő",
  "Stil": "Stílus",
  "Stimme": "Hang",
  "Tempo": "Sebesség",
  "Tonhöhe": "Hangmagasság",
  "Klang": "Hangzás",
  "Standard": "Alapértelmezett",
  "Vorlesen fehlgeschlagen": "A felolvasás sikertelen",
  "Zugangsschlüssel fehlt": "Hiányzó API-kulcs",
  "Keine bayerische Stimme": "Nem bajor hang",
  "ffmpeg fehlt": "Hiányzik az FFmpeg",
  "Name für dieses Paket": "A hangcsomag neve",
  "Bereite vor ...": "Előkészítés…",
  "Erst verbinden": "Előbb csatlakozz",
  "Kein Text": "Nincs szöveg",
  "In dieser Zeile steht nichts zum Vorlesen.": "Ebben a sorban nincs felolvasandó szöveg.",
  "Verbindung fehlgeschlagen": "A kapcsolódás sikertelen",
  "Nicht geladen.": "Nincs betöltve.",
  "Daten": "Adatok",
  "Auswahl": "Kiválasztás",
  "Optionen": "Beállítások",
  "Schriftgröße": "Betűméret",
  "Erste Schritte": "Első lépések",
  "Fertige Pakete": "Kész hangcsomagok",
  "Meine Pakete": "Saját hangcsomagok",
  "Eigene Pakete": "Saját csomagok",
  "Dialekttexte": "Bemondások szövege",
  "Ungültig": "Érvénytelen",
  "Speicherort": "Mentési hely",
  "Erneut laden": "Újratöltés",
  "Noch nichts": "Még semmi",
  "Datei auswählen": "Fájl kiválasztása",
  "Datei öffnen": "Fájl megnyitása",
  "Alle": "Összes",
  "Kein Gerät": "Nincs eszköz",
  "Seite": "Oldal",
  "Status": "Állapot",
  "Bestätigen": "Megerősítés",
  "Wirklich löschen?": "Biztosan törlöd?",
  "Wirklich beenden?": "Biztosan kilépsz?",
  "Ja": "Igen",
  "Nein": "Nem",
  "Herunterladen": "Letöltés",
  "wird geladen": "Betöltés alatt",
  "Offline": "Offline",
  "Online": "Online",
  "Nur Windows": "Csak Windows",
  "Konto": "Fiók",
  "Verfügbare Stimmen": "Elérhető hangok",
  "Ansagen": "Bemondások",
  "Fehler & Wartung": "Hibák és karbantartás",
  "Akku & Laden": "Akkumulátor és töltés",
  "Reinigung": "Takarítás",
  "Basisstation": "Dokkolóállomás",
  "Netzwerk": "Hálózat",
  "Sprachassistent": "Hangasszisztens",
  "Akkustand": "Akkumulátortöltöttség",
  "Sonstiges": "Egyéb"
}

def translate(value):
    """Translate UI-visible German strings; leave unrecognized data untouched."""
    if not isinstance(value, str) or not value:
        return value
    if value in _TRANSLATIONS:
        return _TRANSLATIONS[value]
    # Preserve user input and variable machine identifiers. Only substitute
    # presentation phrases, never arbitrary character patterns.
    result = value
    for de, hu in _TRANSLATIONS.items():
        if len(de) > 12 and de in result and not any(c in de for c in ("\\n", "\\t")):
            result = result.replace(de, hu)
    return result


def enable():
    """Install presentation-only hooks once before the first GUI is created."""
    import tkinter as tk
    from tkinter import ttk, messagebox, simpledialog, filedialog

    if getattr(tk, "_dreame_hu_enabled", False):
        return
    tk._dreame_hu_enabled = True

    widget_classes = (
        tk.Label, tk.Button, tk.Checkbutton, tk.Radiobutton, tk.LabelFrame,
        tk.Message, tk.Menubutton,
        ttk.Label, ttk.Button, ttk.Checkbutton, ttk.Radiobutton,
        ttk.LabelFrame, ttk.Menubutton,
    )
    for cls in widget_classes:
        orig_init = cls.__init__
        orig_configure = cls.configure
        @functools.wraps(orig_init)
        def _init(self, *args, __old=orig_init, **kwargs):
            if "text" in kwargs:
                kwargs["text"] = translate(kwargs["text"])
            return __old(self, *args, **kwargs)
        @functools.wraps(orig_configure)
        def _configure(self, cnf=None, __old=orig_configure, **kwargs):
            if isinstance(cnf, dict):
                cnf = dict(cnf)
                if "text" in cnf:
                    cnf["text"] = translate(cnf["text"])
            if "text" in kwargs:
                kwargs["text"] = translate(kwargs["text"])
            return __old(self, cnf, **kwargs)
        cls.__init__ = _init
        cls.configure = _configure
        cls.config = _configure

    def patch_method(cls, method, names):
        orig = getattr(cls, method)
        @functools.wraps(orig)
        def patched(self, *args, **kwargs):
            aa = list(args)
            if aa and isinstance(aa[0], str):
                aa[0] = translate(aa[0])
            for key in names:
                if key in kwargs:
                    kwargs[key] = translate(kwargs[key])
            return orig(self, *aa, **kwargs)
        setattr(cls, method, patched)

    # Dialogs, window titles and TreeView headers are not regular widget text.
    patch_method(tk.Wm, "wm_title", ())
    tk.Wm.title = tk.Wm.wm_title
    old_heading = ttk.Treeview.heading
    @functools.wraps(old_heading)
    def heading(self, column, *args, **kwargs):
        if "text" in kwargs:
            kwargs["text"] = translate(kwargs["text"])
        return old_heading(self, column, *args, **kwargs)
    ttk.Treeview.heading = heading

    for name in ("showinfo", "showwarning", "showerror", "askyesno", "askokcancel",
                 "askretrycancel", "askquestion", "askyesnocancel"):
        old = getattr(messagebox, name, None)
        if not old:
            continue
        @functools.wraps(old)
        def wrapped(*args, __old=old, **kwargs):
            a = list(args)
            for i in range(min(2, len(a))):
                a[i] = translate(a[i])
            for key in ("title", "message", "detail"):
                if key in kwargs:
                    kwargs[key] = translate(kwargs[key])
            return __old(*a, **kwargs)
        setattr(messagebox, name, wrapped)

    old_askstring = simpledialog.askstring
    @functools.wraps(old_askstring)
    def askstring(title, prompt, **kwargs):
        return old_askstring(translate(title), translate(prompt), **kwargs)
    simpledialog.askstring = askstring

    for name in ("askopenfilename", "askopenfilenames", "askdirectory",
                 "asksaveasfilename"):
        old = getattr(filedialog, name)
        @functools.wraps(old)
        def wrapped(*args, __old=old, **kwargs):
            if "title" in kwargs:
                kwargs["title"] = translate(kwargs["title"])
            if "filetypes" in kwargs:
                kwargs["filetypes"] = [(translate(t), ext)
                                      for t, ext in kwargs["filetypes"]]
            return __old(*args, **kwargs)
        setattr(filedialog, name, wrapped)
