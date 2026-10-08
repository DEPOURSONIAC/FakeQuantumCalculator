# coding: utf-8

# Module
from .operation import Operation

# Class
class Addition(Operation):
    """
    Représente une addition de deux nombres.
    """

    def calculate(self) -> float:
        """
        Additionne les deux nombres.

        Returns:
            float: Résultat de l'addition.
        """
        return self.get_nb1() + self.get_nb2()