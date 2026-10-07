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


if __name__ == '__main__':
    # python3 -m src.operations.multiplication
    """
    It's the multiplication programm.
    """

    # Création d'une soustraction
    multiplication = Multiplication(7.5, 5.0)
    
    # Calcul
    result = multiplication.calculate()
    
    # Affichage
    print(f"Avec {multiplication.get_nb1()} * {multiplication.get_nb2()}, on a: ") # 37.5
    print(f"Résultat -> {result}")