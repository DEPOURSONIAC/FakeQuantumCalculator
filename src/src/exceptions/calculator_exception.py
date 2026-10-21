# coding: utf-8

# Class
class CalculatorException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)