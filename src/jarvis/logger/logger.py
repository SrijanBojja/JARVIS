"""Logger access utilities for the JARVIS application."""

from __future__ import annotations

import logging


def get_logger(name: str) -> logging.Logger:
    """Return a logger for the specified module."""

    return logging.getLogger(name)