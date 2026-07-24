"""
Voice assistant loop.
"""

from __future__ import annotations

from jarvis.voice import (
    Microphone,
    Speaker,
    SpeechRecognizer,
)


class VoiceAssistant:
    """
    Handles voice interaction.
    """

    def __init__(self) -> None:
        self._microphone = Microphone()
        self._recognizer = SpeechRecognizer()
        self._speaker = Speaker()

    def listen(self) -> str:
        """
        Listen for speech.
        """

        audio = self._microphone.listen()

        return self._recognizer.recognize(audio)

    def speak(
        self,
        text: str,
    ) -> None:
        """
        Speak text.
        """

        self._speaker.speak(text)