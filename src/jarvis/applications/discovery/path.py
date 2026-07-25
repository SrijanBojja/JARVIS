"""
PATH application discovery.
"""

from __future__ import annotations

import os
from pathlib import Path

from jarvis.applications.application import Application
from jarvis.applications.discovery.base import (
    ApplicationDiscoverySource,
)
from jarvis.applications.method import LaunchMethod


class PathScanner(ApplicationDiscoverySource):
    """
    Discovers executables available on the system PATH.
    """

    def discover(
        self,
    ) -> list[Application]:
        """
        Discover executables from PATH.
        """

        applications: list[Application] = []
        seen: set[str] = set()

        executable_extensions = {
            ".exe",
            ".cmd",
            ".bat",
            ".com",
        }

        for directory in os.environ.get(
            "PATH",
            "",
        ).split(
            os.pathsep,
        ):

            path = Path(
                directory,
            )

            if not path.is_dir():
                continue

            try:

                for file in path.iterdir():

                    if (
                        not file.is_file()
                        or file.suffix.lower()
                        not in executable_extensions
                    ):
                        continue

                    name = file.stem.lower()

                    if name in seen:
                        continue

                    seen.add(
                        name,
                    )

                    applications.append(
                        Application(
                            name=name,
                            target=str(file),
                            launch_method=LaunchMethod.EXECUTABLE,
                            source="path",
                        )
                    )

            except PermissionError:
                continue

        return applications