"""
List directory contents skill.
"""

from __future__ import annotations

from jarvis.responses import Response
from jarvis.skills import Skill
from jarvis.services.filesystem import FileSystemService


class LsSkill(Skill):
    """
    List directory contents.
    """

    def __init__(
        self,
        filesystem: FileSystemService,
    ) -> None:

        self._filesystem = filesystem

    @property
    def name(self) -> str:
        return "ls"

    @property
    def description(self) -> str:
        return "List directory contents."

    @property
    def aliases(self) -> list[str]:
        return [
            "dir",
            "list",
            "list files",
            "show files",
        ]

    def execute(
        self,
        args: list[str],
    ) -> Response:

        path = (
            args[0]
            if args
            else self._filesystem.current_directory()
        )

        items = self._filesystem.list_directory(
            path,
        )

        if not items:
            return Response(
                "Directory is empty.",
            )

        return Response(
            "\n".join(items),
        )