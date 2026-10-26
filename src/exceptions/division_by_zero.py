# coding: utf-8

# Module
from .calculator_exception import CalculatorException

# Class
class DivisionByZeroException(CalculatorException):
    """Ma propre version de l'exception pour la division par zéro."""
    def __init__(self) -> None:
        super().__init__("Impossible de diviser par zéro.")