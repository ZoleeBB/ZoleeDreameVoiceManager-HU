# Előre elkészített magyar hangcsomagok

Ebbe a mappába **egyetlen alkalommal** töltsd fel a következő két bináris állományt:

| Fájlnév | Mi ez? |
| --- | --- |
| `Zolee_Dreame_HU_Elison_589_OGG.zip` | 589 előre elkészített magyar felvétel, más Dreame modellekhez igazítható |
| `Zolee_Dreame_X50_HU_Elison_Ready.tar.gz` | teljes, Dreame **X50 Ultra Complete** robotcsomag gyári metadata/hangokkal |

**Feltöltés:** GitHub → `voicepacks/assets` → **Add file → Upload files** → a két fájlt **ugyanabba a commitba** töltsd fel. A fájlok mérete 10,9 és 9,5 MB, tehát nem szükséges Git LFS. A 100 MB-os GitHub push-határt messze nem érik el.

A `.github/workflows/release.yml` a ZIP és a tar.gz **méretét, SHA-256 hashét, MD5-azonosítóját, belső hangfájlok darabszámát és formátumát** ellenőrzi, majd automatikusan csatolja mindkét fájlt az aktuális és minden későbbi GitHub Release-hez. Az aktuális Release frissítése automatikusan elindul, amikor ez a mappa megváltozik.

**Ne töltsd ide:** a teljes `Meine Pakete.zip` mentést, előző részleges csomagokat, köztes MP3-akat, `config.json` állományt vagy API-kulcsokat.

**Fontos:** a teljes X50 csomag gyári Dreame-hangokat is tartalmaz, ezért a repót és a Release-t csak a felhasználási jogok ellenőrzése után tedd nyilvánossá. A modellhez igazítható ZIP gyári hangokat nem tartalmaz.

A két eredeti állomány hiteles SHA-256 értékeit a `../elison-20261031.json` fájl rögzíti.
