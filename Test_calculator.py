import pytest
import calculator
from pytest import approx


# Testing Addition Calculator Function
@pytest.mark.parametrize("num1,num2,expectedResult", [(2, 3, 5), (-2, -3, -5), (2, -3, -1)])
def test_Add(num1, num2, expectedResult):
    result = calculator.add(num1, num2)
    assert result == expectedResult


# Testing Subtraction Calculator Function
@pytest.mark.parametrize("num1,num2,expectedResult", [(2, 3, -1), (-2, -3, 1), (2, -3, 5)])
def test_Subtract(num1, num2, expectedResult):
    result = calculator.subtract(num1, num2)
    assert result == expectedResult


# Testing Multiply Calculator Function
@pytest.mark.parametrize("num1,num2,expectedResult", [(2, 3, 6), (-2, -3, 6), (2, -3, -6)])
def test_Multiply(num1, num2, expectedResult):
    result = calculator.multiply(num1, num2)
    assert result == expectedResult


# Testing Division Calculator Function
@pytest.mark.parametrize("num1,num2,expectedResult", [(21, 3, 7), (-21, -3, 7), (-21, 3, -7)])
def test_Divide(num1, num2, expectedResult):
    result = calculator.divide(num1, num2)
    assert result == expectedResult


# Test division rounding decimal places
@pytest.mark.xfail(reason="assert float issue")
def test_DivideRounding():
    result = calculator.divide(1, 3)
    assert result == approx(0.332, 0.001)


# Test Division by Zero error
@pytest.mark.xfail(reason="known issue")
def test_Subtract():
    result = calculator.divide(1, 0)
    assert result == ValueError


# Test Calculator does not take in more than 3 values
@pytest.mark.xfail(reason="known issue")
def test_moreThan2Inputs():
    result = calculator.subtract(-21, 4, 90)
    assert result == ValueError()


# Test Calculator error when only 1 value entered
@pytest.mark.xfail(reason="known issue")
def test_onlyOneValue():
    result = calculator.subtract(9, None)
    assert result == ValueError


# Test Calculator error when nil value entered
@pytest.mark.xfail(reason="known issue")
def test_nilValue():
    result = calculator.subtract(None, None)
    assert result == 0

# Test Calculator when double 0 values entered
def test_doubleZeroInput():
    result = calculator.subtract(0, 0)
    assert result == 0
