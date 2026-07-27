"""
Filesystem action executor.
"""

from __future__ import annotations

from jarvis.actions import (
    Action,
    ActionExecutor,
)
from jarvis.responses import (
    Response,
    ResponseStatus,
)
from jarvis.services.filesystem import FileSystemService


class FileSystemActionExecutor(ActionExecutor):
    """
    Executes filesystem actions.
    """

    def __init__(
        self,
        filesystem: FileSystemService,
    ) -> None:
        self._filesystem = filesystem

    def supports(
        self,
        action: Action,
    ) -> bool:

        return action.name in {
            "read_file",
            "write_file",
            "list_directory",
            "create_directory",
            "delete_file",
            "delete_directory",
            "move_file",
        }

    def execute(
        self,
        action: Action,
    ) -> Response:

        return Response(
            text=(
                "Filesystem actions will be "
                "implemented in the next milestone."
            ),
            status=ResponseStatus.SUCCESS,
        )