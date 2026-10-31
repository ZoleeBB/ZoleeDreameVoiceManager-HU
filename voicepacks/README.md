# Előre elkészített magyar hangcsomag – Elison

> **Nem kell ElevenLabs-fiók, API-kulcs, kredit vagy hanggenerálás.** A letöltött hangok már fel vannak mondva magyarul. A program a ZIP 589 OGG-felvételét a **saját robotod eredeti hangcsomagjához** igazítja és az elkészült csomagot telepíti.

## Automatikusan csatolt Release-fájlok

A `.github/workflows/release.yml` minden új kiadás előtt meghívja a `scripts/verify_release_assets.py` validátort. Ez a rögzített SHA-256/MD5 és méret mellett az OGG-állományok, a teljes csomag 611 hangja, valamint a 6 gyári vezérlőfájl épségét is ellenőrzi.

**Egyszeri üzembe helyezés:** töltsd fel az 589 OGG-s ZIP-et és az X50-es tar.gz-t **ugyanabban a commitban** a `voicepacks/assets/` könyvtárba. Az erre induló workflow a már meglévő aktuális Release hangfájljait is automatikusan hozzáadja/frissíti. A későbbi `VERSION-HU`-emelések ugyanezt elvégzik. Ha bármelyik fájl hiányzik, sérült vagy módosult ellenőrzőösszeg nélkül, a Release **meghiúsul**, nem publikál hiányos csomagot.

## Letöltés

[**Kész magyar Elison hangok – GitHub Releases (v1.4.0-hu.8)**](https://github.com/ZoleeBB/ZoleeDreameVoiceManager-HU/releases/tag/v1.4.0-hu.8)

Az **Assets** résznél a következőt töltsd le:

`Zolee_Dreame_HU_Elison_589_OGG.zip` – 589 már előállított magyar OGG, **10 874 839 bájt**, SHA-256: `3de3e3d6556413caac45e95108354bfcf0fb10d8c9d6e030a2b878c0d8180f48`.

**Figyelem:** a repó jelenleg **privát**. A linket csak olyan személy éri el, akinek hozzáférést adtál; a kész hangcsomag használatához önmagában nem kell ElevenLabs-hozzáférés. A hangfájlokat **egyetlen egyszer** kell a repó [voicepacks/assets](assets/README.md) mappájába feltölteni. A GitHub Actions ezután **automatikusan csatolja a ZIP-et és a teljes X50 `.tar.gz` archívumot minden új Release-hez**, így a későbbi verzióknál nincs szükség ismételt kézi feltöltésre. A repó jelenleg privát; a Release-hez való hozzáférés GitHub-jogosultságot igényel.

## Telepítés a Dreame hangcsomag-kezelővel – másoknak

1. A felhasználó töltse le és indítsa el a `DreameSprachpaket-HU.exe` alkalmazást.
2. A **Start** oldalon jelentkezzen be a **Dreamehome-fiókjába**, válassza ki a saját robotját, és töltse le a modellhez tartozó gyári hangcsomagot a programmal.
3. Nyissa meg a **Hangfelvételek importálása** oldalt. Válassza a **ZIP vagy csomagfájl** importálását; a letöltött `Zolee_Dreame_HU_Elison_589_OGG.zip` fájlt adja meg. **Nem kell kicsomagolni.**
4. A program megvizsgálja az archívumot, ellenőrzi a hangazonosítókat, és a gyári csomagból **helyben** összeállítja a modellhez illeszkedő teljes hangcsomagot. Amikor a fájlt elnevezi, javasolt: `Magyar_Elison_kesz`.
5. Nyissa meg a **Kész hangok** oldalt, válassza a most összeállított **saját** csomagot, hallgasson bele, majd kattintson a **Telepítés a robotra** gombra.
6. A számítógépnek elérhetőnek kell lennie a robot helyi hálózatából, a Windows/ESET tűzfalon engedélyezett helyi szerverporttal. A kész hangok letöltése **nem** igényel ElevenLabs-kulcsot.

> A 589 hang **már kész**; a program importálás közben szükség esetén újrakódolhatja az OGG-kat és hozzáfűzi a robot gyári, le nem fordított bemondásait. Ez **nem új ElevenLabs-generálás**, tehát nem fogyaszt TTS-kreditet.

## Másik megoldás – X50 Ultra Complete-hez már kész teljes csomag

A feltöltött ZIP-ből az utolsó, `_3.tar.gz` változat alapján külön archiváltuk:

`Zolee_Dreame_X50_HU_Elison_Ready.tar.gz` – **9 511 741 bájt**, MD5 `67264df573d1c304658fdf8130b5979b`, SHA-256 `fd70e3627891b959c6ff859b7a5c30f4f8b3d2eaa17dd348008fe9f6fe4cc8a7`.

Ez közvetlenül tartalmazza az X50 robot 611 hangfájlját és a 6 gyári vezérlőállományt; **22 gyári hangot is tartalmaz**, ezért nyilvános továbbterjesztése előtt a Dreame-hanganyagok jogait ellenőrizni kell. Ezt **nem tesszük a forráskódba vagy az alapértelmezett nyilvános Release-be**. Magáncélra az eredeti X50 csomag már bizonyítottan telepíthető; eltérő robotmodellnél **mindig az OGG ZIP-et használd**, ne az X50 teljes archívumot.

## Az adatok ellenőrzése

A repóban lévő `voicepacks/elison-20261031.json` rögzíti a fájlok SHA-256 ellenőrzőösszegeit, a hangazonosítók számát és a forrást. Az ellenőrzéshez:

```powershell
Get-FileHash -Algorithm SHA256 .\Zolee_Dreame_HU_Elison_589_OGG.zip
```

A részletes validátor:

```powershell
python scripts/verify_prebuilt.py .\Zolee_Dreame_HU_Elison_589_OGG.zip
```

A 589 szöveg a `dreamevoice/hu_preset.py` fájlban van. A generált `.mp3` köztes állományok és a 3 korábbi részleges csomag **nincsenek a kiadásban**; ezek új felhasználóknak nem szükségesek.

## Lefedettség és kompatibilitás

| Tulajdonság | Eredmény |
| --- | --- |
| Felhasználó által véglegesített magyar szövegek | **589** |
| Magyar szövegekhez egyező, generált OGG-fájlok | **589 / 589** |
| Az X50 Ultra eredeti hangfájljai | **611** |
| Hiányzó, eredetiben megmaradó hangfájlok | **22** |
| TTS | ElevenLabs, Elison, Flash v2.5 |
| Kipróbált robot | **Dreame X50 Ultra Complete** |
| Egyéb Dreame / MOVA / Trouver modellek | csak ha a gyári hangcsomag-letöltés és saját hangcsomag telepítés támogatott; a ZIP-et a program a modellhez igazítja, de a helyes működés **nem garantált** |

A `594 replaced` érték a kész archívum naplójában szereplő **helyettesített fájlokat** számolja, nem azt jelenti, hogy 594 külön végleges magyar szöveg van. A 589 tétel mindegyikét a feltöltött végleges szövegállomány és a generálási gyorsítótár ujjlenyomatai alapján ellenőriztük.

## Terjesztési és jogi tudnivalók

- A hangok a **felhasználó által írt** magyar szövegek alapján, az ElevenLabs **Elison** hangjával készültek. A hang és generált tartalom felhasználását a vonatkozó ElevenLabs- és Voice Library-feltételek szabályozzák; nagyobb körű megosztás vagy nyilvános közzététel előtt ellenőrizd a jogosultságokat.
- Az **OGG ZIP** nem tartalmaz gyári Dreame-hangfájlokat, így az a **javasolt megosztási változat**.
- Az X50 teljes `.tar.gz` gyári hangokat/metadata-t is tartalmaz, ezért **külön, opcionális** fájl marad.
- A privát GitHub-repóból és privát Release-ből történő letöltés GitHub-hozzáférést igényel.

## Karbantartás

Ha később új mondatot módosítunk, a `hu_preset.py` és a tényleges OGG hang is frissítendő; a szöveg puszta átírása **nem** változtatja meg a már kiadott felvételt. Egy új kiadáshoz készíts új ellenőrzőösszegű ZIP-et és frissítsd a `voicepacks/elison-20261031.json` manifestet vagy hozz létre új, dátumozott manifestet.
