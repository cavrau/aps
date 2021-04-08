import requests
import os

class Movie:
    def __init__(self, Title, Runtime, Year, imdbID, Poster, Genre, Director, Writer, Actors, Plot, Awards, imdbRating, imdbVotes, **kwargs):
        self.title = Title
        self.year = Year
        self.imdbID = imdbID
        r = requests.get(Poster)
        if not os.path.exists(f'database/posters/{imdbID}.jpg'):
            with open(f'database/posters/{imdbID}.jpg', 'wb') as _file:
                _file.write(r.content)
        self.poster = f'database/posters/{imdbID}.jpg'
        self.genre = Genre.split(', ')
        self.director = Director
        self.writer = Writer
        self.actors = Actors.split(', ')
        self.plot = Plot
        self.awards = Awards
        self.imdb_rating = imdbRating
        self.imdb_votes = imdbVotes
        self.runtime = Runtime
        for i in range(0, len(self.plot), 75):
            if i!= 0:
                index = i
                letter = self.plot[i]
                while letter != ' ':
                    index += 1
                    if index < len(self.plot):
                        letter = self.plot[index]  
                    else:
                        return
                self.plot = self.plot[:index] + '\n' + self.plot[index+1:]
        self.nota = 0
        self.comentario = ''

    def set_nota(self, nota):
        self.nota = nota
        
    def set_comentario(self, comentario):
        self.comentario = comentario

class Series(Movie):
    def __init__(self, totalSeasons, *args, **kwargs):
        self.total_seasons = totalSeasons
        super(Series, self).__init__(*args, **kwargs)

