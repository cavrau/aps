import os
import pickle
from datetime import date
from . import view
from .model import User


class UserController:
    def __init__(self):
        self.view = view.TelaUsuarios()
        if os.path.isfile('usuarios.pkl'):
            self.users = pickle.load(open('usuarios.pkl', 'rb'))
        else:
            self.users = {}

    def save_users(self):
        pickle.dump(self.users, open('usuarios.pkl', 'wb'))

    def registrar(self, username, password):
        if not username or not password or username in self.users.keys():
            return None
        user = User(username, password)
        self.users[username] = user
        self.save_users()
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
                    self.view.excecao('Usuário já existente ou inválido.')
                else:
                    invalid = False
            elif action == 'Login':
                user = self.autenticar(**user_dict)
                if not user:
                    self.view.excecao(
                        'Não foi encontrado usuário com esse nome e senha.')
                else:
                    invalid = False
            else:
                return
        return user

    def excluir(self, user):
        if not user.username in self.users.keys():
            return None
        self.users.pop(user.username)
        self.save_users()
        return True

    def alterar_senha(self, user, nova_senha, senha_antiga):
        if not user.username in self.users.keys():
            return None
        user = self.users[user.username]
        if senha_antiga != user.get_senha():
            return None
        user.set_senha(nova_senha)

        self.save_users()
        return True

    # usar return retornar_ao_login(), usado pra quebrar o loop da tela e resetar a aplicação pro estado inicial
    def retornar_ao_login(self):
        return True

    def details(self, user):
        invalid = True
        while invalid:
            action = self.view.detalhes(user)
            if action == 'Excluir':
                result = self.excluir(user)
                if not result:
                    self.view.excecao(
                        'Não foi possível realizar a exclusão.')
                else:
                    return self.retornar_ao_login()
            elif action == 'Trocar Conta':
                return self.retornar_ao_login()
            elif action == 'Alterar senha':
                nova_senha, senha_antiga = self.view.alterar_senha(user)
                result = self.alterar_senha(user, nova_senha, senha_antiga)
                if not result:
                    self.view.excecao(
                        'Não foi possível alterar a senha.')
            else:
                return
