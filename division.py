
#Haciendo una division


numerador = int(input("Escribe el numero que quieras dividir: "))
denominador = int(input("Escribe el donominador, que no puede ser 0 : "))
if denominador == 0:
    print("Error, te dije que no podia ser 0")
else:
    
    dividir = numerador / denominador
    print(f"El resultado es {dividir}")
