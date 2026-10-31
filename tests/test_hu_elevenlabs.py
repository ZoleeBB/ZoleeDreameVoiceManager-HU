"""Regressions for Hungarian ElevenLabs generation and model selection."""
import unittest

from dreamevoice import elevenlabs, hu_elevenlabs
from dreamevoice.hu_preset import KEY


class HungarianElevenLabsTests(unittest.TestCase):
    def test_default_api_model_is_hungarian_compatible(self):
        self.assertEqual(elevenlabs.MODEL, hu_elevenlabs.DEFAULT_MODEL)

    def test_hungarian_pack_detected(self):
        class Pack:
            key = KEY
        self.assertTrue(hu_elevenlabs.is_hungarian_pack(Pack()))
        self.assertFalse(hu_elevenlabs.is_hungarian_pack(None))

    def test_only_verified_hungarian_models_allowed(self):
        self.assertTrue(hu_elevenlabs.supports_hungarian("eleven_flash_v2_5"))
        self.assertTrue(hu_elevenlabs.supports_hungarian("eleven_turbo_v2_5"))
        self.assertFalse(hu_elevenlabs.supports_hungarian("eleven_multilingual_v2"))
        self.assertFalse(hu_elevenlabs.supports_hungarian("eleven_flash_v2"))

    def test_fallback_prefers_flash(self):
        self.assertEqual(
            hu_elevenlabs.preferred_model(
                ["eleven_multilingual_v2", "eleven_turbo_v2_5", "eleven_flash_v2_5"],
                "eleven_multilingual_v2"
            ), "eleven_flash_v2_5"
        )

    def test_preserves_valid_selection(self):
        self.assertEqual(
            hu_elevenlabs.preferred_model(
                ["eleven_flash_v2_5", "eleven_turbo_v2_5"],
                "eleven_turbo_v2_5"
            ), "eleven_turbo_v2_5"
        )

    def test_rejects_unsupported_only(self):
        self.assertIsNone(
            hu_elevenlabs.preferred_model(["eleven_multilingual_v2"], "")
        )


if __name__ == "__main__":
    unittest.main()
