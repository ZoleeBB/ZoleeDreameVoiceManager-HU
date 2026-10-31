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

_TRANSLATIONS.update({
  "Eigene Stimmen für Dreame-Saugroboter - entwickelt und geprüft am X50 Ultra Complete": "Saját hangok Dreame robotporszívókhoz – Dreame X50 Ultra Complete modellen fejlesztve és ellenőrizve.",
  "Dieselben Zugangsdaten wie in deiner Handy-App": "Ugyanazokat az adatokat add meg, mint a telefonos alkalmazásban.",
  "Die Daten gehen ausschließlich an Dreame und werden im Windows-Tresor abgelegt, nicht in einer Datei. Es gibt kein Konto bei diesem Programm und keine Weitergabe an Dritte.": "A bejelentkezési adatokat kizárólag a Dreame kapja meg; a jelszót a Windows hitelesítőadat-tárolója védi. Ez a program nem hoz létre külön fiókot, és nem adja tovább az adatokat.\n\nHa a Dreamehome alkalmazásban Google-fiókkal lépsz be, előbb állíts be külön Dreamehome-jelszót a fiókbeállításokban. Itt a Dreamehome e-mail-címét és saját jelszavát használd, nem a Google-fiókod jelszavát.",
  "Das offizielle Sprachpaket wird geholt": "A gyári hangcsomag letöltése folyamatban.",
  "Jedes eigene Paket entsteht als Kopie des offiziellen - nur so bleibt keine Ansage auf der Strecke. Deshalb wird es einmalig heruntergeladen und danach wiederverwendet.": "A saját hangcsomag a gyári csomagra épül, ezért nem tűnnek el a hiányzó bemondások. A gyári csomagot egyszer letöltjük, később újra felhasználjuk.",
  "Aussuchen, anhören, aufspielen - für jede Stimme gleich. Jede landet an derselben Stelle im Roboter und ersetzt die vorige.": "Válaszd ki a hangot, hallgasd meg, majd telepítsd a robotra. Az új hang mindig az előző egyéni hang helyére kerül.",
  "Jede neue Stimme ersetzt die vorige. Die Werksstimme wird dabei nicht gelöscht - ein Klick auf der Startseite („Originalstimme wiederherstellen“) holt sie zurück.": "Minden új hang lecseréli a korábbi egyéni hangot. A gyári hang nem törlődik: a Kezdőlapon a „Gyári hang visszaállítása” gombbal bármikor visszaállítható.",
  "Dafür müssen dieser PC und der Roboter im selben Netz hängen - kein Gast- oder IoT-WLAN - und die Windows-Firewall muss die App ins private Netzwerk lassen. Klappt das nicht, hilft „Eigene URL“ unter „Einstellungen“.": "A számítógépnek és a robotnak ugyanazon a helyi hálózaton kell lennie, és a Windows tűzfalának engedélyeznie kell a programot a privát hálózaton. Ha ez nem működik, a Beállítások → Egyéni URL segíthet.",
  "Aufnahmen, die du schon hast - selbst gesprochen oder heruntergeladen - werden zu einer Stimme für deinen Roboter. Das fertige Paket steht danach unter „Fertige Stimmen“.": "A saját vagy letöltött hangfelvételekből a robothoz használható hangcsomagot állíthatsz össze. Az elkészült csomag a „Kész hangok” oldalon lesz elérhető.",
  "Die App spricht die Ansagen selbst - in einem Dialekt deiner Wahl. Das fertige Paket steht danach unter „Fertige Stimmen“.": "A program a kiválasztott hanggal felolvassa a bemondásokat és hangcsomagot készít. Az eredmény a „Kész hangok” oldalon jelenik meg.",
  "Fertig gesprochene Ansagen - ganze Sätze auf einmal oder Ansage für Ansage.": "Kész felvételek importálása egyszerre vagy bemondásonként.",
  "'Aufnahmen oder Paket einlesen' nimmt einen ganzen Satz entgegen: eine ZIP-Datei mit Aufnahmen, ein fertiges .tar.gz-Sprachpaket oder einen Ordner voller mp3-, wav- oder ogg-Dateien. Die Zahl im Dateinamen ist die Ansage-Nummer. Fremde Pakete werden vorher geprüft.\n\n'Ansagen einzeln austauschen' öffnet die Liste aller Ansagen: anhören, eine eigene Datei zuweisen, fertig. Aus den Zuweisungen baut dieselbe Schaltfläche dort das Paket.\n\nBeides landet als fertiges Paket in deiner Sammlung und steht danach unter „Fertige Stimmen“ zum Aufspielen bereit.": "A „Hangfelvételek vagy csomag importálása” gomb ZIP-archívumot, kész .tar.gz hangcsomagot vagy MP3-, WAV-, OGG-fájlokat tartalmazó mappát fogad. A fájlnévben lévő szám a bemondás azonosítója. Az idegen hangcsomagokat importálás előtt ellenőrizzük.\n\nA „Bemondások egyenkénti cseréje” gombbal meghallgathatod a gyári hangokat, és külön fájlokat rendelhetsz hozzájuk. Ezekből is készíthető teljes csomag.\n\nAz elkészült hangokat a „Kész hangok” oldalon tudod telepíteni a robotra.",
  "Die App hat die Ansagen im jeweiligen Dialekt aufgeschrieben und lässt sie hier sprechen. Mit der Windows-Stimme läuft das offline und kostenlos, klingt aber nach Hochdeutsch; für echten Dialekt in der Aussprache lässt sich auf ElevenLabs umschalten (eigenes Konto).": "A program előkészíti a bemondások szövegét, és a kiválasztott hanggal felolvastatja. A Windows-felolvasás ingyenes és offline; természetesebb magyar kiejtéshez az ElevenLabs is választható (saját fiókkal).",
  "Unter 'Eigene Textsammlung anlegen' entstehen eigene Texte - etwa im Stil einer Filmfigur. Sie verhält sich wie ein Dialekt: anhören, Texte ändern, mit jeder Stimme erzeugen, nach aufgebrauchtem Kontingent fortsetzen.": "A „Saját szövegcsomag létrehozása” funkcióval saját karaktert készíthetsz. Szerkesztheted, meghallgathatod és bármely támogatott hanggal legenerálhatod; elfogyott keret esetén később folytathatod.",
  "Die Kostprobe spricht drei Sätze mit der gerade gewählten Stimme und spielt sie ab - so hörst du vorher, ob dir das Ergebnis gefällt. Bei ElevenLabs kostet sie gut 100 Zeichen aus dem Monatskontingent.\nUnter 'Texte ansehen und ändern' kannst du jede Ansage umformulieren. Deine Fassung bleibt gespeichert; bereits gesprochene Aufnahmen geänderter Ansagen werden verworfen und beim nächsten Erzeugen neu aufgenommen.\nFür größere Überarbeitungen liegt jeder Dialekt auch als Textdatei im Datenordner: kopieren, von einer Sprach-KI verbessern lassen, zurück in die Datei einfügen und wieder einlesen.": "A hangpróba három mondatot olvas fel a kiválasztott hanggal. ElevenLabs használatakor ez kreditet fogyaszt.\nA „Szövegek megtekintése és szerkesztése” gombbal bármely bemondást átírhatod. A módosítások megmaradnak; csak a megváltoztatott bemondások hangját kell újragenerálni.\nNagyobb szerkesztéshez a szövegek fájlba exportálhatók, majd módosítás után visszaimportálhatók.",
  "Noch keine Roboter geladen - melde dich oben an.": "Még nem töltöttünk be robotokat. Előbb jelentkezz be!",
  "Die App selbst, dein Konto, der Roboter und das Netz.": "Az alkalmazás, a fiók, a robot és a hálózat beállításai.",
  "(nur unter Windows verfügbar)": "(csak Windows alatt érhető el)",
  "(verschlüsselt mit deinem Windows-Konto)": "(a Windows-fiókoddal titkosítva)",
  "Die ausführlichen Anleitungen liegen im Ordner": "A részletes útmutatók a mappában találhatók:",
  "Öffnet sich im Browser.": "Böngészőben nyílik meg.",
  "Freiwillig, ohne Gegenleistung - die App bleibt": "A támogatás önkéntes, ellenszolgáltatás nélkül. Az alkalmazás továbbra is",
  "Erweitert": "Haladó",
  "Dialekte zum Selbersprechen": "Választható beszédstílusok",
  "zum Selbersprechen": "saját hanggeneráláshoz",
  "Keine deutsche oder ungarische Sprachausgabe installiert.": "Nincs telepített német vagy magyar Windows-felolvasóhang.",
  "Kein kompatibles Modell vorhanden": "Nincs megfelelő modell",
  "Keine bayerische Stimme": "Nem bajor hang",
  "Bitte von Hand nachhelfen": "Kézi beavatkozás szükséges",
  "Kein Roboter gefunden": "Nem található robot",
  "Bei den Aufnahmen": "A hangfelvételekben",
  "Einen Moment warten und erneut versuchen.": "Várj egy kicsit, majd próbáld újra.",
  "Die Originalstimme bleibt unberührt": "A gyári hang megmarad",
  "Die Stimme einer real existierenden Person nachzubilden": "Valós személy hangjának utánzása"
})

_DYNAMIC = [
    (r"^Schritt (\d+) von (\d+)$", r"\1. lépés / \2"),
    (r"^Weitere (\d+) anzeigen$", r"További \1 megjelenítése"),
    (r"^(\d+) von (\d+) Ansagen zugewiesen$", r"\1 / \2 bemondás hozzárendelve"),
    (r"^(\d+) Ansagen$", r"\1 bemondás"),
    (r"^(\d+) von (\d+) Ansagen gesprochen$", r"\1 / \2 bemondás elkészült"),
    (r"^(\d+) Ansagen angehört\.", r"\1 bemondás meghallgatva."),
    (r"^Version (.+) ist da\.?$", r"Elérhető a(z) \1 verzió."),
    (r"^Version (.+) ist bereit\.?$", r"A(z) \1 verzió készen áll."),
    (r"^(\d+) Dialekte zum Selbersprechen", r"\1 választható beszédstílus"),
    (r"^Angemeldet \(([^)]+)\)$", r"Bejelentkezve (\1)"),
    (r"^Lade ffmpeg herunter \(etwa (\d+) MB\) \.\.\.$",
     r"FFmpeg letöltése (kb. \1 MB)…"),
    (r"^Lade (.+) \.\.\.$", r"\1 letöltése…"),
    (r"^Zwischenstand: (\d+) von (\d+) Ansagen gesprochen",
     r"Állapot: \1 / \2 bemondás elkészült"),
    (r"^Kostprobe fertig - (\d+) Sätze$",
     r"Hangminta elkészült – \1 mondat"),
    (r"^Bereit: (.+) \((\d+) KB\)$",
     r"Készen áll: \1 (\2 KB)"),
    (r"^(.+) ist die neueste Fassung\.$",
     r"A(z) \1 a legfrissebb verzió."),
]
_DYNAMIC = [(re.compile(pattern), replacement) for pattern, replacement in _DYNAMIC]


_TRANSLATIONS.update({
  "Mit dieser App gibst du deinem Saugroboter eine andere Stimme - zum Beispiel Bayerisch oder Wienerisch.\n\nDiese Tour führt dich in acht Schritten hin. Du machst dabei alles selbst: Was du anklicken sollst, leuchtet in der App auf. Ist es erledigt, geht die Tour von allein weiter.\n\nKeine Sorge: Am Roboter passiert nichts, was sich nicht mit einem Klick rückgängig machen lässt. Beenden kannst du die Tour jederzeit, unter „Hilfe“ findest du sie wieder.": "Ezzel az alkalmazással saját hangot adhatsz a robotporszívódnak – például vicces magyar bemondásokat.\n\nEz a bemutató nyolc lépésen keresztül vezet végig a beállításon. Mindent te végzel el, a következő kattintandó elem ki lesz emelve. Ha teljesítetted a feladatot, a bemutató automatikusan folytatódik.\n\nA változtatások visszaállíthatók. A bemutatót bármikor bezárhatod, később a Súgóból újraindíthatod.",
  "Willkommen": "Üdvözlünk!",
  "Melde dich mit denselben Zugangsdaten an, die du in der App auf deinem Handy benutzt - Dreamehome, MOVA Home oder Trouver.\n\nSetz den Haken bei „Passwort auf diesem PC merken“, dann musst du das nur einmal tun. Das Passwort liegt verschlüsselt im Windows-Tresor, nicht in einer Datei.": "Jelentkezz be azzal a fiókkal, amelyet a telefonos Dreamehome, MOVA Home vagy Trouver alkalmazásban is használsz.\n\nJelöld be a „Jelszó megjegyzése ezen a gépen” lehetőséget, ha nem szeretnél minden alkalommal bejelentkezni. A jelszót a Windows biztonságos hitelesítőadat-tárolója őrzi.",
  "Anmelden": "Bejelentkezés",
  "Gib E-Mail und Passwort ein und klick auf „Anmelden und Roboter suchen“.": "Add meg az e-mail-címed és a jelszavad, majd kattints a „Bejelentkezés és robot keresése” gombra.",
  "Hast du mehrere Roboter, wählst du hier deinen aus. Bei nur einem nimmt die App ihn von selbst.\n\nDanach lädt sie einmalig die Werksstimme deines Modells herunter. Sie ist die Grundlage für jede neue Stimme - so fehlt später keine einzige Ansage.": "Ha több robotod van, válaszd ki azt, amelyiknek új hangot szeretnél adni. Egyetlen robot esetén a program automatikusan kiválasztja.\n\nEzután egyszer letölti a robot gyári hangcsomagját, amely minden új csomag alapja. Így egyetlen fontos bemondás sem tűnik el.",
  "Roboter wählen": "Robot kiválasztása",
  "Wähl deinen Roboter aus und warte, bis die Werksstimme geladen ist.": "Válaszd ki a robotot, majd várd meg a gyári hangcsomag letöltését.",
  "Unter „Fertige Stimmen“ steht alles, was du sofort aufspielen kannst.\n\nKlick eine Stimme in der Liste an und dann auf „Anhören“ - du hörst ein paar typische Ansagen, gleich hier am PC. Auf den Roboter kommt dabei noch nichts.": "A „Kész hangok” oldalon láthatod a telepíthető hangcsomagokat.\n\nVálassz egyet a listából, majd kattints a „Meghallgatás” gombra. Néhány jellemző bemondást a számítógépen hallhatsz meg; ettől még semmi nem kerül fel a robotra.",
  "Eine Stimme anhören": "Hang meghallgatása",
  "Such dir eine Stimme aus und klick auf „Anhören“.": "Válassz egy hangot, majd kattints a „Meghallgatás” gombra.",
  "Gefällt dir die Stimme, klick auf „Aufspielen“. Der Roboter holt sie sich dann selbst; das dauert ein bis zwei Minuten.\n\nDu musst das nicht jetzt tun - „Weiter“ geht auch ohne.": "Ha tetszik a kiválasztott hang, kattints a „Telepítés a robotra” gombra. A robot letölti és beállítja a hangcsomagot.\n\nEzt most át is ugorhatod: a „Tovább” gombbal telepítés nélkül léphetsz tovább.",
  "Aufspielen": "Telepítés a robotra",
  "Wenn du magst: „Aufspielen“ klicken und kurz warten.": "Ha szeretnéd, telepítsd a hangot a robotra, majd lépj tovább.",
  "Wähle in der App auf deinem Handy danach keine Sprache aus. Sonst lädt der Roboter seine alte Stimme nach und deine ist wieder weg.\n\nMeldet die Handy-App, Roboter und App hätten verschiedene Spracheinstellungen, ist das kein Fehler - im Gegenteil: Genau daran erkennst du, dass deine neue Stimme läuft.": "Miután telepítetted a saját hangot, ne válassz új beszédhangot a telefonos alkalmazásban, mert a robot ezzel felülírhatja.\n\nHa a telefonos alkalmazás a robot és az alkalmazás eltérő nyelvbeállítására figyelmeztet, az önmagában nem hiba: a CUSTOM hangcsomag külön azonosítóval működik.",
  "Danach wichtig": "Fontos teendő a telepítés után",
  "Unter „Erweitert“ geht mehr. Mit „Aufnahmen oder Paket einlesen“ übernimmst du Aufnahmen, die du selbst gemacht oder heruntergeladen hast - auch einzelne Ansagen lassen sich austauschen. Fremde Pakete prüft die App vorher auf Schadcode, und auf den Roboter kommt davon nur der Ton.\n\nGleich darunter steht „Dialekt erzeugen“: Da spricht die App die Ansagen selbst, in einem Dialekt deiner Wahl.": "A „Haladó” részben importálhatsz saját vagy letöltött hangfelvételeket a „Hangfelvételek vagy csomag importálása” funkcióval. Egyes bemondásokat külön is lecserélhetsz. Az idegen csomagokat a program ellenőrzi, és a robotra kizárólag hanganyag kerül.\n\nA „Hangcsomag készítése” oldalon saját szövegeket mondathatsz fel Windows TTS-sel vagy ElevenLabs-hanggal.",
  "Eigene Stimmen": "Saját hangcsomagok",
  "Willst du die ursprüngliche Stimme zurück, klick auf der Startseite auf „Originalstimme wiederherstellen“. Der Roboter holt sie direkt bei Dreame - dieser PC ist dabei gar nicht beteiligt. Jetzt musst du ihn natürlich nicht drücken.\n\nDas war's schon. Diese Tour findest du jederzeit unter „Hilfe“. Viel Spaß mit der neuen Stimme!": "Az eredeti gyári hang visszaállításához nyisd meg a Kezdőlapot, és kattints a „Gyári hang visszaállítása” gombra. A robot közvetlenül a gyártótól tölti le a gyári hangcsomagot; a számítógép nem szükséges hozzá.\n\nEnnyi az egész! A bemutatót bármikor újra megtalálod a Súgóban. Jó szórakozást az új magyar hanghoz!",
  "Zurück zur Werksstimme": "A gyári hang visszaállítása"
})


# Additional HU labels, modal titles, status messages and log fragments.
# Presentation-only translations; do not change device identifiers or data.
_TRANSLATIONS.update({
  "ElevenLabs - echte Dialektaussprache": "ElevenLabs – természetes magyar kiejtés",
  "   Zugangsschlüssel": "   API-kulcs",
  "   Stimme": "   Hang",
  "Stimmen-Bibliothek durchsuchen": "Hangkönyvtár böngészése",
  "   Eigene Stimmen-ID": "   Egyéni hangazonosító",
  "(in ElevenLabs: drei Punkte an der Stimme > Copy Voice ID)": "(ElevenLabs: a hang melletti három pont → Hangazonosító másolása)",
  "   Gleichmäßigkeit": "   Stabilitás",
  "   Ausdruck": "   Kifejezőerő",
  "   Tempo": "   Sebesség",
  "   Tonhöhe": "   Hangmagasság",
  "   Schlüssel ist nicht gespeichert.": "   Az API-kulcs nincs elmentve.",
  "   Schlüssel entfernt.": "   Az API-kulcs törölve.",
  "Verbinde ...": "Kapcsolódás…",
  "   Hole die Stimme ...": "   Hangadatok betöltése…",
  "   Durchsuche die Stimmenbibliothek ...": "   Hangkönyvtár keresése…",
  "bei ElevenLabs anhören": "Meghallgatás az ElevenLabs oldalán",
  "Ausgewählte Stimme übernehmen": "Kiválasztott hang használata",
  "Zugangsschlüssel holen": "API-kulcs létrehozása",
  "Vorgang abgebrochen.": "A művelet megszakítva.",
  "Wird abgebrochen ...": "Megszakítás folyamatban…",
  "Abbruch angefordert. Was schon gesprochen ist, ": "Megszakítás kérve. A már elkészült bemondások ",
  "Die Anmeldung hat geklappt, aber in diesem Konto ": "A bejelentkezés sikerült, de ebben a fiókban ",
  "zuletzt von hier aufgespielt - was er gerade spricht, ": "korábban innen telepített hang – hogy most mit mond, ",
  "Noch nichts Eigenes aufgespielt - der Roboter spricht ": "Még nem telepítettél saját hangot – a robot ",
  "Vom Benutzer abgebrochen. Hatte der Roboter ": "A felhasználó megszakította. Ha a robot már ",
  "Vom Benutzer abgebrochen. Auf dem Roboter ": "A felhasználó megszakította. A roboton ",
  "Abgebrochen.": "Megszakítva.",
  "Fehlgeschlagen": "Sikertelen",
  "Auf Standard zurücksetzen": "Alapértelmezett szövegek visszaállítása",
  "Zurücksetzen": "Visszaállítás",
  "Text kopieren": "Szöveg másolása",
  "Kopiert": "Másolva",
  "Design wechseln": "Megjelenés váltása",
  "Einstellungen nicht gespeichert": "Nem sikerült menteni a beállításokat",
  "unbekannt": "ismeretlen",
  "eine Stimme aus dieser App": "az alkalmazásból származó hang",
  "Spiele ab ...": "Lejátszás…",
  "ZIP oder Paketdatei wählen": "ZIP vagy hangcsomag kiválasztása",
  "Ordner mit den Aufnahmen wählen": "Hangfelvételek mappájának kiválasztása",
  "Überarbeitete Dialekttexte einlesen": "Átszerkesztett bemondások importálása",
  "Liste wird aufgebaut ...": "Lista összeállítása…",
  "Prüfe ...": "Ellenőrzés…",
  "Nicht eingelesen": "Nincs importálva",
  "Lese ein ...": "Importálás folyamatban…",
  "Nichts gefunden": "Nincs találat",
  "Wandle um und baue ...": "Hangok átalakítása és csomag összeállítása…",
  "Abgebrochen - es wurde kein Paket angelegt.": "Megszakítva – nem készült új hangcsomag.",
  "Kostprobe fehlgeschlagen": "Nem sikerült a hangminta",
  "Keine deutsche Stimme": "Nincs megfelelő német vagy magyar hang",
  "Spreche die Ansagen ...": "Bemondások generálása…",
  "Auftrag angenommen.": "A telepítési kérést a robot elfogadta.",
  "Webserver beendet.": "A helyi webszerver leállt.",
  "Der Roboter hat das Sprachpaket nicht abgeholt.": "A robot nem töltötte le a hangcsomagot.",
  "Der Roboter kennt den Sprachpaket-Dienst.": "A robot támogatja a hangcsomag-telepítést.",
  "Sende Installationsauftrag über die Dreame-Cloud ...": "Telepítési kérés küldése a Dreame-felhőn keresztül…",
  "Frage beim Roboter nach, ob er Sprachpakete auf dem üblichen Weg entgegennimmt ...": "A hangcsomag-telepítés támogatásának ellenőrzése…",
  "Übertrage auf den Roboter": "Átvitel a robotra",
  "Warte auf den Download": "Várakozás a robot letöltésére…",
  "Bereite Audiodateien vor ...": "Hangok előkészítése…",
  "Baue Archiv auf Basis des Originalpakets ...": "Hangcsomag összeállítása a gyári csomag alapján…",
  "Kontingent aufgebraucht": "Elfogyott az ElevenLabs-kreditkeret",
  "Sprachdienst": "Beszédszolgáltatás",
  "Ausgewählte Stimme": "Kiválasztott hang",
  "Einlesen fehlgeschlagen": "Az importálás sikertelen",
  "Paket nicht gebaut": "Nem sikerült elkészíteni a hangcsomagot",
  "Aufnahmen einlesen?": "Importálod a hangfelvételeket?",
  "Dieses Paket gibt es schon": "Ez a hangcsomag már létezik",
  "Ersetzen": "Felülírás",
  "Danebenlegen": "Új változat készítése",
  "Fertig gesprochen": "Előre generált hangok",
  "Frei verfügbare Stimmen": "Szabadon használható hangok",
  "Eigene Stimmen": "Saját hangok",
  "Aufnahmen oder fertiges Paket": "Hangfelvételek vagy kész hangcsomag",
  "Vom Benutzer abgebrochen.": "A felhasználó megszakította a műveletet.",
  "Zeichen": "Karakter",
  "Alle Ansagen": "Összes bemondás",
  "Stimmen-Bibliothek": "Hangkönyvtár",
})

# Fully anchored German messages composed dynamically by the application.
# Keep user-provided names, numbers, paths and API identifiers unchanged.
_DYNAMIC.extend((re.compile(a), b) for a, b in [
    (r"^Erzeuge Dialektpaket: (.+)$", r"Magyar hangcsomag készítése: \1"),
    (r"^Spreche (\d+) von (\d+) Ansagen auf (.+?)( \.\.\.)?$",
     r"\1 / \2 bemondás generálása: \3…"),
    (r"^Kontingent aufgebraucht nach (\d+) von (\d+) Ansagen\.$",
     r"A hanggenerálás \1 / \2 bemondásnál megszakadt a kreditkeret miatt."),
    (r"^(\d+) von (\d+) Ansagen konnten nicht gesprochen werden(.+)$",
     r"\1 / \2 bemondás nem készült el\3"),
    (r"^(\d+) Ansagen umgewandelt\.$",
     r"\1 bemondás átalakítva."),
    (r"^(\d+) Originalansagen gemessen (.*)$",
     r"\1 gyári bemondás hangereje megmérve: \2"),
    (r"^(\d+) von (\d+) Originalansagen gemessen(.*)$",
     r"\1 / \2 gyári bemondás hangereje megmérve\3"),
    (r"^Hinweis: (\d+) Ansagen fehlen noch(.+)$",
     r"Megjegyzés: még \1 bemondás hiányzik\2"),
    (r"^Spreche (.+) auf (.+) \.\.\.$",
     r"\1 felolvasása, beszédstílus: \2…"),
    (r"^Fertig: (.+?) - ([\d.]+) MB, (\d+) von (\d+) Ansagen ersetzt$",
     r"Elkészült: \1 – \2 MB, \3 / \4 bemondás lecserélve"),
    (r"^(\d+) von (\d+) Ansagen ersetzt$",
     r"\1 / \2 bemondás lecserélve"),
    (r"^Warte bis zu (\d+) Sekunden auf den Download \.\.\.$",
     r"Legfeljebb \1 másodpercig várok a robot letöltésére…"),
    (r"^Eingestellte Lautstärke: (\d+)$",
     r"Beállított hangerő: \1"),
    (r"^Paket:  (.+)$", r"Hangcsomag: \1"),
    (r"^Größe: (\d+) Bytes.*$", r"Méret: \1 bájt"),
    (r"^Kennung: (.+)$", r"Azonosító: \1"),
    (r"^Grundlage: (.+?), (\d+) Ansagen\.$",
     r"Alapcsomag: \1, \2 bemondás."),
    (r"^Grundlage ist jetzt (.+)\.$",
     r"Az alapcsomag mostantól: \1."),
    (r"^Lade (.+?) herunter \.\.\.$",
     r"\1 letöltése…"),
    (r"^Lese (.+) ein \.\.\.$", r"\1 importálása…"),
    (r"^Prüfung von (.+):$", r"\1 ellenőrzése:"),
    (r"^Baue Paket aus (\d+) Aufnahmen \.\.\.$",
     r"Hangcsomag építése \1 felvételből…"),
    (r"^Fertig - (\d+) Ansagen$", r"Elkészült – \1 bemondás"),
    (r"^(\d+) Dialekt-Textdateien geschrieben\.$",
     r"\1 szövegfájl kiírva."),
    (r"^Spiele (.+?) ab \.\.\.$", r"\1 lejátszása…"),
    (r"^Lade ffmpeg herunter \(etwa (\d+) MB\) \.\.\.$",
     r"FFmpeg letöltése (kb. \1 MB)…"),
    (r"^Kostprobe fertig - (\d+) Sätze$",
     r"Hangminta elkészült – \1 mondat"),
    (r"^(\d+) Ansagen  ·  (\d+) selbst geändert$",
     r"\1 bemondás · \2 saját módosítás"),
    (r"^(\d+) selbst geändert$",
     r"\1 saját módosítás"),
    (r"^Zeige (\d+) von (\d+) Ansagen$",
     r"\1 / \2 bemondás megjelenítve"),
])


_TRANSLATIONS.update({
  "IN DER APP ENTHALTEN": "BEÉPÍTETT HANGOK",
  "EIGENE": "SAJÁT HANGOK",
  "FREIE STIMMEN AUS DEM NETZ": "LETÖLTHETŐ HANGOK",
  "In der App enthalten": "Beépített hangok",
  "Eigene": "Saját hangok",
  "Freie Stimmen aus dem Netz": "Internetről letölthető hangok",
  "Eigenes · ": "Saját · ",
  "Mitgelieferte Dialekte lassen sich nicht umbenennen.": "A beépített beszédstílusok nem nevezhetők át.",
  "Mitgelieferte Dialekte lassen sich nicht löschen.": "A beépített beszédstílusok nem törölhetők.",
  "Wähle oben ein Paket aus, das mit 'Eigenes' beginnt.": "Fent válassz ki egy „Saját” kezdetű hangcsomagot.",
  "Eigene Textsammlung": "Saját szövegcsomag",
  "Eigene Textsammlung anlegen ...": "Saját szövegcsomag létrehozása…",
  "nicht verfügbar": "nem érhető el",
  "Im Projekt enthalten": "A projekt része",
  "Heruntergeladen": "Letöltve",
  "Bereits heruntergeladen": "Már le van töltve",
  "Noch kein Paket": "Még nincs hangcsomag",
  "Status unbekannt": "Ismeretlen állapot",
  "Abspielen": "Lejátszás",
  "Öffne im Browser": "Megnyitás böngészőben",
  "Sehe nach ...": "Ellenőrzés…",
  "Verbinde ...": "Csatlakozás…",
  "Kontingent": "Kreditkeret",
  "Kontingent aufgebraucht.": "Elfogyott a kreditkeret.",
  "    noch keine": "    Még nincs",
  "✓ Das hast du schon erledigt.": "✓ Ezt már elvégezted.",
  "Nachsehen, ob es eine neuere Fassung gibt": "Ellenőrzés, hogy elérhető-e újabb verzió.",
  "Diese Fassung:": "Jelenlegi verzió:",
  "Die App fragt bei GitHub nach der neuesten Fassung. Dabei wird nichts über dich oder deinen Roboter übermittelt - aber wie bei jedem Seitenaufruf sieht die Gegenseite deine IP-Adresse. Deshalb ist die Abfrage ausgeschaltet, solange du sie nicht einschaltest.": "Az alkalmazás a GitHubon ellenőrzi, hogy elérhető-e újabb verzió. Ennek során sem rólad, sem a robotodról nem továbbít adatot, de mint minden webes kérésnél, a másik oldal látja az IP-címedet. Ezért ez az ellenőrzés ki van kapcsolva, amíg be nem kapcsolod.",
  "Gefunden wird nichts von selbst installiert. Die App zeigt, was neu ist, und fragt. Erst dann lädt sie die neue Datei, prüft ihre Prüfsumme und ersetzt sich selbst - ohne Installation, ohne Administratorrechte. Dein Datenordner bleibt unberührt.": "A program semmit nem telepít automatikusan. Megmutatja, mi új, és rákérdez. Csak ezután tölti le az új fájlt, ellenőrzi az ellenőrzőösszegét, majd lecseréli saját magát – telepítés és rendszergazdai jogosultság nélkül. Az adatmappád érintetlen marad.",
  "Die App meldet sich mit denselben Zugangsdaten an, die du in deiner Handy-App benutzt - Dreamehome, MOVA Home oder Trouver. Welche es ist, stellst du unten unter 'App' ein. Die Daten gehen ausschließlich an Dreame (MOVA und Trouver gehören dazu), nicht an Dritte. Ohne Anmeldung kennt die App weder dein Robotermodell noch kann sie ihm etwas schicken.": "Az alkalmazás ugyanazokkal a bejelentkezési adatokkal lép be, amelyeket a mobilalkalmazásban használsz – Dreamehome, MOVA Home vagy Trouver. Hogy melyiket használod, azt lent az „Alkalmazás” mezőnél állíthatod be. Az adatok kizárólag a Dreame-hez kerülnek (a MOVA és a Trouver is ide tartozik), harmadik félhez nem. Bejelentkezés nélkül az alkalmazás nem ismeri a robotod típusát, és nem tud neki semmit küldeni.",
  "E-Mail und Passwort wie in deiner Hersteller-App.": "Ugyanaz az e-mail-cím és jelszó, mint a gyártó alkalmazásában.",
  "zeigen": "mutat",
  "Europa (Deutschland, Österreich, Schweiz)": "Európa (Németország, Ausztria, Svájc)",
})

# Disabled-page messages from NavShell and MainWindow; the page label
# is already Hungarian when the user clicks it.
_TRANSLATIONS.update({
    "Dafür muss die App erst wissen, welches Modell dein Roboter ist. Melde dich auf der Startseite an.":
        "Először jelentkezz be a Kezdőlapon, hogy a program felismerje a robotod modelljét.",
    "Dafür fehlt noch das offizielle Sprachpaket deines Roboters. Es wird auf der Startseite einmalig geholt.":
        "Még nincs letöltve a robot gyári hangcsomagja. A Kezdőlapon töltheted le egyszer, a későbbiekben újrahasználjuk.",
    "Melde dich auf der Startseite an und wähle deinen Roboter.":
        "Jelentkezz be a Kezdőlapon, majd válaszd ki a robotodat.",
    "Das offizielle Sprachpaket deines Roboters wird auf der Startseite einmalig geholt.":
        "A Kezdőlapon egyszer kell letöltened a robotod gyári hangcsomagját.",
    "Wähle oben aus, wie dein Roboter klingen soll.":
        "Fent válaszd ki a robot új hangját.",
    "Originalpaket fehlt":
        "Hiányzik a gyári hangcsomag",
})

_DYNAMIC.extend((re.compile(a), b) for a, b in [
    (r"^(.+) geht noch nicht$", r"\1 még nem használható"),
])

def translate(value):
    """Translate only UI-visible text, preserving technical identifiers."""
    if not isinstance(value, str) or not value:
        return value
    exact = _TRANSLATIONS.get(value)
    if exact is not None:
        return exact
    for pattern, replacement in _DYNAMIC:
        if pattern.search(value):
            return pattern.sub(replacement, value)
    # German source constructs some paragraphs by joining string fragments
    # and dynamic identifiers. Only replace known presentation phrases.
    result = value
    for de, hu in _TRANSLATIONS.items():
        if len(de) > 12 and de in result:
            result = result.replace(de, hu)
    return result



HELP_TEXT_HU = """\
A GYORS KEZDÉS

A Dreame Voice Manager HU segítségével saját magyar hangot adhatsz a robotporszívódnak. A használathoz elsősorban két oldalra van szükség:

1. Kezdőlap
   Jelentkezz be ugyanazzal a Dreamehome-, MOVA Home- vagy Trouver-fiókkal, amelyet a telefonodon használsz. A program letölti a robotod gyári hangcsomagját, amely az új hangok alapja. A gyári csomagot csak egyszer kell letölteni.

2. Kész hangok
   Válassz ki egy hangot, hallgasd meg a próbát, majd a „Telepítés a robotra” gombbal telepítsd. Az egyéni hang azonosítója CUSTOM. A gyári hang ettől nem törlődik.

A Haladó részben további funkciók találhatók:
- Hangfelvételek importálása: saját vagy letöltött MP3-, WAV-, OGG- és ZIP-felvételek feldolgozása.
- Hangcsomag készítése: egyedi bemondások és saját hangstílus előállítása Windows-felolvasással vagy ElevenLabs segítségével.
- Beállítások: fiók, robot, hálózat, megjelenés és frissítés.

A szürke menüpontok nem hibásak: előbb jelentkezz be, és töltsd le a gyári hangot.


BIZTONSÁG ÉS VISSZAÁLLÍTÁS

- A program nem módosítja a robot firmware-ét.
- Az egyéni hangcsomag a gyári hangcsomag másolata. Csak a kiválasztott felvételeket cseréli le, a többi hang és vezérlőfájl megmarad.
- A robot ellenőrzi a letöltendő csomag méretét és ellenőrzőösszegét.
- A „Gyári hang visszaállítása” gombbal bármikor visszaállítható az eredeti hang.
- A telepítés nem hivatalos: a felhasználó saját felelősségére történik.


MIÉRT NEM JELENIK MEG AZ EGYÉNI HANG A DREAMEHOME ALKALMAZÁSBAN?

A telefonos alkalmazás csak a Dreame saját hangkatalógusát mutatja. A CUSTOM azonosítójú hang ezért nem jelenik meg a listában. Ha a Dreamehome eltérő nyelvi beállítást jelez, az önmagában nem telepítési hiba.

Fontos: ne válassz új hangot a telefonos Dreamehome alkalmazásban, amíg a saját hangodat szeretnéd használni, mert ezzel felülírhatod. Az aktuális robot-hang a Kezdőlapon ellenőrizhető.


HA A ROBOT NEM TUDJA LETÖLTENI A CSOMAGOT

A robotnak el kell érnie a számítógépet a helyi hálózaton:
- Engedélyezd a programot a Windows tűzfalában a privát hálózaton.
- A robot és a számítógép legyen egymás számára elérhető hálózaton; az elszigetelt vendég- vagy IoT-Wi-Fi ezt akadályozhatja.
- Az aktív VPN megzavarhatja a kapcsolatot.
- A robot legyen ébren.
- Ha helyben nem sikerül, a Beállítások → Egyéni URL mezőben külső, közvetlenül letölthető URL is használható.


MAGYAR HANGCSOMAG ÉS ELEVENLABS

A „Magyar – Vicces házimunkás” a saját szerkeszthető magyar szövegcsomagunk. A szövegeket egyenként módosíthatod, majd hangmintát készíthetsz belőlük.

Windows: offline és ingyenes, telepített magyar Windows-felolvasóhang esetén magyar kiejtéssel.

ElevenLabs: internetkapcsolat és saját API-kulcs szükséges. Magyar szöveghez magyarul beszélő hangot és magyar nyelvet támogató modellt használj (például eleven_flash_v2_5). A hanggenerálás a fiókod kreditkeretéből fogyaszt. Az API-kulcsot csak a helyi alkalmazásban add meg, GitHubra ne töltsd fel.

A kész hangfájlokat a program tárolja, így a generálás folytatható. A robotnak az ElevenLabs-ra nincs szüksége: a kész hangcsomagot helyben játssza le.


HANGFÁJLOK ÉS FFmpeg

A robot OGG Vorbis, mono, 16 kHz formátumú felvételeket vár. A program a támogatott más formátumokat FFmpeg segítségével átalakítja. A saját HU EXE tartalmazza az ellenőrzött FFmpeg-komponenst.

A bemondások legyenek rövidek, hogy jól illeszkedjenek a robot eredeti visszajelzéseinek hosszához.
"""

HAFTUNG_HU = """\
Magáncélú, nyílt forráskódú szabadidős projekt. A szoftvert bármiféle jótállás vagy szavatosság nélkül biztosítjuk; használata a felhasználó saját felelősségére és kockázatára történik. A jogszabályok által megengedett mértékig nem vállalunk felelősséget a robotban, a dokkolóállomásban, az adatokban vagy más vagyontárgyakban okozott károkért.

Ez a projekt nem áll kapcsolatban a Dreame, MOVA, Trouver vagy Xiaomi cégekkel, és egyik gyártó sem támogatja, ellenőrizte vagy hagyta jóvá. A védjegyek és terméknevek a megfelelő jogosultak tulajdonát képezik.

A saját hangcsomagok használata eltérhet a gyártó által meghatározott rendeltetésszerű használattól. Az esetleges garanciális vagy szavatossági következményekről kizárólag az érintett gyártó dönthet.
"""


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
    # Sidebar list items, context menu labels and status logs.
    old_insert = ttk.Treeview.insert
    @functools.wraps(old_insert)
    def tree_insert(self, parent, index, iid=None, **kwargs):
        if "text" in kwargs:
            kwargs["text"] = translate(kwargs["text"])
        return old_insert(self, parent, index, iid=iid, **kwargs)
    ttk.Treeview.insert = tree_insert

    old_item = ttk.Treeview.item
    @functools.wraps(old_item)
    def tree_item(self, item, option=None, **kwargs):
        if "text" in kwargs:
            kwargs["text"] = translate(kwargs["text"])
        return old_item(self, item, option, **kwargs)
    ttk.Treeview.item = tree_item

    for method in ("add_command", "add_cascade", "add_checkbutton", "add_radiobutton"):
        old = getattr(tk.Menu, method)
        @functools.wraps(old)
        def wrapped(self, __old=old, **kwargs):
            if "label" in kwargs:
                kwargs["label"] = translate(kwargs["label"])
            return __old(self, **kwargs)
        setattr(tk.Menu, method, wrapped)

    from dreamevoice.ui.widgets import LogView
    old_append = LogView.append
    @functools.wraps(old_append)
    def log_append(self, message, kind="info"):
        return old_append(self, translate(message), kind)
    LogView.append = log_append

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
