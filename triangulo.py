
lado_1 = int(input("¿Cuanto mide el lado 1: "))
lado_2 = int(input("¿Cuanto mide el lado 2: "))
lado_3 = int(input("¿Cuanto mide el lado 3: "))
if  lado_1 == lado_2 == lado_3: 
    print("El triangulo es equilatero")
elif lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3:
        print("El triangulo es isosceles")
else:
       print("El triangulo es escaleno")

