# coding: utf-8

# Module
from ..operations.operation import Operation
from ..operations.addition import Addition
from ..operations.soustraction import Soustraction
from ..operations.multiplication import Multiplication
from ..operations.division import Division
from ..exceptions.invalid_operation import InvalidOperationException

# Class
class OperationFactory:
    """
    Fabrique l'opération correspondant au symbole fourni.
    """

    def create(self, nb1: float, operation: str, nb2: float) -> Operation:
        retour: Operation

        if operation == "+":
            retour =  Addition(nb1, nb2)

        elif operation == "-":
            retour = Soustraction(nb1, nb2)

        elif operation == "*":
            retour = Multiplication(nb1, nb2)

        elif operation == "/":
            retour = Division(nb1, nb2)

        else:
            raise InvalidOperationException()

        return retour