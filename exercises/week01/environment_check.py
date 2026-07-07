from __future__ import annotations

import platform
import sys


def main() -> None:
    print("AI Engineering Roadmap - Environment Check")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Executable: {sys.executable}")
    print(f"Platform: {platform.platform()}")

    major, minor = sys.version_info[:2]
    if (major, minor) >= (3, 10):
        print("Status: OK - Python 3.10+ is available.")
    else:
        print("Status: Please install Python 3.10 or newer.")


if __name__ == "__main__":
    main()

