def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def divide(a: int, b: int) -> int:
    """Divide two numbers using floor division.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The floor division result of a divided by b.

    Raises:
        ValueError: If b is 0.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a // b
