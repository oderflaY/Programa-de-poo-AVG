from Clase_persona import Persona

class Encargado(Persona):
        def __init__(self,nombre,edad,sexo,turno,puesto):
            super().__init__(nombre,edad,sexo)
            self.Turno=turno
            self.puesto=puesto