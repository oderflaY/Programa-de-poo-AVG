from Clase_persona import Persona

class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,grupo,carrera):
        super().__init__(nombre,edad,sexo)
        self.grupo=grupo
        self.carrera=carrera