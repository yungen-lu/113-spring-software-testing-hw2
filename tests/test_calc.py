import pytest
from calc.Calc import Calculator


def test_add():
    # Create an instance of the Calculator class
    calc = Calculator()

    # Test case 1: Adding two positive numbers
    assert calc.add(2, 3) == 5

    # Test case 2: Adding a positive and a negative number
    assert calc.add(-1, 1) == 0

    # Test case 3: Adding two negative numbers
    assert calc.add(-2, -3) == -5

    # Test case 4: Adding zero
    assert calc.add(5, 0) == 5
