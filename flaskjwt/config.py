import os

DEBUG                       = True
PORT                        = 5000
SECRET_KEY                  = os.urandom(32)
DB_USER                     = os.getenv("JWTPY_USER")
DB_HOST                     = os.getenv("JWTPY_HOST")
DB_PORT                     = os.getenv("JWTPY_PORT")
DB_NAME                     = os.getenv("JWTPY_NAME")


SQLALCHEMY_DATABASE_URI         = "postgres://{}@{}:{}/{}".format(
                                    DB_USER,
                                    DB_HOST,
                                    DB_PORT,
                                    DB_NAME
                                )

SQLALCHEMY_TRACK_MODIFICATIONS = False
