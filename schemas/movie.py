from pydantic import BaseModel, Field # Crear esquemas/plantillas, crear validaciones de datos
from typing import Optional # Campo opcional


# CREAR ESQUEMA/PLANTILLA Y AGREGARLE VALIDACIONES
class Movie(BaseModel):  
    id: Optional[int] = None
    title: str = Field(min_lenght=5, max_lenght=15)
    overview: str = Field(min_lenght=15, max_lenght=50)
    year: int = Field(le=2022)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=20)

    # Adentro de la clase Movie, Añadir valores predeterminados al esquema/plantilla (clave-valor) 
    class Config:
        schema_extra = {
            'example': {
                'id': 1,
                'title': 'Mi peli',
                'overview': 'Descripcion de la pelicula',
                'year': 2022,
                'rating': 9.2,
                'category': 'Acción'
            }
        }
        