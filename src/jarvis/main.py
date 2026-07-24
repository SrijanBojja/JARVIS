"""
JARVIS OS
Main Entry Point

Author: Bojja Srijan
Version: 0.0.1
"""

from jarvis.kernel import Kernel
from jarvis.bootstrap import initialize_filesystem
from jarvis.logger import initialize_logging

def main():
    initialize_filesystem()
    initialize_logging()
    print("=" * 50)
    print("JARVIS OS")
    print("=" * 50)

    kernel = Kernel()
    kernel.start()

    print()
    print("JARVIS is ready.")


if __name__ == "__main__":
    main()