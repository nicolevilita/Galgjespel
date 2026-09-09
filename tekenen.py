"""
ONDERDEEL 2: TEKENEN VAN DE GALG
--------------------------------------------
Alles wat met de tekening op het canvas te maken heeft.
Dit bestand weet niks van woorden of spellogica -- het krijgt gewoon
een canvas en een aantal fouten, en tekent daar de galg op.
"""

# Elk item hieronder tekent 1 lichaamsdeel: (x1, y1, x2, y2).
# Bij bijvoorbeeld 3 fouten pakken we gewoon de eerste 3 items uit dit lijstje.
LICHAAMSDELEN = [
    (120, 45, 160, 85),    # 1. hoofd  (ovaal)
    (140, 85, 140, 140),   # 2. lijf   (lijn)
    (140, 95, 115, 120),   # 3. linkerarm
    (140, 95, 165, 120),   # 4. rechterarm
    (140, 140, 115, 175),  # 5. linkerbeen
    (140, 140, 165, 175),  # 6. rechterbeen
]
MAX_FOUTEN = len(LICHAAMSDELEN)


def teken_galg(canvas, fouten):
    """Tekent de galgconstructie plus zoveel lichaamsdelen als er fouten zijn."""
    canvas.delete("all")

    # De houten constructie staat er altijd
    canvas.create_line(20, 200, 100, 200, width=3)   # grond
    canvas.create_line(50, 200, 50, 20, width=3)     # paal
    canvas.create_line(50, 20, 140, 20, width=3)     # bovenbalk
    canvas.create_line(140, 20, 140, 45, width=3)    # touw

    # Lichaamsdelen die horen bij het huidige aantal fouten
    for i, deel in enumerate(LICHAAMSDELEN[:fouten]):
        if i == 0:
            canvas.create_oval(*deel, width=3)   # het hoofd is een ovaal
        else:
            canvas.create_line(*deel, width=3)   # de rest zijn lijnen


def teken_eindscherm(canvas):
    """Vervangt de tekening door een felicitatie als alle niveaus zijn gehaald."""
    canvas.delete("all")
    canvas.create_text(
        110, 110,
        text="🎉\nALLE NIVEAUS\nAFGEROND!",
        font=("Arial", 16, "bold"),
        fill="green",
        justify="center"
    )