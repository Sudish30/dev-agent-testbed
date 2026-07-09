import pytest
from src.math_utils import add


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_add_floats():
    assert add(2.5, 3.1) == pytest.approx(5.6)
    assert add(-1.5, 1.5) == pytest.approx(0.0)
    assert add(0.0, 0.0) == pytest.approx(0.0)


def test_add_mixed_int_float():
    assert add(2, 3.5) == pytest.approx(5.5)
    assert add(1.5, 2) == pytest.approx(3.5)


def test_add_with_rounding():
    assert add(2.555, 1.001, round_digits=2) == 3.56
    assert add(1.1, 2.2, round_digits=1) == 3.3
    assert add(1, 2, round_digits=0) == 3


def test_add_round_digits_invalid():
    with pytest.raises(ValueError, match="round_digits must be a non-negative integer"):
        add(1, 2, round_digits=-1)
