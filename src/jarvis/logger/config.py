"""Logging configuration for the JARVIS application."""

from __future__ import annotations
_LOGGING_INITIALIZED = False
import logging
from pathlib import Path

from .formatter import create_formatter
from .handlers import (
    create_console_handler,
    create_file_handler,
)


def initialize_logging() -> None:
    """Configure the logging system for the JARVIS application."""
    global _LOGGING_INITIALIZED
    if _LOGGING_INITIALIZED:
        return

    
    log_directory = Path("logs")
    log_directory.mkdir(exist_ok=True)

    log_file = log_directory / "jarvis.log"

    formatter = create_formatter()

    console_handler = create_console_handler(formatter)

    file_handler = create_file_handler(
        log_file,
        formatter,
    )
    

    root_logger = logging.getLogger()

    root_logger.setLevel(logging.INFO)

    root_logger.handlers.clear()

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)
    
    _LOGGING_INITIALIZED = True