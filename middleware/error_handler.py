from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None: # Crear metodo constructor que recibe la app q es de tipo FastAPI
        super().__init__(app)

    # Metodo para detectar errores en la app
    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            #si no ocurre ningun error pasa a la siguiente llamada (call_next)
            return await call_next(request)
        # Si ocurre algun error se captura con except
        except Exception as e:
            return JSONResponse(status_code=500, content={'error': str(e)})
