from abstracts.abstract_view import AbstractView
from .screens import TelaRating

class RatingViews(AbstractView):
    def add_rating(self):
        tela = TelaRating()
        button, data = tela.show()
        tela.close()
        if button is None or button == 'Voltar':
            return None
        elif data['nota'] in ['', ' ', None] or data['comentario'] in ['', ' ', None]:
            self.excecao('Preencha os campos comentário e nota')
        elif type(int(data['nota'])) is not int:
            self.excecao('O campo nota precisa ser um numero inteiro')
        elif button == 'Avaliar':
            return data