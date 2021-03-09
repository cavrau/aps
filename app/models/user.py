from datetime import date

class UserManager:
    def __init__():
        self.users = []
        
    def add(self, username, password):
        for user in self.users:
            if user.username == username:
                raise Exception()
        self.users.append(User(username, password))

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.date = date.today()
