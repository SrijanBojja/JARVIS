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


    def run(self) -> None:
        """
        Start the voice assistant.
        """

        while True:

            text = self.listen()

            if not text:
                if self._session.expired():
                    self.speak("Going back to sleep.")
                    self._session.stop()
                continue

            print(f"You: {text}")

            if text.lower() == "exit voice":
                self._presentation_pipeline.present(
                    Response(
                        "Leaving voice mode.",
                    ),
                )
                break

            if not self._session.active:

                command_text = self._wake_word.extract(
                    text,
                )

                if command_text is None:
                    continue

                self._session.start()

                if command_text:

                    text = command_text

                else:
                    self._presentation_service.present(
                        Response(
                            "Yes?",
                        ),
                    )
                    continue

            self._session.refresh()

            command, args = self._parser.parse(
                text,
            )

            response = self._conversation_manager.handle(
                command,
                args,
            )

            if response is not None:
                self._presentation_service.present(
                    response,
                )

            if self._session.expired():
                self._presentation_service.present(
                    Response(
                        "Going back to sleep.",
                    ),
                )
                self._session.stop()