# coding: utf-8

# Module
import customtkinter as ctk

# Class
class CalculatorWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre
        self.title("Calculatrice V2")
        self.geometry("850x520")
        self.minsize(700, 450)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.configure(fg_color="#17171D")

        # Grille principale : calcul à gauche, historique à droite
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # Frame de calcul (on l'a crée et on la place)
        self.calculator_frame = ctk.CTkFrame(self, fg_color="#222229", corner_radius=16,)
        self.calculator_frame.grid(row=0, column=0, padx=(20, 10), pady=20, sticky="nsew",)

        # Frame d'historique (on l'a crée et on la place)
        self.history_frame = ctk.CTkFrame(self, fg_color="#222229", corner_radius=16,)
        self.history_frame.grid(row=0, column=1, padx=(10, 20), pady=20, sticky="nsew",)

        # Affichage des lables (gère le texte)

        # Pour le calculator classique
        self.calculator_title = ctk.CTkLabel(self.calculator_frame, text="Calculatrice", font=("Arial", 22, "bold"), text_color="#FFFFFF",)
        self.calculator_title.grid( row=0, column=0, padx=20, pady=(20, 10), sticky="w",)

        # Pour l'historique
        self.history_title = ctk.CTkLabel(self.history_frame, text="Historique", font=("Arial", 20, "bold"), text_color="#FFFFFF",)
        self.history_title.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w",)

    def create_buttons(self) -> None:
        """
        """
        pass

if __name__ == "__main__":
    # python3 src/ui/calculator_window.py
    """
        Windows program.
    """
    
    app = CalculatorWindow()
    app.mainloop()