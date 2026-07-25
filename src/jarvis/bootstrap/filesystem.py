"""
Filesystem bootstrap utilities.
"""

from jarvis.config import settings


def initialize_filesystem() -> None:
    """
    Create the required project directories if they do not already exist.
    """

    settings.data_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    settings.logs_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    applications_file = (
        settings.data_dir /
        "applications.json"
    )

    if not applications_file.exists():
        applications_file.write_text(
            '{\n    "applications": []\n}\n',
            encoding="utf-8",
        )