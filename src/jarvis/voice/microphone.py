"""
Microphone implementation.
"""

from __future__ import annotations

import speech_recognition as sr


class Microphone:
    """
    Captures audio from the microphone.
    """

    def __init__(self) -> None:
        self._recognizer = sr.Recognizer()

    def listen(self) -> sr.AudioData | None:
        """
        Listen for audio.
        """

        with sr.Microphone() as source:
            print()
            print("🎤 Listening...")

            self._recognizer.adjust_for_ambient_noise(
                source,
                duration=1.0,
            )

            try:
                audio = self._recognizer.listen(
                    source,
                    timeout=2,
                    phrase_time_limit=10,
                )

                return audio

            except sr.WaitTimeoutError:
                return None

