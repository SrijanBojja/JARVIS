"""
Conversation manager.
"""

from __future__ import annotations

from jarvis.commands.module import CommandModule
from jarvis.commands.exceptions import CommandNotFoundError
from jarvis.skills.module import SkillModule
from jarvis.responses import Response
from jarvis.ai import AIService

class ConversationManager:
    """
    Coordinates user conversations.
    """

    def __init__(
        self,
        command_module: CommandModule,
        skill_module: SkillModule,
        ai_service: AIService,
    ) -> None:
        """
        Initialize the conversation manager.
        """

        self._command_module = command_module
        self._skill_module = skill_module
        self._ai_service = ai_service

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
            response = self._skill_module.execute(
                command,
                args,
            )

            if response is not None:
                return response

        message = " ".join(
            [command, *args],
        ).strip()

        return self._ai_service.chat(
            message,
        )