import flet as ft
from almacen import Almacen
from Clase_encargado import Encargado

class VerPeticionesPage(ft.Column):
    def __init__(self, router: any, almacen: Almacen, user: Encargado):
        self.router = router
        self.almacen = almacen
        
        self.table = ft.DataTable(columns=[
            ft.DataColumn(ft.Text('ID')),
            ft.DataColumn(ft.Text('usuario')),
            ft.DataColumn(ft.Text('Matricula')),
            ft.DataColumn(ft.Text('petición')),
            ft.DataColumn(ft.Text('cantidad')),
            ft.DataColumn(ft.Text('Fecha')),
            ft.DataColumn(ft.Text('actions'))
        ], rows=[])
        
        for id, peticion in self.almacen.obtener_peticiones():
            self.table.rows.insert(0, ft.DataRow([
                ft.DataCell(ft.Text(id)),
                ft.DataCell(ft.Text(peticion['persona'].nombre)),
                ft.DataCell(ft.Text(peticion['persona'].matricula)),
                ft.DataCell(ft.Text(peticion['equipo'].nombre)),
                ft.DataCell(ft.Text(peticion['cantidad'])),
                ft.DataCell(ft.Text(peticion['fecha'])),
                ft.DataCell(ft.Row(controls=[
                    ft.FilledButton(text='✅', on_click=lambda e: self.actualizar_tabla(id, user)),
                ]))
            ]))
        
        self.botonAtras = ft.FilledButton(text="Atras", on_click=lambda e: self.router('index'))
        
        super().__init__(controls=[
                ft.Text("Inventario"),
                self.table,
                self.botonAtras
            ], horizontal_alignment="center",)
        
    def actualizar_tabla(self, id: int, encargado: Encargado):
        self.almacen.agregar_registro(id, encargado)
        self.table.rows = []
        for id, peticion in self.almacen.obtener_peticiones():
            self.table.rows.insert(0, ft.DataRow([
                ft.DataCell(ft.Text(id)),
                ft.DataCell(ft.Text(peticion['persona'].nombre)),
                ft.DataCell(ft.Text(peticion['persona'].matricula)),
                ft.DataCell(ft.Text(peticion['equipo'].nombre)),
                ft.DataCell(ft.Text(peticion['cantidad'])),
                ft.DataCell(ft.Text(peticion['fecha'])),
                ft.DataCell(ft.Row(controls=[
                    ft.FilledButton(text='✅', on_click=lambda e: self.almacen.agregar_registro(id, self.almacen.encargado)),
                ]))
            ]))
        self.table.update()