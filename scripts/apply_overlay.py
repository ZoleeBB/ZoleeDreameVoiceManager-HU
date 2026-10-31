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
    # Turn on Hungarian presentation hooks before the Tkinter UI is imported.
    # The machine-facing German source identifiers remain unchanged.
    patch("main.py", [
        (
            "        from dreamevoice.ui.app import run\n        run()",
            "        from dreamevoice.ui_hu import enable\n"
            "        enable()\n"
            "        from dreamevoice.ui.app import run\n        run()",
        ),
    ])

    # Help and license are displayed in Tk Text (not Label) widgets;
    # use fully reviewed Hungarian copy without changing user-edited text.
    patch("dreamevoice/ui/app.py", [
        (
            "from ..paths import data_dir, icon_file, log_file",
            "from ..paths import data_dir, icon_file, log_file\n"
            "from ..ui_hu import HELP_TEXT_HU, HAFTUNG_HU",
        ),
        (
            'text.insert("1.0", HELP_TEXT)',
            'text.insert("1.0", HELP_TEXT_HU)',
        ),
        (
            'text.insert("1.0", HAFTUNG)',
            'text.insert("1.0", HAFTUNG_HU)',
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

    # A restricted ElevenLabs key can allow speech+voice listing but deny
    # GET /user/subscription (401/403). Do not require account-wide access
    # merely to synthesize a voice pack; listing voices validates the key.
    patch("dreamevoice/ui/tab_store.py", [
        (
            '            quota = elevenlabs.check_key(key)\n'
            '            voices = elevenlabs.list_voices(key)',
            '            try:\n'
            '                quota = elevenlabs.check_key(key)\n'
            '            except Exception:\n'
            '                quota = None  # Restricted key: quota endpoint denied.\n'
            '            voices = elevenlabs.list_voices(key)',
        ),
        (
            '            enough = quota.left >= needed\n'
            '            self.lbl_eleven.configure(\n'
            '                text=(f"   Verbunden. Kontingent: {quota.describe()}. "\n'
            '                      f"Für {wofuer} werden rund {needed} Zeichen "\n'
            '                      f"gebraucht - " +\n'
            '                      ("das reicht." if enough else "das reicht derzeit nicht.")),\n'
            '                style="Success.TLabel" if enough else "Warning.TLabel")',
            '            if quota is None:\n'
            '                self.lbl_eleven.configure(\n'
            '                    text=(f"   Verbunden. Kontingent mit eingeschränktem "\n'
            '                          f"API-Schlüssel nicht auslesbar. "\n'
            '                          f"Für {wofuer} werden rund {needed} Zeichen benötigt."),\n'
            '                    style="Success.TLabel")\n'
            '            else:\n'
            '                enough = quota.left >= needed\n'
            '                self.lbl_eleven.configure(\n'
            '                    text=(f"   Verbunden. Kontingent: {quota.describe()}. "\n'
            '                          f"Für {wofuer} werden rund {needed} Zeichen "\n'
            '                          f"gebraucht - " +\n'
            '                          ("das reicht." if enough else "das reicht derzeit nicht.")),\n'
            '                    style="Success.TLabel" if enough else "Warning.TLabel")',
        ),
    ])

    # ElevenLabs HTTP 429 can mean either concurrency throttling or a
    # genuinely exhausted quota. Preserve the original upstream contract
    # for quota_exceeded and character_limit_exceeded, but prioritize
    # structured transient error status over free-form message text.
    # Limit simultaneous TTS requests to two for Starter / Free plans.
    patch("dreamevoice/elevenlabs.py", [
        (
            "MAX_GLEICHZEITIG = 8\nSTART_GLEICHZEITIG = 3",
            "MAX_GLEICHZEITIG = 2\nSTART_GLEICHZEITIG = 1",
        ),
        (
            "MAX_VERSUCHE = 4\n",
            "MAX_VERSUCHE = 8\n",
        ),
        (
            "MAX_WELLEN_GEDROSSELT = 10\n",
            "MAX_WELLEN_GEDROSSELT = 12\n",
        ),
        (
            '        if any(w in meldung for w in ("quota", "character_limit", "credit",\n'
            '                                      "exceeded", "aufgebraucht")):\n'
            '            raise NetworkError(\n'
            '                "Das Kontingent bei ElevenLabs ist aufgebraucht.",\n'
            '                "Das Freikontingent füllt sich jeden Monat wieder auf. Bis "\n'
            '                "dahin kannst du das Paket mit der Windows-Stimme erzeugen.")\n'
            '        raise Ueberlastet(',
            '        # The explicit ElevenLabs status is more precise than the\n'
            '        # message text: a concurrency *rate quota* is not a\n'
            '        # depleted character/credit quota.\n'
            '        fehlerstatus = ""\n'
            '        try:\n'
            '            detail = resp.json().get("detail", {})\n'
            '            if isinstance(detail, dict):\n'
            '                fehlerstatus = str(detail.get("status") or "").lower()\n'
            '        except (ValueError, TypeError, AttributeError):\n'
            '            pass\n'
            '        echtes_limit = fehlerstatus in (\n'
            '            "quota_exceeded", "character_limit_exceeded",\n'
            '            "insufficient_credits", "credit_limit_exceeded",\n'
            '            "insufficient_quota")\n'
            '        if not fehlerstatus:\n'
            '            # Legacy servers may return no structured status.\n'
            '            echtes_limit = any(w in meldung for w in (\n'
            '                "character_limit_exceeded", "quota_exceeded",\n'
            '                "insufficient_credits", "insufficient credit",\n'
            '                "credit limit exceeded", "out of credits"))\n'
            '        if echtes_limit:\n'
            '            raise NetworkError(\n'
            '                "Das Kontingent bei ElevenLabs ist aufgebraucht.",\n'
            '                "ElevenLabs API: " + (_server_message(resp) or "(nincs részlet)")[:220]\n'
            '                + "\\nEllenőrizd a kulcs és a fiók korlátait.")\n'
            '        raise Ueberlastet(',
        ),
        (
            "    return resp\n\n\ndef check_key(api_key: str) -> Quota:",
            '    if resp.status_code in (500, 502, 503, 504):\n'
            '        raise Ueberlastet(\n'
            '            f"ElevenLabs átmeneti HTTP {resp.status_code} hibát jelzett.",\n'
            '            "Átmeneti szolgáltatáshiba; a program megpróbálja újra. "\n'
            '            f"Kód: {(_server_message(resp) or \u0027nincs részlet\u0027)[:160]}")\n'
            '    return resp\n\n\ndef check_key(api_key: str) -> Quota:',
        ),
    ])
    patch("dreamevoice/elevenlabs.py", [
        (
            '                        log("Das Bisherige bleibt gespeichert. Beim nächsten "\n'
            '                            "Versuch macht die App genau hier weiter.")',
            '                        log("ElevenLabs részlet: " + str(fehler)[:420])\n'
            '                        log("Das Bisherige bleibt gespeichert. Beim nächsten "\n'
            '                            "Versuch macht die App genau hier weiter.")',
        ),
    ])

    # Intermittent service errors should be retried, not packaged as partial
    # HU voice sets. This adjustment only targets the known transient error.
    patch("dreamevoice/elevenlabs.py", [
        (
            '            if isinstance(fehler, Ueberlastet):\n'
            '                # Eine Drosselung kostet kein Kontingent - erneut',
            '            if (isinstance(fehler, NetworkError) and\n'
            '                    fehler.message == "ElevenLabs ist nicht erreichbar."):\n'
            '                fehler = Ueberlastet(\n'
            '                    "ElevenLabs-hálózati hiba: újrapróbálkozás.",\n'
            '                    str(fehler))\n'
            '            if isinstance(fehler, Ueberlastet):\n'
            '                # Eine Drosselung kostet kein Kontingent - erneut',
        ),
    ])

    # Full-coverage HU workflow: export all genuinely missing robot sound IDs
    # with a strict LLM translation prompt, import ONLY new validated texts.
    patch("dreamevoice/ui/tab_store.py", [
        (
            'from .. import (audio, custom, dialect, dialektpakete, elevenlabs,',
            'from .. import hu_translation\n'
            'from .. import (audio, custom, dialect, dialektpakete, elevenlabs,',
        ),
        (
            '        ttk.Label(card.content,\n'
            '                  text=("Die Kostprobe spricht drei Sätze',
            '        ttk.Button(dateien, text="Hiányzó magyar hangok exportálása",\n'
            '                   style="Small.TButton",\n'
            '                   command=self._hu_export_missing).pack(side="left", padx=(8, 0))\n'
            '        ttk.Button(dateien, text="Magyar fordítások importálása",\n'
            '                   style="Small.TButton",\n'
            '                   command=self._hu_import_missing).pack(side="left", padx=(8, 0))\n'
            '\n'
            '        ttk.Label(card.content,\n'
            '                  text=("Die Kostprobe spricht drei Sätze',
        ),
        (
            '    def _on_export_texts(self) -> None:',
            '    def _hu_export_missing(self) -> None:\n'
            '        """Create an AI translation prompt for every uncovered robot sound."""\n'
            '        from datetime import datetime\n'
            '        pack = self._selected_dialect()\n'
            '        if pack is None or pack.key != "magyar_vicces":\n'
            '            messagebox.showinfo("Magyar hangcsomag",\n'
            '                                "Válaszd ki a Magyar – Vicces házimunkás csomagot.",\n'
            '                                parent=self)\n'
            '            return\n'
            '        if not self.state.has_base_pack:\n'
            '            messagebox.showwarning("Hiányzó gyári csomag",\n'
            '                                   "Előbb töltsd le a robot gyári hangcsomagját.",\n'
            '                                   parent=self)\n'
            '            return\n'
            '        try:\n'
            '            ids = official.list_sound_ids(self.state.base_pack_path)\n'
            '            stamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")\n'
            '            destination = textfiles.folder() / (\n'
            '                f"magyar_vicces_hianyzo_{stamp}.txt")\n'
            '            path, count, unknown = hu_translation.export_prompt(\n'
            '                ids, self._effective_dialect(pack).texts,\n'
            '                self.state.catalog, destination)\n'
            '        except (OSError, ValueError) as exc:\n'
            '            show_error(self, self.theme, "Exportálási hiba", str(exc))\n'
            '            return\n'
            '        show_info(self, self.theme, "Magyar fordítási prompt elkészült",\n'
            '                  f"{count} hiányzó bemondás listája exportálva.\\n{path}",\n'
            '                  f"{unknown} hanghoz nincs megbízható szöveges leírás; "\n'
            '                  "ezeket a gyári hang alapján kell beazonosítani. "\n'
            '                  "A meglévő magyar szövegek érintetlenek maradtak. "\n'
            '                  "A fájlt add át a fordításhoz, majd importáld vissza.")\n'
            '\n'
            '    def _hu_import_missing(self) -> None:\n'
            '        """Merge only missing HU strings, preserving user edits and audio."""\n'
            '        from dataclasses import replace\n'
            '        pack = self._selected_dialect()\n'
            '        if pack is None or pack.key != "magyar_vicces":\n'
            '            messagebox.showinfo("Magyar hangcsomag",\n'
            '                                "Válaszd ki a Magyar – Vicces házimunkás csomagot.",\n'
            '                                parent=self)\n'
            '            return\n'
            '        if not self.state.has_base_pack:\n'
            '            messagebox.showwarning("Hiányzó gyári csomag",\n'
            '                                   "Előbb töltsd le a robot gyári hangcsomagját.",\n'
            '                                   parent=self)\n'
            '            return\n'
            '        path = filedialog.askopenfilename(\n'
            '            parent=self, title="Magyar bemondások importálása",\n'
            '            initialdir=str(textfiles.folder()),\n'
            '            filetypes=[("Szövegfájlok", "*.txt"), ("Minden fájl", "*.*")])\n'
            '        if not path:\n'
            '            return\n'
            '        try:\n'
            '            ids = official.list_sound_ids(self.state.base_pack_path)\n'
            '            raw = Path(path).read_text(encoding="utf-8-sig")\n'
            '            existing = self._effective_dialect(pack).texts\n'
            '            result = hu_translation.parse_missing(raw, ids, existing)\n'
            '        except (OSError, UnicodeError, ValueError) as exc:\n'
            '            show_error(self, self.theme, "Importálási hiba", str(exc))\n'
            '            return\n'
            '        if not result.new:\n'
            '            show_warning(self, self.theme, "Nincs új magyar szöveg",\n'
            '                         "A fájlban nem található új, kitöltött bemondás.",\n'
            '                         "A [FORDÍTANDÓ] és [HANGMINTA ELLENŐRZÉSE SZÜKSÉGES] "\n'
            '                         "jelölők nem számítanak fordításnak.")\n'
            '            return\n'
            '        if not messagebox.askyesno(\n'
            '            "Hiányzó bemondások hozzáadása",\n'
            '            f"{len(result.new)} új magyar bemondást adunk a csomaghoz.\\n"\n'
            '            f"{len(result.skipped_existing)} már meglévő szöveg érintetlen marad.\\n"\n'
            '            f"{len(result.skipped_placeholder)} ellenőrizendő sor kimarad.\\n\\n"\n'
            '            "A már elkészült hangfelvételek is megmaradnak. Folytatod?",\n'
            '            parent=self):\n'
            '            return\n'
            '        try:\n'
            '            updated = replace(pack, texts={**pack.texts, **result.new})\n'
            '            custom.save(updated)\n'
            '        except OSError as exc:\n'
            '            show_error(self, self.theme, "Mentési hiba", str(exc))\n'
            '            return\n'
            '        self._refill_dialect_picker()\n'
            '        self.log.append(f"{len(result.new)} új magyar bemondás hozzáadva.", "ok")\n'
            '        show_info(self, self.theme, "Magyar szövegek hozzáadva",\n'
            '                  f"{len(result.new)} új hangazonosító kapott magyar szöveget.",\n'
            '                  "A korábbi szövegek és felvételek változatlanok. "\n'
            '                  "A következő hanggenerálás csak a hiányzó új mondatokat "\n'
            '                  "készíti el.")\n'
            '\n'
            '    def _on_export_texts(self) -> None:',
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
