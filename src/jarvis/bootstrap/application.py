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
from jarvis.ai import (
    AIService,
    OllamaProvider,
)
from jarvis.ai.memory import ConversationMemory
from jarvis.voice import VoiceAssistant
from jarvis.intents import IntentResolver
from jarvis.actions import (
    ActionBuilder,
    ActionEngine,
)
from jarvis.actions.executors import (
    EchoActionExecutor,
    OpenApplicationExecutor,
)
from jarvis.applications import (
    ApplicationCache,
    ApplicationLauncher,
    ApplicationManager,
    ApplicationRegistry,
    ApplicationScanner,
)


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

        provider = OllamaProvider()
        memory = ConversationMemory()

        ai_service = AIService(
            provider,
            memory,
        )
        intent_resolver = IntentResolver()
        action_engine = ActionEngine()
        action_builder = ActionBuilder()
        application_registry = ApplicationRegistry()
        application_cache = ApplicationCache()
        application_scanner = ApplicationScanner()
        application_launcher = ApplicationLauncher()

        application_manager = ApplicationManager(
            application_registry,
            application_cache,
            application_scanner,
        )
        application_manager.initialize()

        action_engine.register(
            EchoActionExecutor(),
        )
        action_engine.register(
            OpenApplicationExecutor(
                application_registry,
                application_launcher,
            ),
        )


        conversation_manager = ConversationManager(
            command_module,
            skill_module,
            ai_service,
            intent_resolver,
            action_builder,
            action_engine,
        )

        voice_assistant = VoiceAssistant(
            conversation_manager,
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

        self._container.register(
            AIService,
            ai_service,
        )

        self._container.register(
            IntentResolver,
            intent_resolver,
        )

        self._container.register(
            ActionEngine,
            action_engine,
        )

        self._container.register(
            ActionBuilder,
            action_builder,
        )

        self._container.register(
            ApplicationRegistry,
            application_registry,
        )

        self._container.register(
            ApplicationCache,
            application_cache,
        )

        self._container.register(
            ApplicationManager,
            application_manager,
        )

        self._container.register(
            ApplicationScanner,
            application_scanner,
        )

        self._container.register(
            ApplicationLauncher,
            application_launcher,
        )

        self._container.register(
            ConversationMemory,
            memory,
        )

        self._container.register(
            VoiceAssistant,
            voice_assistant,
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