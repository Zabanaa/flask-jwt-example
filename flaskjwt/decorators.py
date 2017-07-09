from flask import jsonify, request
from flaskjwt import app
from flaskjwt.response import Response
import jwt

def token_required(request_handler):

    def decorated(*args, **kwargs):

        if "Authorization" not in request.headers:
            return Response.missing_auth_header()

        try:
            token = request.headers["Authorization"].split(" ")[1]
        except:
            return Response.badly_formatted_request()

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])

        except jwt.exceptions.InvalidTokenError as e:

            return Response.invalid_json_web_token()

        return request_handler(*args, **kwargs)

    return decorated
