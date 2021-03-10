from .screens import MenuScreen

class MenuView():
    def menu_switch(self):
        tela = MenuScreen()
        value, _ = tela.show()
        tela.close()
        return value
