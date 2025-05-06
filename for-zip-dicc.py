
#La función zip() combina múltiples iterables, emparejando los elementos
#correspondientes a cada uno. Esto permite iterar varios objetos iterables en paralelo.

nombres = ["Yamila","Juan","Gaston","Carolina","Felicia","Irene","Paz"]
edades = [30,54,21,87,25,36,25]
for nombre, edad in zip(nombres,edades):
    print(f"{nombre} tiene {edad} años")
          
# Declaracion for en diccionarios

#for clave in diccionario:
# Itera sobre las claves
 #for valor in diccionario.values():
# Itera sobre los valores
  #for clave, valor in diccionario.items():
# Itera sobre pares clave-valor  

diccionario = {'a': 1, 'b': 2, 'c': 3}
for clave, valor in diccionario.items():
  print(clave, valor) # Imprime pares clave-valor