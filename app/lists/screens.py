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
                [Text(item.title)]    
            ]
        self.window = Window(f'Detalhes da lista: {_list.title}').layout(
            layout +
            [
                [Button('Voltar'), Button('Remover Item da lista')]
            ]
        )
