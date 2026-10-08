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