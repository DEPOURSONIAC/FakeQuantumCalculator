# coding: utf-8

# Module
from .operation import Operation

# Class
class Soustraction (Operation):
    """
    Représente une soustraction de deux nombres.
    """

    def calculate(self) -> float:
        """
        Soustrait les deux nombres.

        Returns:
            float: Résultat de la soustraction.
        """
        return self.get_nb1() - self.get_nb2()