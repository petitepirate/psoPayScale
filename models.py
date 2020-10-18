from flask_sqlalchemy import SQLAlchemy
#from flask_bcrpyt import Bcrypt


db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.Text, nullable=False, unique=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False, unique=True)
    # password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        u = self
        return f"<User id={u.id} user_name={u.user_name} first_name={u.first_name} last_name={u.last_name} email={u.email}>"
