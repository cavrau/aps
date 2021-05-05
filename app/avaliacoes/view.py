from abstracts.abstract_view import AbstractView
from .screens import TelaRating, TelaShowItens

class RatingViews(AbstractView):
    def add_rating(self):
        tela = TelaRating()
        button, data = tela.show()
        tela.close()
        if button is None or button == 'Voltar':
            return None
        elif data['nota'] in ['', ' ', None] or data['comentario'] in ['', ' ', None]:
            self.excecao('Preencha os campos comentário e nota')
        elif data is not None:
            try:
                _data = int(data['nota'])
                if _data < 0 or _data > 10:
                    self.excecao('O campo nota não pode ser menor que 0 ou maior que 10')
                else:
                    return data
            except ValueError:
                self.excecao('O campo nota precisa ser um inteiro')
    
    def show_itens(self, _list):
        tela = TelaShowItens(_list)
        button, data = tela.show()
        tela.close()
        if button is None or button == 'Voltar':
            return None
        else:
            return button