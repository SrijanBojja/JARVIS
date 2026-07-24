"""
Chat message model for JARVIS.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Message:
    """
    Represents a chat message.
    """

    role: str
    content: str