"""
Window service exceptions.
"""


class WindowError(Exception):
    """
    Base window exception.
    """


class WindowNotFoundError(WindowError):
    """
    Raised when a window cannot be located.
    """


class WindowOperationError(WindowError):
    """
    Raised when a window operation fails.
    """