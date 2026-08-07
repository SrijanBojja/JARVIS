"""
Automation execution result.
"""

from __future__ import annotations

from dataclasses import dataclass

from jarvis.actions import Action
from jarvis.responses import Response


@dataclass(slots=True, frozen=True)
class AutomationResult:
    """
    Represents the result of an automation.
    """

    actions: list[Action]

    responses: list[Response]
    