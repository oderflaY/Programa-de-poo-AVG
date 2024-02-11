import flet as ft
from almacen import Almacen
from Clase_encargado import Encargado
from Clase_estudiante import Estudiante

class RealizarPeticion(ft.Column):
    def __init__(self, router: any, user: Estudiante | Encargado, almacen: Almacen = None):
        print(almacen.peticiones)
        self.router = router
        self.user = user
        self.almacen = almacen
        
        self.dropdown = ft.Dropdown(label="Equipo")
        for equipo in almacen.inventario:
            self.dropdown.options.append(ft.dropdown.Option(equipo['equipo'].nombre))
            
        self.cantidadInput = ft.TextField(label="Cantidad",)
        self.botonEnviar = ft.FilledButton(text="Enviar", on_click=self.enviar)
        self.botonAtras = ft.FilledButton(text="Atras", on_click=lambda e: self.router('index'))
        
        super().__init__(controls=[
                ft.Text("Realizar petición"),
                self.dropdown,
                self.cantidadInput,
                self.botonEnviar,
                self.botonAtras
            ], horizontal_alignment="center",)
        
    def enviar(self, e):
        self.almacen.agregar_peticion(self.almacen.buscar_inventario(self.dropdown.value)['equipo'], int(self.cantidadInput.value), self.user);

        print(self.almacen.peticiones)