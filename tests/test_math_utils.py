from src.math_utils import multiply


def test_multiply_two_positive_integers():
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    assert multiply(5, 0) == 0
    assert multiply(0, 5) == 0


def test_multiply_two_negative_integers():
    assert multiply(-3, -4) == 12


def test_multiply_positive_and_negative():
    assert multiply(-3, 4) == -12


def test_multiply_by_one():
    assert multiply(7, 1) == 7
    assert multiply(1, 7) == 7
