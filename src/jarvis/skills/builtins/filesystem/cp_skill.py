"""
Copy file skill.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from jarvis.responses import Response
from jarvis.skills import Skill
from jarvis.services.filesystem import FileSystemService


class CpSkill(Skill):
    """
    Copy a file.
    """

    def __init__(
        self,
        filesystem: FileSystemService,
    ) -> None:

        self._filesystem = filesystem

    @property
    def name(self) -> str:
        return "cp"

    @property
    def description(self) -> str:
        return "Copy a file."

    @property
    def aliases(self) -> list[str]:
        return [
            "copy",
        ]

    def execute(
        self,
        args: list[str],
    ) -> Response:

        if len(args) != 2:
            return Response(
                "Usage: cp <source> <destination>",
            )

        source = args[0]
        destination = args[1]

        if not self._filesystem.exists(source):
            return Response(
                f"'{source}' does not exist."
            )

        try:
            if Path(source).is_dir():
                shutil.copytree(
                    source,
                    destination,
                )
            else:
                shutil.copy2(
                    source,
                    destination,
                )

        except Exception as exc:
            return Response(
                f"Copy failed: {exc}"
            )

        return Response(
            f"Copied '{source}' to '{destination}'."
        )