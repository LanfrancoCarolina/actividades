
#Docstrings: Son comentarios que se utilizan para documentar módulos, clases y
#funciones. Utilizan triples comillas y son accesibles con la función help().

#Hay dos formas de acceder al contenido de un docstring:

#1. Usando la función help()
#Esto muestra la documentación de la función de una manera detallada y organizada:


def funcion_ejemplo():
    """Esto es un docstring.
    Describe el propósito de la función y sus parámetros."""
    pass

help(funcion_ejemplo)

#2. Accediendo directamente con .__doc__
#Esto es más directo y simplemente imprime el contenido del docstring como una cadena:

print(funcion_ejemplo.__doc__)
