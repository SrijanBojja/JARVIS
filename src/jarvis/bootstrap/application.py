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
from jarvis.conversation import (
    ConversationManager,
    ConversationSession,
)
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
    ApplicationAliasGenerator,
    ApplicationCache,
    ApplicationLauncher,
    ApplicationManager,
)
from jarvis.applications.search import (
    ApplicationSearchEngine,
)
from jarvis.applications.search.matchers import (
    ExactMatchMatcher,
)
from jarvis.applications.discovery import (
    ApplicationDiscoveryService,
    StartMenuScanner,
    PathScanner,
)
from jarvis.applications.store import (
    ApplicationStore,
)

from jarvis.applications.store.indexes import (
    NameIndex,
    AliasIndex,
    SourceIndex,
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
        conversation_session = ConversationSession()

        ai_service = AIService(
            provider,
            memory,
        )
        intent_resolver = IntentResolver()
        action_engine = ActionEngine()
        action_builder = ActionBuilder()
        application_alias_generator = ApplicationAliasGenerator()

        name_index = NameIndex()

        alias_index = AliasIndex(
            application_alias_generator,
        )

        source_index = SourceIndex()

        application_store = ApplicationStore(
            name_index,
            alias_index,
            source_index,
        )

        application_cache = ApplicationCache()

        start_menu_scanner = StartMenuScanner()
        path_scanner = PathScanner()

        application_discovery = ApplicationDiscoveryService()

        application_discovery.register(
            start_menu_scanner,
        )

        application_discovery.register(
            path_scanner,
        )

        application_launcher = ApplicationLauncher()
        application_search_engine = (
            ApplicationSearchEngine()
        )

        exact_match_matcher = ExactMatchMatcher(
            application_alias_generator,
        )

        application_search_engine.register(
            exact_match_matcher,
        )

        application_manager = ApplicationManager(
            application_store,
            application_cache,
            application_discovery,
        )
        application_manager.initialize()

        action_engine.register(
            EchoActionExecutor(),
        )
        action_engine.register(
            OpenApplicationExecutor(
                application_search_engine,
                application_store,
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
            conversation_session,
            application_launcher,
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
            ConversationSession,
            conversation_session,
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
            ApplicationStore,
            application_store,
        )

        self._container.register(
            NameIndex,
            name_index,
        )

        self._container.register(
            AliasIndex,
            alias_index,
        )

        self._container.register(
            SourceIndex,
            source_index,
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
            StartMenuScanner,
            start_menu_scanner,
        )

        self._container.register(
            PathScanner,
            path_scanner,
        )

        self._container.register(
            ApplicationDiscoveryService,
            application_discovery,
        )

        self._container.register(
            ApplicationAliasGenerator,
            application_alias_generator,
        )

        self._container.register(
            ApplicationLauncher,
            application_launcher,
        )

        self._container.register(
            ApplicationSearchEngine,
            application_search_engine,
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