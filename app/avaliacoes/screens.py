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