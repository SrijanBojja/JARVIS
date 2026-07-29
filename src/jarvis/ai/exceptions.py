"""
AI exceptions for JARVIS.
"""


class AIError(Exception):
    """
    Base exception for all AI-related errors.
    """


class AIRuntimeError(AIError):
    """
    Raised when an AI runtime fails.
    """


class AIProviderError(AIError):
    """
    Raised when an AI provider fails.
    """