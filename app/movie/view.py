from abstracts.abstract_view import AbstractView
from .screens import TelaPesquisa, TelaSelecao, TelaDetalhes
class MovieView(AbstractView):
    def search_movie(self): 
        tela = TelaPesquisa()
        _, title = tela.show()
        tela.close()
        return title['title']
    
    def select_movie(self, movies, page):
        tela = TelaSelecao(movies, page)
        movie, _ = tela.show()
        tela.close()
        return movie
    
    def movie_details(self, movie):
        tela = TelaDetalhes(movie)
        res, _ = tela.show()
        tela.close()
        return res
