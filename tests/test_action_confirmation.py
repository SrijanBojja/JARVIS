from jarvis.confirmation.manager import ConfirmationManager

manager = ConfirmationManager()

manager.request(
    title="Shutdown",
    message="Confirm shutdown",
    payload="shutdown_action",
)

result = manager.confirm()

print(result)
print(manager.has_pending())