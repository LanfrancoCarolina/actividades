#Las f-strings (o "formatted string literals") son una forma de formatear cadenas de texto
#Se escriben anteponiendo una f o F antes de las comillas de la cadena, y dentro del texto puedes insertar variables entre llaves {}.
#Formatear cadenas → Es insertar variables o valores dentro de una cadena de texto.
#Son más legibles.
#Te permiten incluir directamente variables o expresiones.
# #Son más rápidas que otros métodos de formateo (como format() o concatenación).
#Aceptan expresiones complejas, no solo variables.

# Usando f-string

nombre = "Ana"
edad = 25

mensaje = f"Hola, me llamo {nombre} y tengo {edad} años."
print(mensaje)

#Usando format():

mensaje = "Hola, me llamo {} y tengo {} años.".format(nombre, edad)

#Concatenando cadenas:

mensaje = "Hola, me llamo " + nombre + " y tengo " + str(edad) + " años."

