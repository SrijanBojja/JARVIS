"""Handler utilities for the JARVIS logging system."""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def create_console_handler(
    formatter: logging.Formatter,
) -> logging.Handler:
    """Create the console log handler."""

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    return handler


def create_file_handler(
    log_file: Path,
    formatter: logging.Formatter,
) -> logging.Handler:
    """Create the rotating file log handler."""

    handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=1_000_000,
        backupCount=5,
        encoding="utf-8",
    )

    handler.setFormatter(formatter)

    return handler