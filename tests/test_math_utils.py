from src.math_utils import add, subtract, multiply


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -1) == -2


def test_add_zero():
    assert add(0, 5) == 5


def test_subtract_positive_numbers():
    assert subtract(10, 4) == 6


def test_subtract_negative_numbers():
    assert subtract(-3, -2) == -1


def test_subtract_zero():
    assert subtract(7, 0) == 7


def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    assert multiply(5, 0) == 0


def test_multiply_negative_numbers():
    assert multiply(-2, -3) == 6


def test_multiply_mixed_sign():
    assert multiply(-3, 4) == -12


def test_multiply_by_one():
    assert multiply(7, 1) == 7
