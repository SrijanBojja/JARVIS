"""
Process service exceptions.
"""

from __future__ import annotations


class ProcessServiceError(Exception):
    """
    Base exception for process services.
    """


class ProcessLaunchError(ProcessServiceError):
    """
    Raised when a target cannot be launched.
    """


class ProcessNotFoundError(ProcessServiceError):
    """
    Raised when the requested process cannot be found.
    """


class ProcessTerminationError(ProcessServiceError):
    """
    Raised when a process cannot be terminated.
    """