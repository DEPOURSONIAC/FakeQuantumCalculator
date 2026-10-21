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