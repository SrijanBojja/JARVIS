from datetime import datetime, timedelta

from jarvis.confirmation.pending import PendingAction


def hello():
    print("Hello")


action = PendingAction(
    action_id="demo",
    title="Demo",
    message="Testing pending action.",
    callback=hello,
    created_at=datetime.now(),
    expires_at=datetime.now() + timedelta(minutes=1),
)

print(action)