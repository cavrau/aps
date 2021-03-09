from abstracts.abstract_view import AbstractView
from .screens import *
validator = {}

class TelaUsuarios(AbstractView):
    def __init__(self):
        self.__validator = validator

    def autentica_usuario(self):
        tela = TelaAutenticacao()
        botao, user = tela.show()
        print(botao)
        user['action'] = botao
        tela.close()
        return user

    def detalhes(self, func):
       tela = TelaDetalhes(func)
       tela.show()
       tela.close()