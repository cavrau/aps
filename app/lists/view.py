from abstracts.abstract_view import AbstractView
from .screens import TelaSelecao, TelaDetalhes

class ListsView(AbstractView):
    def select_list(self, lists): 
        tela = TelaSelecao(lists)
        selected, _ = tela.show()
        tela.close()
        return selected

    def list_details(self, _list): 
        tela = TelaDetalhes(_list)
        action, _ = tela.show()
        tela.close()
        return action
 