from pathlib import Path

from jarvis.services.clipboard.windows import WindowsClipboardService
from jarvis.services.perception.windows import WindowsPerceptionService


def main() -> None:
    print("=" * 60)
    print("JARVIS PERCEPTION TEST")
    print("=" * 60)

    clipboard = WindowsClipboardService()
    perception = WindowsPerceptionService(clipboard)

    state = perception.capture_state()

    print(f"Timestamp          : {state.timestamp}")
    print(f"Active Window      : {state.active_window}")
    print(f"Clipboard          : {state.clipboard!r}")
    print(f"Running Processes  : {state.running_processes}")
    print(f"Screenshot         : {state.screenshot}")

    print("\nVisible Windows")
    print("-" * 60)

    for i, window in enumerate(state.windows, start=1):
        print(f"{i:02}. {window}")

    print("\nScreenshot exists:", Path(state.screenshot).exists())


if __name__ == "__main__":
    main()