import jwt
from flaskjwt import app

def generate_token(payload):

    token = jwt.encode(
        payload,
        app.config["SECRET_KEY"]
    )

    return token.decode("utf-8")
