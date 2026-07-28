"""
Presentation service.
"""

from __future__ import annotations

from jarvis.presentation.presenter import Presenter
from jarvis.responses import Response


class PresentationPipeline:
    """
    Delivers responses through registered presenters.
    """

    def __init__(self) -> None:
        """
        Initialize the presentation service.
        """

        self._presenters: list[Presenter] = []

    def register(
        self,
        presenter: Presenter,
    ) -> None:
        """
        Register a presenter.
        """

        self._presenters.append(
            presenter,
        )

    def present(
        self,
        response: Response,
    ) -> None:
        """
        Present a response using all registered presenters.
        """

        for presenter in self._presenters:
            presenter.present(
                response,
            )