import os
import pickle
from datetime import date
from . import view
from .model import User

class UserController:
    def __init__(self):
        self.view = view.TelaUsuarios()
        if os.path.isfile('funcionarios.pkl'):
            self.users = pickle.load(open('funcionarios.pkl', 'rb'))
        else: 
            self.users = {}
    
    def registrar(self, username, password):
        if username in self.users.keys():
            return None
        user = User(username, password)
        self.users[username] =  user
        return user

    def autenticar(self, username, password):
        for user in self.users.values():
            if user.username == username and password == user.password:
                return user
        return None

    def login(self):
        invalid = True
        user = None
        while invalid:
            user_dict = self.view.autentica_usuario()
            action = user_dict.pop('action')

            if action == 'Registrar':
                user = self.registrar(**user_dict)
                if not user:
                    self.view.excecao('Já existe um usuário com esse nome.')
                else:
                    invalid = False
            elif action == 'Login':
                user = self.autenticar(**user_dict)
                if not user:
                    self.view.excecao('Não foi encontrado usuário com esse nome e senha.')
                else:
                    invalid = False
            else:
                return
        return user

    def details(self, user):
        self.view.detalhes(user)
        
         

