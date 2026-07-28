"""
Speaker implementation.
"""

from jarvis.voice.engines.base import SpeechEngine
from jarvis.voice.engines.piper_engine import PiperEngine


class Speaker:
    """
    High-level speech interface.
    """

    def __init__(
        self,
        engine: SpeechEngine | None = None,
    ) -> None:
        """
        Initialize the speaker.
        """

        self._engine = engine or PiperEngine()

    def speak(
        self,
        text: str,
    ) -> None:
        """
        Speak the given text.
        """

        self._engine.speak(text)