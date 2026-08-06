"""
Speech recognizer.
"""

from __future__ import annotations

from faster_whisper import WhisperModel


class SpeechRecognizer:
    """
    Converts speech into text.
    """

    def __init__(self) -> None:

        self._model: WhisperModel | None = None

    def _load_model(
        self,
    ) -> None:

        if self._model is not None:
            return

        print("[Voice] Loading Whisper model...")

        self._model = WhisperModel(
            "small",
            device="cpu",
            compute_type="int8",
        )

        print("[Voice] Whisper ready.")

    def recognize(
        self,
        audio,
    ) -> str:
        """
        Convert speech to text.
        """

        self._load_model()

        audio_data = audio.get_wav_data()

        with open("temp.wav", "wb") as file:
            file.write(audio_data)

        segments, _ = self._model.transcribe(
            "temp.wav",
            beam_size=5,
            language="en",
        )

        text = " ".join(
            segment.text
            for segment in segments
        )

        return text.strip()