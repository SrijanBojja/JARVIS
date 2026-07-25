"""
Application alias generator.
"""

from pathlib import Path

from jarvis.applications.application import Application
from jarvis.applications.method import LaunchMethod


class ApplicationAliasGenerator:
    """
    Generates aliases for applications.
    """

    def generate(
        self,
        application: Application,
    ) -> set[str]:
        """
        Generate aliases for an application.
        """

        aliases: set[str] = set()

        aliases.add(
            application.name.lower(),
        )

        aliases.update(
            application.aliases,
        )

        words = application.name.lower().split()

        aliases.update(
            words,
        )

        if (
            application.launch_method
            is LaunchMethod.EXECUTABLE
        ):
            executable = Path(
                application.target,
            ).stem.lower()

            aliases.add(
                executable,
            )

        return aliases