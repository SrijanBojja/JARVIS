from __future__ import annotations

from dataclasses import dataclass

from .plan import Plan


@dataclass(slots=True)
class PlanningResult:
    """
    Result returned by the rule planner.
    """

    plan: Plan

    remaining_text: str