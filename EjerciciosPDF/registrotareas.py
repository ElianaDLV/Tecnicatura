class Tarea:
    tareas = []

    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.__completada = completada
        Tarea.tareas.append(self)

    def __str__(self):
        estado = "Completada" if self.__completada else "Pendiente"
        return f"Tarea: {self.descripcion} - Estado: {estado}"
    
    def __len__(self):
        return len(Tarea.tareas)
    
tarea1= Tarea("Rollear en discord")
tarea2= Tarea("Leer pdf's pendientes")
tarea3= Tarea("Jugar lol")

print(tarea1)

print(len(tarea1))