# coding: utf-8

# Module
from .calculator_exception import CalculatorException

# Class
class DivisionByZeroException(CalculatorException):
    def __init__(self) -> None:
        super().__init__("Impossible de diviser par zéro.")