from flask import request, jsonify
from app.services.auth_service import register_user, authenticate_user
from app.models import User

def register_auth_routes(app):

    @app.route("/register", methods=["POST"])
    def register():
        data = request.get_json()

        if not data or "username" not in data or "password" not in data:
            return jsonify({"error":"Username and password required"}), 400
        
        if User.query.filter_by(username=data["username"]).first():
            return jsonify({"error": "User already first"}), 400
        
        user = register_user(data["username"], data["password"])
        return jsonify({"message": "User created", "id": user.id}), 201
    
    @app.route("/login", methods=["POST"])
    def login():
        data = request.get_json()

        token = authenticate_user(data["username"], data["password"])

        if not token:
            return jsonify({"error": "Invalid credentials"}), 401
        
        return jsonify({"access_token":token})