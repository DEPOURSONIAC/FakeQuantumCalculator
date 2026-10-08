# coding: utf-8
"""
Tests de la fabrique OperationFactory.
"""

# Module
from src.services.operation_factory import OperationFactory
from src.operations.addition import Addition
from src.operations.soustraction import Soustraction
from src.operations.multiplication import Multiplication
from src.operations.division import Division
from src.exceptions.invalid_operation import InvalidOperationException

# Fct
def test_factory_addition() -> None:
    factory = OperationFactory()

    operation = factory.create(5, "+", 7)

    assert isinstance(operation, Addition)
    assert operation.calculate() == 12


def test_factory_soustraction() -> None:
    factory = OperationFactory()

    operation = factory.create(10, "-", 4)

    assert isinstance(operation, Soustraction)
    assert operation.calculate() == 6


def test_factory_multiplication() -> None:
    factory = OperationFactory()

    operation = factory.create(5, "*", 4)

    assert isinstance(operation, Multiplication)
    assert operation.calculate() == 20


def test_factory_division() -> None:
    factory = OperationFactory()

    operation = factory.create(10, "/", 2)

    assert isinstance(operation, Division)
    assert operation.calculate() == 5


def test_factory_invalid_operation() -> None:
    factory = OperationFactory()

    try:
        factory.create(5, "%", 7)
    except InvalidOperationException as error:
        assert str(error) == "Opération invalide."
        return

    raise AssertionError("InvalidOperationException attendue.")


if __name__ == "__main__":
    # python3 -m tests.test_operation_factory
    """
    It's the test_operation_factory program.
    """

    test_factory_addition()
    test_factory_soustraction()
    test_factory_multiplication()
    test_factory_division()
    test_factory_invalid_operation()

    print("Tous les tests sont passés.")