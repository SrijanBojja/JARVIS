"""
Date skill.
"""

from __future__ import annotations

from datetime import datetime

from jarvis.responses import Response
from jarvis.skills import Skill


class DateSkill(Skill):
    """
    Show today's date.
    """

    @property
    def name(self) -> str:
        return "date"

    @property
    def description(self) -> str:
        return "Show today's date."

    @property
    def aliases(self) -> list[str]:
        return [
            "today",
            "current date",
            "what date",
        ]

    def execute(
        self,
        args: list[str],
    ) -> Response:

        today = datetime.now().strftime("%Y-%m-%d")

        return Response(
            f"Today's date: {today}",
        )