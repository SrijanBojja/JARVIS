"""
Filesystem service abstraction.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from jarvis.services import Service


class FileSystemService(Service, ABC):
    """
    Abstract filesystem service.
    """

    @abstractmethod
    def read_text(
        self,
        path: str,
    ) -> str:
        """
        Read a UTF-8 text file.
        """

    @abstractmethod
    def write_text(
        self,
        path: str,
        text: str,
    ) -> None:
        """
        Write a UTF-8 text file.
        """

    @abstractmethod
    def exists(
        self,
        path: str,
    ) -> bool:
        """
        Return whether the path exists.
        """

    @abstractmethod
    def current_directory(
        self,
    ) -> str:
        """
        Return the current working directory.
        """

    @abstractmethod
    def create_directory(
        self,
        path: str,
    ) -> None:
        """
        Create a directory.
        """

    @abstractmethod
    def delete_file(
        self,
        path: str,
    ) -> None:
        """
        Delete a file.
        """

    @abstractmethod
    def delete_directory(
        self,
        path: str,
    ) -> None:
        """
        Delete a directory.
        """

    @abstractmethod
    def list_directory(
        self,
        path: str,
    ) -> list[str]:
        """
        List directory contents.
        """

    @abstractmethod
    def move(
        self,
        source: str,
        destination: str,
    ) -> None:
        """
        Move or rename a file.
        """