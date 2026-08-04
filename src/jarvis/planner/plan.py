from __future__ import annotations

from dataclasses import dataclass

from jarvis.actions import Action


@dataclass(slots=True)
class Plan:

    actions: list[Action]