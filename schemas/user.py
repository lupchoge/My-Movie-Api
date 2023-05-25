from pydantic import BaseModel # Crear esquemas/plantillas, crear validaciones de datos


# CREAR ESQUEMA/PLANTILLA
class User(BaseModel):
    email: str 
    password: str