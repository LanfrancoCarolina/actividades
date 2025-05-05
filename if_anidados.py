
numero_1 = 10
numero_2 = 25
numero_3 = 8

# Utilizando if anidados
if numero_1 > numero_2:
  if numero_1 > numero_3:
    print(f"El mayor de los tres números es: {numero_1}")
  else:
    print(f"El mayor de los tres números es: {numero_3}")
else:
 if numero_2 > numero_3:
     print(f"El mayor de los tres números es: {numero_2}")
 else:
   print(f"El mayor de los tres números es: {numero_3}")

#Asi lo hice yo en un principio pero no estaban anidados
if numero_1 > numero_2:
 print(f"El mayor de los dos números es: {numero_1}")
elif numero_1 > numero_3:
 print(f"El mayor de los numeros es {numero_1}")
elif numero_3 > numero_2 > numero_1:
 print(f"El numero mayor es el numero {numero_3}")
else:
 print(f"El mayor de los dos números es: {numero_2}")


#Usando comparadores logicos
 if (numero_1 >= numero_2) and (numero_1 >= numero_3):
    mayor = numero_1
 elif (numero_2 >= numero_1) and (numero_2 >= numero_3):
    mayor = numero_2
 else:
    mayor = numero_3

print(f"El mayor de los tres números es: {mayor}")