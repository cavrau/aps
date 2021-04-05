from abstracts.abstract_view import AbstractView
from .screens import TelaSelecao, TelaDetalhes, TelaMenu, TelaCriacao, TelaEdicao

class ListsView(AbstractView):
    def select_list(self, lists): 
        tela = TelaSelecao(lists)
        selected, _ = tela.show()
        tela.close()
        return selected

    def menu(self): 
        tela = TelaMenu()
        selected, _ = tela.show()
        tela.close()
        return selected

    def list_details(self, _list): 
        tela = TelaDetalhes(_list)
        action, _ = tela.show()
        tela.close()
        return action
 
    def create_list(self): 
        while True:
            tela = TelaCriacao()
            button, data = tela.show()
            tela.close()
            if button is None or button == 'Voltar':
                return None
            elif data['title'] in ['', ' ', None]: 
                self.excecao('Preencha o campo Título')
            else:
                return data 

    def edit_list(self, _list):
        tela = TelaEdicao()
        button, data = tela.show()
        tela.close()
        if button is None or button == 'Voltar':
            return None
        elif button == 'Atualizar':
            return data