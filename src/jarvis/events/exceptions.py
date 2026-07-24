class EventBusError(Exception):
    """
    Base exception for all Event Bus errors.
    """


class SubscriptionError(EventBusError):
    """
    Raised when a subscription operation fails.
    """


class PublishError(EventBusError):
    """
    Raised when an event publication fails.
    """