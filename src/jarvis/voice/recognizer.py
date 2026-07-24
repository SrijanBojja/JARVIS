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
        print("[Voice] Loading Whisper model...")

        self._model = WhisperModel(
            "base",
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

        audio_data = audio.get_wav_data()

        with open("temp.wav", "wb") as file:
            file.write(audio_data)

        segments, _ = self._model.transcribe(
            "temp.wav",
            beam_size=5,
        )

        text = " ".join(
            segment.text
            for segment in segments
        )

        return text.strip()