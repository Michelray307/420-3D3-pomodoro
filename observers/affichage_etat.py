import tkinter as tk
from observers.observer import Observateur


class AffichageEtat(Observateur):

    def __init__(self, parent):
        self._label = tk.Label(parent, text="Travail", font=("Arial", 16, "bold"))
        self._label.pack(pady=5)

    def actualiser(self, sujet) -> None:
        # À compléter :
        # Récupérez etat depuis sujet.get_donnees()
        # Mettez à jour le label
        # Couleur : noir pour "Travail", bleu pour "Pause"
        donnes = sujet.get_donnes()
        etat = donnes["état"]

        self.label.config(text=etat)
        if etat == "Travail":
            self.label.config(fg="black")
        elif etat == "Pause":
            self.label.config(fg="blue")
