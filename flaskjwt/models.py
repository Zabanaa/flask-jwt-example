from flaskjwt import db
import uuid

class User(db.Model):

    id          = db.Column(db.Integer, primary_key=True)
    public_id   = db.Column(db.String(100), unique=True)
    username    = db.Column(db.String(80), unique=True, nullable=False)
    password    = db.Column(db.String(15), nullable=True)

    def __init__(self, payload):

        for key, value in payload.items():
            setattr(self, key, value)
        self.public_id  = str(uuid.uuid4())

    @classmethod
    def create(cls, payload):
        return cls(payload).save()

    @classmethod
    def exists(cls, username):
        user    = cls.query.filter_by(username=username).first()
        return user if user else None

    @classmethod
    def valid_credentials(cls, user, password):

        try:
            return user.password == password

        except AttributeError as e:
            print("User does not exist")
            return False

    def save(self):

        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            return False
        else:
            return self

    def __repr__(self):
        return "User: {}".format(self.username)
