"""
Speaker implementation.
"""

from __future__ import annotations

import pyttsx3


class Speaker:
    """
    Speaks text aloud.
    """

    def __init__(self) -> None:
        self._engine = pyttsx3.init()

        self._engine.setProperty("rate", 180)
        self._engine.setProperty("volume", 1.0)

    def speak(
        self,
        text: str,
    ) -> None:
        """
        Speak text aloud.
        """

        print(f"JARVIS: {text}")

        self._engine.say(text)
        self._engine.runAndWait()