"""
Skill manager.
"""

from __future__ import annotations

from jarvis.skills.skill import Skill


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

    def resolve(
        self,
        name: str,
    ) -> Skill | None:
        return self._skills.get(name)

    @property
    def skills(self) -> list[Skill]:
        return list(self._skills.values())