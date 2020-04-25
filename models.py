from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100))
    password_hash = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    username = db.Column(db.string(50))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __str__(self):
        return f"{name}'s username is {username}'"

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))