"""
Hybrid interaction mode.
"""

from __future__ import annotations

from threading import Thread

from jarvis.shell import Shell
from jarvis.voice import VoiceAssistant


class HybridInteraction:
    """
    Runs both shell and voice simultaneously.
    """

    def __init__(
        self,
        shell: Shell,
        voice: VoiceAssistant,
    ) -> None:

        self._shell = shell
        self._voice = voice

    def run(
        self,
    ) -> None:
        """
        Start both interaction modes.
        """

        voice_thread = Thread(
            target=self._voice.run,
            daemon=True,
        )

        voice_thread.start()

        self._shell.run()