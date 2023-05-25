from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from utils.jwt_manager import validate_token

# Middleware para solicitar token al usuario y validarlo  
class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request): # call permite acceder a la peticion del usuario 'request'
        auth = await super().__call__(request) # super() = HTTPBearer; devuelve el token/credenciales
        data = validate_token(auth.credentials)
        if data['email'] != 'admin@gmail.com':
            raise HTTPException(status_code=403, detail='Credenciales son invalidas') # lanzar error
