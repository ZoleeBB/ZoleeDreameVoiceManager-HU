# Zolee - Dreame Voice Manager HU – privát fejlesztői változat

**Alap:** [Anon365-Project/dreame-sprachpaket-manager](https://github.com/Anon365-Project/dreame-sprachpaket-manager), **v1.4.0**. Az eredeti forrás MIT-licenc alatt áll. Az eredeti LICENSE és szerzői információk változatlanul megmaradnak. Az eredeti német hanganyagok ettől független, saját felhasználási feltételek alá esnek; a saját HU build nem csomagolja őket.

## Jelenlegi felépítés és CI/CD

A privát repóban csak a **magyar kiegészítés (overlay)** van. A fordító workflow a GitHubról klónozza az eredeti program pontosan rögzített `v1.4.0` kiadását (`852f3043727fc85a3c06cb54231a00de013b1492`), majd a `scripts/apply_overlay.py` módosításait és a **saját szövegeidet** (`dreamevoice/hu_preset.py`) alkalmazza.

Ez szándékos: az upstream forrás nem kell még egyszer a repóba, és a magyar szövegeket a build sosem írja felül.

**Teendők:**
1. Merge előtt a PR-nél ellenőrizd a `Dreame HU - Windows Build` eredményét.
2. A sikeres build `DreameVoiceManager-HU` artifactja 7 napig tölthető le.
3. A PR merge után a `main` branch `Actions → Dreame HU - Windows Release → Run workflow` menüjében állítsd a verziót `v1.4.0-hu.1` értékre. A build tesztel, majd a Releases felületre feltölti az EXE-t és az ellenőrzőösszeget.
4. A Windows EXE nem aláírt. Indítás után ellenőrizd a magyar TTS-hangot és hallgasd meg az egyes bemondásokat a robotra telepítés előtt.

**Helyi fordítás:** PowerShellben futtasd a `./scripts/prepare-source.ps1` scriptet a repó gyökeréből, utána `cd _upstream-src`, majd `./scripts/build-release.ps1`. Az eredmény: `_upstream-src/dist/DreameSprachpaket-HU.exe`.

A régi `setup-private-repo.ps1` csak egy **új, üres** repository egyszeri létrehozására készült; **itt már nem kell futtatni**.

## Fordítás és kiadás

- CI: `.github/workflows/build.yml` — `main`, `develop`, PR és kézi indítás.
- Release: `.github/workflows/release.yml` — `v*` tageknél létrehozza a release-t, feltölti az EXE-t és a SHA-256 ellenőrzőösszeget.
- Python 3.12, `windows-2022`, PyInstaller és requests verzió pinelve a `requirements-hu-build.txt` fájlban.
- FFmpeg letöltés csak előzetesen rögzített SHA-256 ellenőrzéssel történik. A BtbN `latest` hivatkozása időközben megváltozhat: ebben az esetben a build biztonságosan leáll, és kézi ellenőrzés/új SHA szükséges a `scripts/build-release.ps1` fájlban.
- A magyar EXE neve `DreameSprachpaket-HU.exe`. Ez a saját build nem frissíti magát az eredeti projekt aláíratlan EXE-jére. A frissítések a saját GitHub Releases felületről tölthetők le.
- Nem használ GitHub secretet a Dreame-bejelentkezéshez; a jelszó csak helyben, az alkalmazásba kerülhet.

## Magyar hangcsomag

Első indításkor a program létrehozza a `Magyar – Vicces házimunkás` szerkeszthető **saját** hangcsomagot. Az ismert takarítási és hibaüzenetekhez vannak magyar mondatok, és a százalékos akkumulátorbemondásokat, helyiségneveket is magyarul készíti elő. **Nem teljes fordítás**: a még le nem fedett azonosítók az eredeti gyári hangon maradnak, így nem tűnnek el fontos figyelmeztetések.

A kezelőfelületen a `Dialekt erzeugen` (Dialekt előállítása) résznél az `Eigenes · Magyar – Vicces házimunkás` elemet válaszd. A Windows-hangok között ez a változat már német **és magyar** hangokat is felsorol. Ha nincs `hu-HU` hang, Windows **Settings → Time & language → Language & region → Hungarian → Language options → Text-to-speech** résznél add hozzá, ha elérhető. A lista telepített hangoktól függ; előbb hallgasd meg a próbát, és csak utána generáld a csomagot. A kötelező eredeti Dreame hangcsomagot a program letölti a gyári forrásból.

**Nem magyarítottuk le még a teljes Tkinter felületet.** A hangszövegek magyarok, a kezelőfelület jelenleg nagyrészt német marad. A magyar hangsáv is Windows magyar TTS-hangot igényel; ElevenLabs esetén külön fiók/kulcs és szolgáltatási díj merülhet fel.

## Biztonsági és működési korlátok

- A saját build nem bizonyítja a kártevőmentességet; a források, az FFmpeg és a CI-függőségek ellenőrzése továbbra is szükséges.
- A CI build minden induláskor harmadik féltől származó Python-csomagokat telepít a PyPI-ról. A közvetlen verziók rögzítettek, a tranzitív függőségek még nincsenek teljes hash-lockkal lezárva.
- A Microsoft Defender SmartScreen figyelmeztethet a nem digitálisan aláírt saját EXE-re.
- A robot hangcsomag-telepítése gyári funkcióra épül, de nem hivatalosan támogatott. Nem módosítja a firmware-t, ám az X50 modellen való működés helyszíni ellenőrzése szükséges.
- A CI eredményét a GitHub Actions futási naplója igazolja; a Windows TTS tényleges hangminőségét és a roboton való működést külön ellenőrizni kell. A kezdeti projektfájlok szerkezetét és Python-szintaxisát helyben ellenőriztük, a Windows TTS-t és az FFmpeg-es EXE-t itt nem tudtuk végigtesztelni.

## Saját változat frissítése

Az `upstream` remote az eredeti publikus projekt. Új upstream kiadást előbb ellenőrzött fejlesztői branchbe hozz be, futtasd a teszteket, és PR-rel egyesítsd. A saját magyar presetet nem írjuk felül az újraindításkor: ha egyszer már létrejött és szerkesztetted, változatlan marad.
