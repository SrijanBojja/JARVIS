from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ActionPayload:
    """
    Base class for all action payloads.
    """