from pprint import pprint

from jarvis.system.monitor import SystemMonitor

monitor = SystemMonitor()

pprint(monitor.snapshot())
