import pytest
from src.math_utils import add, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_divide_normal_cases():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3
    assert divide(-7, 2) == -4
    assert divide(0, 5) == 0

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
