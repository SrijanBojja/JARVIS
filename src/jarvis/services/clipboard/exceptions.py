"""
Clipboard service exceptions.
"""

from __future__ import annotations


class ClipboardServiceError(Exception):
    """
    Base clipboard service exception.
    """


class ClipboardReadError(ClipboardServiceError):
    """
    Raised when clipboard contents cannot be read.
    """


class ClipboardWriteError(ClipboardServiceError):
    """
    Raised when clipboard contents cannot be written.
    """


class ClipboardClearError(ClipboardServiceError):
    """
    Raised when clipboard cannot be cleared.
    """