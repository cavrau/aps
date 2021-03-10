from .view import ListsView
from app.movie.controller import MovieController

from .model import List

class ListController:
    def __init__(self):
        self.lists_view = ListsView()
        self.movies_controller = MovieController() 
    
    def select_list(self, user):
        title = self.lists_view.select_list(user.lists.values())
        if title != 'Voltar' and title is not None:
            for _list in user.lists.values():
                if _list.title == title:
                    return _list
        return False

    def add_item_to_list(self, item, user):
        _list = self.select_list(user)
        if not _list:
            return
        res = self.lists_view.confirmacao(f'Adicionar item {item.title} a lista {_list.title}')
        if res[0] == 'S':
            _list.add_item(item)
    
    def list_details(self, user):
        _list = self.select_list(user)
        if not _list:
            return
        action = self.lists_view.list_details(_list)
        if action == 'Remover Item da lista':
            self.remove_item_from_list(_list)
        return action
        
    def remove_item_from_list(self, _list: List):
        page = 1
        items = list(_list.items.values())
        invalid = True
        while invalid:
            paginated_list = items[(page-1) * 10 : page*10]
            option = self.movies_controller.select_movie(paginated_list, page)
            if option == 'Próxima Página':
                page+=1
            elif option == 'Página Anterior':
                if page !=1:
                    page -=1
                else:
                    self.lists_view.excecao('Você não pode voltar para a página 0')
            elif option == 'Ok' or option is None:
                return 
            else:
                invalid = False
                for movie in items:
                    if movie.title == option:
                        selected_movie = movie
                        break
                res = self.lists_view.confirmacao(f'Remover item {selected_movie.title} da lista {_list.title}')
                if res[0] == 'S':
                    del _list.items[selected_movie.imdbID]
                return
                