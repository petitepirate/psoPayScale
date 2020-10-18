from flask import Flask, request, redirect, render_template
from models import db, connect_db, User


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///psopayscale'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "shenanigans"

connect_db(app)
db.create_all()
# toolbar = DebugToolbarExtension(app)


@app.route("/")
def enterpage():
    data = open('index.html').read()    
    return data

@app.route("/home")
def homepage():
    return render_template('index2.html')

@app.route("/about")
def aboutpage():
    return render_template('about.html')

@app.route("/user/new", methods=["GET"])
def users_new_form():
    """Show a form to create a new user"""

    return render_template('newuser.html')

@app.route("/user/new", methods=["POST"])
def add_user():
    new_user = User(
        user_name=request.form["user_name"],
        first_name=request.form["first_name"],
        last_name=request.form["last_name"],
        email=request.form["email"])

    db.session.add(new_user)
    db.session.commit()
    return redirect('/user/info')


@app.route("/user/info", methods=["GET"])
def user_page():
    return render_template('userinfo.html')
