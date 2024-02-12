import flet as ft
from datetime import date
from Clase_encargado import Encargado
from Clase_estudiante import Estudiante
from almacen import Almacen

class VerAdeudos(ft.Column):
    def __init__(self, router: any, user: Encargado | Estudiante, almacen: Almacen):
        self.router = router
        self.user = user
        self.almacen = almacen
        
        self.adeudos = ft.Row(wrap=True)
        for i, adeudo in self.almacen.buscar_registro(self.user.nombre):
            tiempo = (adeudo['fecha'] - date.today()).days
            self.adeudos.controls.append(ft.Card(content=ft.Column(controls=[
                ft.Text(adeudo['peticion']['equipo'].nombre),
                ft.Text(adeudo['peticion']['cantidad']),
                ft.Text(f'id: {i}'),
                ft.Text(f"hace {tiempo} dias"),
            ]),
            width=300,))
            if tiempo > 3:
                self.adeudos.controls[-1].content.controls.append(ft.Text(f'{tiempo} días atrasados, se debe pagar: {(tiempo * 20)}', color="red"))
            
        self.botonAtras = ft.FilledButton(text="Atras", on_click=lambda e: self.router('index'))
            
        super().__init__(controls=[
                ft.Text("Adeudos"),
                self.adeudos,
                self.botonAtras
            ], horizontal_alignment="center",)
        