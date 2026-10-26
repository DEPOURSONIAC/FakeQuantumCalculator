# coding: utf-8

# Class
class CalculatorException(Exception):
    """Mes propres exceptions."""
    def __init__(self, message: str) -> None:
        super().__init__(message)