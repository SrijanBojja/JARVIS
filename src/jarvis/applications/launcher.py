"""
Application launcher.
"""

from __future__ import annotations

import subprocess

from jarvis.applications.application import Application


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

        subprocess.Popen(
            [application.executable],
        )