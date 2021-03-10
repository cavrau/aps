from PySimpleGUI import Window, Text, Input, Button
from abstracts.abstract_tela import AbstractTela

class TelaAutenticacao(AbstractTela):
    def __init__(self):
        self.window = Window('Autenticação de Usuário').layout(
            [
                [Text('Usuário: '), Input(key='username')],
                [Text('Senha: '), Input(key='password')],
                [Button('Registrar'), Button('Login')]
            ]
        )
        

class TelaDetalhes(AbstractTela):
    def __init__(self, user):
        self.window = Window('Autenticação de Usuário').layout(
            [
                [Text(f'Usuário: {user.username}')],
                [Text(f'Senha: {user.password}')],
                [Text(f'Data inserção: {user.date}')],
                [Button('Ok')]
            ]
        )
        
