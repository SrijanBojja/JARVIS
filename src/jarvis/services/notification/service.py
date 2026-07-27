"""
Notification service interface.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class NotificationService(ABC):
    """
    Platform-independent notification service.
    """

    @abstractmethod
    def notify(
        self,
        title: str,
        message: str,
    ) -> None:
        """
        Display a notification.
        """