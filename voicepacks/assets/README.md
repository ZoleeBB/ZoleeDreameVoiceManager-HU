# Előre elkészített magyar hangcsomagok

Ebben a mappában már megtalálható a következő két bináris állomány:

| Fájlnév | Mi ez? |
| --- | --- |
| `Zolee_Dreame_HU_Elison_589_OGG.zip` | 589 előre elkészített magyar felvétel, más Dreame modellekhez igazítható |
| `Zolee_Dreame_X50_HU_Elison_Ready.tar.gz` | teljes, Dreame **X50 Ultra Complete** robotcsomag gyári metadata/hangokkal |

**Karbantartás:** a fájlok már a repóban vannak, ezért újabb kiadáskor nem kell feltölteni őket. Csak a hangok tényleges módosításakor cseréld az archívumokat, a manifestben rögzített ellenőrzőösszegekkel együtt.

A `.github/workflows/release.yml` a ZIP és a tar.gz **méretét, SHA-256 hashét, MD5-azonosítóját, belső hangfájlok darabszámát és formátumát** ellenőrzi, majd automatikusan csatolja mindkét fájlt az aktuális és minden későbbi GitHub Release-hez. Az aktuális Release frissítése automatikusan elindul, amikor ez a mappa megváltozik.

**Ne töltsd ide:** a teljes `Meine Pakete.zip` mentést, előző részleges csomagokat, köztes MP3-akat, `config.json` állományt vagy API-kulcsokat.

**Fontos:** a repository már nyilvános. A teljes X50 csomag gyári Dreame-hangokat is tartalmaz; a nyilvános újraterjesztés jogait külön ellenőrizni kell. A modellhez igazítható ZIP gyári hangokat nem tartalmaz.

A két eredeti állomány hiteles SHA-256 értékeit a `../elison-20261031.json` fájl rögzíti.
