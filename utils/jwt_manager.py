from jwt import encode, decode

def create_token(data: dict) -> str:
    token: str = encode(payload=data, key='my_secrete_key', algorithm='HS256')
    return token
    # payload -> contenido que se convierte en token (data)
    # key -> es necesaria para generar el token
    #algorithm -> generar el token con ese tipo de algoritmo

def validate_token(token: str) -> dict:
    data: dict = decode(token, key='my_secrete_key', algorithms=['HS256'])
    return data
