from datetime import date
from app.lists.model import List


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.date = date.today()
        self.lists = {}
        self.points = 0
        self.rankings = {}
        self.goal = None
        self.add_list(
            List('Para assistir', 'Filmes/Séries que ainda tenho que assistir'))
        self.add_list(List('Os melhores Filmes',
                           'Os melhores filmes que já assisti'))
        self.add_list(List('Já assistidos', 'Filmes/Séries que eu já assisti'))

    def add_list(self, _list):
        self.lists[_list._id] = _list

    def get_senha(self):
        return self.password

    def set_senha(self, new_password):
        self.password = new_password
