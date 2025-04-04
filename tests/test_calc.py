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


def test_subtract():
    # Create an instance of the Calculator class
    calc = Calculator()

    # Test case 1: Subtracting two positive numbers
    assert calc.subtract(5, 3) == 2

    # Test case 2: Subtracting a positive and a negative number
    assert calc.subtract(1, -1) == 2

    # Test case 3: Subtracting two negative numbers
    assert calc.subtract(-2, -3) == 1

    # Test case 4: Subtracting zero
    assert calc.subtract(5, 0) == 5
