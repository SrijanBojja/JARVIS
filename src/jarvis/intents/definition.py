"""
Intent definition model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class IntentDefinition:
    """
    Defines an intent and the phrases that trigger it.
    """

    name: str
    aliases: tuple[str, ...]