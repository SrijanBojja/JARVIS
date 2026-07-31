"""
Windows filesystem implementation.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from .exceptions import (
    DirectoryCreateError,
    DirectoryDeleteError,
    DirectoryListError,
    FileDeleteError,
    FileReadError,
    FileWriteError,
    MoveFileError,
)
from .service import FileSystemService


class WindowsFileSystemService(FileSystemService):
    """
    Windows filesystem implementation.
    """

    def read_text(
        self,
        path: str,
    ) -> str:

        try:
            return Path(path).read_text(
                encoding="utf-8",
            )

        except Exception as exc:
            raise FileReadError(
                f"Unable to read '{path}'."
            ) from exc

    def write_text(
        self,
        path: str,
        text: str,
    ) -> None:

        try:
            Path(path).write_text(
                text,
                encoding="utf-8",
            )

        except Exception as exc:
            raise FileWriteError(
                f"Unable to write '{path}'."
            ) from exc

    def exists(
        self,
        path: str,
    ) -> bool:

        return Path(path).exists()

    def create_directory(
        self,
        path: str,
    ) -> None:

        try:
            Path(path).mkdir(
                parents=True,
                exist_ok=True,
            )

        except Exception as exc:
            raise DirectoryCreateError(
                f"Unable to create '{path}'."
            ) from exc

    def delete_file(
        self,
        path: str,
    ) -> None:

        try:
            Path(path).unlink()

        except Exception as exc:
            raise FileDeleteError(
                f"Unable to delete '{path}'."
            ) from exc

    def delete_directory(
        self,
        path: str,
    ) -> None:

        try:
            shutil.rmtree(path)

        except Exception as exc:
            raise DirectoryDeleteError(
                f"Unable to delete '{path}'."
            ) from exc

    def list_directory(
        self,
        path: str,
    ) -> list[str]:

        try:
            directory = Path(path)

            return sorted(
                item.name
                for item in directory.iterdir()
            )

        except Exception as exc:
            raise DirectoryListError(
                f"Unable to list '{path}'."
            ) from exc

    def move(
        self,
        source: str,
        destination: str,
    ) -> None:

        try:
            shutil.move(
                source,
                destination,
            )

        except Exception as exc:
            raise MoveFileError(
                f"Unable to move '{source}'."
            ) from exc

    def current_directory(
        self,
    ) -> str:

        return str(
            Path.cwd(),
        )