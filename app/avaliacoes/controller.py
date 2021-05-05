from .model import Rating
from .view import RatingViews
from app.lists.controller import ListController
from app.movie.model import Movie, Series

class RatingController:
    def __init__(self):
        self.__avaliacoes_view = RatingViews()
        self.__list_controller = ListController()

    def add_rating(self, user):
        _list = self.__list_controller.select_list(user)
        if _list is False:
            return
        _item = self.select_item(_list)
        if _item is None:
            return
        data = self.__avaliacoes_view.add_rating()
        if data is None:
            return
        else:
            rating = Rating(data['comentario'], data['nota'])
            _item.set_rating(rating)

    def select_item(self, _list):
        title = self.__avaliacoes_view.show_itens(_list)
        if title != 'Voltar' and title is not None:
            for item in _list.items.values():
                if item.title == title:
                    return item
        return None