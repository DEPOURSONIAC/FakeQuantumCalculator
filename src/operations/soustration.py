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


if __name__ == '__main__':
    # python3 -m src.operations.soustration
    """
    It's the soustraction programm.
    """

    # Création d'une soustraction
    soustraction = Soustraction(7.5, 5.0)
    
    # Calcul
    result = soustraction.calculate()
    
    # Affichage
    print(f"Avec {soustraction.get_nb1()} - {soustraction.get_nb2()}, on a: ") # 2.5
    print(f"Résultat -> {result}")