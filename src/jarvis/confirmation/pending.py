"""
Pending confirmation action.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Callable


@dataclass(slots=True)
class PendingAction:
    """
    Represents an action waiting for user confirmation.
    """

    action_id: str
    title: str
    message: str

    callback: Callable[..., Any]

    created_at: datetime
    expires_at: datetime