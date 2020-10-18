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

# @app.route("/regions")
# def aboutpage():
#     return render_template('regions.html')

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

@app.route("/ocean/1", methods=["GET"])
def ocean1_page():
    return render_template('id1.html')
    
@app.route("/ocean/2", methods=["GET"])
def ocean2_page():
    return render_template('id2.html')

@app.route("/ocean/3", methods=["GET"])
def ocean3_page():
    return render_template('id3.html')

@app.route("/ocean/4", methods=["GET"])
def ocean4_page():
    return render_template('id4.html')

@app.route("/ocean/5", methods=["GET"])
def ocean5_page():
    return render_template('id5.html')

@app.route("/ocean/6", methods=["GET"])
def ocean6_page():
    return render_template('id6.html')

@app.route("/ocean/7", methods=["GET"])
def ocean7_page():
    return render_template('id7.html')

@app.route("/ocean/8", methods=["GET"])
def ocean8_page():
    return render_template('id8.html')

@app.route("/ocean/9", methods=["GET"])
def ocean9_page():
    return render_template('id9.html')

@app.route("/ocean/10", methods=["GET"])
def ocean10_page():
    return render_template('id10.html')

@app.route("/ocean/11", methods=["GET"])
def ocean11_page():
    return render_template('id11.html')

@app.route("/ocean/12", methods=["GET"])
def ocean12_page():
    return render_template('id12.html')

@app.route("/ocean/13", methods=["GET"])
def ocean13_page():
    return render_template('id13.html')

@app.route("/ocean/14", methods=["GET"])
def ocean14_page():
    return render_template('id14.html')

@app.route("/ocean/15", methods=["GET"])
def ocean15_page():
    return render_template('id15.html')
