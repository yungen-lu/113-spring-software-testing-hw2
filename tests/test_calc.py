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


def test_multiply():
    # Create an instance of the Calculator class
    calc = Calculator()

    # Test case 1: Multiplying two positive numbers
    assert calc.multiply(2, 3) == 6

    # Test case 2: Multiplying a positive and a negative number
    assert calc.multiply(-2, 3) == -6

    # Test case 3: Multiplying two negative numbers
    assert calc.multiply(-2, -3) == 6

    # Test case 4: Multiplying by zero
    assert calc.multiply(5, 0) == 0


def test_divide():
    # Create an instance of the Calculator class
    calc = Calculator()

    # Test case 1: Dividing two positive numbers with integer result
    assert calc.divide(6, 2) == 3

    # Test case 2: Dividing a positive and a negative number with integer result
    assert calc.divide(-6, 2) == -3

    # Test case 3: Dividing two negative numbers with integer result
    assert calc.divide(-6, -2) == 3

    # Test case 4: Dividing by zero should raise an exception
    with pytest.raises(ValueError):
        calc.divide(5, 0)
        
    # Test case 5: Dividing with floating-point result
    assert calc.divide(5, 2) == 2.5
    
    # Test case 6: Dividing with floating-point result (negative)
    assert calc.divide(-5, 2) == -2.5
    
    # Test case 7: Dividing with floating-point result (both negative)
    assert calc.divide(-5, -2) == 2.5
    
    # Test case 8: Dividing with floating-point result (smaller number)
    assert calc.divide(2, 5) == 0.4
