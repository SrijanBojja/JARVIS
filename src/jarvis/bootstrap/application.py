"""
Application bootstrapper.
"""

from jarvis.bootstrap import initialize_filesystem
from jarvis.container import ServiceContainer
from jarvis.logger import initialize_logging
from jarvis.kernel import Kernel
from jarvis.commands.module import CommandModule
from jarvis.shell import Shell
from jarvis.utils import CommandHistory
from jarvis.skills import SkillModule
from jarvis.voice import VoiceModule
from jarvis.conversation import ConversationManager


class ApplicationBootstrap:
    """
    Coordinates application startup.
    """

    def __init__(self) -> None:
        """
        Initialize the application bootstrapper.
        """

        self._container = ServiceContainer()

    @property
    def container(self) -> ServiceContainer:
        """
        Return the application's service container.
        """

        return self._container

    def initialize(self) -> None:
        """
        Initialize the application.
        """

        initialize_filesystem()
        initialize_logging()

        history = CommandHistory()
        voice_module = VoiceModule()
        kernel = Kernel()

        command_module = CommandModule(
            kernel,
            history,
        )

        skill_module = SkillModule()

        conversation_manager = ConversationManager(
            command_module,
            skill_module,
        )

        shell = Shell(
            conversation_manager,
            history,
        )

        self._container.register(
            CommandModule,
            command_module,
        )

        self._container.register(
            SkillModule,
            skill_module,
        )

        self._container.register(
            ConversationManager,
            conversation_manager,
        )

        self._container.register(
            VoiceModule,
            voice_module,
        )

        self._container.register(
            Kernel,
            kernel,
        )

        self._container.register(
            CommandHistory,
            history,
        )

        self._container.register(
            Shell,
            shell,
        )

        kernel.modules.register(
            command_module,
        )

        kernel.modules.register(
            skill_module,
        )

        kernel.modules.register(
            voice_module,
        )

        self._container.resolve(Kernel).start()
        self._container.resolve(Shell).run()