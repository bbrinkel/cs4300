# Imports pytest and gets calculate_discount function from task4 source file
import pytest
from task4 import calculate_discount

@pytest.mark.parametrize("price, discount, expected", [(46, 25, 34.5), (101.55, 33, 68.04), (94, 33.67, 62.35),
(200.10, 45.5, 109.05), (110, 0, 110), (110, 100, 0)])
def test_calculation(price, discount, expected):
    """
    Uses parameterized values (cases) to ensure that correct outputs are given from calculate_discount() function.

    Args:
        price: int or float
        discount: int or float

    """

    test = calculate_discount(price, discount)

    assert test == expected, f'Expected return value of {expected}'

@pytest.mark.parametrize("price, discount", [(46, ' '), ('Hello', 33), ('', 'Hello')])
def test_types(price, discount):
    """
    Uses parameterized values (cases) to ensure that when a non numerical type is given a TypeError is raised.
    
    Args:
        price: non int or float
        discount: non int or float
    
    """

    with pytest.raises(TypeError):
        calculate_discount(price, discount)

def test_negative_discount():
    """Simple test that ensures ValueError raised when there is a negative discount."""

    with pytest.raises(ValueError):
        calculate_discount(99, -10)

def test_enourmous_discount():
    """Simple test that ensures ValueError raised when discount over 100%."""

    with pytest.raises(ValueError):
        calculate_discount(30, 135)

def test_negative_price():
    """Simple test that ensures ValueError raised when price is less than or equal to 0."""

    with pytest.raises(ValueError):
        calculate_discount(-15, 30)