import requests
import os
from datetime import date, timedelta

class Goal:
    def __init__(self, deadline: int, objective: int, genre: str):
        self.deadline = date.today() + timedelta(days=deadline)
        self.objective = objective
        self.genre = genre
        self.progress = 0