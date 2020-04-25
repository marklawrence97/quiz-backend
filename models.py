from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100))
    password_hash = db.Column(db.String(100))
    name = db.Column(db.String(100))
    username = db.Column(db.String(50))
    quizes = db.relationship('Quiz', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __str__(self):
        return f"{name}'s username is {username}'"

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    rounds = db.relationship('Round', backref='quiz', lazy=True)

    def __str__(self):
        return f"A quiz called {name}"

class Round(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    round_number = db.Column(db.Integer)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'),
        nullable=False)
    questions = db.relationship('Question', backref='round', lazy=True)

    def __str__(self):
        return f"This round is called {name}"

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100))
    question_number = db.Column(db.Integer)
    round_id = db.Column(db.Integer, db.ForeignKey('round.id'),
        nullable=False)
    answers = db.relationship('Answer', backref='question', lazy=True)

    def __str__(self):
        return f"{question}"

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(20))
    round_number = db.Column(db.Integer)
    correct_answer = db.Column(db.String(1))
    questions_id = db.Column(db.Integer, db.ForeignKey('question.id'),
        nullable=False)

    def __str__(self):
        return f"{answer}"

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))



