from Clase_persona import Persona

class Estudiante(Persona):
    def __init__(self,nombre,edad,matricula, grupo,carrera):
        super().__init__(nombre,edad,matricula)
        self.grupo=grupo
        self.carrera=carrera