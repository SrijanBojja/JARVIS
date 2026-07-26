import time

from jarvis.confirmation.manager import (
    ConfirmationManager,
)
from jarvis.confirmation.exceptions import (
    ActionExpiredError,
)


def hello():
    print("Hello!")


manager = ConfirmationManager()

manager.request(
    title="Shutdown",
    message="Testing expiration.",
    callback=hello,
    timeout=2,
)

print(manager.has_pending())
print(manager.is_expired())

time.sleep(3)

print(manager.is_expired())

try:
    manager.confirm()
except ActionExpiredError as error:
    print(error)

print(manager.pending)