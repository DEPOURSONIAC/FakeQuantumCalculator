# coding: utf-8

# Module
from ..operations.operation import Operation

# Class
class Calculator:
    """
    Service responsable de l'exécution des opérations mathématiques.
    """

    def calculate(self, operation: Operation) -> float:
        return operation.calculate()


if __name__ == '__main__':
    # python3 -m src.services.calculator
    """
        It's the calculator programm.
    """

    from ..operations.addition import Addition

    # Décla
    var : type

    # Instance
    addition = Addition(5, 7.5)
    calculator = Calculator()

    result = calculator.calculate(addition)

    print(f"Résultat : {result}")