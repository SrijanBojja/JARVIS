"""
Windows notification service.
"""

from __future__ import annotations

from plyer import notification

from .exceptions import NotificationError
from .service import NotificationService


class WindowsNotificationService(NotificationService):
    """
    Windows implementation of NotificationService.
    """

    def notify(
        self,
        title: str,
        message: str,
    ) -> None:
        """
        Display a desktop notification.
        """

        try:
            notification.notify(
                title=title,
                message=message,
                app_name="JARVIS",
                timeout=5,
            )

        except Exception as exc:
            raise NotificationError(
                "Failed to display notification."
            ) from exc