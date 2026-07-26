from jarvis.actions.action import Action
from jarvis.actions.engine import ActionEngine
from jarvis.confirmation.manager import ConfirmationManager
from jarvis.actions.executors.echo import EchoActionExecutor

confirmation = ConfirmationManager()

engine = ActionEngine(
    confirmation=confirmation,
)

engine.register(
    EchoActionExecutor(),
)

action = Action(
    name="echo",
    target="Hello JARVIS!",
    requires_confirmation=True,
)

response = engine.execute(action)

print(response.text)
print(confirmation.has_pending())

response = engine.execute_pending()

print(response.text)
print(confirmation.has_pending())