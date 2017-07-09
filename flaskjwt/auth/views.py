import datetime
from flask import Blueprint, request, jsonify
from flaskjwt.response import Response
from flaskjwt.models import User
from flaskjwt.helpers import generate_token
from flaskjwt.decorators import token_required

auth        = Blueprint("auth", __name__)
TOKEN_EXP   = datetime.datetime.utcnow() + datetime.timedelta(minutes=2)

@auth.route("/token", methods=["POST"])
def issue_token():

    if request.authorization is None:
        return Response.basic_auth_error()

    user        = User.exists(request.authorization["username"])
    valid_info  = User.valid_credentials(user, request.authorization["password"])

    if user and valid_info:

        response =  jsonify({
            "meta": {
                "type": "success",
                "status": 200
            },
            "body": {
                "token": generate_token({
                            "public_id": user.public_id,
                            "exp": TOKEN_EXP
                })
            }
        })

        response.status_code = 200
        return response

    else:
        return Response.basic_auth_error()

