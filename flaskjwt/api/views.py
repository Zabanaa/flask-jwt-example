from flask import Blueprint
from flaskjwt.decorators import token_required

api     = Blueprint("api", __name__)

@api.route("/secretendpoint")
@token_required
def secret_endpoint():
    return "Wow much private, very secret"


