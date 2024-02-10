from material import Equipo
from Clase_encargado import Encargado
from Clase_estudiante import Estudiante
from datetime import date

class almacen:
    inventario = []
    registros = []
    peticiones = []
    
    def __init__(self):
        self.inventario = []
        self.registros = []
        self.peticiones = []

    def agregar_inventario(self, equipo: Equipo, cantidad: int = 1):
        en_inventario = self.buscar_inventario(equipo.nombre)
        if en_inventario != None:
            en_inventario['cantidad'] += cantidad
            return
        
        self.inventario.append({
            'equipo': equipo,
            'cantidad': cantidad
        })
        
    #metodos para manejar el inventario
    def remover_inventario(self, equipo: Equipo, cantidad: int = 1):
        self.agregar_inventario(equipo, -cantidad)
        
    def buscar_inventario(self, nombre: str):
        for equipo in self.inventario:
            if equipo['equipo'].nombre == nombre:
                return equipo
        return None
    
    #metodos para manejar los registros
    def agregar_registro(self, peticionID: int, encargado: Encargado):
        self.peticiones[peticionID]['aprovada'] = True
        self.registros.append({
            'petición': self.peticiones[peticionID],
            'encargado': encargado,
            'fecha': date.now()
        })
        
    def buscar_registro(self, nombre: str):
        registros = []
        for id, registro in enumerate(self.registros):
            if registro['persona'].nombre == nombre or registro['persona'].matricula == nombre:
                registros.append((id, registro))
        return registros
    
    def obtener_registro(self, id: int):
        return self.registros[id]
    
    #metodos para manejar las peticiones
    def agregar_peticion(self, equipo: Equipo, cantidad: int, persona: Estudiante):
        self.peticiones.append({
            'equipo': equipo,
            'cantidad': cantidad,
            'persona': persona,
            'aprovada': False,
            'fecha': date.now()
        })
        
    def buscar_peticion(self, nombre: str):
        peticiones = []
        for id, peticion in enumerate(self.peticiones):
            if (peticion['persona'].nombre == nombre or peticion['persona'].matricula == nombre) and not peticion['aprovada']:
                peticiones.append((id, peticion))
        return peticiones
    
    def obtener_peticion(self, id: int):
        return self.peticiones[id]