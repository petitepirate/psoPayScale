from models import User, db
from app import app

db.drop_all()
db.create_all()

p1 = User(user_name="mini", first_name="Megan", last_name="McManus", email="wildlife.megan@gmail.com")
p2 = User(user_name="mini2", first_name="Megan2", last_name="McManus2", email="megan@gmail.com")
p3 = User(user_name="mini3", first_name="Megan3", last_name="McManus3", email="wildlife@gmail.com")


db.session.add(p1)

db.session.add(p2)

db.session.add(p3)

db.session.commit()
