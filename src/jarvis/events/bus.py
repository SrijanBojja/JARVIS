from collections.abc import Callable
from typing import Any

from ..logger import get_logger
from .event import Event


class EventBus:
    """
    Central event dispatcher for the JARVIS operating system.
    """

    def __init__(self) -> None:
        self._subscribers: dict[str, set[Callable[[Event], Any]]] = {}
        self._logger = get_logger(__name__)
    
    def subscribe(
        self,
        event_name: str,
        listener: Callable[[Event], Any],
    ) -> None:
        """
        Register a listener for an event.
        """

        self._subscribers.setdefault(event_name, set()).add(listener)
    
    def unsubscribe(
        self,
        event_name: str,
        listener: Callable[[Event], Any],
    ) -> None:
        """
        Remove a listener from an event.
        """

        listeners = self._subscribers.get(event_name)

        if listeners is None:
            return

        listeners.discard(listener)

        if not listeners:
            del self._subscribers[event_name]
    
    def publish(self, event: Event) -> None:
        """
        Publish an event to all registered listeners.
        """

        self._logger.debug("Publishing event: %s", event.name)

        listeners = self._subscribers.get(event.name)

        if listeners is None:
            return

        for listener in listeners:
            try:
                listener(event)

            except Exception:
                self._logger.exception(
                    "Listener '%s' failed while handling event '%s'",
                    getattr(listener, "__name__", repr(listener)),
                    event.name,
                )