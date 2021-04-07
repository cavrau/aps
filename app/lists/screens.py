from abstracts.abstract_tela import AbstractTela
from PySimpleGUI import Window, Text, Button, Input, Image as ImageField
from .model import List

class TelaSelecao(AbstractTela):
    def __init__(self, lists):
        layout = [ [Button(_list.title)] for _list in lists]
        self.window = Window('Seleção de lista').layout(
            layout +
            [
                [Button('Voltar')]
            ]
        )

class TelaMenu(AbstractTela):
    def __init__(self):
        self.window = Window('Seleção de lista').layout(
            [
                [Text('O que você deseja fazer?')],
                [Text('Gerenciar Listas'), Button('1')],
                [Text('Criar nova Lista'), Button("2")],
            ]
        )

class TelaDetalhes(AbstractTela):
    def __init__(self, _list: List):
        layout = [
            [Text(f'Título: {_list.title}')],
            [Text(f'Descrição: {_list.description}')],
            [Text(f'Created: {_list.created}')],
            [Text('Items: ')]
        ]
        for item in _list.items.values():
            layout += [
                [Text(f'Título: {item.title}')],
                [Text(f'Comentário: {item.comentario}')],
                [Text(f'Nota: {item.nota}')]    
            ]
        self.window = Window(f'Detalhes da lista: {_list.title}').layout(
            layout +
            [
                [Button('Voltar'), Button('Remover Item da lista'), Button('Deletar lista'), Button('Editar lista')]
            ]
        )


class TelaCriacao(AbstractTela):
    def __init__(self):
        self.window = Window('Criação de lista').layout(
            [
                [Text('Titulo: '), Input(key='title')],
                [Text('Descrição: '), Input(key='description')],
                [Button('Voltar'), Button('Cadastrar')]
            ]
        )

class TelaEdicao(AbstractTela):
    def __init__(self):
        self.window = Window('Edição de lista').layout(
            [
                [Text('Novo titulo: '), Input(key='title')],
                [Button('Atualizar'), Button('Voltar')]
            ]
        )