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
        self.window = Window('Minha conta').layout(
            [
                [Text(f'Usuário: {user.username}')],
                [Text(f'Senha: {user.password}')],
                [Text(f'Data inserção: {user.date}')],
                [Button('Alterar senha')],
                [Button('Voltar'), Button('Trocar Conta'), Button('Excluir')]
            ]
        )


class TelaAlterarSenha(AbstractTela):
    def __init__(self, user):
        self.window = Window('Alterar senha').layout(
            [
                [Text(f'Senha atual: '), Input(key='old_password')],
                [Text('Nova senha: '), Input(key='password')],
                [Button('Voltar'), Button('Confirmar')]
            ]
        )
