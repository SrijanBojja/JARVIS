"""
Filesystem service.
"""

from .exceptions import (
    DirectoryCreateError,
    DirectoryDeleteError,
    DirectoryListError,
    FileDeleteError,
    FileReadError,
    FileSystemServiceError,
    FileWriteError,
    MoveFileError,
)
from .service import FileSystemService
from .windows import WindowsFileSystemService

__all__ = [
    "DirectoryCreateError",
    "DirectoryDeleteError",
    "DirectoryListError",
    "FileDeleteError",
    "FileReadError",
    "FileSystemService",
    "FileSystemServiceError",
    "FileWriteError",
    "MoveFileError",
    "WindowsFileSystemService",
]