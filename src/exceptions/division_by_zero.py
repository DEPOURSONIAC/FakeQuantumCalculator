# coding: utf-8

# Module
from .calculator_exception import CalculatorException

# Class
class DivisionByZeroException(CalculatorException):
    def __init__(self) -> None:
        super().__init__("Impossible de diviser par zéro.")




if __name__ == '__main__':
    # python3 -m src.exceptions.division_by_zero
    """
    It's the zero error programm where I'm making my own 'division_by_zero'.
    """

    error = DivisionByZeroException()
    print(error)