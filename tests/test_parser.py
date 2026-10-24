# coding: utf-8

# Module
from src.services.expression_parser import ExpressionParser

# Fct 
def test_parser()-> None:
    parser = ExpressionParser()
    is_working: bool = True
    
    while is_working:
        try:
            expression = input("Calcul (Ctrl+C pour quitter) : ")
            resultat = parser.calculate_expression(expression)
            print(f"Résultat : {resultat}")
    
        except KeyboardInterrupt:
            print("\nAu revoir !")
            is_working = False
    
        except Exception as error:
            print(f"Erreur : {error}")

if __name__ == '__main__':
    # python3 -m tests.test_parser
    """
        It's the test_parser program.
    """

    test_parser()

    print("Tous les tests sont passés.")