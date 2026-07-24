"""
Voice assistant loop.
"""

from __future__ import annotations

from jarvis.voice import (
    Microphone,
    Speaker,
    SpeechRecognizer,
)
from jarvis.conversation import ConversationManager
from jarvis.utils import CommandParser


class VoiceAssistant:
    """
    Handles voice interaction.
    """

    def __init__(
        self,
        conversation_manager: ConversationManager,
    ) -> None:
        self._conversation_manager = conversation_manager
        self._parser = CommandParser()
        self._microphone = Microphone()
        self._recognizer = SpeechRecognizer()
        self._speaker = Speaker()

    def listen(self) -> str:
        """
        Listen for speech.
        """

        audio = self._microphone.listen()

        return self._recognizer.recognize(audio)

    def speak(
        self,
        text: str,
    ) -> None:
        """
        Speak text.
        """

        self._speaker.speak(text)

    def run(self) -> None:
        """
        Start the voice assistant.
        """

        while True:

            text = self.listen()

            if not text:
                continue
            
            if text.lower() == "exit voice":
                self.speak("Leaving voice mode.")
                break
            
            print(f"You: {text}")

            command, args = self._parser.parse(
                text,
            )

            response = self._conversation_manager.handle(
                command,
                args,
            )

            if response is None:
                continue

            self.speak(
                response.text,
            )