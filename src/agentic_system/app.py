"""Application entry point."""

from agentic_system import __version__


def greet(name: str = "world") -> str:
    return f"Hello, {name}! (agentic-system {__version__})"


def main() -> None:
    print(greet())


if __name__ == "__main__":
    main()
