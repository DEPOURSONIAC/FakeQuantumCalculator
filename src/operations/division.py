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


if __name__ == '__main__':
    # python3 -m src.operations.division
    """
    It's the division programm.
    """

    print('-----P1-----')

    # Création d'une division
    division = Division(7.5, 5.0)
    
    # Calcul
    result = division.calculate()
    
    # Affichage
    
    print(f"Avec {division.get_nb1()} / {division.get_nb2()}, on a: ") # 1.5
    print(f"Résultat -> {result}")

    # Avec erreur

    print('-----P2-----')
    try:
        # Création d'une division
            division = Division(7.5, 0)
            
            # Calcul
            result = division.calculate()
            
            # Affichage
        
            print(f"Avec {division.get_nb1()} / {division.get_nb2()}, on a: ") # 1.5
            print(f"Résultat -> {result}")
    except DivisionByZeroException as Error:
        print(Error)