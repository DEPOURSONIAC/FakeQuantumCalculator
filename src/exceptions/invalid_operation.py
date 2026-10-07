# coding: utf-8

# Module
from .calculator_exception import CalculatorException

# Class
class InvalidOperationException(CalculatorException):
    """
    Exception levée lorsqu'une opération n'est pas reconnue.
    """

    def __init__(self) -> None:
        super().__init__("Opération invalide.")


if __name__ == '__main__':
    # python3 -m src.exceptions.invalid_operation
    """
        It's the invalid operation error programm .
    """

    error = InvalidOperationException()

    print(error)