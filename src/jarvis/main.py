"""
JARVIS OS
Main Entry Point

Author: Bojja Srijan
Version: 0.0.1
"""

from jarvis.bootstrap.application import ApplicationBootstrap


def main() -> None:
    bootstrap = ApplicationBootstrap()

    print("=" * 50)
    print("JARVIS OS")
    print("=" * 50)

    bootstrap.initialize()

    print()
    print("JARVIS is ready.")


if __name__ == "__main__":
    main()