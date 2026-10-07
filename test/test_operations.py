# coding: utf-8

# Module
from src.operations.addition import Addition
from src.operations.soustration import Soustraction
from src.operations.multiplication import Multiplication
from src.operations.division import Division

# Fct
def test_addition()-> None:
    operation = Addition(2, 3)

    result = operation.calculate()

    assert result == 5


def test_soustraction()-> None:
    operation = Soustraction(5, 3)

    result = operation.calculate()

    assert result == 2


def test_multiplication()-> None:
    operation = Multiplication(4, 3)

    result = operation.calculate()

    assert result == 12


def test_division()-> None:
    operation = Division(10, 2)

    result = operation.calculate()

    assert result == 5


if __name__ == "__main__":
    # python3 -m test.test_operations
    """
        It's the test_operations programm.
    """
    test_addition()
    test_soustraction()
    test_multiplication()
    test_division()

    print("Tous les tests sont réussis !")