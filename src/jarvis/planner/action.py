from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Action:

    name: str

    arguments: list[str]