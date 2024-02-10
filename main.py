import flet as ft
from login import LoginPage

def main(page: ft.Page):
    page.title = "Main Page"
    
    def router(route: str):
        page.remove_at(0)
        if route == 'index':
            page.add(ft.Text("Index"))
        else:
            page.add(LoginPage(on_submit=router))
            
        page.update()
    
    page.add(LoginPage(on_submit=router))
    
ft.app(target=main)