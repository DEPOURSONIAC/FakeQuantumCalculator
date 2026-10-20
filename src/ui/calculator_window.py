# coding: utf-8

# Module
import customtkinter as ctk

# Class
class CalculatorWindow(ctk.CTk):
    """
    Crée la fenêtre principale de la calculatrice.
    """

    def __init__(self) -> None:
        """
        Initialise et configure la fenêtre.
        """
        super().__init__()

        # Configuration de la fenêtre
        self.title("Calculatrice V2")
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

    def _configure_layout(self) -> None:
        """
        Configure la grille principale de la fenêtre.
        """
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

    def _create_frames(self) -> None:
        """
        Crée les zones de calcul et d'historique.
        """
        # Calcul
        self.calculator_frame: ctk.CTkFrame = ctk.CTkFrame(self, fg_color="#222229", corner_radius=16,)
        self.calculator_frame.grid(row=0, column=0, padx=(20, 10), pady=20, sticky="nsew",)

        # Histo
        self.history_frame: ctk.CTkFrame = ctk.CTkFrame(self, fg_color="#222229", corner_radius=16,)
        self.history_frame.grid(row=0, column=1, padx=(10, 20), pady=20, sticky="nsew",)

        # Configuration de calcul
        self.calculator_frame.grid_columnconfigure(0, weight=1)
        self.calculator_frame.grid_rowconfigure(2, weight=1)

        # Configuration de l'historique
        self.history_frame.grid_columnconfigure(0, weight=1)
        self.history_frame.grid_rowconfigure(1, weight=1)

    def _create_titles(self) -> None:
        """
        Crée les titres des zones principales.
        """
        # Titre de la calculatrice
        self.calculator_title: ctk.CTkLabel = ctk.CTkLabel(self.calculator_frame, text="Calculatrice", font=("Arial", 22, "bold"), text_color="#FFFFFF",)
        self.calculator_title.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w",)

        # Titre de l'historique
        self.history_title: ctk.CTkLabel = ctk.CTkLabel(self.history_frame, text="Historique", font=("Arial", 20, "bold"), text_color="#FFFFFF",)
        self.history_title.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w",)

    def _create_display(self) -> None:
        """
        Crée la zone d'affichage du calcul et du résultat.
        """
        self.display_frame: ctk.CTkFrame = ctk.CTkFrame(self.calculator_frame, fg_color="#17171D", corner_radius=12,)
        self.display_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew",)

        # Expression que le user donne
        self.expression_label: ctk.CTkLabel = ctk.CTkLabel(self.display_frame, text="En attente d'un calcul...", font=("Arial", 14), text_color="#B8B8C5", anchor="e",)
        self.expression_label.pack(fill="x", padx=15, pady=(12, 5),)

        # Résultat du user
        self.result_label: ctk.CTkLabel = ctk.CTkLabel(self.display_frame, text="0", font=("Arial", 28, "bold"), text_color="#FFFFFF", anchor="e",)
        self.result_label.pack( fill="x", padx=15, pady=(5, 12),)

    def _create_buttons(self) -> None:
        """
        Crée et positionne les boutons de la calculatrice.
        """
        self.buttons_frame: ctk.CTkFrame = ctk.CTkFrame( self.calculator_frame, fg_color="transparent",)
        self.buttons_frame.grid( row=2, column=0, padx=20, pady=(10, 20), sticky="nsew",)

        # Configuration de la grille des boutons
        for column_index in range(4):
            self.buttons_frame.grid_columnconfigure(column_index, weight=1, uniform="calculator_columns",)

        for row_index in range(5):
            self.buttons_frame.grid_rowconfigure(row_index, weight=1, uniform="calculator_rows",)

        # Organisation fixe des boutons
        buttons: list[list[str]] = [
            ["C", "<-", "(", ")"],
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "−"],
            ["0", ".", "=", "+"],
        ]

        # Création des boutons avec une boucle
        for row_index, row_buttons in enumerate(buttons):
            for column_index, button_text in enumerate(row_buttons):
                self._create_button(button_text, row_index, column_index,)

    def _create_button(self, text: str, row: int, column: int,) -> None:
        """
        Crée un bouton et le place dans la grille.
        """
        # Couleur des boutons
        if text in ["÷", "×", "−", "+", "="]:
            button_color: str = "#345A9C"
        elif text in ["C", "<-"]:
            button_color = "#454550"
        else:
            button_color = "#303039"

        # Création du bouton
        button: ctk.CTkButton = ctk.CTkButton(self.buttons_frame,command=lambda: self._on_button_click(text),  text=text, font=("Arial", 18, "bold"), fg_color=button_color, hover_color="#506FA5", corner_radius=10, height=40,)
        button.grid( row=row, column=column, padx=4, pady=4, sticky="nsew",)

    def _on_button_click(self, value: str) -> None:
        """
        Gère le clic sur un bouton de la calculatrice.
        """
        print(f"Bouton cliqué : {value}")

# Main
if __name__ == "__main__":
    # python3 src/ui/calculator_window.py
    """
    Lance l'application graphique.
    """

    # Configuration de l'apparence
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    # Instanciation de la fenêtre
    app: CalculatorWindow = CalculatorWindow()

    # Lancement de la boucle graphique
    app.mainloop()

    # print('Fin du programme...')