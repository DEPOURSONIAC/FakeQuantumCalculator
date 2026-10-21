# coding: utf-8
"""
Tests des exceptions de la calculatrice.
"""

# Module
from src.exceptions.calculator_exception import CalculatorException
from src.exceptions.division_by_zero import DivisionByZeroException
from src.exceptions.invalid_operation import InvalidOperationException

# Fct
def test_calculator_exception() -> None:
    error = CalculatorException("Erreur de calcul.")

    assert str(error) == "Erreur de calcul."


def test_division_by_zero_exception() -> None:
    error = DivisionByZeroException()

    assert isinstance(error, CalculatorException)
    assert str(error) == "Impossible de diviser par zéro."


def test_invalid_operation_exception() -> None:
    error = InvalidOperationException()

    assert isinstance(error, CalculatorException)
    assert str(error) == "Opération invalide."


if __name__ == "__main__":
    # python3 -m tests.test_exceptions
    """
    It's the test_exceptions program.
    """

    test_calculator_exception()
    test_division_by_zero_exception()
    test_invalid_operation_exception()

    print("Tous les tests sont passés.")