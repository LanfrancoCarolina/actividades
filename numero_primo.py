#Escribe un programa que a partir de un número entero positivo,
#muestre por pantalla si es primo o no.

while True:
    numero = int(input("Escribe un número entero positivo (o 0 para salir): "))
    
    if numero == 0:
        print("¡Programa terminado!")
        break  # Sale del bucle

    if numero > 1:
        es_primo = True
        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            print("Es un número primo.")
        else:
            print("No es un número primo.")
    else:
        print("No es un número primo.")