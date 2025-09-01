
# caro_barato.py

def evaluar_precio(precio, cantidad):
    if precio == 0 or cantidad == 0:
        return "¿Fue gratis, o no compraste nada?"
    elif precio > 100 or (cantidad < 10 and precio > 50):
        return "Caro"
    else:
        return "Barato"