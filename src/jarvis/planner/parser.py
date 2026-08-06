"""
Planner JSON parser.
"""

from __future__ import annotations

import json

from jarvis.actions import Action

from .plan import Plan


class PlannerParser:
    """
    Converts AI planner JSON into a Plan.
    """

    def parse(
        self,
        response: str,
    ) -> Plan:
        """
        Parse planner JSON.
        """

        data = json.loads(
            response,
        )

        actions = []

        for item in data.get(
            "actions",
            [],
        ):
            actions.append(
                Action(
                    name=item["name"],
                    target=item.get(
                        "target",
                    ),
                )
            )

        return Plan(
            actions=actions,
        )