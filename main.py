import flet as ft
from almacen import Almacen
from material import Equipo

from login import LoginPage
from index import IndexPage
from realizar_peticion import RealizarPeticion

almacen = Almacen()
almacen.agregar_inventario(Equipo('audifonos', 'periferico', 123456, 'sansun', 'a200', 'gffhgcgfcbvccncvc'))

def main(page: ft.Page):
    page.title = "Main Page"
    
    def router(route: str):
        page.remove_at(0)
        if route == 'index':
            page.add(index)
        elif route == 'estudiante/ver-peticiones':
            pass
        elif route == 'estudiante/realizar-peticion':
            page.add(realizarPeticion)
        else:
            page.add(LoginPage(on_submit=router))
            
        page.update()
        
    login = LoginPage(on_submit=router)
    index = IndexPage(router=router)
    realizarPeticion = RealizarPeticion(router=router, almacen=almacen)
    
    page.add(login)
    
ft.app(target=main)