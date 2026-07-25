"""
Defines the Action model.
"""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class Action:
    """
    Represents an executable action.
    """

    name: str
    target: str | None = None
    data: Any = None