"""
Application launch methods.
"""

from enum import Enum


class LaunchMethod(str, Enum):
    """
    Supported application launch methods.
    """

    EXECUTABLE = "executable"
    URI = "uri"
    APPX = "appx"
    SHELL = "shell"
    URL = "url"