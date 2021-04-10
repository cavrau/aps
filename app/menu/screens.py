from PySimpleGUI import *
from abstracts.abstract_tela import AbstractTela

class MenuScreen(AbstractTela):
    def __init__(self):
        layout = [
            [Text('O que você quer fazer?')],
            [Text('Detalhes do usuário'), Button('0')],
            [Text('Pesquisar filme'), Button('1')],
            [Text('Ver listas'), Button('2')],
            [Text('Ver meta'), Button('3')],
            [Button('Sair')]
        ]
        self.window = Window('Cinefilia').Layout(layout)
