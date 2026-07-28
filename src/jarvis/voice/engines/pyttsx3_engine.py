"""
pyttsx3 speech engine implementation.
"""

import pyttsx3

from jarvis.voice.engines.base import SpeechEngine


class Pyttsx3Engine(SpeechEngine):
    """
    Speech engine powered by pyttsx3.
    """

    def __init__(self) -> None:
        """
        Initialize the speech engine.
        """

        self._engine = pyttsx3.init()

    def speak(
        self,
        text: str,
    ) -> None:
        self._engine.say(text)
        self._engine.runAndWait()