"""
Voice assistant loop.
"""

from __future__ import annotations
from jarvis.voice.wakeword import WakeWordDetector
from jarvis.voice.session import VoiceSession
from jarvis.voice.microphone import Microphone
from jarvis.voice.recognizer import SpeechRecognizer
from jarvis.presentation import PresentationPipeline
from jarvis.conversation import ConversationManager
from jarvis.utils import CommandParser
from jarvis.responses import Response

class VoiceAssistant:
    """
    Handles voice interaction.
    """

    def __init__(
        self,
        conversation_manager: ConversationManager,
        microphone: Microphone,
        recognizer: SpeechRecognizer,
        wake_word: WakeWordDetector,
        session: VoiceSession,
        presentation_pipeline: PresentationPipeline,
    ) -> None:
        self._conversation_manager = conversation_manager
        self._parser = CommandParser()
        self._microphone = microphone
        self._recognizer = recognizer
        self._wake_word = wake_word
        self._session = session
        self._presentation_pipeline = presentation_pipeline

    def listen(self) -> str:
        """
        Listen for speech.
        """

        audio = self._microphone.listen()

        if audio is None:
            return ""

        return self._recognizer.recognize(audio)


    def run(
        self,
    ) -> None:
        """
        Start the voice assistant.
        """

        self._session.start()

        EXIT_COMMANDS = {
            "exit",
            "quit",
            "bye",
            "goodbye",
            "stop listening",
            "exit voice",
        }

        while True:

            text = (
                self.listen()
                .strip()
                .rstrip(".!?")
            )

            if not text:

                if self._session.expired():

                    self._presentation_pipeline.present(
                        Response(
                            "Going back to sleep.",
                        ),
                    )

                    self._session.stop()

                continue

            print(f"You: {text}")

            normalized = (
                text.lower()
                .strip()
                .rstrip(".!?")
            )

            if any(
                command in normalized
                for command in EXIT_COMMANDS
            ):

                self._presentation_pipeline.present(
                    Response(
                        "Leaving voice mode.",
                    ),
                )

                break


            self._session.refresh()

            command, args = self._parser.parse(
                text,
            )

            response = self._conversation_manager.handle(
                command,
                args,
            )

            if response is not None:

                self._presentation_pipeline.present(
                    response,
                )

            if self._session.expired():

                self._presentation_pipeline.present(
                    Response(
                        "Going back to sleep.",
                    ),
                )

                self._session.stop()