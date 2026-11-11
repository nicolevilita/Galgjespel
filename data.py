
import random

# Steden per niveau: van heel bekend (niveau 1) naar onbekend (niveau 4)
STEDEN = [
    ["Amsterdam", "Rotterdam", "Utrecht", "Eindhoven", "Groningen"],
    ["Maastricht", "Breda", "Nijmegen", "Arnhem", "Haarlem"],
    ["Zwolle", "Deventer", "Alkmaar", "Delft", "Leeuwarden"],
    ["Weesp", "Bolsward", "Elburg", "Ravenstein", "Vianen"],
]

ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def kies_woord(niveau):
    """kiest willekeurig een stad uit het opgegeven niveau (0 = niveau 1)."""
    return random.choice(STEDEN[niveau]).upper()


def is_gewonnen(woord, geraden_letters):
    """true als alle letters van het woord al geraden zijn."""
    return all(letter in geraden_letters for letter in woord)


def toon_streepjes(woord, geraden_letters):
    """geeft het woord terug met streepjes voor niet-geraden letters, bv: A _ S T _ R D _ M."""
    return " ".join(letter if letter in geraden_letters else "_" for letter in woord)