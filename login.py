import flet as ft
from Clase_persona import Persona

class LoginPage(ft.Column):
    current_user = None
    
    def __init__(self, users: list[Persona], on_submit: any):
        self.users = users
        self.current_user = None
        self.on_submit = on_submit
    
        self.botonEnviar = ft.FilledButton(text="Enviar", on_click=self.enviar)
        self.matriculaInput = ft.TextField(label="Matricula")
        super().__init__(controls=[
                ft.Text("Bienvenido al sistema de centro de computo", size=40),
                self.matriculaInput,
                self.botonEnviar
            ], horizontal_alignment="center")
        
    def enviar(self, e):
        for user in self.users:
            if user.matricula == self.matriculaInput.value:
                self.current_user = user
                print(self.current_user)
                self.on_submit('index')
                return
        self.matriculaInput.value = ''
        self.matriculaInput.error_text = 'Usuario no encontrado'
        self.matriculaInput.page.update()