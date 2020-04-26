import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_restful import Resource, Api

login_manager = LoginManager()

app = Flask(__name__)
api = Api(app)

# Configurate envionment and database
app.config.from_object(os.getenv('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager.init_app(app)
db = SQLAlchemy(app)

# Import models and configure migrations
import models
migrate = Migrate(app, db)

from resources import Register

api.add_resource(Register, '/register')

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()