"""
Voice command for JARVIS.
"""

from __future__ import annotations

from jarvis.commands import Command
from jarvis.responses import Response
from jarvis.voice import VoiceAssistant


class VoiceCommand(Command):
    """
    Start voice mode.
    """

    def __init__(
        self,
        assistant: VoiceAssistant,
    ) -> None:
        self._assistant = assistant

    @property
    def name(self) -> str:
        return "voice"

    @property
    def description(self) -> str:
        return "Start voice mode."

    def execute(
        self,
        args: list[str],
    ) -> Response:

        print()
        print("Voice mode started.")
        print("Say 'exit voice' to return to the shell.")
        print()

        self._assistant.run()

        return Response(
            "Voice mode ended.",
        )