from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field # Crear esquemas/plantillas, crear validaciones de datos
from typing import Optional, List # Campo opcional
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middleware.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

# Crear app a nivel de router
movie_router = APIRouter() # Crear instancia de APIRouter



# METODO GET : OBTENER ELEMENTOS 
@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())]) # Depends hace que se ejecute la funcion que esta en la clase JWTBearer
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    # result = db.query(MovieModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# AGREGAR UN PARAMETRO A LA RUTA PARA FILTRAR (por id)
@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie, status_code=200)  # id es el parametro que espera recibir la ruta
def get_movie(id: int = Path(ge= 1, le= 1000)) -> Movie:  # se usa el parametro de la ruta en la funcion y se especifica su tipo de dato (int)
    db = Session()
    result = MovieService(db).get_movie(id)
    # result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'mesagge': 'id not found'})  
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
  
# Busqueda y filtrado con parametros query (categoria)
@movie_router.get('/movies/', tags=['movies'], status_code=200)
def get_movies_by_category(category:str = Query(min_length=5, max_length=20)): # Cuando se colocan parametros en la funcion y no en la ruta es parametro query
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    # result = db.query(MovieModel).filter(MovieModel.category == category).all()
    if result:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=404, content={'mesagge': 'category not found'})
     
# POST : AGREGAR ELEMENTO (DICT)     
@movie_router.post('/movies/', tags=['movies'], status_code=201)
def create_movie(movie: Movie): # Recibe como parametro elemento que es una clase que es de tipo esquema/plantilla (Movie)
    db = Session()
    MovieService(db).create_movie(movie)
    # new_movie = MovieModel(**movie.dict())
    # db.add(new_movie)
    # db.commit()
    # Ya no hace falta agragar la pelicula con esta linea -> movies.append(movie)
    return JSONResponse(status_code=201, content={'message': 'Se ha añadido la película'})

# MODIFICAR/ACTUALIZAR ELEMENTO
@movie_router.put('/movies/{id}', tags=['movies'], status_code=200)
def update_movie(id:int, movie: Movie):
    db = Session()
    result = MovieService(db).get_movie(id)
    if result:
        MovieService(db).update_movie(id, movie)
        return JSONResponse(status_code=200, content={'mesagge': 'se ha modificado la pelicula'})
    return JSONResponse(status_code=404, content={'mesagge': 'id not found'})
    # for item in movies:
    #     if item['id'] == id:
    #         item['title'] = movie.title
    #         item['overview'] = movie.overview
    #         item['year'] = movie.year
    #         item['rating'] = movie.rating
    #         item['category'] = movie.category


# ELIMINAR ELEMENTO
@movie_router.delete('/movies/{id}', tags=['movies'], status_code=200)
def delete_movie(id:int):
    db = Session()
    result = MovieService(db).get_movie(id)
    if result: 
        MovieService(db).delete_movie(id)
        return JSONResponse(status_code=200, content={'mesagge': 'se ha eliminado la pelicula'})
    return JSONResponse(status_code=404, content={'mesagge': 'id not found'})
    # def delete_movie_by_id(id:int): 
    # global movies
    # original_length = len(movies)
    # movies = list(filter(lambda movie:movie['id'] != id, movies))
    # if len(movies) < original_length:  
    #     return movies
    # else:
    #     return {'message': 'id not found'}