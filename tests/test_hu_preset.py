"""A felhasználó végleges magyar hangcsomagjának regressziós ellenőrzése."""
import hashlib
import json
import unittest
from unittest import mock

from dreamevoice import hu_preset
from dreamevoice.hu_preset import TEXTS, KEY, NAME, DESCRIPTION
from dreamevoice.dialects import muster

# Az eredeti, kézzel jóváhagyott 589 magyar mondat teljes ellenőrzőösszege.
# Megváltoztatása csak a felhasználó által jóváhagyott új szövegkészletnél indokolt.
USER_APPROVED_TEXTS_SHA256 = "a4d56a5409ce7a634f01bfd024cf10ad616ffa0d7b955dfa171d98805484e4f7"


class HungarianPresetTests(unittest.TestCase):
    def test_key_and_identity(self):
        self.assertEqual(KEY, "magyar_vicces")
        self.assertEqual(NAME, "Magyar – Vicces házimunkás")
        self.assertIn("Magyar, csipkelődő robotkarakter", DESCRIPTION)

    def test_full_589_entry_preset(self):
        self.assertEqual(len(TEXTS), 589)
        self.assertEqual(len(set(TEXTS)), 589)
        self.assertTrue(all(isinstance(i, int) and i >= 0 for i in TEXTS))

    def test_user_approved_texts_unchanged(self):
        # A megadott JSON "texts" objektumának kanonikus SHA-256 értéke.
        content = json.dumps(
            {str(i): t for i, t in TEXTS.items()},
            ensure_ascii=False, sort_keys=True, separators=(",", ":"),
        ).encode("utf-8")
        self.assertEqual(hashlib.sha256(content).hexdigest(),
                         USER_APPROVED_TEXTS_SHA256)

    def test_critical_messages_present(self):
        for sound_id in [7, 12, 13, 20, 35, 40, 101, 111, 142, 377, 378, 857]:
            self.assertIn(sound_id, TEXTS)
            self.assertTrue(TEXTS[sound_id].strip())

    def test_final_personalized_texts(self):
        self.assertEqual(
            TEXTS[304],
            "Wi-Fi kapcsolat létrejött. Mostmár cseszegethetsz az aplikációból."
        )
        self.assertEqual(
            TEXTS[626], "Az akkumulátorom csontra lemerült baszki."
        )
        self.assertEqual(
            TEXTS[35],
            "Valamit bekapott a főkefém. Emelj fel és cibáld ki belőlem légyszi!"
        )

    def test_battery_percentage_range(self):
        self.assertIn("100 százalék", TEXTS[muster.AKKU_ERSTE_ID])
        self.assertIn("lemerült", TEXTS[muster.AKKU_LETZTE_ID])

    def test_audio_text_safe(self):
        for value in TEXTS.values():
            self.assertLess(len(value), 500)
            self.assertNotIn("|", value)
            self.assertTrue(value.strip())

    def test_never_overwrite_existing_user_preset(self):
        # Új kiadás se módosítsa a meglévő saját, helyben szerkesztett JSON-t.
        with mock.patch.object(hu_preset.custom, "exists", return_value=True), \
             mock.patch.object(hu_preset.custom, "save") as save:
            self.assertFalse(hu_preset.install_if_missing())
            save.assert_not_called()


if __name__ == "__main__":
    unittest.main()
