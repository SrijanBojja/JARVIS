"""
Chat message model for JARVIS.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class Message:
    """
    Represents a chat message.
    """

    role: str

    content: str

    tool_call_id: str | None = None

    name: str | None = None

    metadata: dict[str, object] = field(
        default_factory=dict,
    )