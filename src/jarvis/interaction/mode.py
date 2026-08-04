from __future__ import annotations

from enum import Enum


class InteractionMode(Enum):

    SHELL = "shell"
    VOICE = "voice"
    HYBRID = "hybrid"