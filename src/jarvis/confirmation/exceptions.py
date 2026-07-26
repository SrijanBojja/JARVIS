"""
Confirmation framework exceptions.
"""

from __future__ import annotations


class ConfirmationError(Exception):
    """
    Base exception for confirmation framework.
    """


class PendingActionError(ConfirmationError):
    """
    Raised when a pending action is invalid.
    """


class NoPendingActionError(ConfirmationError):
    """
    Raised when no action is awaiting confirmation.
    """


class ActionExpiredError(ConfirmationError):
    """
    Raised when a pending action has expired.
    """