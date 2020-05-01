import os

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_restful import Resource, Api
from flask_cors import CORS
from config import Config


login_manager = LoginManager()

app = Flask(__name__)
cors = CORS(app)
api = Api(app)


# Configurate envionment and database
app.config.from_object(os.getenv('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager.init_app(app)
db = SQLAlchemy(app)


# Import models and configure migrations
from app import models
migrate = Migrate(app, db)

from app import resources

api.add_resource(resources.Register, '/register')
api.add_resource(resources.Profile, '/profile')