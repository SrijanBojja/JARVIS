"""
Terminal presenter.
"""

from __future__ import annotations

from jarvis.presentation.presenter import Presenter
from jarvis.responses import Response


class TerminalPresenter(Presenter):
    """
    Presents responses in the terminal.
    """

    def present(
        self,
        response: Response,
    ) -> None:
        """
        Present a response in the terminal.
        """

        print(
            response.text,
        )