"""
Planner validator.
"""

from __future__ import annotations

from .plan import Plan


class PlannerValidator:
    """
    Validates AI-generated plans.
    """

    SUPPORTED_ACTIONS = {
        "open",
        "close",
        "focus",
        "maximize",
        "minimize",
        "restore",
        "press",
        "hotkey",
        "type",
        "click",
        "double_click",
        "right_click",
        "scroll",
        "move_mouse",
    }

    def validate(
        self,
        plan: Plan,
    ) -> Plan:
        """
        Validate an AI-generated plan.
        """

        actions = []

        for action in plan.actions:

            if action.name not in self.SUPPORTED_ACTIONS:
                continue

            actions.append(
                action,
            )

        return Plan(
            actions=actions,
        )