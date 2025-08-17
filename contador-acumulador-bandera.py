
#Una variable contador se llama así porque lleva la cuenta de cuántas veces se repite algo.
#En Python, suele usarse en un bucle for con la función range():

#Objetivo: Hacer un programa que cuente regresivamente desde 5 hasta 1 y luego diga "¡Despegue!".

for num in range(5,0,  -1):
 print(num)
print("¡Despegue!")

#Una variable acumulador sirve para sumar (o juntar) valores progresivamente en un bucle.
#Por ejemplo, para sumar los números del 1 al 5:
suma = 0  # acumulador

for i in range(1, 6):
    suma += i  # suma = suma + i
print("La suma es:", suma)

#-----------------------------------------------------------------------------------------------

#Ejercicio: suma de números pares
# Escribí un programa que:
#Pida al usuario 5 números (uno por uno).
#Solo sume los números pares (es decir, divisibles por 2).
#Al final, muestre la suma total de esos números pares.

suma_pares = 0
for i in range(5):
    numero = int(input("Decime un numero"))
    if numero % 2 == 0:  # Si es par
        suma_pares += numero  # Lo sumamos

print("La suma de los números pares es:", suma_pares)

#---------------------------------------------------------------------------------------------

#Contar cuántos números impares ingresás
#Pedile al usuario 5 números.
#Contá cuántos de esos son impares (número % 2 ≠ 0).
#Mostrá la cantidad total de impares al final.

contar_impares = 0
for i in range(5):
    numero = int(input("decime un numero: "))
    if numero % 2 != 0: #impar
        contar_impares += 1
print("la suma de los impares es:",contar_impares)       

#----------------------------------------------------------------------------------------

#¿Qué es una bandera?
#Una bandera es una variable que indica si algo ha pasado o no.
#Suele tener valores True o False.

#Ejemplo: querés saber si existe algún número negativo en una lista:

numeros = [4, 7, -3, 2]
bandera_negativo = False  # bandera

for n in numeros:
    if n < 0:
        bandera_negativo = True
        break  # ya no hace falta seguir buscando

if bandera_negativo:
    print("¡Hay al menos un número negativo!")
else:
    print("Todos los números son positivos.")

