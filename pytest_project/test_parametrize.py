import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-5, 5, 0),
    (100, 200, 300),
    (-10, -20, -30),
])
def test_add_parametrized(calc, a, b, expected):
    assert calc.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (9, 3, 3),
    (100, 10, 10),
    (7, 2, 3.5),
    
])
def test_divide_parametrized(calc, a, b, expected):
    assert calc.divide(a, b) == expected
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (0, 5, 0),
    (-2, 3, -6),
    (-4, -5, 20),
    (10, 10, 100),
])
def test_multiply_parametrized(calc, a, b, expected):
    assert calc.multiply(a, b) == expected