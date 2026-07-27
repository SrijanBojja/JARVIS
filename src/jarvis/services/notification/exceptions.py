"""
Notification service exceptions.
"""

from __future__ import annotations


class NotificationServiceError(Exception):
    """
    Base notification service exception.
    """


class NotificationError(NotificationServiceError):
    """
    Raised when a notification cannot be displayed.
    """