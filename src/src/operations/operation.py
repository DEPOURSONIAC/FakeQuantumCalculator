# coding: utf-8

# Module
from abc import ABC, abstractmethod

# Class
class Operation(ABC):
    """
    Classe mère représentant une opération mathématique.

    Une opération possède deux nombres et doit fournir
    une méthode calculate() implémentée par ses classes filles.
    """

    def __init__(self, nb1: float, nb2: float) -> None:
        self.__nb1: float = nb1
        self.__nb2: float = nb2

    def get_nb1(self) -> float:
        """
        Retourne le premier nombre.
        """
        return self.__nb1

    def get_nb2(self) -> float:
        """
        Retourne le deuxième nombre.
        """
        return self.__nb2

    def set_nb1(self, nb1: float) -> None:
        """
        Modifie le premier nombre.
        """
        self.__nb1 = nb1

    def set_nb2(self, nb2: float) -> None:
        """
        Modifie le deuxième nombre.
        """
        self.__nb2 = nb2

    @abstractmethod
    def calculate(self) -> float:
        """
        Effectue l'opération.

        Cette méthode doit être implémentée par les classes filles.
        """
        pass