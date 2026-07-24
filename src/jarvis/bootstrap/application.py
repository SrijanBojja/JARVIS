"""
Application bootstrapper.
"""

from jarvis.bootstrap import initialize_filesystem
from jarvis.container import ServiceContainer
from jarvis.logger import initialize_logging
from jarvis.kernel import Kernel

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

        self._container.register(
            Kernel,
            Kernel(),
        )

        kernel = self._container.resolve(Kernel)

        kernel.start()