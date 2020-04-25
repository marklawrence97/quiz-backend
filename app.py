import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

login_manager = LoginManager()

app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager.init_app(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()