
import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    """Создаёт новый калькулятор перед каждым тестом."""
    return Calculator()

@pytest.fixture
def calc_with_history():
    """Калькулятор с уже выполненными операциями."""
    c = Calculator()
    c.add(2, 3)
    c.add(10, 20)
    c.multiply(3, 3)
    return c

def test_add(calc):
    assert calc.add(2, 3) == 5

def test_subtract(calc):
    assert calc.subtract(10, 4) == 6

def test_multiply(calc):
    assert calc.multiply(3, 4) == 12

def test_divide(calc):
    assert calc.divide(10, 2) == 5

def test_divide_by_zero(calc):
    with pytest.raises(ValueError, match="Деление на ноль"):
        calc.divide(10, 0)

def test_history_count(calc_with_history):
    assert len(calc_with_history.get_history()) == 3

def test_clear_history(calc_with_history):
    calc_with_history.clear_history()
    assert calc_with_history.get_history() == []
