"""
Present working directory skill.
"""

from __future__ import annotations

from jarvis.responses import Response
from jarvis.skills import Skill
from jarvis.services.filesystem import FileSystemService


class PwdSkill(Skill):
    """
    Display the current working directory.
    """

    def __init__(
        self,
        filesystem: FileSystemService,
    ) -> None:

        self._filesystem = filesystem

    @property
    def name(self) -> str:
        return "pwd"

    @property
    def description(self) -> str:
        return "Show the current working directory."

    @property
    def aliases(self) -> list[str]:
        return [
            "current directory",
            "working directory",
            "where am i",
        ]

    def execute(
        self,
        args: list[str],
    ) -> Response:

        return Response(
            self._filesystem.current_directory(),
        )