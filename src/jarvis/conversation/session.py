"""
Conversation session.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from jarvis.applications.search import (
    ApplicationSearchResult,
)
from jarvis.actions import Action
from jarvis.responses import (
    Response,
    ResponseStatus,
)
from .memory import ConversationMemory


@dataclass(slots=True)
class ConversationSession:
    """
    Stores temporary conversation state.
    """

    pending_applications: (
        list[ApplicationSearchResult] | None
    ) = None

    memory: ConversationMemory = field(
        default_factory=ConversationMemory,
    )

    variables: dict[
        str,
        Any,
    ] = field(default_factory=dict)

    last_action: str | None = None
    last_response: str | None = None

    @property
    def waiting_for_application(
        self,
    ) -> bool:
        return (
            self.pending_applications is not None
        )

    @property
    def last_application(self) -> str | None:
        return self.get_entity("application")

    @last_application.setter
    def last_application(
        self,
        value: str | None,
    ) -> None:

        if value is None:
            self.forget_entity("application")
        else:
            self.remember_entity(
                "application",
                value,
            )

    @property
    def last_file(self) -> str | None:
        return self.get_entity("file")

    @last_file.setter
    def last_file(
        self,
        value: str | None,
    ) -> None:

        if value is None:
            self.forget_entity("file")
        else:
            self.remember_entity(
                "file",
                value,
            )

    @property
    def last_directory(self) -> str | None:
        return self.get_entity("directory")

    @last_directory.setter
    def last_directory(
        self,
        value: str | None,
    ) -> None:

        if value is None:
            self.forget_entity("directory")
        else:
            self.remember_entity(
                "directory",
                value,
            )

    def remember_entity(
        self,
        entity_type: str,
        value: Any,
    ) -> None:
        """
        Remember an entity for later reference.
        """

        self.memory.remember_entity(
            entity_type,
            value,
        )

    def get_entity(
        self,
        entity_type: str,
    ) -> Any | None:
        """
        Return a remembered entity.
        """

        return self.memory.get_entity(
            entity_type,
        )

    def forget_entity(
        self,
        entity_type: str,
    ) -> None:
        """
        Forget a remembered entity.
        """

        self.memory.forget_entity(
            entity_type,
        )

    def set_variable(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Store a conversation variable.
        """

        self.variables[key] = value

    def get_variable(
        self,
        key: str,
    ) -> Any | None:
        """
        Return a stored conversation variable.
        """

        return self.variables.get(
            key,
        )

    def remove_variable(
        self,
        key: str,
    ) -> None:
        """
        Remove a conversation variable.
        """

        self.variables.pop(
            key,
            None,
        )

    def remember_action(
        self,
        action: str,
    ) -> None:
        """
        Remember the last executed action.
        """

        self.last_action = action

    def remember_response(
        self,
        response: str,
    ) -> None:
        """
        Remember the last response.
        """

        self.last_response = response

    def clear(self) -> None:
        """
        Clear transient conversation state.

        Note:
            Remembered entities and variables are preserved.
        """

        self.pending_applications = None

    def reset(self) -> None:
        """
        Reset the entire conversation.
        """

        self.pending_applications = None

        self.memory.clear()
        self.variables.clear()

        self.last_action = None
        self.last_response = None

    def update_from_action(
        self,
        action: Action,
        response: Response,
    ) -> None:
        """
        Update conversation state from a successful action.
        """

        if response.status != ResponseStatus.SUCCESS:
            return

        self.remember_action(action.name)
        self.remember_response(response.text)

        if action.target is None:
            return

        if action.name == "open":
            self.remember_entity(
                "application",
                action.target,
            )

        elif action.name in {
            "read_file",
            "write_file",
            "delete_file",
        }:
            self.remember_entity(
                "file",
                action.target,
            )

        elif action.name in {
            "create_directory",
            "list_directory",
            "delete_directory",
        }:
            self.remember_entity(
                "directory",
                action.target,
            )