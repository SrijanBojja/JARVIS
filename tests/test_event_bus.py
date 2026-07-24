from jarvis.events import EventBus, Event


def listener(event: Event) -> None:
    print(f"Received: {event.name}")


bus = EventBus()

bus.subscribe("APPLICATION_STARTED", listener)
bus.unsubscribe("APPLICATION_STARTED", listener)

event = Event(name="APPLICATION_STARTED")

bus.publish(event)

print("Test completed.")