from typing import Union, Optional


def add(a: Union[int, float], b: Union[int, float], round_digits: Optional[int] = None) -> Union[int, float]:
    """Add two numbers, with optional rounding of the result.

    Args:
        a: The first number (int or float).
        b: The second number (int or float).
        round_digits: If provided, rounds the result to this many decimal places.
                      Must be a non-negative integer. Defaults to None (no rounding).

    Returns:
        The sum of a and b, optionally rounded to round_digits decimal places.

    Raises:
        ValueError: If round_digits is a negative integer.
    """
    result = a + b
    if round_digits is not None:
        if round_digits < 0:
            raise ValueError("round_digits must be a non-negative integer")
        return round(result, round_digits)
    return result
