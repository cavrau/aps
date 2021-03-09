from .telas.telaExcecao import TelaExcecao
from .telas.telaConfirmacao import telaConfirmacao
from .telas.telaSucesso import telaSucesso

class AbstractView():
    def excecao(self, message):
        tela = TelaExcecao(message)
        tela.show()
        tela.close()

    def sucesso(self, message):
        tela = telaSucesso(message)
        tela.show()
        tela.close()

    def confirmacao(self, acao):
        tela = telaConfirmacao(acao)
        resposta = tela.show()
        tela.close()
        return resposta
