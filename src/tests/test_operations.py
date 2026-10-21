# coding: utf-8
"""
Tests des différentes opérations de la calculatrice.
"""

# Module
from src.operations.addition import Addition
from src.operations.soustraction import Soustraction
from src.operations.multiplication import Multiplication
from src.operations.division import Division
from src.exceptions.division_by_zero import DivisionByZeroException

# Fct
def test_addition() -> None:
    operation = Addition(5, 7)

    assert operation.calculate() == 12


def test_soustraction() -> None:
    operation = Soustraction(10, 4)

    assert operation.calculate() == 6


def test_multiplication() -> None:
    operation = Multiplication(5, 4)

    assert operation.calculate() == 20


def test_division() -> None:
    operation = Division(10, 2)

    assert operation.calculate() == 5


def test_division_by_zero() -> None:
    operation = Division(10, 0)

    try:
        operation.calculate()
    except DivisionByZeroException as error:
        assert str(error) == "Impossible de diviser par zéro."
        return

    raise AssertionError("DivisionByZeroException attendue.")


if __name__ == "__main__":
    # python3 -m tests.test_operations
    """
    It's the test_operations program.
    """

    test_addition()
    test_soustraction()
    test_multiplication()
    test_division()
    test_division_by_zero()

    print("Tous les tests sont passés.")