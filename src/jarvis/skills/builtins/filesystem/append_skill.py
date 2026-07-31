"""
Append text to a file skill.
"""

from __future__ import annotations

from jarvis.responses import Response
from jarvis.skills import Skill
from jarvis.services.filesystem import FileSystemService


class AppendSkill(Skill):
    """
    Append text to a file.
    """

    def __init__(
        self,
        filesystem: FileSystemService,
    ) -> None:

        self._filesystem = filesystem

    @property
    def name(self) -> str:
        return "append"

    @property
    def description(self) -> str:
        return "Append text to a file."

    @property
    def aliases(self) -> list[str]:
        return [
            "add",
        ]

    def execute(
        self,
        args: list[str],
    ) -> Response:

        if len(args) < 2:
            return Response(
                "Usage: append <file> <text>",
            )

        path = args[0]
        new_text = " ".join(args[1:])

        if self._filesystem.exists(path):
            existing = self._filesystem.read_text(path)

            if existing:
                text = existing + "\n" + new_text
            else:
                text = new_text
        else:
            text = new_text

        self._filesystem.write_text(
            path,
            text,
        )

        return Response(
            f"Appended to '{path}'."
        )