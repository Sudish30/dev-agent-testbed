def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def divide(a: int, b: int) -> int:
    """Divide two numbers using floor division."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a // b
