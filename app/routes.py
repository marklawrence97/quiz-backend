from app import api
from flask_restful import Resource
from flask import request, jsonify
from app import models
from app import db

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
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return jsonify({"success": "success"})

api.add_resource(Register, '/register')