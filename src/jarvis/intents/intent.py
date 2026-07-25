"""
Intent model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Intent:
    """
    Represents the user's intent.
    """

    name: str
    confidence: float