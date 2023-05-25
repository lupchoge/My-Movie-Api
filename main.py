from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middleware.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router
 

# CREACION DE LA APLICACION
app = FastAPI()  # Crear instancia de fastapi
app.title = "Mi app con fastAPI"  # Cambiar titulo
app.version = '0.0.1'  # Cambiar version

# añadir middleware para que detecte errores
app.add_middleware(ErrorHandler)

app.include_router(movie_router)

app.include_router(user_router)

#Crear base de datos visible para vscode
Base.metadata.create_all(bind=engine) 


movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'       
    },
    {
        'id': 2,
        'title': 'Boogie el aceitoso',
        'overview': "Es un ex militar a quien la guerra le causo un amor por la sangre y ...",
        'year': '2020',
        'rating': 8.8,
        'category': 'Acción' 
    },
    {
        'id': 3,
        'title': 'Boogie el aceitoso',
        'overview': "Es un ex militar a quien la guerra le causo un amor por la sangre y ...",
        'year': '2020',
        'rating': 8.8,
        'category': 'suspenso' 
    }
]

# Retornar msg
@app.get('/', tags=['home'])  # @app.get('nombre del end point', tags=[nombre del contenedor de endpoints])
def message():
    return HTMLResponse('<h1>Hello world</h1>')  # puede retornar str, int, bool, html...




    

    