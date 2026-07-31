"""
Remove file or directory skill.
"""

from __future__ import annotations

from pathlib import Path

from jarvis.responses import Response
from jarvis.skills import Skill
from jarvis.services.filesystem import FileSystemService


class RmSkill(Skill):
    """
    Remove a file or directory.
    """

    def __init__(
        self,
        filesystem: FileSystemService,
    ) -> None:

        self._filesystem = filesystem

    @property
    def name(self) -> str:
        return "rm"

    @property
    def description(self) -> str:
        return "Remove a file or directory."

    @property
    def aliases(self) -> list[str]:
        return [
            "delete",
        ]

    def execute(
        self,
        args: list[str],
    ) -> Response:

        if not args:
            return Response(
                "Usage: rm <path>",
            )

        path = args[0]

        if not self._filesystem.exists(path):
            return Response(
                f"'{path}' does not exist."
            )

        if Path(path).is_dir():
            self._filesystem.delete_directory(path)
        else:
            self._filesystem.delete_file(path)

        return Response(
            f"Removed '{path}'."
        )