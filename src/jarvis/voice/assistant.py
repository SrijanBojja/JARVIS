"""
Voice assistant loop.
"""

from __future__ import annotations
from jarvis.voice.wakeword import WakeWordDetector
from jarvis.voice.session import VoiceSession
from jarvis.voice.microphone import Microphone
from jarvis.voice.recognizer import SpeechRecognizer
from jarvis.voice.speaker import Speaker
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
        self._wake_word = WakeWordDetector()
        self._session = VoiceSession()

    def listen(self) -> str:
        """
        Listen for speech.
        """

        audio = self._microphone.listen()

        if audio is None:
            return ""

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
                if self._session.expired():
                    self.speak("Going back to sleep.")
                    self._session.stop()
                continue

            print(f"You: {text}")

            if text.lower() == "exit voice":
                self.speak("Leaving voice mode.")
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
                    self.speak("Yes?")
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
                self.speak(
                    response.text,
                )

            if self._session.expired():
                self.speak("Going back to sleep.")
                self._session.stop()