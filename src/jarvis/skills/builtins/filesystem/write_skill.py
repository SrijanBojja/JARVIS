"""
Write text to a file skill.
"""

from __future__ import annotations

from jarvis.responses import Response
from jarvis.skills import Skill
from jarvis.services.filesystem import FileSystemService


class WriteSkill(Skill):
    """
    Write text to a file.
    """

    def __init__(
        self,
        filesystem: FileSystemService,
    ) -> None:

        self._filesystem = filesystem

    @property
    def name(self) -> str:
        return "write"

    @property
    def description(self) -> str:
        return "Write text to a file."

    @property
    def aliases(self) -> list[str]:
        return [
            "save",
        ]

    def execute(
        self,
        args: list[str],
    ) -> Response:

        if len(args) < 2:
            return Response(
                "Usage: write <file> <text>",
            )

        path = args[0]
        text = " ".join(args[1:])

        self._filesystem.write_text(
            path,
            text,
        )

        return Response(
            f"Wrote to '{path}'.",
        )