"""
Defines the Action model.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Action:
    """
    Represents an executable action.
    """

    name: str
    target: str | None = None
    requires_confirmation: bool = False