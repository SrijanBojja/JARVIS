"""
Wake word detection.
"""

from __future__ import annotations


class WakeWordDetector:
    """
    Detects whether the user is trying to wake JARVIS.
    """

    def __init__(
        self,
        wake_words: tuple[str, ...] = (
            "jarvis",
            "hey jarvis",
            "okay jarvis",
        ),
    ) -> None:
        self._wake_words = tuple(
            word.lower()
            for word in wake_words
        )

    def extract(
        self,
        text: str,
    ) -> str | None:
        """
        Extract the spoken command after the wake word.
        """

        text = text.strip()

        lower = text.lower()

        for wake_word in self._wake_words:

            if lower.startswith(wake_word):

                return text[len(wake_word):].strip(" ,.")

        return None