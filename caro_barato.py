
precio = int(input("¿Cuánto costó el producto?:"))
cantidad = int(input("¿Cuantos compraste?: "))
if precio == 0 or cantidad == 0:
    print("¿Fue gratis, o no compraste nada?")
else: 
    if precio > 100 or (cantidad < 10 and precio > 50):
        print("Caro")
    else:
        print("barato") 