"""
Start Menu application discovery.
"""

from __future__ import annotations

from pathlib import Path

from jarvis.applications.application import Application
from jarvis.applications.method import LaunchMethod
from jarvis.applications.shortcut import ShortcutResolver
from jarvis.applications.discovery.base import ApplicationDiscoverySource


class StartMenuScanner(ApplicationDiscoverySource):
    """
    Discovers applications from the Windows Start Menu.
    """

    def discover(
        self,
    ) -> list[Application]:
        """
        Discover Start Menu applications.
        """

        resolver = ShortcutResolver()

        applications: list[Application] = []

        locations = [
            Path(
                r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
            ),
            Path.home()
            / r"AppData\Roaming\Microsoft\Windows\Start Menu\Programs",
        ]

        for location in locations:

            if not location.exists():
                continue

            for shortcut in location.rglob("*.lnk"):

                target = resolver.resolve(
                    shortcut,
                )

                if target is None:
                    continue

                applications.append(
                    Application(
                        name=shortcut.stem.lower(),
                        target=str(target),
                        launch_method=LaunchMethod.EXECUTABLE,
                        source="start_menu",
                    )
                )

        return applications