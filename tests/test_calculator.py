# coding: utf-8
"""
Tests du service Calculator.
"""

# Module
from src.services.calculator import Calculator
from src.operations.addition import Addition
from src.operations.soustraction import Soustraction
from src.operations.multiplication import Multiplication
from src.operations.division import Division
from src.exceptions.division_by_zero import DivisionByZeroException

# Fct
def test_calculator_addition() -> None:
    calculator = Calculator()
    operation = Addition(5, 7)

    result = calculator.calculate(operation)

    assert result == 12


def test_calculator_soustraction() -> None:
    calculator = Calculator()
    operation = Soustraction(10, 4)

    result = calculator.calculate(operation)

    assert result == 6


def test_calculator_multiplication() -> None:
    calculator = Calculator()
    operation = Multiplication(5, 4)

    result = calculator.calculate(operation)

    assert result == 20


def test_calculator_division() -> None:
    calculator = Calculator()
    operation = Division(10, 2)

    result = calculator.calculate(operation)

    assert result == 5


def test_calculator_division_by_zero() -> None:
    calculator = Calculator()
    operation = Division(10, 0)

    try:
        calculator.calculate(operation)
    except DivisionByZeroException as error:
        assert str(error) == "Impossible de diviser par zéro."
        return

    raise AssertionError("DivisionByZeroException attendue.")

if __name__ == "__main__":
    # python3 -m tests.test_calculator
    """
    It's the test_calculator program.
    """

    test_calculator_addition()
    test_calculator_soustraction()
    test_calculator_multiplication()
    test_calculator_division()
    test_calculator_division_by_zero()

    print("Tous les tests sont passés.")