"""
Conversation manager.
"""

from __future__ import annotations

from jarvis.ai import AIService
from jarvis.applications import ApplicationLauncher
from jarvis.commands.exceptions import CommandNotFoundError
from jarvis.commands.module import CommandModule
from jarvis.actions import (
    ActionBuilder,
    ActionEngine,
)
from jarvis.intents import IntentResolver
from jarvis.responses import (
    Response,
    ResponseStatus,
)
from jarvis.skills.module import SkillModule
from .session import ConversationSession


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
        conversation_session: ConversationSession,
        application_launcher: ApplicationLauncher,
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
        self._conversation_session = conversation_session
        self._application_launcher = application_launcher

    def handle(
        self,
        command: str,
        args: list[str],
    ) -> Response | None:
        """
        Handle parsed user input.
        """

        message = " ".join(
            [command, *args],
        ).strip().lower()

        if self._action_engine.confirmation.has_pending():

            if message in {
                "yes",
                "y",
                "confirm",
                "ok",
                "okay",
            }:
                return self._action_engine.execute_pending()

            if message in {
                "no",
                "n",
                "cancel",
                "exit",
            }:
                self._action_engine.confirmation.cancel()

                return Response(
                    text="Cancelled.",
                    status=ResponseStatus.SUCCESS,
                )

        if (
            self._conversation_session.waiting_for_application
        ):
            matches = (
                self._conversation_session.pending_applications
            )

            if matches is None:
                self._conversation_session.clear()

            elif message in {
                "cancel",
                "exit",
            }:
                self._conversation_session.clear()

                return Response(
                    text="Cancelled.",
                )

            elif message.isdigit():

                index = int(message) - 1

                if 0 <= index < len(matches):

                    application = (
                        matches[index].application
                    )

                    self._conversation_session.clear()

                    self._application_launcher.launch(
                        application,
                    )

                    return Response(
                        text=f"Opening {application.name}...",
                        status=ResponseStatus.SUCCESS,
                    )

                return Response(
                    text="Invalid selection.",
                )

            else:

                for result in matches:

                    application = result.application

                    if (
                        message
                        == application.name.lower()
                    ):
                        self._conversation_session.clear()

                        self._application_launcher.launch(
                            application,
                        )

                        return Response(
                            text=f"Opening {application.name}...",
                            status=ResponseStatus.SUCCESS,
                        )

                return Response(
                    text=(
                        "Please choose one of the listed "
                        "applications or type 'cancel'."
                    ),
                )

        #
        # Resolve simple conversational references.
        #

        if args:

            resolved_args = args.copy()

            if resolved_args[-1].lower() == "it":

                if command == "close":
                    if (
                        self._conversation_session.last_application
                        is not None
                    ):
                        resolved_args[-1] = (
                            self._conversation_session.last_application
                        )

                elif (
                    command == "delete"
                    and len(resolved_args) >= 2
                ):
                    kind = resolved_args[0].lower()

                    if (
                        kind == "file"
                        and self._conversation_session.last_file
                    ):
                        resolved_args[-1] = (
                            self._conversation_session.last_file
                        )

                    elif (
                        kind == "directory"
                        and self._conversation_session.last_directory
                    ):
                        resolved_args[-1] = (
                            self._conversation_session.last_directory
                        )

                elif command == "open":
                    if (
                        self._conversation_session.last_directory
                    ):
                        resolved_args[-1] = (
                            self._conversation_session.last_directory
                        )

            args = resolved_args

        intent = self._intent_resolver.resolve(
            command,
            args,
        )

        action = self._action_builder.build(
            intent,
            args,
        )

        if action is not None:

            response = self._action_engine.execute(
                action,
            )

            if (
                response.status
                == ResponseStatus.AMBIGUOUS
            ):
                self._conversation_session.pending_applications = (
                    response.data
                )
            else:
                self._conversation_session.clear()

                self._conversation_session.remember(
                    action,
                    response,
                )
            return response

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

        return self._ai_service.chat(
            " ".join(
                [command, *args],
            ).strip(),
        )

        print(f"DEBUG: command={command!r}")
        print(f"DEBUG: args={args!r}")
        print(f"DEBUG: message={message!r}")