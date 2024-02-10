import flet as ft

class LoginPage(ft.Column):
    def __init__(self, on_submit: any):
        self.users = [{
            'matricula': '123456',
        }]
        
        self.on_submit = on_submit
    
        self.botonEnviar = ft.FilledButton(text="Enviar", on_click=self.enviar)
        self.matriculaInput = ft.TextField(label="Matricula")
        super().__init__(controls=[
                ft.Text("Bienvenido al sistema de centro de computo"),
                self.matriculaInput,
                self.botonEnviar
            ], horizontal_alignment="center")
        
    def enviar(self, e):
        for user in self.users:
            if user['matricula'] == self.matriculaInput.value:
                self.on_submit('index')
                return