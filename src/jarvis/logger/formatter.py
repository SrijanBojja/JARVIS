"""Formatter utilities for the JARVIS logging system."""

from __future__ import annotations

import logging


def create_formatter() -> logging.Formatter:
    """Create the standard formatter used by all log handlers."""

    return logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )