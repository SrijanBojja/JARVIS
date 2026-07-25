"""
Conversation manager.
"""

from __future__ import annotations

from jarvis.commands.module import CommandModule
from jarvis.commands.exceptions import CommandNotFoundError
from jarvis.skills.module import SkillModule
from jarvis.responses import Response
from jarvis.ai import AIService
from jarvis.intents import (
    Intent,
    IntentResolver,
)
from jarvis.actions import (
    ActionBuilder,
    ActionEngine,
)

class ConversationManager:
    """
    Coordinates user conversations.
    """

    def __init__(
        self,
        command_module: CommandModule,
        skill_module: SkillModule,
        ai_service: AIService,
        intent_resolver: IntentResolver,
        action_builder: ActionBuilder,
        action_engine: ActionEngine,
    ) -> None:
        """
        Initialize the conversation manager.
        """

        self._command_module = command_module
        self._skill_module = skill_module
        self._ai_service = ai_service
        self._intent_resolver = intent_resolver
        self._action_builder = action_builder
        self._action_engine = action_engine

    def handle(
        self,
        command: str,
        args: list[str],
    ) -> Response | None:
        """
        Handle parsed user input.
        """

        intent = self._intent_resolver.resolve(
            command,
        )
        action = self._action_builder.build(
            intent,
            args,
        )

        if action is not None:
            return self._action_engine.execute(
                action,
            )

        try:
            return self._command_module.execute(
                intent.name,
                args,
            )

        except CommandNotFoundError:
            response = self._skill_module.execute(
                intent.name,
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