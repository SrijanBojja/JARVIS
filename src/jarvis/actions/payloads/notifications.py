from dataclasses import dataclass

from .base import ActionPayload


@dataclass(frozen=True, slots=True)
class NotificationPayload(ActionPayload):
    message: str