# coding: utf-8

# Module
from .operation import Operation
from ..exceptions.division_by_zero import DivisionByZeroException

# Class
class Division (Operation):
    """
    Représente une division de deux nombres.
    """

    def calculate(self) -> float:
        """
        Divise les deux nombres.

        Returns:
            float: Résultat de la division.
        """

        if self.get_nb2() == 0:
            raise DivisionByZeroException()
        
        return self.get_nb1() / self.get_nb2()