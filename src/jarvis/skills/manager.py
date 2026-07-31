"""
Skill manager.
"""

from __future__ import annotations

from jarvis.skills.skill import Skill
from jarvis.skills.exceptions import (
    SkillNotFoundError,
)

class SkillManager:
    """
    Registers and executes skills.
    """

    def __init__(self) -> None:
        self._skills: dict[str, Skill] = {}

    def register(
        self,
        skill: Skill,
    ) -> None:

        self._skills[skill.name] = skill

        for alias in skill.aliases:
            self._skills[alias] = skill

    def resolve(
        self,
        name: str,
    ) -> Skill:

        skill = self._skills.get(name)

        if skill is None:
            raise SkillNotFoundError(
                f"Unknown skill: {name}",
            )

        return skill

    @property
    def skills(self) -> list[Skill]:
        return list(self._skills.values())