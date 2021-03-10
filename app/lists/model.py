from datetime import date
import uuid
class List:
    def __init__(self, title, description):
        self.items = {}
        self.created = date.today()
        self.title = title
        self.description = description
        self._id = uuid.uuid4()
    
    def add_item(self, item):
        self.items[item.imdbID] = item
