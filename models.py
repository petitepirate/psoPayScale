from flask_sqlalchemy import SQLAlchemy
#from flask_bcrpyt import Bcrypt


db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

DEFAULT_IMG = "https://images.unsplash.com/photo-1562037283-072818fb6d8f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=250&q=80"

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.Text, nullable=False, unique=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False, unique=True)
    image_url = db.Column(db.Text,
                          nullable=False, default=DEFAULT_IMG)
    # password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        u = self
        return f"<User id={u.id} user_name={u.user_name} first_name={u.first_name} last_name={u.last_name} email={u.email}>"
