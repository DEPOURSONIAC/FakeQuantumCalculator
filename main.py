# coding: utf-8

"""Point d'entrée de la calculatrice graphique."""

# Module
import customtkinter as ctk

from src.ui.calculator_window import CalculatorWindow


def main() -> int:
    """Configure et lance la fenêtre de la calculatrice."""

    # Configuration de l'apparence
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    # Création de la fenêtre principale
    app = CalculatorWindow()

    # Lancement de la calculatrice
    app.mainloop()

    return 0


if __name__ == "__main__":
    # python3 main.py
    """
       It's the main program.
    """
    main()