from models.movie import Movie as MovieModel
from schemas.movie import Movie

class MovieService():

    # Cada vez q se llama a este servicio se le envie una sesion a la base de datos
    def __init__(self, db) -> None:  # Metodo constructor
        self.db = db 

    # Creacion de metodo
    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result

    # Creacion de metodo
    def get_movie(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result

    # Creacion de metodo
    def get_movies_by_category(self, category):
        result = self.db.query(MovieModel).filter(MovieModel.category == category).first()
        return result

    # Creacion de metodo
    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return 

    # Creacion de metodo
    def update_movie(self, id: int, data: Movie):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating 
        movie.category = data.category
        self.db.commit()
        return

    # Creacion de metodo
    def delete_movie(self, id: int):
        self.db.query(MovieModel).filter(MovieModel.id == id).delete()
        self.db.commit()
        return