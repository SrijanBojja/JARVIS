"""
Create empty file skill.
"""

from __future__ import annotations

from jarvis.responses import Response
from jarvis.skills import Skill
from jarvis.services.filesystem import FileSystemService


class TouchSkill(Skill):
    """
    Create an empty file.
    """

    def __init__(
        self,
        filesystem: FileSystemService,
    ) -> None:

        self._filesystem = filesystem

    @property
    def name(self) -> str:
        return "touch"

    @property
    def description(self) -> str:
        return "Create an empty file."

    @property
    def aliases(self) -> list[str]:
        return [
            "create file",
        ]

    def execute(
        self,
        args: list[str],
    ) -> Response:

        if not args:
            return Response(
                "Usage: touch <file>",
            )

        path = args[0]

        if self._filesystem.exists(path):
            return Response(
                f"File '{path}' already exists.",
            )

        self._filesystem.write_text(
            path,
            "",
        )

        return Response(
            f"File '{path}' created.",
        )