import flet as ft
from Clase_encargado import Encargado
from Clase_estudiante import Estudiante

class IndexPage(ft.Column):
    def __init__(self, router: any, user: any = None):
        print(type(user))
        
        self.router = router
        super().__init__(controls=[
                ft.Text("Menú del centro de cómputo"),
                ft.FilledButton(text="ver mis peticiones", on_click=self.ver_peticiones),
                ft.FilledButton(text="realizar peticion", on_click=self.realizar_peticion),
            ], horizontal_alignment="center",)
        
    def ver_peticiones(self, e):
        self.router('estudiante/ver-peticiones')
        
    def realizar_peticion(self, e):
        self.router('estudiante/realizar-peticion')