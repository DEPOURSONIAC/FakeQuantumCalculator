# coding: utf-8

# Module
from .operation import Operation

# Class
class Multiplication (Operation):
    """
    Représente une multiplication de deux nombres.
    """

    def calculate(self) -> float:
        """
        Multiplie les deux nombres.

        Returns:
            float: Résultat de la multiplication.
        """
        return self.get_nb1() * self.get_nb2()