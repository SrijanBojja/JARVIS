"""
Filesystem bootstrap utilities.
"""

from jarvis.config import settings


def initialize_filesystem() -> None:
    """
    Create the required project directories if they do not already exist.
    """

    settings.data_dir.mkdir(parents=True, exist_ok=True)
    settings.logs_dir.mkdir(parents=True, exist_ok=True)