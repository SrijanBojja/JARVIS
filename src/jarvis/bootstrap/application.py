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

        kernel = Kernel()

        command_module = CommandModule(
            kernel,
            history
        )
        shell = Shell(
            command_module,
            history
        )

        self._container.register(
            CommandModule,
            command_module,
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

        self._container.resolve(Kernel).start()
        self._container.resolve(Shell).run()