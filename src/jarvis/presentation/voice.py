"""
Voice presenter.
"""

from __future__ import annotations

from jarvis.presentation.presenter import Presenter
from jarvis.responses import Response
from jarvis.voice.module import VoiceModule


class VoicePresenter(Presenter):
    """
    Presents responses using speech.
    """

    def __init__(
        self,
        voice_module: VoiceModule,
    ) -> None:
        """
        Initialize the voice presenter.
        """

        self._voice_module = voice_module

    def present(
        self,
        response: Response,
    ) -> None:
        """
        Speak a response.
        """

        self._voice_module.speak(
            response.text,
        )