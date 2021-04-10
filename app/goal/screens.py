from abstracts.abstract_tela import AbstractTela
from PySimpleGUI import Window, Text, Button, Input, Combo

class TelaCriarMeta(AbstractTela):
    def __init__(self, genres):
        self.window = Window('Criar meta').layout(
            [
                [Text('Prazo: '), Input(key='prazo'), Text(' dias')],
                [Text('Objetivo: '), Input(key='objetivo'), Text(' obras')],
                [Text('Genero: '), Combo(genres, key='genre')],
                [Button('Voltar'), Button('Criar meta')]
            ]
        )

class TelaDetalhes(AbstractTela):
    def __init__(self, goal):
        self.window = Window('Detalhes meta').layout(
            [
                [Text(f'Prazo: {goal.deadline}')],
                [Text(f'Objetivo: {goal.objective}')],
                [Text(f'Genero: {goal.genre}')],
                [Button('Voltar')]
            ]
        )
