import flet as ft
from Clase_encargado import Encargado
from Clase_estudiante import Estudiante

class IndexPage(ft.Column):
    def __init__(self, router: any, user: Encargado | Estudiante):
        self.router = router
        
        self.botonSalir = ft.FilledButton(text="Salir", on_click=lambda e: self.router('login'))
        
        if type(user) == Estudiante:
            super().__init__(controls=[
                    ft.Text("Menú del centro de cómputo"),
                    ft.FilledButton(text="ver mis peticiones", on_click=self.ver_peticiones),
                    ft.FilledButton(text="realizar peticion", on_click=self.realizar_peticion),
                    self.botonSalir
                ], horizontal_alignment="center",)
        elif type(user) == Encargado:
            super().__init__(controls=[
                    ft.Text("Panel de control"),
                    ft.FilledButton(text="ver inventario", on_click=lambda e: self.router('encargado/ver-inventario')),
                    ft.FilledButton(text="ver peticiones", on_click=self.realizar_peticion),
                    self.botonSalir
                ], horizontal_alignment="center",)
        else:
            super().__init__(horizontal_alignment="center",)
        
    def ver_peticiones(self, e):
        self.router('estudiante/ver-peticiones')
        
    def realizar_peticion(self, e):
        self.router('estudiante/realizar-peticion')