"""
Application launcher.
"""

from __future__ import annotations


from jarvis.applications.application import Application
from jarvis.applications.method import LaunchMethod
from jarvis.services.process import ProcessService
from jarvis.services.window import WindowService

class ApplicationLauncher:
    """
    Launches applications.
    """
    def __init__(
        self,
        process_service: ProcessService,
        window_service: WindowService,
    ) -> None:
        self._process_service = process_service
        self._window_service = window_service

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
    ) -> bool:
        """
        Close an application.
        """

        if not self.is_running(application):
            return False

        self._process_service.terminate(
            application.target,
        )

        return True

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

    def focus(
        self,
        application: Application,
    ) -> bool:
        """
        Focus an application's window.
        """

        if not self.is_running(application):
            return False

        self._window_service.focus(
            application.target,
        )

        return True


    def minimize(
        self,
        application: Application,
    ) -> bool:
        """
        Minimize an application's window.
        """

        if not self.is_running(application):
            return False

        self._window_service.minimize(
            application.target,
        )

        return True


    def maximize(
        self,
        application: Application,
    ) -> bool:
        """
        Maximize an application's window.
        """

        if not self.is_running(application):
            return False

        self._window_service.maximize(
            application.target,
        )

        return True


    def restore(
        self,
        application: Application,
    ) -> bool:
        """
        Restore an application's window.
        """

        if not self.is_running(application):
            return False

        self._window_service.restore(
            application.target,
        )

        return True