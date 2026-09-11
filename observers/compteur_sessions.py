import tkinter as tk
from observers.observer import Observateur


class CompteurSessions(Observateur):

    def __init__(self, parent):
        self._label = tk.Label(
            parent,
            text="Sessions complétées : 0",
            font=("Arial", 12)
        )
        self._label.pack(pady=5)

    def actualiser(self, sujet) -> None:
        # À compléter :
        # Récupérez sessions_completees depuis sujet.get_donnees()
        # Mettez à jour le label
        session = sujet.get_donnees()
        session_complete = session["session complété"]
        self._label.config(text=f"Sessions complétées : {session_complete}")
