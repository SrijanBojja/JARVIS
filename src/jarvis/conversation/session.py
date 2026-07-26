"""
Conversation session.
"""

from __future__ import annotations

from dataclasses import dataclass

from jarvis.applications.search import (
    ApplicationSearchResult,
)

@dataclass(slots=True)
class ConversationSession:
    """
    Stores temporary conversation state.
    """

    pending_applications: (
        list[ApplicationSearchResult] | None
    ) = None

    @property
    def waiting_for_application(
        self,
    ) -> bool:
        return (
            self.pending_applications is not None
        )

    def clear(self) -> None:
        self.pending_applications = None