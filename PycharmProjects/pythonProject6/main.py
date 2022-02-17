class Persona:

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def saludar(self):
        print("Hola, soy un humano")

    def despedirse(self, nombre="Miarma"):
        print(f"Adios", nombre)

    def __str__(self):
        return f"Persona: {self.nombre} {self.apellidos}"


class Alumno(Persona):

    def despedirse(self):
        print("No me molestes que estoy programando")


p = Persona("Luismi", "Lopez")
a = Alumno("Vicente", "Rufo")
print(a)
a.despedirse()
print(p)
p.despedirse()
