"""
Power service exceptions.
"""

from __future__ import annotations


class PowerServiceError(Exception):
    """
    Base exception for power services.
    """


class SleepNotSupportedError(PowerServiceError):
    """
    Raised when sleep is not supported on the current platform.
    """


class HibernateNotSupportedError(PowerServiceError):
    """
    Raised when hibernate is not supported on the current platform.
    """


class ShutdownFailedError(PowerServiceError):
    """
    Raised when shutdown cannot be performed.
    """


class RestartFailedError(PowerServiceError):
    """
    Raised when restart cannot be performed.
    """


class LogoutFailedError(PowerServiceError):
    """
    Raised when logout cannot be performed.
    """