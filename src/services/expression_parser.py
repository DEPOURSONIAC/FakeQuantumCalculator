# coding: utf-8

# Module
import re

from src.services.calculator import Calculator
from src.services.operation_factory import OperationFactory

# Class
class ExpressionParser:
    """Analyse et calcule des expressions mathématiques."""

    def __init__(self) -> None:
        self.__calculator = Calculator()
        self.__factory = OperationFactory()
        self.__tokens: list[str] = []
        self.__position = 0

    def calculate_expression(self, expression: str) -> float:
        """Analyse et calcule une expression."""
        if not expression or not expression.strip():
            raise ValueError("L'expression ne peut pas être vide.")

        expression = (expression.replace("x", "*").replace(",", "."))
        expression = re.sub(r"\s+", "", expression)

        self.__tokens = re.findall(r"(?:\d+(?:\.\d*)?|\.\d+)|[()+\-*/]", expression,)

        if "".join(self.__tokens) != expression:
            raise ValueError("Caractère invalide dans l'expression.")

        self.__position = 0
        result = self.__parse_expression()

        if self.__position != len(self.__tokens):
            raise ValueError("Expression invalide ou incomplète.")

        return result

    def __current_token(self) -> str | None:
        """Retourne le token courant, ou None en fin de liste."""
        token = None

        if self.__position < len(self.__tokens):
            token = self.__tokens[self.__position]

        return token

    def __consume(self) -> str:
        """Consomme et retourne l'élément courant."""
        token = self.__current_token()

        if token is None:
            raise ValueError("Expression incomplète.")

        self.__position += 1
        return token

    def __parse_expression(self) -> float:
        """Analyse les additions et les soustractions."""
        result = self.__parse_term()

        while self.__current_token() in ("+", "-"):
            operator = self.__consume()
            right = self.__parse_term()
            result = self.__execute_operation(result, operator, right)

        return result

    def __parse_term(self) -> float:
        """Analyse les multiplications et les divisions."""
        result = self.__parse_factor()

        while self.__current_token() in ("*", "/"):
            operator = self.__consume()
            right = self.__parse_factor()
            result = self.__execute_operation(result, operator, right)

        return result

    def __parse_factor(self) -> float:
        """Analyse un nombre, un signe ou une parenthèse."""
        token = self.__current_token()

        if token == "+":
            self.__consume()
            return self.__parse_factor()

        if token == "-":
            self.__consume()
            return -self.__parse_factor()

        if token == "(":
            self.__consume()
            result = self.__parse_expression()

            if self.__current_token() != ")":
                raise ValueError("Parenthèse fermante manquante.")

            self.__consume()
            return result

        if token is not None and re.fullmatch(r"(?:\d+(?:\.\d*)?|\.\d+)", token,):
            return float(self.__consume())

        raise ValueError("Un nombre ou une parenthèse est attendu.")

    def __execute_operation(self, nb1: float, operator: str, nb2: float,) -> float:
        """Crée et exécute l'opération demandée."""
        operation = self.__factory.create(nb1, operator, nb2)
        return self.__calculator.calculate(operation)