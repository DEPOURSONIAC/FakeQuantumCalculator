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


if __name__ == '__main__':
    # python3 -m src.operations.addition
    """
    It's the addition programm.
    """

    # Création d'une addition
    addition = Addition(7.5, 5.0)
    
    # Calcul
    result = addition.calculate()
    
    # Affichage
    print(f"Avec {addition.get_nb1()} + {addition.get_nb2()}, on a: ") # 12.5
    print(f"Résultat -> {result}")