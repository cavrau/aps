from datetime import date
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.date = date.today()
        self.lists = {}