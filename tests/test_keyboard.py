from __future__ import annotations

import time

from jarvis.services.desktop import KeyboardController


def main() -> None:

    keyboard = KeyboardController()

    print("Click into Notepad within 5 seconds...")
    time.sleep(5)

    keyboard.type(
        "Hello from JARVIS!",
    )

    keyboard.press(
        "enter",
    )

    keyboard.type(
        "Keyboard controller works.",
    )


if __name__ == "__main__":
    main()