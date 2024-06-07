class Persona:
    def __init__(self,
                 nombre,
                 edad):
        self.nombre = nombre
        self.edad = edad

    def datosPersona(self):
        print(self.nombre, self.edad)

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def gradoEstudiante(self):
        print(self.grado)

estu = Estudiante("Nicolas", "24", "1ro")

estu.datosPersona()
estu.gradoEstudiante()