from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app     = Flask(__name__)
app.config.from_object("flaskjwt.config")

db      = SQLAlchemy(app)

from flaskjwt.auth.views import auth
from flaskjwt.api.views import api

app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(api, url_prefix="/api")

@app.route("/")
def index():
    return "Hello Bro"
