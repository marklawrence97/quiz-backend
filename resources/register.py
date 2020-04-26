from flask import jsonify, request
from flask_restful import Resource

class Register(Resource):

    def post(self):
        username = request.headers["username"]
        fname = request.headers["fname"]
        lname = request.headers["lname"]
        email = request.headers["email"]
        password = request.headers["password"]


        return jsonify({"success": "success"})