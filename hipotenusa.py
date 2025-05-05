#calculando hipotenusa
cateto_a = int(input("Decime cuanto mide el cateto a: "))
cateto_b = int(input("Decime cuanto mide el cateto b: "))
hipotenusa_cuadrado = (cateto_a **2) + (cateto_b **2)
hipotenusa = hipotenusa_cuadrado ** 0.5
print(f"si el cateto a mide {cateto_a} y el cateto b mide {cateto_b} la hipotenusa mide {round(hipotenusa,2)}")



import math
raiz= math.sqrt(hipotenusa_cuadrado)
print(f"la hipotenusa es {raiz}")
