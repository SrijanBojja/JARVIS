"""
Custom exceptions for the Service Container.
"""


class ContainerError(Exception):
    """Base exception for all container-related errors."""


class ServiceAlreadyRegisteredError(ContainerError):
    """Raised when attempting to register an existing service."""


class ServiceNotFoundError(ContainerError):
    """Raised when a requested service is not registered."""