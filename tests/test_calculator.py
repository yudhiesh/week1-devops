from src.calculator import add, sub, mul, div
import pytest

def test_add():
    assert add(1, 1) == 2
    assert add(-1, 1) == 0
    assert add(1.5, 2.5) == 4

def test_sub():
    assert sub(1, 1) == 0
    assert sub(-1, -1) == 0
    assert sub(5.5, 2.5) == 3

def test_mul():
    assert mul(1, 1) == 1
    assert mul(-1, 1) == -1
    assert mul(3, 0.5) == 1.5

def test_div():
    assert div(2, 1) == 2
    assert div(-2, 1) == -2
    assert div(5, 2) == 2.5
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
