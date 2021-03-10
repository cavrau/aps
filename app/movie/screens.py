from abstracts.abstract_tela import AbstractTela
from PySimpleGUI import Window, Text, Button, Input, Image as ImageField
import io
from PIL import Image, ImageTk
from .model import Movie, Series

class TelaPesquisa(AbstractTela):
    def __init__(self):
        self.window = Window('Pesquisa de filme').layout(
            [
                [Text('Pesquise aqui um filme/série:')],
                [Input(key='title')],
                [Button('Pesquisar')]
            ]
        )

class TelaSelecao(AbstractTela):
    def __init__(self, movies, page):
        if len(movies) == 0 :
            layout = [
                [Text('Não há filmes')],
                [Button('Página Anterior' if page != 1 else 'Ok')] 
            ]
        else:
            layout =  [[Button(movie.get('Title')) if isinstance(movie, dict) else Button(movie.title)] for movie in movies]
            layout += [
                [Button('Página Anterior'), Button('Próxima Página')] if page != 0 else [Button('Próxima Página')]
            ]
        self.window = Window('Selecionar Filme').layout(
            layout
        )
    
class TelaDetalhes(AbstractTela):
    def __init__(self, movie):
        image = Image.open(movie.poster)
        image.thumbnail((400, 400))
        bio = io.BytesIO()
        image.save(bio, format="GIF")
        if isinstance(movie, Movie):
            self.window = Window(f'Filme : {movie.title}').layout(
                [
                    [ImageField(data=bio.getvalue())],
                    [Text(movie.title), Text(movie.year)],
                    [Text('Genres:')],
                    [Text(', '.join(movie.genre))],
                    [Text('Actors:')],
                    [Text(', '.join(movie.actors))],
                    [Text('Plot:  ' + movie.plot)],
                    [Text('Awards:  ' + movie.awards)],
                    [Text('Director: '), Text(movie.director)],
                    [Text('Writer: '), Text(movie.writer)],
                    [Button('Voltar'), Button('Adicionar a Lista')]
                ]
            )