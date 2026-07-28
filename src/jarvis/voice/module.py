"""
Voice module.
"""

from __future__ import annotations

from jarvis.modules import Module
from jarvis.voice.speaker import Speaker


class VoiceModule(Module):
    """
    Manages voice services.
    """

    def __init__(self) -> None:
        self._speaker = Speaker()

    @property
    def speaker(self) -> Speaker:
        return self._speaker

    def initialize(self) -> None:
        pass

    def start(self) -> None:
        self._speaker.speak("Voice module initialized.")

    def stop(self) -> None:
        self._speaker.speak("Voice module stopped.")
    
    def speak(
        self,
        text: str,
    ) -> None:
        """
        Speak text.
        """

        self._speaker.speak(
            text,
        )