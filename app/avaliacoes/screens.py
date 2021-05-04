from abstracts.abstract_tela import AbstractTela
from PySimpleGUI import Window, Text, Button, Input
from .model import Rating

class TelaRating(AbstractTela):
    def __init__(self):
        self.window = Window('Avaliação de filme').layout(
            [
                [Text('Nota'), Input(key='nota')],
                [Text('Comentário'), Input(key='comentario')],
                [Button('Voltar'), Button('Avaliar')]
            ]
        )

class TelaShowItens(AbstractTela):
    def __init__(self, _list):
        layout = []
        for item in _list.items.values():
            layout += [
                [Button(f'{item.title}')],
            ]
        self.window = Window('Selecione um item').layout(
            layout +
            [
                [Button('Voltar')]
            ]
        )