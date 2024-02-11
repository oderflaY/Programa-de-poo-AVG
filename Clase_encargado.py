from Clase_persona import Persona

class Encargado(Persona):
        def __init__(self,nombre,edad, matricula, turno,puesto):
            super().__init__(nombre,edad,matricula)
            self.Turno=turno
            self.puesto=puesto