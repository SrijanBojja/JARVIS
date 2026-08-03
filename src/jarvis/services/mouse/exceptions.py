"""
Mouse service exceptions.
"""


class MouseServiceError(Exception):
    """
    Base mouse exception.
    """


class MouseMoveError(MouseServiceError):
    pass


class MouseClickError(MouseServiceError):
    pass