"""
Application scanner.
"""

from __future__ import annotations

from pathlib import Path

from jarvis.applications.application import Application
from jarvis.applications.shortcut import ShortcutResolver

class ApplicationScanner:
    """
    Discovers installed applications.
    """
    
    def scan(
        self,
    ) -> list[Application]:
        """
        Scan Windows Start Menu shortcuts.
        """
        resolver = ShortcutResolver()
        applications: list[Application] = []

        locations = [
            Path(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs"),
            Path.home() /
            r"AppData\Roaming\Microsoft\Windows\Start Menu\Programs",
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
                        executable=str(target),
                        source="start_menu",
                    )
                )

        return applications