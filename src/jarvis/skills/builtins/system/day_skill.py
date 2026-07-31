"""
Day skill.
"""

from __future__ import annotations

from datetime import datetime

from jarvis.responses import Response
from jarvis.skills import Skill


class DaySkill(Skill):
    """
    Show today's weekday.
    """

    @property
    def name(self) -> str:
        return "day"

    @property
    def description(self) -> str:
        return "Show today's weekday."

    @property
    def aliases(self) -> list[str]:
        return [
            "weekday",
            "today day",
            "what day",
        ]

    def execute(
        self,
        args: list[str],
    ) -> Response:

        weekday = datetime.now().strftime("%A")

        return Response(
            f"Today is: {weekday}",
        )