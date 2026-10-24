# coding: utf-8

# Module
import customtkinter as ctk
from src.ui.calculator_window import CalculatorWindow

# Fct 
def test_window()-> None:
    # Configuration de l'apparence
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
        
    # Instanciation de la fenêtre de ma calculatrice
    app = CalculatorWindow()
        
    # Lancement de la calculatrice
    app.mainloop()

if __name__ == '__main__':
    # python3 -m tests.test_window
    """
        It's the test_window program.
    """

    test_window()