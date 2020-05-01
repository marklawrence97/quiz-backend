from app import api
from flask_restful import Resource
from flask import request, jsonify, redirect
from app import models
from app import db
from app import login_manager
from flask_login import login_user, current_user, logout_user

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
                return jsonify({"success": True, "logIn": True, "error": False})
            return jsonify({"success": True, "logIn": False, "error": "Our bad... our server messed up please try again!"})
        except:
            return jsonify({"success": "nope", "logIn": False, "error": "We're afraid there is already a user with that name!"})

        return jsonify({"test": "test"})

class Profile(Resource):

    def get(self):
        if current_user.is_authenticated:
            return {"username": current_user.username}
        return {"username": "Please log in!"}

class LogOut(Resource):

    def get(self):
        if current_user.is_authenticated:
            logout_user(current_user)
            return {"status": "logged out!"}
        return {"status": "You weren't signed in!"}

class LogIn(Resource):

    def post(self):
        try:
            username = request.headers["username"]
        except:
            return {
                "success": False,
                "logIn": False,
                "error": "please enter a username!"
            }

        try:
            password = request.headers["password"]
        except:
            return {
                "success": False,
                "logIn": False,
                "error": "please enter a password!"
            }
        
        user = models.User.query.filter_by(username=username).first()

        if user is None:
            return {
                "success": True, 
                "logIn": False, 
                "error": "We don't have a user with that name!"
                }
        
        if user.check_password(password):
            if login_user(user):
                return {"success": True, "logIn": True, "error": False}
            return {
                "success": True, 
                "logIn": False, 
                "error": "Our bad... our server messed up please try again!"
                }
        return {
                "success": True, 
                "logIn": False, 
                "error": "You're password didn't match the one we have!"
                }
