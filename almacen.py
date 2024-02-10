from material import Equipo

class almacen:
    inventario = []
    registros = []
    peticiones = []
    
    def __init__(self):
        self.inventario = []
        self.registros = []
        self.peticiones = []

    def add_inventario(self, equipo: Equipo):
        self.inventario.append(equipo)