import flet as ft
from login import LoginPage
from index import IndexPage

def main(page: ft.Page):
    page.title = "Main Page"
    
    def router(route: str):
        page.remove_at(0)
        if route == 'index':
            page.add(index)
        elif route == 'estudiante/ver-peticiones':
            pass
        elif route == 'estudiante/realizar-peticion':
            pass
        else:
            page.add(LoginPage(on_submit=router))
            
        page.update()
        
    login = LoginPage(on_submit=router)
    index = IndexPage(router=router)
    page.add(login)
    
ft.app(target=main)