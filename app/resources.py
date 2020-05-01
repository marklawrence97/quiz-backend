from app import api
from flask_restful import Resource
from flask import request, jsonify
from app import models
from app import db
from app import login_manager
from flask_login import login_user

class Register(Resource):

    def post(self):
        username = request.headers["username"]
        fname = request.headers["fname"]
        lname = request.headers["lname"]
        email = request.headers["email"]
        password = request.headers["password"]

        user = models.User()
        user.username = username
        user.fname = fname
        user.lname = lname
        user.email = email
        user.set_password(password)

        try: 
            db.session.add(user)
            db.session.commit()
            
            if login_user(user):
                return jsonify({"success": True, "logIn": True})
            return jsonify({"success": True, "logIn": False})
        except:
            return jsonify({"success": "nope", "logIn": False})

        return jsonify({"test": "test"})

api.add_resource(Register, '/register')