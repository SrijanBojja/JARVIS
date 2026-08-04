from jarvis.services.desktop import WindowController


def main():

    controller = WindowController()

    print(
        "Active:",
        controller.active_window(),
    )


if __name__ == "__main__":
    main()
    