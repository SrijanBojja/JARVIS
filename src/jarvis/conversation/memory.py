"""
Conversation memory.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ConversationMemory:
    """
    Stores remembered conversation entities.
    """

    latest_entities: dict[
        str,
        Any,
    ] = field(default_factory=dict)

    entity_history: dict[
        str,
        list[Any],
    ] = field(default_factory=dict)

    def remember_entity(
        self,
        entity_type: str,
        value: Any,
    ) -> None:
        """
        Remember an entity.
        """

        self.latest_entities[
            entity_type
        ] = value

        history = self.entity_history.setdefault(
            entity_type,
            [],
        )

        history.append(value)

    def get_entity(
        self,
        entity_type: str,
    ) -> Any | None:
        """
        Return a remembered entity.
        """

        return self.latest_entities.get(
            entity_type,
        )

    def forget_entity(
        self,
        entity_type: str,
    ) -> None:
        """
        Forget an entity.
        """

        self.latest_entities.pop(
            entity_type,
            None,
        )

    def clear(
        self,
    ) -> None:
        """
        Clear all remembered entities.
        """

        self.latest_entities.clear()
        self.entity_history.clear()

    def get_history(
        self,
        entity_type: str,
    ) -> list[Any]:
        """
        Return the remembered history
        for an entity type.
        """

        return self.entity_history.get(
            entity_type,
            [],
        )
