import flet as ft
from almacen import Almacen

class RealizarPeticion(ft.Column):
    def __init__(self, router: any, user: any = None, almacen: Almacen = None):
        self.router = router
        
        self.dropdown = ft.Dropdown(label="Equipo")
        for equipo in almacen.inventario:
            self.dropdown.options.append(ft.dropdown.Option(equipo['equipo'].nombre))
            
        super().__init__(controls=[
                ft.Text("Realizar petición"),
                self.dropdown
            ], horizontal_alignment="center",)