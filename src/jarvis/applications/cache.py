"""
Application cache.
"""

from __future__ import annotations

import json

from jarvis.applications.application import Application
from jarvis.config import settings


class ApplicationCache:
    """
    Stores discovered applications.
    """

    @property
    def _path(self):
        return settings.data_dir / "applications.json"

    def load(
        self,
    ) -> list[Application]:
        """
        Load cached applications.
        """

        with self._path.open(
            "r",
            encoding="utf-8",
        ) as file:

            data = json.load(
                file,
            )

        return [
            Application(
                name=item["name"],
                executable=item["executable"],
            )
            for item in data["applications"]
        ]

    def save(
        self,
        applications: list[Application],
    ) -> None:
        """
        Save applications.
        """

        data = {
            "applications": [
                {
                    "name": application.name,
                    "executable": application.executable,
                }
                for application in applications
            ]
        }

        with self._path.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
            )