from abstracts.abstract_view import AbstractView
from .screens import TelaCriarMeta, TelaDetalhes


class GoalView(AbstractView):

    def create_goal(self, genres): 
        while True:
            tela = TelaCriarMeta(list(genres))
            _, data = tela.show()
            tela.close()
            if _ == 'Voltar':
                return None
            try:
                data['prazo'] = int(data['prazo'])
                data['objetivo'] = int(data['objetivo'])
                assert data['genre'] in genres and data['objetivo'] > 0
            except Exception:
                self.excecao('Tipo invalido de dado inserido. Os valores de prazo e objetivo devem ser números inteiros e maiores que 0.')
            else:
                break
        return data
 

    def show_goal(self, goal): 
        tela = TelaDetalhes(goal)
        _, __ = tela.show()
        tela.close()
