"""
UUID skill.
"""

from __future__ import annotations

import uuid

from jarvis.responses import Response
from jarvis.skills import Skill


class UUIDSkill(Skill):
    """
    Generate a UUID.
    """

    @property
    def name(self) -> str:
        return "uuid"

    @property
    def description(self) -> str:
        return "Generate a UUID."

    @property
    def aliases(self) -> list[str]:
        return [
            "guid",
            "unique id",
            "generate uuid",
        ]

    def execute(
        self,
        args: list[str],
    ) -> Response:

        return Response(
            f"UUID: {uuid.uuid4()}",
        )