<h1 align="center"><img src="assets/branding/readme-banner.svg" alt="Zolee Dreame Voice Manager HU" width="1600"></h1>

<p align="center">
  <a href="https://ko-fi.com/E1H8299KGN"><img src="assets/branding/kofi-support.svg" alt="Ko-fi támogatás" width="230" height="42"></a>
  &nbsp;
  <a href="https://revolut.me/zoleebb"><img src="assets/branding/revolut-support.svg" alt="Revolut-me támogatás" width="230" height="42"></a>
</p>

<p align="center"><strong>Magyar nyelvű hangcsomag-kezelő Dreame, MOVA és Trouver robotporszívókhoz – Windowsra.</strong></p>

**[Windows-alkalmazás letöltése](https://github.com/ZoleeBB/ZoleeDreameVoiceManager-HU/releases/latest)** · **[Részletes hangcsomag-útmutató](voicepacks/README.md)** · **[Hibabejelentés](https://github.com/ZoleeBB/ZoleeDreameVoiceManager-HU/issues)**

## A program bemutatása

A **Zolee Dreame Voice Manager HU** egy Windows alatt futó, magyar kezelőfelületű alkalmazás, amellyel kompatibilis robotporszívók hangbemondásait lehet magyarra vagy saját karakterhangra cserélni. A program a robot eredeti, modellfüggő hangcsomagját használja alapként: a kiválasztott felvételeket lecseréli, a többi bemondást és a szükséges vezérlőfájlokat megtartja. A megoldás **nem írja át a robot firmware-ét**.

A projekt az [Anon365-Project/dreame-sprachpaket-manager](https://github.com/Anon365-Project/dreame-sprachpaket-manager) **v1.4.0** verziójára épül, magyar nyelvi és funkcionális kiegészítésekkel. A kipróbált robotmodell a **Dreame X50 Ultra Complete**. Más modelleknél a működés a gyári hangcsomag-kezelés támogatásától függ.

### Mit lehet vele csinálni?

- **Előre elkészített magyar hangokat telepíteni:** az Elison hanggal felmondott 589 magyar OGG-felvétel használata API-kulcs és újabb hanggenerálás nélkül.
- **Saját hangfelvételeket importálni:** MP3, WAV, OGG, ZIP és támogatott hangcsomagfájlok feldolgozása.
- **Bemondásokat egyenként cserélni:** eredeti hang meghallgatása, saját fájl hozzárendelése és teljes hangcsomag összeállítása.
- **Magyar szövegcsomagot szerkeszteni:** a „Magyar – Vicces házimunkás” alapcsomag mondatai egyedileg módosíthatók.
- **Új hangokat generálni:** megfelelő magyar Windows TTS-hanggal offline, vagy ElevenLabs-fiókkal és kompatibilis beszédmodellel.
- **Hiányzó bemondásokat feldolgozni:** a robot gyári hangazonosítóit összevetni a magyar fordításokkal; a hiányzó tételek exportálhatók és ellenőrzés után visszaimportálhatók.
- **Gyári hangot visszaállítani:** a saját hang lecserélhető az eredeti hangra.
- **Programfrissítést ellenőrizni:** a magyar változat saját GitHub Release-kiadásait keresi, és jóváhagyás után ellenőrzőösszeg-vizsgálattal frissíti az EXE-t.

## Letöltés és első indítás

1. Nyisd meg a **[legfrissebb GitHub Release-t](https://github.com/ZoleeBB/ZoleeDreameVoiceManager-HU/releases/latest)**.
2. Az **Assets** alatt töltsd le a `DreameSprachpaket-HU.exe` alkalmazást. A repository **nyilvános**, a nyilvánosan közzétett kiadások eléréséhez nem szükséges külön repository-meghívás.
3. Indítsd el Windows alatt. Az alkalmazás hordozható, külön telepítőprogram nélkül használható. A letöltött EXE nincs digitálisan aláírva, ezért a Windows SmartScreen figyelmeztetést jeleníthet meg.
4. A **Kezdőlap** felületen válaszd ki a Dreamehome / MOVA Home / Trouver fiókodnak megfelelő szolgáltatást, jelentkezz be, majd válaszd ki a robotodat.
5. Töltsd le a kiválasztott robot **gyári hangcsomagját** a programon keresztül; ez szükséges a később telepített saját hangok alapjához.

A bejelentkezéshez a gyártói alkalmazásban használt fiók szükséges. Ha a telefonon csak Google-alapú bejelentkezést használsz, a Dreamehome-fiókhoz külön jelszó beállítására lehet szükség. Ne a Google-fiókod jelszavát add meg.

## A kezelőfelület részletesen

| Oldal | Funkciók |
| --- | --- |
| **Kezdőlap** | Gyártói fiók, robot kiválasztása, gyári hangcsomag letöltése, aktuális hang ellenőrzése és gyári hang visszaállítása |
| **Kész hangok** | Elérhető és saját hangcsomagok megtekintése, hangpróba, robotra telepítés, kész magyar Elison-hang letöltési hivatkozása |
| **Hangfelvételek importálása** | Kész felvételek, archívumok és csomagok importálása; egyedi bemondások hozzárendelése |
| **Hangcsomag készítése** | Szövegek szerkesztése, Windows/ElevenLabs hangválasztás, hangpróba, generálás, folytatás és hiányzó fordítások kezelése |
| **Beállítások** | Gyártói fiók, hálózati elérés, megjelenés, programfrissítés és alkalmazásbeállítások |
| **Súgó / Névjegy** | Használati és biztonsági információk, projekt- és támogatási hivatkozások |

A fő fejléc alatt a **Ko-fi támogatás** és **Revolut-me támogatás** gombok minden oldalon elérhetők. A támogatás önkéntes, nem feltétele a program használatának.

## Kész magyar Elison-hangcsomag – ajánlott megoldás

A letölthető **`Zolee_Dreame_HU_Elison_589_OGG.zip`** 589 előre elkészített magyar hangfelvételt tartalmaz. **Ehhez nem kell ElevenLabs-fiók, API-kulcs vagy kredit.** A hanggenerálás már megtörtént; a program a saját robotod gyári csomagjához illeszti a megfelelő felvételeket.

**Telepítés menete:**

1. Töltsd le az [OGG ZIP-et a GitHub Release Assets részéből](https://github.com/ZoleeBB/ZoleeDreameVoiceManager-HU/releases/latest); **ne csomagold ki**.
2. A **Kezdőlap** oldalon jelentkezz be, és töltsd le a robotod eredeti hangcsomagját.
3. Nyisd meg a **Hangfelvételek importálása** oldalt, és add meg a ZIP-fájlt.
4. A program a gyári csomag alapján létrehozza a saját, modellhez illeszkedő hangcsomagot.
5. A **Kész hangok** oldalon hallgasd meg az eredményt, majd válaszd a **Telepítés a robotra** műveletet.
6. Ellenőrizd a roboton a hangokat és a fontos figyelmeztetéseket. A **Kezdőlap** felületéről bármikor visszaállíthatod a gyári hangot.

**Lefedettség a kipróbált X50 modellnél:** 589 magyar felvétel a 611 gyári hangazonosítóból, azaz **96,4%**. A fennmaradó **22 hang eredeti nyelven marad**; így nem vesznek el az ismeretlen vagy még nem fordított gyári figyelmeztetések.

A repository egy **`Zolee_Dreame_X50_HU_Elison_Ready.tar.gz`** teljes, X50-specifikus archívumot is tartalmaz. Ebben gyári hangok és vezérlőfájlok is vannak. **Más robotmodellhez ne ezt használd**, hanem az 589 hangos ZIP-importot. A gyári anyag továbbterjesztésének jogosultságát külön szükséges tisztázni; a nyilvános repository önmagában nem jelent újrafelhasználási engedélyt.

**[Részletes telepítés, fájlnevek és ellenőrzőösszegek](voicepacks/README.md)** · **[Hangcsomag-manifeszt](voicepacks/elison-20261031.json)**

## Saját magyar szövegek és beszédgenerálás

Első indításkor a program előkészíti a szerkeszthető **„Magyar – Vicces házimunkás”** szövegcsomagot. A kiinduló készlet 589 véglegesített magyar szöveget tartalmaz. A módosítható mondatok között vannak hétköznapi takarítási visszajelzések és műszaki figyelmeztetések is. **Biztonsági, hiba- és karbantartási üzeneteknél a pontos teendő megőrzése fontosabb a humornál.**

A **Hangcsomag készítése** oldalon hangot és generálási módot választhatsz:

- **Windows szövegfelolvasás:** helyben futó, jellemzően ingyenes működés; jó magyar kiejtéshez telepített, támogatott `hu-HU` hang szükséges.
- **ElevenLabs:** saját API-kulcsot és internetkapcsolatot igényel. A magyar kiegészítés alapértelmezése az `eleven_flash_v2_5`; a magyar csomagnál a kompatibilis modellek közül választhatsz. A szolgáltatás használata kreditet fogyaszthat.

A generálás előtt célszerű hangmintát készíteni. A hosszabb futásoknál a program megtartja az elkészült felvételeket, és egyező hang-, modell- és generálási beállítások mellett a hiányzó tételekkel folytatható a munka. Átmeneti API-terhelés vagy HTTP 429 esetén korlátozott újrapróbálkozás történik; a kimerült kreditkeretet ettől eltérően kezeli.

**Hiányzó fordítások:** a program a valóban jelen lévő gyári hangazonosítókból előállíthatja a még lefordítandó sorok listáját. Külső segítséggel elkészített, ellenőrzött magyar szövegek visszaimportálhatók, de a hiányzó vagy ismeretlen jelentésű hangokat nem szabad találgatással lefordítani. A meglévő egyedi szövegek megőrzésére külön ellenőrzések szolgálnak.

## Robotkompatibilitás

A program nem egyetlen robotmodellre van rögzítve: a gyártói szolgáltatásból lekérdezi a kiválasztott robothoz elérhető hangcsomagot. A kompatibilitás feltétele, hogy a készülék támogatott fiókkal elérhető legyen, legyen letölthető gyári hangcsomagja és elfogadja a saját hang telepítését.

A kiinduló projekt korábbi felmérése **402, hangcsomag-katalógussal rendelkező modellazonosítót** talált (288 Dreame, 97 MOVA, 17 Trouver). Ez **nem** naprakész vagy garantált kompatibilitási lista. **A magyar kiegészítés helyben kipróbált modellje a Dreame X50 Ultra Complete**; más készülékeknél próbáld ki és ellenőrizd a működést.

Forrás: [eredeti projekt modellkompatibilitási dokumentációja](https://github.com/Anon365-Project/dreame-sprachpaket-manager/blob/v1.4.0/docs/Modelle.md).

## Hálózat, telepítés és visszaállítás

A robot az új hangcsomagot a számítógépen ideiglenesen kiszolgált fájlból töltheti le. Emiatt:

- A számítógép és a robot legyen egymás számára elérhető hálózaton; az elszigetelt vendég- vagy IoT-hálózat problémát okozhat.
- A Windows tűzfalában engedélyezni kell a program helyi hálózati kommunikációját.
- VPN, hibás hálózati cím vagy az alvó robot akadályozhatja az átvitelt.
- A **Beállítások → Egyéni URL** opció a hálózati problémák egy részében használható.
- A telepítés végén ellenőrizd az eredményt. Ha szükséges, használd a **Gyári hang visszaállítása** lehetőséget.

A telefonos gyártói alkalmazás nem feltétlenül mutatja az egyéni `CUSTOM` hangcsomagot a hivatalos katalógusban. A gyártói alkalmazásban történő hangváltás felülírhatja a saját hangodat.

## Programfrissítés

A **Beállítások → Frissítések keresése** funkció a **[ZoleeBB/ZoleeDreameVoiceManager-HU](https://github.com/ZoleeBB/ZoleeDreameVoiceManager-HU)** repository legfrissebb GitHub Release-kiadását ellenőrzi, és a `DreameSprachpaket-HU.exe` alkalmazást keresi. Új kiadás esetén a letöltés és telepítés jóváhagyást kér; a program a letöltött fájl SHA-256 ellenőrzőösszegét is ellenőrzi, mielőtt lecseréli a futó EXE-t.

Az indításkori automatikus ellenőrzés a beállításokban kapcsolható. Az alkalmazás **nem** az eredeti német projekt EXE-jére frissít. A program saját adatkönyvtára és korábban készített hangcsomagjai a normál EXE-frissítés során megmaradnak.

A naprakész kiadások és változásnaplók a **[GitHub Releases](https://github.com/ZoleeBB/ZoleeDreameVoiceManager-HU/releases)** oldalon találhatók; a README-ben külön verziótörténetet nem vezetünk.

## Fejlesztőknek: felépítés és kiadás

A repository a magyar **overlay** állományait, tesztjeit, dokumentációját és a kész hanganyagokat tartalmazza. A build a rögzített upstream **v1.4.0** forrást (`852f3043727fc85a3c06cb54231a00de013b1492`) tölti le, ellenőrzi, majd alkalmazza a `scripts/apply_overlay.py` módosításait.

- **`VERSION-HU`** – az alkalmazás, az EXE-verzióadatok és a Release címkéjének közös verzióforrása.
- **`dreamevoice/hu_preset.py`** – a szerkeszthető magyar alapbemondások.
- **`dreamevoice/ui_hu.py`** – magyar felületi fordítások.
- **`voicepacks/assets/`** – előre elkészített hangarchívumok; állományellenőrzés a `scripts/verify_release_assets.py` segítségével.
- **`.github/workflows/build.yml`** – Windows build és regressziós ellenőrzések; a build artifactja hét napig elérhető.
- **`.github/workflows/release.yml`** – EXE, SHA-256 ellenőrzőösszegek és hangarchívumok kiadása a GitHub Releases alatt.

Helyi fordítás (Windows, PowerShell, Git és megfelelő Python-környezet):

```powershell
./scripts/prepare-source.ps1
cd _upstream-src
./scripts/build-release.ps1
```

Eredmény: `_upstream-src/dist/DreameSprachpaket-HU.exe`. A build ellenőrzött forrású FFmpeg-komponenst használ. A CI az upstream önteszteket és a magyar regressziós teszteket is futtatja; a magyar EXE-fájlnév és az upstreamhez nem csomagolt hangarchívumok miatti, ellenőrzött eltérések külön kezeltek. A zöld CI önmagában nem helyettesíti a roboton végzett tényleges próbát.

## Biztonság, adatvédelem és jogok

A program **nem hivatalos**, a használata saját felelősségre történik. A gyártó nem támogatja vagy hagyta jóvá. A robot firmware-e nem változik, de a hangcsomag csere ettől még befolyásolhatja a működést; a kritikus hibaüzeneteket mindig ellenőrizd.

A fiókadatokat kizárólag az alkalmazásba add meg, **ne** commitold GitHubra és ne helyezd a README-be, issue-ba vagy hangcsomagba. Az ElevenLabs API-kulcsra is ez vonatkozik. A Windows EXE nincs digitálisan aláírva; a kiadás mellé csatolt SHA-256 ellenőrzőösszeggel ellenőrizhető.

Az eredeti forrás **MIT-licencű**; a gyári Dreame-hangfelvételek, az ElevenLabs által előállított hangok és az esetleges külső hangminták felhasználási és továbbterjesztési jogai ettől elkülönülnek. A repository nyilvánossága nem jelenti azt, hogy minden benne található hanganyag korlátozás nélkül újraterjeszthető.

**További információ:** [hangcsomag-telepítési útmutató](voicepacks/README.md) · [hanganyagok mappája](voicepacks/assets/README.md) · [eredeti projekt](https://github.com/Anon365-Project/dreame-sprachpaket-manager) · [licenc](LICENSE).
