"""
Create directory skill.
"""

from __future__ import annotations

from jarvis.responses import Response
from jarvis.skills import Skill
from jarvis.services.filesystem import FileSystemService


class MkdirSkill(Skill):
    """
    Create a directory.
    """

    def __init__(
        self,
        filesystem: FileSystemService,
    ) -> None:

        self._filesystem = filesystem

    @property
    def name(self) -> str:
        return "mkdir"

    @property
    def description(self) -> str:
        return "Create a new directory."

    @property
    def aliases(self) -> list[str]:
        return [
            "md",
            "make directory",
        ]

    def execute(
        self,
        args: list[str],
    ) -> Response:

        if not args:
            return Response(
                "Usage: mkdir <directory>",
            )

        path = args[0]

        self._filesystem.create_directory(
            path,
        )

        return Response(
            f"Directory '{path}' created.",
        )