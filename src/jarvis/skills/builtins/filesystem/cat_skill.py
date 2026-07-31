"""
Read text file skill.
"""

from __future__ import annotations

from jarvis.responses import Response
from jarvis.skills import Skill
from jarvis.services.filesystem import FileSystemService


class CatSkill(Skill):
    """
    Display a text file.
    """

    def __init__(
        self,
        filesystem: FileSystemService,
    ) -> None:

        self._filesystem = filesystem

    @property
    def name(self) -> str:
        return "cat"

    @property
    def description(self) -> str:
        return "Display a text file."

    @property
    def aliases(self) -> list[str]:
        return [
            "type",
            "read",
        ]

    def execute(
        self,
        args: list[str],
    ) -> Response:

        if not args:
            return Response(
                "Usage: cat <file>",
            )

        path = args[0]

        if not self._filesystem.exists(path):
            return Response(
                f"File '{path}' does not exist.",
            )

        text = self._filesystem.read_text(
            path,
        )

        return Response(
            text,
        )