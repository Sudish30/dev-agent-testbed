from src.math_utils import multiply


def test_multiply_two_positive_integers():
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    assert multiply(5, 0) == 0
    assert multiply(0, 5) == 0


def test_multiply_negative_numbers():
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6


def test_multiply_one_as_identity():
    assert multiply(7, 1) == 7
    assert multiply(1, 7) == 7
