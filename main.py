# coding: utf-8

# Module
from src.services.calculator import Calculator
from src.services.operation_factory import OperationFactory
from src.exceptions.calculator_exception import CalculatorException

# Fct
def main()-> int:
    print("----- Calculatrice -----")
    print("Entrez une opération sous la forme : 5 + 7")
    print("Appuyez sur Ctrl+C pour quitter.\n")

    factory = OperationFactory()
    calculator = Calculator()

    is_running: bool = True

    while is_running:
        try:
            expression = input("Calcul : ")

            # Séparation de l'expression
            parts = expression.split()

            # Vérification du nombre d'éléments
            if len(parts) != 3:
                print("Erreur : utilisez le format 'nombre opérateur nombre'.")
                continue

            # Récupération des éléments
            nb1 = float(parts[0])
            operation_symbol = parts[1]
            nb2 = float(parts[2])

            # Création de l'opération
            operation = factory.create(nb1, operation_symbol, nb2)

            # Calcul
            result = calculator.calculate(operation)

            print(f"Résultat : {result}\n")

        except CalculatorException as error:
            print(f"Erreur : {error}\n")

        except ValueError:
            print("Erreur : veuillez entrer des nombres valides.\n")

        except KeyboardInterrupt:
            print("\nProgramme terminé.")
            is_running = False

    return 0

if __name__ == '__main__':
    # python3 main.py
    """
        It's the main program.
    """

    main()