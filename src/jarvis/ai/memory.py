"""
Conversation memory for JARVIS.
"""

from __future__ import annotations

from jarvis.ai.message import Message


class ConversationMemory:
    """
    Stores recent conversation history.
    """

    def __init__(
        self,
        max_messages: int = 20,
    ) -> None:
        self._messages: list[Message] = []
        self._max_messages = max_messages

    def add_user_message(
        self,
        message: str,
    ) -> None:

        self._add(
            Message(
                role="user",
                content=message,
            )
        )

    def add_assistant_message(
        self,
        message: str,
    ) -> None:

        self._add(
            Message(
                role="assistant",
                content=message,
            )
        )

    def messages(
        self,
    ) -> list[Message]:
        """
        Return the conversation history.
        """

        return list(
            self._messages,
        )

    def clear(
        self,
    ) -> None:

        self._messages.clear()

    def _add(
        self,
        message: Message,
    ) -> None:

        self._messages.append(
            message,
        )

        if len(self._messages) > self._max_messages:
            self._messages.pop(0)