from jarvis.system.controller import SystemController
from jarvis.system.power import PowerController
from jarvis.system.session import SessionController
from jarvis.system.desktop import DesktopController
from jarvis.system.monitor import SystemMonitor

system = SystemController(
    power=PowerController(),
    session=SessionController(),
    desktop=DesktopController(),
    monitor=SystemMonitor(),
)

print(system.monitor.snapshot())