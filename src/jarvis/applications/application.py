"""
Application model.
"""

from dataclasses import dataclass, field

from jarvis.applications.method import LaunchMethod


@dataclass(slots=True)
class Application:
    """
    Represents a launchable application.
    """

    name: str

    target: str

    launch_method: LaunchMethod = (
        LaunchMethod.EXECUTABLE
    )

    source: str = ""

    aliases: list[str] = field(
        default_factory=list,
    )