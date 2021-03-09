
from abc import ABC, abstractmethod

class AbstractTela(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def show(self):
        button, value = self.window.Read()
        if button is None:
            self.close()
        return button, value


    def close(self):
        self.window.Close()