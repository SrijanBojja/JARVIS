"""
Skill module for JARVIS.
"""

from __future__ import annotations

from jarvis.modules import Module
from jarvis.skills.builtins import (
    BUILTIN_SKILLS,
)
from jarvis.skills.builtins.filesystem import (
    FILESYSTEM_SKILLS,
)
from jarvis.skills.manager import SkillManager
from jarvis.responses import Response
from jarvis.skills.exceptions import (
    SkillNotFoundError,
)
from jarvis.services.filesystem import FileSystemService

class SkillModule(Module):
    """
    Manages JARVIS skills.
    """

    def __init__(
        self,
        filesystem: FileSystemService,
    ) -> None:

        self._manager = SkillManager()
        self._filesystem = filesystem

    @property
    def skill_manager(self) -> SkillManager:
        return self._manager

    def execute(
        self,
        name: str,
        args: list[str],
    ) -> Response | None:

        try:
            skill = self._manager.resolve(
                name,
            )

        except SkillNotFoundError:
            return None

        return skill.execute(
            args,
        )

    def initialize(self) -> None:

        for skill in BUILTIN_SKILLS:

            if skill in FILESYSTEM_SKILLS:
                self._manager.register(
                    skill(
                        self._filesystem,
                    ),
                )
            else:
                self._manager.register(
                    skill(),
                )

    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass