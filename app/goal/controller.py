import requests
from datetime import date
from .view import GoalView

from .model import Goal
from app.usuario.model import User
from app.lists.model import List

class GoalController:
    def __init__(self):
        self.goal_view = GoalView()

    def goal(self, user: User):
        if user.goal:
            self.goal_view.show_goal(user.goal)
        else:
            genres = []
            for _list in user.lists.values():
                for item in _list.items.values():
                    genres += item.genre 
            genres = set(genres)
            data = self.goal_view.create_goal(genres)
            if not data:
                return
            goal = Goal(data['prazo'], data['objetivo'], data['genre'])
            user.goal = goal
            return

    def check_goal(self, user):
        if user.goal: 
            if user.goal.objective == user.goal.progress:
                self.goal_view.sucesso(f'Meta de ver {user.goal.objective} filmes de {user.goal.genre} com limite {user.goal.deadline} concluida!!')
                user.goal = None
            elif date.today() > user.goal.deadline:
                self.goal_view.excecao(f'Meta de ver {user.goal.objective} filmes de {user.goal.genre} com limite {user.goal.deadline} Falhada. Foram vistos {user.goal.progress}.')
                user.goal = None

