# coding: utf-8

# Class
class CalculatorException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
    
if __name__ == '__main__':
    # python3 -m src.exceptions.calculator_exception
    """
    It's the exception classic programm where I'm making my own exception.
    """

    error = CalculatorException("Une erreur de calcul est survenue.")
    print(error)