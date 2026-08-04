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
from jarvis.voice.module import VoiceModule
from jarvis.conversation import (
    ApplicationReferences,
    ReferenceResolver,
    ConversationManager,
    ConversationSession,
)
from jarvis.ai import (
    AIService,
    OllamaProvider,
)
from jarvis.ai.memory import ConversationMemory
from jarvis.voice.assistant import VoiceAssistant
from jarvis.voice.microphone import Microphone
from jarvis.voice.recognizer import SpeechRecognizer
from jarvis.voice.wakeword import WakeWordDetector
from jarvis.voice.session import VoiceSession
from jarvis.intents import IntentResolver
from jarvis.actions import (
    ActionBuilder,
    ActionEngine,
)
from jarvis.workflows import (
    WorkflowBuilder,
    WorkflowManager,
    WorkflowRunner,
)
from jarvis.decision import (
    DecisionEngine,
)
from jarvis.actions.executors import (
    EchoActionExecutor,
    OpenApplicationExecutor,
    CloseApplicationExecutor,
    WindowApplicationExecutor,
    CheckApplicationExecutor,
    SystemActionExecutor,
    TypeTextExecutor,
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
from jarvis.confirmation import ConfirmationManager
from jarvis.services.power.service import (
    PowerService,
)
from jarvis.services.power.windows import (
    WindowsPowerService,
)
from jarvis.services.process.service import (
    ProcessService,
)
from jarvis.services.process.windows import (
    WindowsProcessService,
)
from jarvis.services.clipboard import (
    ClipboardService,
    WindowsClipboardService,
)
from jarvis.services.perception import (
    PerceptionService,
    WindowsPerceptionService,
)
from jarvis.services.desktop import (
    MouseController,
    KeyboardController,
    WindowController,
)
from jarvis.actions.executors import (
    ClipboardActionExecutor,
)
from jarvis.services.filesystem import (
    FileSystemService,
    WindowsFileSystemService,
)
from jarvis.actions.executors import (
    FileSystemActionExecutor,
)
from jarvis.services.notification import (
    NotificationService,
    WindowsNotificationService,
)
from jarvis.actions.executors import (
    NotificationActionExecutor,
)
from jarvis.services.window import (
    WindowService,
    WindowsWindowService,
)
from jarvis.presentation import (
    PresentationPipeline,
    TerminalPresenter,
    VoicePresenter,
)
from jarvis.tools import(ToolRegistry)
from jarvis.vision import VisionService
from jarvis.planner import Planner
from jarvis.interaction import (
    InteractionMode,
    HybridInteraction,
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
        print()
        print("=" * 50)
        print("Select Interaction Mode")
        print("=" * 50)
        print("1. Shell")
        print("2. Voice")
        print("3. Hybrid")
        print()

        choice = input("Choice > ").strip()

        match choice:

            case "2":
                interaction_mode = InteractionMode.VOICE

            case "3":
                interaction_mode = InteractionMode.HYBRID

            case _:
                interaction_mode = InteractionMode.SHELL
        voice_module = VoiceModule()
        voice_pipeline = PresentationPipeline()

        microphone = None
        recognizer = None
        wake_word = None
        voice_session = None

        if interaction_mode in {
            InteractionMode.VOICE,
            InteractionMode.HYBRID,
        }:

            microphone = Microphone()
            recognizer = SpeechRecognizer()
            wake_word = WakeWordDetector()
            voice_session = VoiceSession()
            

        
        shell_pipeline = PresentationPipeline()
        shell_pipeline.register(
            TerminalPresenter(),
        )
        shell_pipeline.register(
            VoicePresenter(
                voice_module,
            ),
        )

        voice_pipeline.register(
            TerminalPresenter(),
        )

        voice_pipeline.register(
            VoicePresenter(
                voice_module,
            ),
        )
        kernel = Kernel()

        command_module = CommandModule(
            kernel,
            history,
        )


        provider = OllamaProvider()
        memory = ConversationMemory()
        conversation_session = ConversationSession()
        application_references = (
            ApplicationReferences(
                conversation_session,
            )
        )
        reference_resolver = ReferenceResolver(
            application_references,
            conversation_session,
        )

        tool_registry = ToolRegistry()
        ai_service = AIService(
            provider,
            memory,
            tool_registry,
        )
        power_service = WindowsPowerService()
        process_service = WindowsProcessService()
        window_service = WindowsWindowService()
        clipboard_service = WindowsClipboardService()
        perception_service = WindowsPerceptionService(
            clipboard_service,
        )
        vision_service = VisionService(
            perception_service,
        )
        mouse_controller = MouseController()
        keyboard_controller = KeyboardController()
        window_controller = WindowController()
        filesystem_service = WindowsFileSystemService()
        skill_module = SkillModule(
            filesystem_service,
        )
        notification_service = WindowsNotificationService()
        confirmation_manager = ConfirmationManager()

        intent_resolver = IntentResolver()

        action_engine = ActionEngine(
            confirmation=confirmation_manager,
        )

        action_builder = ActionBuilder()

        workflow_manager = WorkflowManager()

        workflow_builder = WorkflowBuilder(
            action_builder,
        )

        workflow_runner = WorkflowRunner(
            workflow_manager,
            action_engine,
        )
    
        planner = Planner()

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

        application_launcher = ApplicationLauncher(
            process_service,
            window_service,
        )
        type_text_executor = TypeTextExecutor(
            keyboard_controller,
        )
        decision_engine = DecisionEngine(
            command_module=command_module,
            skill_module=skill_module,
            ai_service=ai_service,
            intent_resolver=intent_resolver,
            workflow_builder=workflow_builder,
            workflow_runner=workflow_runner,
            conversation_session=conversation_session,
            reference_resolver=reference_resolver,
            vision_service=vision_service,
            planner=planner,
            action_engine=action_engine,
        )
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
        action_engine.register(
            type_text_executor,
        )
        action_engine.register(
            CloseApplicationExecutor(
                application_search_engine,
                application_store,
                application_launcher,
            ),
        )
        action_engine.register(
            CheckApplicationExecutor(
                application_search_engine,
                application_store,
                application_launcher,
            ),
        )
        action_engine.register(
            WindowApplicationExecutor(
                application_search_engine,
                application_store,
                application_launcher,
            ),
        )

        action_engine.register(
            SystemActionExecutor(
                power_service,
            ),
        )
        action_engine.register(
            ClipboardActionExecutor(
                clipboard_service,
            ),
        )
        action_engine.register(
            FileSystemActionExecutor(
                filesystem_service,
            ),
        )
        action_engine.register(
            NotificationActionExecutor(
                notification_service,
            ),
        )

        conversation_manager = ConversationManager(
            conversation_session=conversation_session,
            application_launcher=application_launcher,
            workflow_runner=workflow_runner,
            decision_engine=decision_engine,
        )

        voice_assistant = None

        if interaction_mode in {
            InteractionMode.VOICE,
            InteractionMode.HYBRID,
        }:

            voice_assistant = VoiceAssistant(
                conversation_manager,
                microphone,
                recognizer,
                wake_word,
                voice_session,
                voice_pipeline,
            )

        shell = Shell(
            conversation_manager,
            history,
            shell_pipeline,
        )

        hybrid = None

        if (
            interaction_mode
            == InteractionMode.HYBRID
        ):

            from jarvis.interaction import HybridInteraction

            hybrid = HybridInteraction(
                shell,
                voice_assistant,
            )

            self._container.register(
                HybridInteraction,
                hybrid,
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
            ApplicationReferences,
            application_references,
        )

        self._container.register(
            ReferenceResolver,
            reference_resolver,
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
            ConfirmationManager,
            confirmation_manager,
        )

        self._container.register(
            ActionBuilder,
            action_builder,
        )

        self._container.register(
            WorkflowManager,
            workflow_manager,
        )

        self._container.register(
            WorkflowBuilder,
            workflow_builder,
        )

        self._container.register(
            WorkflowRunner,
            workflow_runner,
        )

        self._container.register(
            DecisionEngine,
            decision_engine,
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

        if voice_assistant is not None:

            self._container.register(
                VoiceAssistant,
                voice_assistant,
            )
        
        self._container.register(
            PresentationPipeline,
            shell_pipeline,
        )

        self._container.register(
            PowerService,
            power_service,
        )
        self._container.register(
            ProcessService,
            process_service,
        )
        self._container.register(
            WindowService,
            window_service,
        )
        self._container.register(
            ClipboardService,
            clipboard_service,
        )
        self._container.register(
            PerceptionService,
            perception_service,
        )

        self._container.register(
            VisionService,
            vision_service,
        )
        self._container.register(
            MouseController,
            mouse_controller,
        )
        self._container.register(
            KeyboardController,
            keyboard_controller,
        )
        self._container.register(
            WindowController,
            window_controller,
        )

        self._container.register(
            Planner,
            planner,
        )

        self._container.register(
            FileSystemService,
            filesystem_service,
        )
        self._container.register(
            NotificationService,
            notification_service,
        )
        self._container.register(
            ToolRegistry,
            tool_registry,
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

        match interaction_mode:

            case InteractionMode.SHELL:

                self._container.resolve(
                    Shell,
                ).run()

            case InteractionMode.VOICE:

                voice_assistant.run()

            case InteractionMode.HYBRID:

                self._container.resolve(
                    HybridInteraction,
                ).run()