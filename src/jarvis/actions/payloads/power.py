from dataclasses import dataclass

from .base import ActionPayload


@dataclass(frozen=True, slots=True)
class PowerPayload(ActionPayload):
    operation: str