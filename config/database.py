import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base  # Manipular las tablas de las bases de datos

# Nombre de la base de datos
sqlite_file_name = '../database.sqlite'
# Leer el directorio actual de este archivo (o sea database.py)
base_dir = os.path.dirname(os.path.realpath(__file__))

# Crear URL a la base de datos; sqlite:/// -> conectarse a la base de datos; con .join hace la union de las 2 variables
database_url = f'sqlite:///{os.path.join(base_dir, sqlite_file_name)}'

# 'Motor' de la base de datos; se pasa como parametro la url y 'echo' al momento de crear la database nos deja ver por consola el codigo)
engine = create_engine(database_url, echo=True)

# Crear sesion para conectarse a la base de datos
Session = sessionmaker(bind=engine)

# definir una clase base (plantilla de la base de datos), que se hereda para crear modelos de base de datos
Base = declarative_base()