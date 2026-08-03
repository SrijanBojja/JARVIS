"""
Perception state model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path


@dataclass(slots=True)
class PerceptionState:
    """
    Represents the current observable state of the desktop.
    """

    timestamp: datetime

    active_window: str

    clipboard: str

    running_processes: int

    screenshot: Path

    windows: list[str] = field(default_factory=list)