from pathlib import Path

from jarvis.applications import ShortcutResolver


def main() -> None:

    resolver = ShortcutResolver()

    shortcut = Path(
        r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
    )

    target = resolver.resolve(
        shortcut,
    )

    print(target)


if __name__ == "__main__":
    main()