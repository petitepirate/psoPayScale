from models import User, db
from app import app

db.drop_all()
db.create_all()

p1 = User(user_name="mini", first_name="Megan", last_name="McManus", email="wildlife.megan@gmail.com", image_url="https://images.unsplash.com/photo-1562037283-072818fb6d8f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=250&q=80")
p2 = User(user_name="mini2", first_name="Megan2", last_name="McManus2", email="megan@gmail.com", image_url="https://images.unsplash.com/photo-1562037283-072818fb6d8f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=250&q=80")
p3 = User(user_name="mini3", first_name="Megan3", last_name="McManus3", email="wildlife@gmail.com", image_url="https://images.unsplash.com/photo-1562037283-072818fb6d8f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=250&q=80")


db.session.add(p1)

db.session.add(p2)

db.session.add(p3)

db.session.commit()
