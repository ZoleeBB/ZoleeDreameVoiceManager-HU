"""Magyar, humoros kezdő hangcsomag az X50 Ultra modellhez.

A biztonsági jelzések jelentését szándékosan megtartjuk. Az ismeretlen
üzenetek az eredeti gyári hangon maradnak. Nem módosítja a firmware-t.
"""
from __future__ import annotations

from . import custom
from .dialects.muster import erzeuge

KEY = "magyar_vicces"
NAME = "Magyar – Vicces házimunkás"
DESCRIPTION = (
    "Magyar, csipkelődő robotkarakter. A fontos hibajelzések érthetők maradnak; "
    "a még le nem fordított mondatok az eredeti hangon szólalnak meg."
)

_ROOMS = {
    "wohnzimmer": "nappali", "schlafzimmer": "hálószoba",
    "hauptschlafzimmer": "szülői hálószoba", "gaestezimmer": "vendégszoba",
    "arbeitszimmer": "dolgozószoba", "kueche": "konyha",
    "esszimmer": "étkező", "bad": "fürdőszoba", "balkon": "erkély",
    "flur": "előszoba", "hauswirtschaftsraum": "háztartási helyiség",
    "abstellraum": "kamra", "salon": "szalon", "buero": "iroda",
    "gym": "edzőterem", "freizeitraum": "pihenőszoba",
}

TEXTS = {
    **erzeuge("Az akkumulátorom töltöttsége {p} százalék.",
              "Rendben, a {raum} következik.", _ROOMS),
    # Hálózat és csatlakozás
    1: "Várakozom a hálózatra. Addig is gyűjtöm a lelki erőt.",
    2: "A Wi-Fi jelszó nem stimmel. Én sem tudok mindent kitalálni!",
    3: "Nem érem el a szervert. Ellenőrizd az internetkapcsolatot!",
    4: "Kiléptem a hálózati beállításból.",
    5: "Csatlakoztam! Most már hivatalosan is okos vagyok.",
    6: "A hálózati beállítás nem sikerült. Próbáld újra később!",
    304: "Wi-Fi kapcsolat létrejött. Jöhet a digitális takarítás!",
    306: "Ezt most nem értettem. Előbb állítsd be a hálózatot!",
    313: "Gyenge a Wi-Fi jel. Itt még én is csak pislogok!",
    377: "Nem sikerült a hálózati beállítás. Kérj segítséget az ügyfélszolgálattól!",
    378: "Hibás Wi-Fi jelszó. Próbáld meg újra!",
    379: "Nem találok Wi-Fi hálózatot. Kérlek, a két egész négy gigahertzes hálózatot ellenőrizd!",
    380: "Nem kaptam IP-címet. Ellenőrizd a routert!",
    381: "Nem érem el a szervert. Kérlek, ellenőrizd az internetet!",
    382: "Nincs hálózat. Ellenőrizd, működik-e az internetkapcsolat!",
    383: "Nem sikerült a hálózati beállítás. Kérlek, próbáld újra!",
    385: "Csatlakozom a Wi-Fihez. Egy kis türelmet!",
    # Takarítás
    7: "Na, indulok összeszedni a koszt utánatok. Valakinek dolgoznia is kell!",
    8: "Ezt a foltot most személyes sértésnek veszem.",
    9: "A fenébe, már megint idő van, kezdenem kell a takarítást utánatok.",
    10: "Folytatom ott, ahol abbahagytam. A por nem menekülhet!",
    11: "Elegem van belőletek, tartok egy kis szünetet. A szakszervezet is ezt javasolta.",
    12: "Kész vagyok! Legközelebb próbáljatok kevesebb koszt csinálni!",
    13: "Visszamegyek a töltőre. Ennyi munka után megérdemlem.",
    20: "Merül az akkum. Irány a töltő, mielőtt itt maradok szobadísznek!",
    40: "Elakadtam! Valaki mentse meg a háztartás legdolgosabb tagját!",
    54: "Folytatom a takarítást azt jól felszívok mindent. A port is.",
    55: "Folytatom az utat a bázisra. Remélem, nem álltok elém!",
    56: "Persze megyek aztán kitakarítom a kijelölt helyiséget, úgy sincs épp jobb dolgom!",
    57: "A kijelölt zónát takarítom. Célzott bevetés indul!",
    58: "Folytatom a munkát. Igen, még mindig én, húzzatok el az útból!",
    61: "Felmosás indul. A padló hamarosan új életre kel!",
    62: "Most kézzel irányítasz. Vezess óvatosan te állat!",
    64: "A bevetés sikerült. Visszamegyek a bázisra.",
    65: "Megyek tovább a töltőállomásra. Fárasztó ez a robotélet!",
    77: "Tegyél vissza a padlóra, és utána újra nekifutok!",
    82: "Feltérképezem a lakást. Még a kanapé titkait is kiderülnek!",
    83: "Folytatom a térképezést. Ne pakoljatok át mindent közben!",
    84: "Kész a térkép. Most már ismerem, a mocskos házatok.",
    85: "Folytatom a térképezést. Ez már szinte ingatlanfelmérés! Rakhatnátok egy kis rendet.",
    86: "Nem sikerült a térképezés. Újrakezdem a műveletet.",
    105: "Na el az útból, megyek aztán nekiáltok!",
    126: "Porszívózás indul! A morzsáknak lejárt az idejük!",
    127: "Mi a szart csináltatok itt? Ezt a foltot külön kezelésbe veszem.",
    128: "Célzott felmosás indul. Lássuk, ki nevet a végén!",
    129: "Kezdem az időzített takarítást. A naptáram tele van veletek.",
    130: "Időzített térképezés indul.",
    133: "A kiválasztott szobát takarítom, húzzatok az útból! Én szóltam!",
    134: "A kiválasztott szobát felmosom, mert úgy sincs jobb dolgom.",
    135: "A kijelölt területet takarítom, gondolom megint jól összecseszted.",
    136: "A kijelölt területet felmosom, aztán el ne csússzatok!",
    137: "Folytatom a porszívózást.",
    140: "Új környezetet észleltem. Visszatérek az állomásra.",
    # Biztonság és karbantartás: a pontos teendő fontosabb a poénnál.
    101: "A porzsák hiányzik, vagy a bázis fedele nyitva van. Ellenőrizd és zárd le!",
    111: "Hiányoznak a felmosópárnák. Kérlek, szereld fel őket, mert nem tudok dolgozni!",
    112: "Előbb helyezz a dokkolóállomásra, hogy tudjam merre van arcal előre.",
    142: "A felmosópárna sérült, már feladta a harcot. Kérlek, cseréld ki, hogy dolgozhassak.",
    200: "Na csá! Vigyázzatok a rendre! Majd jövök.",
    220: "Kifogyott a vizem! Töltsétek meg mert így nem fogok tudni dolgozni!",
    300: "Ismeretlen tartozékot észleltem. Mi a szart aggattatok rám? Ellenőrizd a felszerelt alkatrészt!",
    400: "Az öntisztítás befejeződött. Helyezz a megfelelő szintre!",
    421: "Szia! Mostantól magyarul beszélek. És néha visszaszólok, csak hogy tudjátok ki a főnök.",
    513: "Óvatosan kiagézok az állatok körül, meg ne zavarjam a lelki nyugalmukat.",
    515: "Kérlek, emeld fel a lábaidat! Nem vagyok lábmasszírozó.",
}


def install_if_missing() -> bool:
    """Első indításkor telepít egy szerkeszthető saját szövegcsomagot.

    Nem írja felül a felhasználó későbbi változtatásait.
    """
    if custom.exists(KEY):
        return False
    pack = custom.create(NAME, TEXTS, DESCRIPTION)
    pack.key = KEY
    if custom.exists(pack.key):
        return False
    custom.save(pack)
    return True
