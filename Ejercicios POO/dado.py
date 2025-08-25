
import random

class Dado:
    def __init__(self, caras=6):   # Por defecto tiene 6 caras
        self.caras = caras

    def lanzar(self):
        return random.randint(1, self.caras)


dado1 = Dado()         # un dado de 6 caras
dado2 = Dado(12)       # un dado de 12 caras

print("Dado de 6 caras:", dado1.lanzar())
print("Dado de 12 caras:", dado2.lanzar())   



