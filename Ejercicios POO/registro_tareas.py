
class Tarea:
   def __init__(self,descripcion,prioridad,estado,fecha):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = estado
        self.fecha = fecha
   def __str__(self):
        return f"Tarea: {self.descripcion} | Prioridad: {self.prioridad} | Estado: {self.estado} | Fecha: {self.fecha}"
class ListaTareas:
    def __init__(self):
        self.tareas = []
    def agregar_tarea(self,tarea):
        self.tareas.append(tarea)
    def __len__(self):
        return len(self.tareas)
    def __str__(self):
        return "\n".join(str(t) for t in self.tareas)

    
t1 = Tarea("Reunión del trabajo", "Alta", "Pendiente", "20/08/2025")
t2 = Tarea("Reserva de vuelo", "Alta", "Pendiente", "18/08/2025")
t3 = Tarea("Turno medico", "Alta", "Realizado", "16/08/2025")
t4 = Tarea("Ir a la farmacia", "Alta", "Pendiente", "16/08/2025")

lista = ListaTareas()


lista.agregar_tarea(t1)
lista.agregar_tarea(t2)
lista.agregar_tarea(t3)
lista.agregar_tarea(t4)


print("Tareas registradas:")
print(lista)


print(f"\nCantidad total de tareas: {len(lista)}")