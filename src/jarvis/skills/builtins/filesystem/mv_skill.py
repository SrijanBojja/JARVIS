"""
Move or rename a file or directory skill.
"""

from __future__ import annotations

from jarvis.responses import Response
from jarvis.skills import Skill
from jarvis.services.filesystem import FileSystemService


class MvSkill(Skill):
    """
    Move or rename a file or directory.
    """

    def __init__(
        self,
        filesystem: FileSystemService,
    ) -> None:

        self._filesystem = filesystem

    @property
    def name(self) -> str:
        return "mv"

    @property
    def description(self) -> str:
        return "Move or rename a file or directory."

    @property
    def aliases(self) -> list[str]:
        return [
            "move",
            "rename",
        ]

    def execute(
        self,
        args: list[str],
    ) -> Response:

        if len(args) != 2:
            return Response(
                "Usage: mv <source> <destination>",
            )

        source = args[0]
        destination = args[1]

        if not self._filesystem.exists(source):
            return Response(
                f"'{source}' does not exist."
            )

        self._filesystem.move(
            source,
            destination,
        )

        return Response(
            f"Moved '{source}' to '{destination}'."
        )