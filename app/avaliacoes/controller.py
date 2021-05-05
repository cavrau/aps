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
        _item = self.select_item(_list)
        print(type(_item))
        print(_item)
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
                print(item.title)
                print(title)
                if item.title == title:
                    return item
        return False