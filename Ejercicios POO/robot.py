# Herencia hibrida: Para que sea una herencia hibrida si o si se tiene que combinar una herencia multiple con una herencia multinivel o
#jerarquica. Pero si o si tiene que estar el factor herencia multiple. 
class Maquina:
    def __init__(self, marca):
        self.marca = marca
    def encender(self):
        return f"La máquina de marca {self.marca} se ha encendido."

class Robot(Maquina):
    def __init__(self, marca, tipo, nombre):
        super().__init__(marca)
        self.tipo = tipo
        self.nombre = nombre
    def saludar(self):
        return f"Soy {self.nombre}, un robot de tipo {self.tipo}. ¡Hola!"

class Sensores:
    def __init__(self, sensores_disponibles):
        self.sensores_disponibles = sensores_disponibles
    def mostrar_sensores(self):
        return f"Sensores disponibles: {', '.join(self.sensores_disponibles)}"

class Herramientas:
    def __init__(self, herramientas_disponibles):
        self.herramientas_disponibles = herramientas_disponibles
    def mostrar_herramientas(self):
        return f"Herramientas disponibles: {', '.join(self.herramientas_disponibles)}"

# RobotExplorador: herencia múltiple (Robot + Sensores)
class RobotExplorador(Robot, Sensores):
    def __init__(self, marca, tipo, nombre, sensores_disponibles):
        Robot.__init__(self, marca, tipo, nombre)
        Sensores.__init__(self, sensores_disponibles)
    def explorar(self):
        return f"{self.nombre} está explorando usando sus sensores."

# RobotCocinero: herencia múltiple (Robot + Herramientas)
class RobotCocinero(Robot, Herramientas):
    def __init__(self, marca, tipo, nombre, herramientas_disponibles):
        Robot.__init__(self, marca, tipo, nombre)
        Herramientas.__init__(self, herramientas_disponibles)
    def cocinar(self):
        return f"{self.nombre} está preparando una deliciosa comida."

# RobotInteligente: herencia multinivel (Robot → RobotInteligente)
class RobotInteligente(Robot):
    def __init__(self, marca, tipo, nombre, nivel_inteligencia):
        super().__init__(marca, tipo, nombre)
        self.nivel_inteligencia = nivel_inteligencia
    def tomar_decision(self):
        return f"{self.nombre} está tomando una decisión de nivel {self.nivel_inteligencia}."

# --- Ejemplo de uso ---
explorador = RobotExplorador("AI Tech", "Explorador", "Rover", ["cámara", "luz infrarroja"])
cocinero = RobotCocinero("AI Tech", "Cocinero", "ChefBot", ["hornalla", "batidora"])
inteligente = RobotInteligente("AI Tech", "Android", "Brainy", 5)

print(explorador.encender())
print(explorador.saludar())
print(explorador.mostrar_sensores())
print(explorador.explorar())

print(cocinero.encender())
print(cocinero.saludar())
print(cocinero.mostrar_herramientas())
print(cocinero.cocinar())

print(inteligente.encender())
print(inteligente.saludar())
print(inteligente.tomar_decision())