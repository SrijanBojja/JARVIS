"""
Piper speech engine implementation.
"""

from pathlib import Path
import tempfile
import wave
import os
import tempfile
import wave
import winsound


from piper import PiperVoice

from jarvis.voice.engines.base import SpeechEngine
from jarvis.config.settings import settings


class PiperEngine(SpeechEngine):
    """
    Speech engine powered by Piper.
    """

    def __init__(self) -> None:
        """
        Initialize the Piper speech engine.
        """

        root = Path(__file__).resolve().parents[3]

        voice_path = (
            root
            / "assets"
            / "voices"
            / f"{settings.voice_model}.onnx"
        )

        self._voice = PiperVoice.load(
            voice_path,
        )
        if not voice_path.exists():
            raise FileNotFoundError(
                f"Piper voice model '{settings.voice_model}' was not found: {voice_path}"
            )

    def speak(
        self,
        text: str,
    ) -> None:
        """
        Speak the given text.
        """

        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False,
        ) as temp_file:
            temp_path = temp_file.name

        try:
            with wave.open(
                temp_path,
                "wb",
            ) as wav_file:
                self._voice.synthesize_wav(
                    text,
                    wav_file,
                )

            winsound.PlaySound(
                temp_path,
                winsound.SND_FILENAME,
            )

        finally:
            if os.path.exists(
                temp_path,
            ):
                os.remove(
                    temp_path,
                )