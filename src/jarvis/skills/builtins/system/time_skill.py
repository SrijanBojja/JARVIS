"""
Time skill.
"""

from __future__ import annotations

from datetime import datetime

from jarvis.responses import Response
from jarvis.skills import Skill


class TimeSkill(Skill):
    """
    Show the current local time.
    """

    @property
    def name(self) -> str:
        return "time"

    @property
    def description(self) -> str:
        return "Show the current local time."

    @property
    def aliases(self) -> list[str]:
        return [
            "clock",
            "current time",
            "what time",
        ]

    def execute(
        self,
        args: list[str],
    ) -> Response:

        current_time = datetime.now().strftime("%H:%M:%S")

        return Response(
            f"Current time: {current_time}",
        )