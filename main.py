import flet as ft
from almacen import Almacen
from material import Equipo
from Clase_encargado import Encargado
from Clase_estudiante import Estudiante

from login import LoginPage
from index import IndexPage
from realizar_peticion import RealizarPeticion
from ver_adeudos import VerAdeudos

# inicializacion de datos
almacen = Almacen()
almacen.agregar_inventario(Equipo('audifonos', 'periferico', 123456, 'sansun', 'a200', 'gffhgcgfcbvccncvc'))
almacen.agregar_inventario(Equipo('router', 'periferico', 123456, 'sansun', 'a200', 'gffhgcgfcbvccncvc'))
almacen.agregar_inventario(Equipo('lapiz', 'periferico', 123456, 'sansun', 'a200', 'gffhgcgfcbvccncvc'))

usuarios = [
    Estudiante('alfredo', 20, '000001', '2B', 'isw'),
    Encargado('Alejandro', 18, '000002', 'vespertino', 'encargado')
]

# inicializacion de paginas
def main(page: ft.Page):
    page.title = "Main Page"
    
    def router(route: str):
        page.remove_at(0)
        
        if route == 'index':
            page.add(IndexPage(router=router, user=login.current_user))
        elif route == 'estudiante/ver-peticiones':
            page.add(VerAdeudos(router=router, user=login.current_user, almacen=almacen))
        elif route == 'estudiante/realizar-peticion':
            page.add(RealizarPeticion(router=router, almacen=almacen, user=login.current_user))
        else:
            page.add(LoginPage(on_submit=router))
            
        page.update()
        
    login = LoginPage(on_submit=router, users=usuarios)
    
    page.add(login)
    
ft.app(target=main)