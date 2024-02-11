import flet as ft
from almacen import Almacen

class VerInventarioPage(ft.Column):
    def __init__(self, router: any, almacen: Almacen):
        self.router = router
        self.almacen = almacen
        
        content = []
        
        print(almacen.inventario)
        
        self.table = ft.DataTable(columns=[
            ft.DataColumn(ft.Text('Nombre')),
            ft.DataColumn(ft.Text('Tipo')),
            ft.DataColumn(ft.Text('Serie')),
            ft.DataColumn(ft.Text('Fabricante')),
            ft.DataColumn(ft.Text('Modelo')),
            ft.DataColumn(ft.Text('Descripcion')),
            ft.DataColumn(ft.Text('cantidad'), numeric=True),
            ft.DataColumn(ft.Text('actions'))
        ], rows=[])
        
        for equipo in self.almacen.inventario:
            self.table.rows.insert(0, ft.DataRow([
                ft.DataCell(ft.Text(equipo['equipo'].nombre)),
                ft.DataCell(ft.Text(equipo['equipo'].tipo)),
                ft.DataCell(ft.Text(equipo['equipo'].serie)),
                ft.DataCell(ft.Text(equipo['equipo'].fabricante)),
                ft.DataCell(ft.Text(equipo['equipo'].modelo)),
                ft.DataCell(ft.Text(equipo['equipo'].descripcion)),
                ft.DataCell(ft.Text(equipo['cantidad'])),
                ft.DataCell(ft.Row(controls=[
                    ft.FilledButton(text='+'),
                    ft.FilledButton(text='-')
                ]))
            ]))
        
        self.botonAtras = ft.FilledButton(text="Atras", on_click=lambda e: self.router('index'))
        
        super().__init__(controls=[
                ft.Text("Inventario"),
                self.table,
                self.botonAtras
            ], horizontal_alignment="center",)