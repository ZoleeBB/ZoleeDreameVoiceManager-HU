"""Safe ElevenLabs model choices for the Hungarian Dreame voice pack.

The upstream multilingual-v2 model does not support hu-HU. Flash v2.5 is
supported and preferred over the legacy Turbo v2.5, per ElevenLabs docs.
Only these verified v2.5 models are enabled for HU packs because newer
models can require different audio settings or synthesis parameters.
"""
from __future__ import annotations

PACK_KEY = "magyar_vicces"
DEFAULT_MODEL = "eleven_flash_v2_5"
HU_MODEL_IDS = frozenset({"eleven_flash_v2_5", "eleven_turbo_v2_5"})


def is_hungarian_pack(pack: object) -> bool:
    return getattr(pack, "key", None) == PACK_KEY


def supports_hungarian(model_id: str) -> bool:
    return model_id in HU_MODEL_IDS


def preferred_model(available: list[str], preferred: str = "") -> str | None:
    """Keep a compatible explicit choice; otherwise prefer Flash v2.5."""
    allowed = [item for item in available if supports_hungarian(item)]
    if preferred in allowed:
        return preferred
    if DEFAULT_MODEL in allowed:
        return DEFAULT_MODEL
    return allowed[0] if allowed else None
