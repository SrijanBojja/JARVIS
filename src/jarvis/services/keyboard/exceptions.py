"""
Keyboard exceptions.
"""


class KeyboardServiceError(Exception):
    """
    Base keyboard exception.
    """


class KeyboardTypeError(KeyboardServiceError):
    pass


class KeyboardPressError(KeyboardServiceError):
    pass