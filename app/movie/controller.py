import requests
from .view import MovieView

from .model import Movie, Series

class MovieController:
    def __init__(self):
        self.movie_view = MovieView()

    def select_movie(self, movies, page):
        return self.movie_view.select_movie(movies, page)


    def search_movie(self):
        invalid = True
        page = 1
        item = None
        while invalid:
            title= self.movie_view.search_movie()
            while item is None:
                url = f'https://www.omdbapi.com/?s={title}&apikey=d4f67e2e&page={page}'
                res = requests.get(url)
                movies = res.json()['Search'] if 'Search' in res.json().keys() else []
                option = self.select_movie(movies, page)
                if option == 'Próxima Página':
                    page+=1
                elif option == 'Página Anterior':
                    if page !=1:
                        page -=1
                    else:
                        self.movie_view.excecao('Você não pode voltar para a página 0')
                elif option == 'Ok' or option is None:
                    return 
                else:
                    invalid = False
                    for movie in movies:
                        if movie.get('Title') == option:
                            selected_movie = movie
                            break
                    _id = selected_movie.get('imdbID')
                    movie_info = requests.get(f'http://www.omdbapi.com/?i={_id}&&apikey=d4f67e2e')
                    if movie_info.json().get('Type')== 'movie':
                        item = Movie(**movie_info.json())
                    elif movie_info.json().get('Type')== 'series':
                        item = Series(**movie_info.json())
                    return item
    
    def movie_details(self, movie: Movie):
        action = self.movie_view.movie_details(movie)
        if action == 'Adicionar a Lista':
            return True
        return 
