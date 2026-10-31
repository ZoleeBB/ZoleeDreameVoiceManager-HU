import unittest
from dreamevoice.hu_preset import TEXTS, KEY
from dreamevoice.dialects import muster


class HungarianPresetTests(unittest.TestCase):
    def test_key(self):
        self.assertEqual(KEY, 'magyar_vicces')

    def test_critical_messages_present(self):
        for sound_id in [7, 12, 13, 20, 40, 101, 111, 142, 377, 378]:
            self.assertIn(sound_id, TEXTS)
            self.assertTrue(TEXTS[sound_id].strip())

    def test_battery_percentage_range(self):
        self.assertIn('100 százalék', TEXTS[muster.AKKU_ERSTE_ID])
        self.assertIn('0 százalék', TEXTS[muster.AKKU_LETZTE_ID])

    def test_audio_text_safe(self):
        for value in TEXTS.values():
            self.assertLess(len(value), 500)
            self.assertNotIn('|', value)


if __name__ == '__main__':
    unittest.main()
