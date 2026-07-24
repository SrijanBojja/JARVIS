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

    def listen(self) -> bytes:
        """
        Listen for audio.
        """

        with sr.Microphone() as source:
            print()
            print("🎤 Listening...")

            self._recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5,
            )

            audio = self._recognizer.listen(source)

            return audio