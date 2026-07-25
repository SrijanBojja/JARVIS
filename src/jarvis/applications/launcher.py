"""
Application launcher.
"""

from __future__ import annotations

import os
import subprocess

from jarvis.applications.application import Application
from jarvis.applications.method import LaunchMethod


class ApplicationLauncher:
    """
    Launches applications.
    """

    def launch(
        self,
        application: Application,
    ) -> None:
        """
        Launch an application.
        """

        match application.launch_method:

            case LaunchMethod.EXECUTABLE:
                subprocess.Popen(
                    [application.target],
                )

            case LaunchMethod.URI:
                os.startfile(
                    application.target,
                )

            case _:
                raise NotImplementedError(
                    f"Unsupported launch method: "
                    f"{application.launch_method}"
                )