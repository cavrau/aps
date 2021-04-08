from .model import Rating
from .view import RatingViews

class AvaliacaoController:
    def __init__(self):
        self.__avaliacoes_view = RatingViews()

    def add_rating(self):
        data = self.__avaliacoes_view.add_rating()
        rating = Rating(data['comentario'], data['nota'])
        return rating
    
    def get_comment(self, rating: Rating):
        return rating.get_comment()
    
    def get_grade(self, rating: Rating):
        return rating.get_grade()