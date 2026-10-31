"""ElevenLabs HU: retries and quota-vs-throttling regression tests.

All requests are mocked: no ElevenLabs account, credits or keys are used.
"""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from dreamevoice import elevenlabs
from dreamevoice.errors import NetworkError


class FakeResponse:
    def __init__(self, status=200, code=None, message=None):
        self.status_code = status
        self.content = b"X" * 2048
        self._detail = {
            "status": code or "success",
            "message": message or "",
        }
        self.text = json.dumps({"detail": self._detail})

    def json(self):
        return {"detail": self._detail}


class RateLimitRegressionTests(unittest.TestCase):
    def test_starter_safe_concurrency(self):
        self.assertLessEqual(elevenlabs.MAX_GLEICHZEITIG, 2)
        self.assertLessEqual(elevenlabs.START_GLEICHZEITIG, 2)

    def test_429_concurrency_is_retryable_even_if_message_says_quota(self):
        error = FakeResponse(
            429, "too_many_concurrent_requests",
            "Request quota exceeded for concurrent requests"
        )
        with mock.patch.object(elevenlabs, "_http", return_value=error):
            with self.assertRaises(elevenlabs.Ueberlastet):
                elevenlabs._request(
                    "POST", "text-to-speech/voice-test", "sk_unit_test",
                    json={"text": "Magyar próba", "model_id": "eleven_flash_v2_5"}
                )

    def test_429_rate_limited_is_retryable(self):
        error = FakeResponse(429, "rate_limit_exceeded", "Too many requests")
        with mock.patch.object(elevenlabs, "_http", return_value=error):
            with self.assertRaises(elevenlabs.Ueberlastet):
                elevenlabs._request("POST", "text-to-speech/voice-test", "sk_test")

    def test_503_service_busy_is_retryable(self):
        error = FakeResponse(503, "system_busy", "Please retry")
        with mock.patch.object(elevenlabs, "_http", return_value=error):
            with self.assertRaises(elevenlabs.Ueberlastet):
                elevenlabs._request("POST", "text-to-speech/voice-test", "sk_test")

    def test_402_real_exhaustion_is_not_retryable(self):
        error = FakeResponse(402, "insufficient_credits", "Insufficient credits")
        with mock.patch.object(elevenlabs, "_http", return_value=error):
            with self.assertRaises(NetworkError) as context:
                elevenlabs._request("POST", "text-to-speech/voice-test", "sk_test")
        self.assertNotIsInstance(context.exception, elevenlabs.Ueberlastet)

    def test_429_then_success_does_not_make_partial_pack(self):
        responses = [
            FakeResponse(429, "concurrent_limit_exceeded", "Rate quota exceeded"),
            FakeResponse(), FakeResponse(), FakeResponse(), FakeResponse(),
        ]
        with tempfile.TemporaryDirectory() as d:
            with (mock.patch.object(elevenlabs, "_http", side_effect=responses),
                  mock.patch.object(elevenlabs.time, "sleep")):
                result = elevenlabs.synthesize(
                    {1: "Egy", 2: "Kettő", 3: "Három", 4: "Négy"},
                    Path(d), api_key="sk_test", voice_id="voice-test",
                    model="eleven_flash_v2_5",
                    use_voice_settings=False,
                )
            self.assertEqual(sorted(result), [1, 2, 3, 4])
            for p in result.values():
                self.assertGreater(p.stat().st_size, 1024)


if __name__ == "__main__":
    unittest.main()
