"""
Module manager for the JARVIS Operating System.
"""

from __future__ import annotations

from .module import Module


class ModuleManager:
    """
    Manages the lifecycle of all registered modules.
    """

    def __init__(self) -> None:
        self._modules: dict[type[Module], Module] = {}

    def register(
        self,
        module: Module,
    ) -> None:
        """
        Register a module.
        """

        self._modules[type(module)] = module
    
    def initialize_all(self) -> None:
        """
        Initialize all registered modules.
        """

        for module in self._modules.values():
            module.initialize()

    def start_all(self) -> None:
        """
        Start all registered modules.
        """

        for module in self._modules.values():
            module.start()

    def stop_all(self) -> None:
        """
        Stop all registered modules.
        """

        for module in self._modules.values():
            module.stop()