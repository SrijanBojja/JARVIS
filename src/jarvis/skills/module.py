"""
Skill module for JARVIS.
"""

from __future__ import annotations

from jarvis.modules import Module
from jarvis.skills.builtins import CalculatorSkill
from jarvis.skills.manager import SkillManager


class SkillModule(Module):
    """
    Manages JARVIS skills.
    """

    def __init__(self) -> None:
        self.manager = SkillManager()

    @property
    def skill_manager(self) -> SkillManager:
        return self.manager

    def execute(
        self,
        name: str,
        args: list[str],
    ) -> bool:

        skill = self.manager.resolve(name)

        if skill is None:
            return False

        skill.execute(args)

        return True

    def initialize(self) -> None:
        self.manager.register(
            CalculatorSkill(),
        )

    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass