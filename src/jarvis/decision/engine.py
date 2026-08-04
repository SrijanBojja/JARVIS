"""
Decision Engine.

Responsible for deciding which subsystem should handle a user request.
"""

from __future__ import annotations

from jarvis.ai import AIService
from jarvis.commands.exceptions import CommandNotFoundError
from jarvis.commands.module import CommandModule
from jarvis.conversation.resolver import ReferenceResolver
from jarvis.conversation.session import ConversationSession
from jarvis.intents import IntentResolver
from jarvis.intents import Intent
from jarvis.responses import (
    Response,
    ResponseStatus,
)
from jarvis.skills.module import SkillModule
from jarvis.workflows import (
    WorkflowBuilder,
    WorkflowRunner,
)
from jarvis.vision import VisionService
from jarvis.planner import Planner
from jarvis.actions.engine import ActionEngine


class DecisionEngine:

    def __init__(
        self,
        command_module: CommandModule,
        skill_module: SkillModule,
        ai_service: AIService,
        intent_resolver: IntentResolver,
        workflow_builder: WorkflowBuilder,
        workflow_runner: WorkflowRunner,
        conversation_session: ConversationSession,
        reference_resolver: ReferenceResolver,
        vision_service: VisionService,
        planner: Planner,
        action_engine: ActionEngine,
    ) -> None:

        self._command_module = command_module
        self._skill_module = skill_module
        self._ai_service = ai_service
        self._intent_resolver = intent_resolver
        self._workflow_builder = workflow_builder
        self._workflow_runner = workflow_runner
        self._conversation_session = conversation_session
        self._reference_resolver = reference_resolver
        self._vision_service = vision_service
        self._planner = planner
        self._action_engine = action_engine

    def handle(
        self,
        command: str,
        args: list[str],
    ) -> Response | None:

        message = " ".join(
            [command, *args],
        ).lower().strip()

        VISION_COMMANDS = {
            "what is on my screen",
            "describe my screen",
            "describe screen",
            "look at my screen",
            "what do you see",
        }

        if message in VISION_COMMANDS:

            description = self._vision_service.describe_screen()

            return Response(
                text=description,
                status=ResponseStatus.SUCCESS,
            )

        intent, resolved_args = self._resolve_request(
            command,
            args,
        )

        plan = self._planner.build(message)

        if plan.actions:

            response = None

            for action in plan.actions:
                response = self._action_engine.execute(
                    action,
                )

            if response is not None:
                return response
        
        response = self._execute_workflow(
            intent,
            resolved_args,
        )

        if response is not None:
            return response

        response = self._execute_command(
            intent.name,
            resolved_args,
        )

        if response is not None:
            return response

        response = self._execute_skill(
            intent.name,
            resolved_args,
        )

        if response is not None:
            return response

        return self._chat_with_ai(
            command,
            args,
        )


    def _resolve_request(
        self,
        command: str,
        args: list[str],
    ) -> tuple[Intent, list[str]]:

        resolved_args = self._reference_resolver.resolve(
            command,
            args,
        )

        intent = self._intent_resolver.resolve(
            command,
            resolved_args,
        )

        return intent, resolved_args

    def _execute_workflow(
        self,
        intent: Intent,
        args: list[str],
    ) -> Response | None:

        workflow = self._workflow_builder.build(
            intent,
            args,
        )

        if workflow is None:
            return None

        result = self._workflow_runner.execute(
            workflow,
        )

        for action, response in zip(
            result.executed_actions,
            result.responses,
        ):
            self._conversation_session.update_from_action(
                action,
                response,
            )

        if not result.responses:
            return None

        response = result.responses[-1]

        if response.status == ResponseStatus.AMBIGUOUS:
            self._conversation_session.pending_applications = (
                response.data
            )
        else:
            self._conversation_session.clear()

        return response

    def _execute_command(
        self,
        intent_name: str,
        args: list[str],
    ) -> Response | None:

        try:
            return self._command_module.execute(
                intent_name,
                args,
            )

        except CommandNotFoundError:
            return None

    def _execute_skill(
        self,
        intent_name: str,
        args: list[str],
    ) -> Response | None:

        return self._skill_module.execute(
            intent_name,
            args,
        )

    def _chat_with_ai(
        self,
        command: str,
        args: list[str],
    ) -> Response:

        return self._ai_service.chat(
            " ".join(
                [command, *args],
            ).strip(),
        )