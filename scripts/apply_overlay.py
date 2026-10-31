"""Idempotens, ellenőrzött minimális módosítások az upstream v1.4.0 fájljain.

Nem keres-vaktában: hiányzó/eltérő mintánál leáll, és nem készít hibás kódot.
"""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def patch(path: str, edits: list[tuple[str, str]]) -> None:
    file = ROOT / path
    source = file.read_text(encoding="utf-8-sig")
    original = source
    for before, after in edits:
        if after in source:
            continue
        n = source.count(before)
        if n != 1:
            raise RuntimeError(f"{path}: expected one occurrence, found {n}: {before[:85]!r}")
        source = source.replace(before, after)
    if source != original:
        file.write_text(source, encoding="utf-8")
        print(f"Patched: {path}")


def main() -> None:
    patch("README.md", [
        (
            "# Dreame Sprachpaket-Manager",
            "# Dreame Sprachpaket-Manager\n\n> Magyar privát változat: [README-HU.md](README-HU.md) – saját Windows build, magyar beszédhang és vicces szövegcsomag.",
        ),
    ])
    patch("main.py", [
        (
            "    try:\n        from dreamevoice.ui.app import run\n        run()",
            "    try:\n        from dreamevoice.hu_preset import install_if_missing\n"
            "        install_if_missing()\n"
            "        from dreamevoice.ui.app import run\n        run()",
        ),
    ])
    patch("dreamevoice/tts.py", [
        (
            "def pick_german_voice(preferred: str = \"\") -> Optional[Voice]:",
            "def supported_voices() -> List[Voice]:\n"
            "    \"\"\"German and Hungarian Windows TTS voices (HU extension).\"\"\"\n"
            "    voices = [v for v in list_voices()\n"
            "              if v.culture.lower().startswith((\"de\", \"hu\"))]\n"
            "    return sorted(voices, key=lambda v: (not v.is_male, v.name.lower()))\n\n\n"
            "def pick_german_voice(preferred: str = \"\") -> Optional[Voice]:",
        ),
        (
            "    chosen = pick_german_voice(voice)",
            "    # Explicitly selected Hungarian voices are allowed; unspecified voices\n"
            "    # still default to the upstream German voice for compatibility.\n"
            "    chosen = (next((v for v in supported_voices() if v.name == voice), None)\n"
            "              if voice else None) or pick_german_voice(voice)",
        ),
        (
            "        # Beide Wege benutzen SSML, damit Tempo und Tonhöhe gleich wirken.\n"
            "        if chosen.engine == ENGINE_ONECORE:",
            "        # Use the actual Windows TTS locale, never hard-code de-DE.\n"
            "        locale = chosen.culture if chosen.culture.lower().startswith((\"de\", \"hu\")) else \"de-DE\"\n"
            "        # Beide Wege benutzen SSML, damit Tempo und Tonhöhe gleich wirken.\n"
            "        if chosen.engine == ENGINE_ONECORE:",
        ),
        (
            "script = _ONECORE_SCRIPT.format(voice=_ps_quote(chosen.name),",
            "script = _ONECORE_SCRIPT.format(locale=locale, voice=_ps_quote(chosen.name),",
        ),
        (
            "script = _SAPI_SCRIPT.format(voice=_ps_quote(chosen.name),",
            "script = _SAPI_SCRIPT.format(locale=locale, voice=_ps_quote(chosen.name),",
        ),
    ])
    # Both SSML templates must use the selected voice's language.
    tts_path = ROOT / "dreamevoice/tts.py"
    tts_text = tts_path.read_text(encoding="utf-8-sig")
    if "xml:lang='de-DE'" in tts_text:
        if tts_text.count("xml:lang='de-DE'") != 2:
            raise RuntimeError("Expected exactly two hardcoded SSML language tags")
        tts_path.write_text(tts_text.replace("xml:lang='de-DE'", "xml:lang='{locale}'"), encoding="utf-8")
        print("Patched: SSML language")


    # The German upstream defaults to multilingual v2, which does not speak
    # Hungarian. Flash v2.5 supports Hungarian and is our safe default.
    patch("dreamevoice/elevenlabs.py", [
        (
            'MODEL = "eleven_multilingual_v2"',
            'MODEL = "eleven_flash_v2_5"',
        ),
    ])
    patch("dreamevoice/config.py", [
        (
            '"elevenlabs_model": "",          # leer = eleven_multilingual_v2',
            '"elevenlabs_model": "",          # leer = eleven_flash_v2_5 (HU-kompatibilis)',
        ),
    ])
    patch("dreamevoice/ui/tab_store.py", [
        (
            'from .. import (audio, custom, dialect, dialektpakete, elevenlabs,',
            'from .. import hu_elevenlabs\nfrom .. import (audio, custom, dialect, dialektpakete, elevenlabs,',
        ),
        (
            'self.combo_model.set("Standard (eleven_multilingual_v2)")',
            'self.combo_model.set("Standard (eleven_flash_v2_5)")',
        ),
        (
            '        self.refresh_progress()\n\n    def _work_dir(self, pack=None) -> Path:',
            '        self.refresh_progress()\n'
            '        if hasattr(self, "_available_eleven_models") and hasattr(self, "combo_model"):\n'
            '            self._set_models(self._available_eleven_models)\n\n'
            '    def _work_dir(self, pack=None) -> Path:',
        ),
        (
            '        if self.var_own_settings.get():\n'
            '            return modell, None, True',
            '        pack = self._selected_dialect()\n'
            '        if hu_elevenlabs.is_hungarian_pack(pack) and not hu_elevenlabs.supports_hungarian(modell):\n'
            '            # Never submit a model that cannot read Hungarian.\n'
            '            modell = hu_elevenlabs.DEFAULT_MODEL\n'
            '        if self.var_own_settings.get():\n'
            '            return modell, None, True',
        ),
        (
            '        if (not chosen.is_bavarian and not chosen.is_own_creation',
            '        if (pack.key != hu_elevenlabs.PACK_KEY\n'
            '                and not chosen.is_bavarian and not chosen.is_own_creation',
        ),
    ])
    # The original method is replaced only if it matches the audited v1.4.0.
    patch("dreamevoice/ui/tab_store.py", [
        (
            '    def _set_models(self, models) -> None:\n'
            '        """Füllt die Modellauswahl. Ein neueres Modell klingt oft lebendiger."""\n'
            '        self._models = [{"id": m["id"], "label": f"{m[\'name\']} ({m[\'id\']})"}\n'
            '                        for m in models]\n'
            '        if not self._models:\n'
            '            self._models = [{"id": elevenlabs.MODEL,\n'
            '                             "label": f"Standard ({elevenlabs.MODEL})"}]\n'
            '\n'
            '        self.combo_model.configure(values=[m["label"] for m in self._models])\n'
            '        gespeichert = self.state.config["elevenlabs_model"] or elevenlabs.MODEL\n'
            '        treffer = next((m for m in self._models if m["id"] == gespeichert), None)\n'
            '        self.combo_model.set((treffer or self._models[0])["label"])',
            '    def _set_models(self, models) -> None:\n'
            '        """In HU packs list only models known to support Hungarian."""\n'
            '        previous = next((m["id"] for m in getattr(self, "_models", [])\n'
            '                         if m["label"] == self.combo_model.get()), None)\n'
            '        self._available_eleven_models = list(models)\n'
            '        pack = self._selected_dialect()\n'
            '        if hu_elevenlabs.is_hungarian_pack(pack):\n'
            '            models = [m for m in models\n'
            '                      if hu_elevenlabs.supports_hungarian(m.get("id", ""))]\n'
            '        self._models = [{"id": m["id"], "label": f"{m[\'name\']} ({m[\'id\']})"}\n'
            '                        for m in models]\n'
            '        if not self._models:\n'
            '            if hu_elevenlabs.is_hungarian_pack(pack) and self._available_eleven_models:\n'
            '                self.combo_model.configure(values=[])\n'
            '                self.combo_model.set("Nincs magyar TTS-modell a fiókban")\n'
            '                return\n'
            '            self._models = [{"id": elevenlabs.MODEL,\n'
            '                             "label": f"Standard ({elevenlabs.MODEL})"}]\n'
            '        self.combo_model.configure(values=[m["label"] for m in self._models])\n'
            '        preferred = previous or self.state.config["elevenlabs_model"] or elevenlabs.MODEL\n'
            '        if hu_elevenlabs.is_hungarian_pack(pack):\n'
            '            preferred = hu_elevenlabs.preferred_model(\n'
            '                [m["id"] for m in self._models], preferred) or elevenlabs.MODEL\n'
            '        choice = next((m for m in self._models if m["id"] == preferred), None)\n'
            '        self.combo_model.set((choice or self._models[0])["label"])',
        ),
    ])

    # This call occurs in 4 guard locations as well as the voice combobox.
    path = ROOT / "dreamevoice/ui/tab_store.py"
    s = path.read_text(encoding="utf-8-sig")
    if "tts.german_voices()" in s:
        s = s.replace("tts.german_voices()", "tts.supported_voices()")
        s = s.replace("Keine deutsche Stimme", "Keine kompatible Stimme")
        s = s.replace("Es ist keine deutsche Sprachausgabe installiert.",
                      "Es ist keine deutsche oder ungarische Sprachausgabe installiert.")
        path.write_text(s, encoding="utf-8")
        print("Patched: dreamevoice/ui/tab_store.py")

    # The original update mechanism fetches an EXE from the upstream project.
    # Prevent a custom -HU binary from replacing itself with upstream's EXE.
    patch("dreamevoice/aktualisierung.py", [
        (
            "    pfad = _repo_pfad(projekt_url)\n",
            "    if getattr(sys, \"frozen\", False) and Path(sys.executable).stem.endswith(\"-HU\"):\n"
            "        return None  # Release updates only through private GitHub Actions.\n"
            "    pfad = _repo_pfad(projekt_url)\n",
        ),
    ])
    print("Hungarian overlay applied successfully.")


if __name__ == "__main__":
    main()
