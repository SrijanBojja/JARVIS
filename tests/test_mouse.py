from __future__ import annotations

import time

from jarvis.services.desktop import MouseController


def main() -> None:

    mouse = MouseController()

    print("Current position:", mouse.position())

    print("Move in 3 seconds...")
    time.sleep(3)

    x, y = mouse.position()

    mouse.move_to(
        x + 200,
        y,
    )

    print("Mouse moved.")


if __name__ == "__main__":
    main()