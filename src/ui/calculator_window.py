# coding: utf-8

# Modules
import customtkinter as ctk

from src.exceptions.calculator_exception import CalculatorException
from src.services.expression_parser import ExpressionParser

# Class
class CalculatorWindow(ctk.CTk):
    """Crée la fenêtre principale de la calculatrice."""

    def __init__(self) -> None:
        """Initialise et configure la fenêtre."""
        super().__init__()

        # Expression mathématique
        self.__expression: str = ""

        # Parser et historique
        self.__parser = ExpressionParser()
        self.__history: list[str] = []

        # Configuration de la fenêtre
        self.title("Calculatrice")
        self.geometry("850x520")
        self.minsize(700, 450)
        self.configure(fg_color="#17171D")

        # Configuration de la grille principale
        self._configure_layout()

        # Création des zones principales
        self._create_frames()

        # Création des titres
        self._create_titles()

        # Création de l'affichage
        self._create_display()

        # Création des boutons
        self._create_buttons()

        # Création de l'historique
        self._create_history()

    def _configure_layout(self) -> None:
        """Configure la grille principale de la fenêtre."""
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

    def _create_frames(self) -> None:
        """Crée les zones de calcul et d'historique."""

        # Calculatrice
        self.calculator_frame = ctk.CTkFrame(self, fg_color="#222229", corner_radius=16,)
        self.calculator_frame.grid(row=0, column=0, padx=(20, 10), pady=20, sticky="nsew",)

        # Historique
        self.history_frame = ctk.CTkFrame(self, fg_color="#222229", corner_radius=16,)
        self.history_frame.grid(row=0, column=1, padx=(10, 20), pady=20, sticky="nsew",)

        # Configuration de la calculatrice
        self.calculator_frame.grid_columnconfigure(0, weight=1)
        self.calculator_frame.grid_rowconfigure(2, weight=1)

        # Configuration de l'historique
        self.history_frame.grid_columnconfigure(0, weight=1)
        self.history_frame.grid_rowconfigure(1, weight=1)

    def _create_titles(self) -> None:
        """Crée les titres des zones principales."""

        self.calculator_title = ctk.CTkLabel(self.calculator_frame, text="Calculatrice", font=("Arial", 22, "bold"), text_color="#FFFFFF",)
        self.calculator_title.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w",)

        self.history_title = ctk.CTkLabel(self.history_frame, text="Historique", font=("Arial", 20, "bold"), text_color="#FFFFFF",)
        self.history_title.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w",)

    def _create_display(self) -> None:
        """Crée la zone d'affichage du calcul et du résultat."""

        self.display_frame = ctk.CTkFrame(self.calculator_frame, fg_color="#17171D", corner_radius=12,)
        self.display_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew",)

        # Expression saisie
        self.expression_label = ctk.CTkLabel(self.display_frame, text="En attente d'un calcul...", font=("Arial", 14), text_color="#B8B8C5", anchor="e",)
        self.expression_label.pack(fill="x", padx=15, pady=(12, 5),)

        # Résultat
        self.result_label = ctk.CTkLabel(self.display_frame, text="0", font=("Arial", 28, "bold"), text_color="#FFFFFF", anchor="e",)
        self.result_label.pack(fill="x", padx=15, pady=(5, 12),)

    def _create_buttons(self) -> None:
        """Crée et positionne les boutons de la calculatrice."""

        self.buttons_frame = ctk.CTkFrame(self.calculator_frame, fg_color="transparent",)
        self.buttons_frame.grid(row=2, column=0, padx=20, pady=(10, 20), sticky="nsew",)

        # Configuration de la grille des boutons
        for column_index in range(4):
            self.buttons_frame.grid_columnconfigure(column_index, weight=1, uniform="calculator_columns",)

        for row_index in range(5):
            self.buttons_frame.grid_rowconfigure(row_index, weight=1, uniform="calculator_rows",)

        # Organisation des boutons
        buttons: list[list[str]] = [
            ["C", "<-", "(", ")"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]

        for row_index, row_buttons in enumerate(buttons):
            for column_index, button_text in enumerate(row_buttons):
                self._create_button(button_text, row_index, column_index,)

    def _create_button(self, text: str, row: int, column: int,) -> None:
        """Crée un bouton et le place dans la grille."""

        if text in ["÷", "×", "−", "+", "="]:
            button_color = "#345A9C"
        elif text in ["C", "<-"]:
            button_color = "#454550"
        else:
            button_color = "#303039"

        button = ctk.CTkButton(self.buttons_frame, command=lambda: self._on_button_click(text), text=text, font=("Arial", 18, "bold"), fg_color=button_color, hover_color="#506FA5", corner_radius=10, height=40,)
        button.grid(row=row, column=column, padx=4, pady=4, sticky="nsew",)

    def _create_history(self) -> None:
        """Crée la zone affichant l'historique des calculs."""

        self.history_textbox = ctk.CTkTextbox(self.history_frame, font=("Arial", 14), fg_color="#17171D", text_color="#FFFFFF", corner_radius=10, state="disabled",)
        self.history_textbox.grid(row=1, column=0, padx=15, pady=(5, 15), sticky="nsew",)

    def _add_to_history(self, expression: str, result: float,) -> None:
        """Ajoute un calcul réussi à l'historique."""

        entry = f"{expression} = {result:g}"
        self.__history.append(entry)

        self.history_textbox.configure(state="normal")
        self.history_textbox.insert("end", entry + "\n")
        self.history_textbox.see("end")
        self.history_textbox.configure(state="disabled")
  
    def _on_button_click(self, value: str) -> None:
        """Gère les clics sur les boutons de la calculatrice."""


        if value == "C":
            self.__expression = ""

        elif value == "<-":
            self.__expression = self.__expression[:-1]

        elif value == "=":
            expression = self.__expression.strip()

            if expression:
                try:
                    result = self.__parser.calculate_expression(expression)

                except (CalculatorException, ValueError, ZeroDivisionError, OverflowError,) as error:
                    self.result_label.configure(text="Erreur")
                    self.expression_label.configure(text=str(error))

                else:
                    # Ajouter le calcul réussi à l'historique
                    self._add_to_history(expression, result)

                    self.expression_label.configure(text=expression)
                    self.result_label.configure(text=f"{result:g}")

                    # Permettre de poursuivre le calcul à partir du résultat
                    self.__expression = str(result)

        else:
            self.__expression += value

        # Actualiser l'affichage uniquement hors calcul
        if value != "=":
            self.expression_label.configure(text=self.__expression or "En attente d'un calcul...")
            self.result_label.configure(text=self.__expression or "0")

        return