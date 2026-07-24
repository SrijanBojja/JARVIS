"""
Conversation manager.
"""

from __future__ import annotations

from jarvis.commands.module import CommandModule
from jarvis.commands.exceptions import CommandNotFoundError
from jarvis.skills.module import SkillModule
from jarvis.responses import Response

class ConversationManager:
    """
    Coordinates user conversations.
    """

    def __init__(
        self,
        command_module: CommandModule,
        skill_module: SkillModule,
    ) -> None:
        """
        Initialize the conversation manager.
        """

        self._command_module = command_module
        self._skill_module = skill_module

    def handle(
        self,
        command: str,
        args: list[str],
    ) -> Response | None:
        """
        Handle parsed user input.
        """

        try:
            return self._command_module.execute(
                command,
                args,
            )

        except CommandNotFoundError:
            if self._skill_module.execute(
                command,
                args,
            ):
                return None

            return None