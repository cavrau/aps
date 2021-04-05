from .model import Rating
from .view import RatingViews

class classificacaoController:
    def __init__(self):
        self.__avaliacoes_view = AvaliacoesView()

    def add_rating(self):
        user_rate = self.__avaliacoes_view.add_rating()
        rating = Rating(user_rate[comentario], user_rate[nota])
        return rating
    
    def get_comment(self, rating: Rating):
        return rating.get_comment()
    
    def get_grade(self, rating: Rating):
        return rating.get_grade()