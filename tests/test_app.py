from agentic_system.app import greet


def test_greet_default() -> None:
    assert greet() == "Hello, world! (agentic-system 0.1.0)"


def test_greet_name() -> None:
    assert greet("Suresh") == "Hello, Suresh! (agentic-system 0.1.0)"
