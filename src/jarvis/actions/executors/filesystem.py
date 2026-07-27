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
        """
        Execute a filesystem action.
        """

        try:

            if action.target is None:
                return Response(
                    text="Missing filesystem target.",
                    status=ResponseStatus.ERROR,
                )

            if action.name == "create_directory":
                self._filesystem.create_directory(
                    action.target,
                )

                return Response(
                    text=f"Directory created: {action.target}",
                    status=ResponseStatus.SUCCESS,
                )

            if action.name == "list_directory":
                entries = self._filesystem.list_directory(
                    action.target,
                )

                if not entries:
                    return Response(
                        text="Directory is empty.",
                        status=ResponseStatus.SUCCESS,
                    )

                return Response(
                    text="\n".join(entries),
                    status=ResponseStatus.SUCCESS,
                )

            if action.name == "read_file":
                content = self._filesystem.read_text(
                    action.target,
                )

                return Response(
                    text=content,
                    status=ResponseStatus.SUCCESS,
                )

            if action.name == "write_file":
                self._filesystem.write_text(
                    action.target,
                    "",
                )

                return Response(
                    text=f"File written: {action.target}",
                    status=ResponseStatus.SUCCESS,
                )

            if action.name == "move_file":
                return Response(
                    text=(
                        "Move file support will be "
                        "completed in the next milestone."
                    ),
                    status=ResponseStatus.SUCCESS,
                )

            if action.name == "delete_file":
                self._filesystem.delete_file(
                    action.target,
                )

                return Response(
                    text=f"File deleted: {action.target}",
                    status=ResponseStatus.SUCCESS,
                )

            if action.name == "delete_directory":
                self._filesystem.delete_directory(
                    action.target,
                )

                return Response(
                    text=f"Directory deleted: {action.target}",
                    status=ResponseStatus.SUCCESS,
                )

            return Response(
                text=f"Unsupported filesystem action: {action.name}",
                status=ResponseStatus.ERROR,
            )

        except Exception as exc:
            return Response(
                text=str(exc),
                status=ResponseStatus.ERROR,
            )