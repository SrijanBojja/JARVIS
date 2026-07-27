"""
Filesystem service exceptions.
"""

from __future__ import annotations


class FileSystemServiceError(Exception):
    """
    Base filesystem service exception.
    """


class FileReadError(FileSystemServiceError):
    """
    Raised when reading a file fails.
    """


class FileWriteError(FileSystemServiceError):
    """
    Raised when writing a file fails.
    """


class FileDeleteError(FileSystemServiceError):
    """
    Raised when deleting a file fails.
    """


class DirectoryCreateError(FileSystemServiceError):
    """
    Raised when creating a directory fails.
    """


class DirectoryDeleteError(FileSystemServiceError):
    """
    Raised when deleting a directory fails.
    """


class DirectoryListError(FileSystemServiceError):
    """
    Raised when listing a directory fails.
    """


class MoveFileError(FileSystemServiceError):
    """
    Raised when moving or renaming fails.
    """