"""
ONDERDEEL 3: SCHERM EN SPELLOGICA
--------------------------------------------
Bouwt het venster op (knoppen, labels, canvas) en regelt de spelflow:
wat er gebeurt als je op een letter klikt, wanneer je wint/verliest,
en wanneer je naar het volgende niveau gaat.

Gebruikt de functies uit data.py (woorden) en tekenen.py (de galg).
"""

import tkinter as tk
from tkinter import messagebox

from data import STEDEN, ALFABET, kies_woord, is_gewonnen, toon_streepjes
from tekenen import teken_galg, teken_eindscherm, MAX_FOUTEN


class GalgjeSpel:
    def __init__(self, root):
        self.root = root
        root.title("Galgje - Nederlandse Steden")
        self.niveau = 0

        # --- Scherm opbouwen ---
        self.niveau_label = tk.Label(root, font=("Arial", 14, "bold"))
        self.niveau_label.pack(pady=5)

        self.canvas = tk.Canvas(root, width=220, height=220, bg="white")
        self.canvas.pack()

        self.woord_label = tk.Label(root, font=("Courier", 20, "bold"))
        self.woord_label.pack(pady=5)

        self.status_label = tk.Label(root, font=("Arial", 11))
        self.status_label.pack(pady=5)

        knoppen_frame = tk.Frame(root)
        knoppen_frame.pack(pady=10)
        self.knoppen = {}
        for i, letter in enumerate(ALFABET):
            knop = tk.Button(knoppen_frame, text=letter, width=3,
                              command=lambda l=letter: self.raad_letter(l))
            knop.grid(row=i // 7, column=i % 7, padx=2, pady=2)
            self.knoppen[letter] = knop

        self.opnieuw_knop = tk.Button(root, text="Opnieuw spelen", command=self.nieuw_woord)
        self.opnieuw_knop.pack(pady=10)

        self.nieuw_woord()

    def nieuw_woord(self):
        """Start een nieuwe ronde op het huidige niveau."""
        self.woord = kies_woord(self.niveau)
        self.geraden = set()
        self.fouten = 0

        self.niveau_label.config(text=f"Niveau {self.niveau + 1} van {len(STEDEN)}")
        self.status_label.config(text="Kies een letter!")
        for knop in self.knoppen.values():
            knop.config(state="normal")

        teken_galg(self.canvas, self.fouten)
        self.woord_label.config(text=toon_streepjes(self.woord, self.geraden))

    def raad_letter(self, letter):
        """Verwerkt een klik op een letterknop."""
        self.geraden.add(letter)
        self.knoppen[letter].config(state="disabled")

        if letter not in self.woord:
            self.fouten += 1
            teken_galg(self.canvas, self.fouten)

        self.woord_label.config(text=toon_streepjes(self.woord, self.geraden))

        if is_gewonnen(self.woord, self.geraden) or self.fouten >= MAX_FOUTEN:
            self.spel_afgerond(is_gewonnen(self.woord, self.geraden))

    def spel_afgerond(self, gewonnen):
        """Regelt wat er gebeurt na winst of verlies."""
        for knop in self.knoppen.values():
            knop.config(state="disabled")

        laatste_niveau = self.niveau == len(STEDEN) - 1

        if gewonnen and laatste_niveau:
            teken_eindscherm(self.canvas)
            self.status_label.config(text="Gefeliciteerd, je hebt het hele spel uitgespeeld!")
            self.niveau = 0  # volgende "Opnieuw spelen" begint weer vanaf niveau 1
            return

        if gewonnen:
            messagebox.showinfo("Gewonnen!", f"Het woord was: {self.woord}")
            self.niveau += 1
        else:
            messagebox.showinfo("Helaas!", f"Het woord was: {self.woord}")

        self.nieuw_woord()


if __name__ == "__main__":
    root = tk.Tk()
    GalgjeSpel(root)
    root.mainloop()

