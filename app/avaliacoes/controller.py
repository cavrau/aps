from .model import Rating
from .view import RatingViews

class AvaliacaoController:
    def __init__(self):
        self.__avaliacoes_view = RatingViews()

    def add_rating(self):
        data = self.__avaliacoes_view.add_rating()
        if data is None:
            return
        else:
            return Rating(data['comentario'], data['nota'])
