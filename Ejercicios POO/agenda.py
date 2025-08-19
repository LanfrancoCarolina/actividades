
class Contacto:
    def __init__(self, nombre, apellido, telefono, direccion, email):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.email = email

    def __str__(self):
        return f"Contacto: {self.nombre} {self.apellido}, Teléfono: {self.telefono}, Dirección: {self.direccion}, Email: {self.email}"
    
    def __setitem__(self, key, value):
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            raise KeyError(f"El atributo '{key}' no existe en Contacto")
        
c1 = Contacto("Ana", "Gómez", "4635652", "Av. Libertad 45", "ana@gmail.com")
print(c1)

c1["nombre"] = "carolina"
# Cambiamos la dirección
c1["direccion"] = "san martin 62"

print(c1)