"""
Conversation session.
"""

from __future__ import annotations

from dataclasses import dataclass

from jarvis.applications.search import (
    ApplicationSearchResult,
)
from jarvis.actions.action import Action
from jarvis.responses import Response, ResponseStatus

@dataclass(slots=True)
class ConversationSession:
    """
    Stores temporary conversation state.
    """

    pending_applications: (
        list[ApplicationSearchResult] | None
    ) = None

    last_application: str | None = None
    last_file: str | None = None
    last_directory: str | None = None

    @property
    def waiting_for_application(
        self,
    ) -> bool:
        return (
            self.pending_applications is not None
        )

    def remember(
        self,
        action: Action,
        response: Response,
    ) -> None:
        """
        Remember successful actions for later reference.
        """

        if response.status != ResponseStatus.SUCCESS:
            return

        if action.target is None:
            return

        if action.name == "open":
            self.last_application = action.target

        elif action.name in {
            "read_file",
            "write_file",
            "delete_file",
        }:
            self.last_file = action.target

        elif action.name in {
            "create_directory",
            "list_directory",
            "delete_directory",
        }:
            self.last_directory = action.target

    def clear(self) -> None:
        """
        Clear transient conversation state.

        Note:
            This does NOT clear remembered entities.
        """

        self.pending_applications = None

    def reset(self) -> None:
        """
        Reset the entire conversation.
        """

        self.pending_applications = None
        self.last_application = None
        self.last_file = None
        self.last_directory = None