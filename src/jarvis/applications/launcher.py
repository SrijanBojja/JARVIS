"""
Application launcher.
"""

from __future__ import annotations


from jarvis.applications.application import Application
from jarvis.applications.method import LaunchMethod
from jarvis.services.process import ProcessService

class ApplicationLauncher:
    """
    Launches applications.
    """
    def __init__(
        self,
        process_service: ProcessService,
    ) -> None:
        self._process_service = process_service

    def launch(
        self,
        application: Application,
    ) -> bool:
        """
        Launch an application.

        Returns True if the application was launched.
        Returns False if it is already running.
        """

        if self.is_running(application):
            return False

        match application.launch_method:

            case LaunchMethod.EXECUTABLE:
                self._process_service.launch(
                    application.target,
                )

            case LaunchMethod.URI:
                self._process_service.launch(
                    application.target,
                )

            case _:
                raise NotImplementedError(
                    f"Unsupported launch method: "
                    f"{application.launch_method}"
                )

        return True
    def close(
        self,
        application: Application,
    ) -> None:
        """
        Close an application.
        """

        self._process_service.terminate(
            application.target,
        )

    def is_running(
        self,
        application: Application,
    ) -> bool:
        """
        Check whether an application is running.
        """

        return self._process_service.is_running(
            application.target,
        )