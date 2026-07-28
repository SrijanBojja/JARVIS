"""
Application reference helpers.
"""

from __future__ import annotations

from jarvis.conversation.session import (
    ConversationSession,
)


class ApplicationReferences:
    """
    Resolves conversational references to applications.
    """

    def __init__(
        self,
        conversation_session: ConversationSession,
    ) -> None:
        self._conversation_session = (
            conversation_session
        )

    def latest(self):
        """
        Return the most recently remembered application.
        """

        return (
            self._conversation_session.get_entity(
                "application",
            )
        )