import PySimpleGUI as sg
from abstracts.abstract_tela import AbstractTela

class telaSucesso(AbstractTela):
    def __init__(self, acao):
        layout = [
            [sg.Text('Ação concluida com sucesso:')],
            [sg.Text(acao)],
            [sg.Button('Voltar')]
        ]
        self.window = sg.Window('Ação concluida').layout(layout)