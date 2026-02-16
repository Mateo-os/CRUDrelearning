from flask import Flask, jsonify
from flask_jwt_extended import JWTManager

from app.database import db
from app.routes import register_routes
from app.routes_auth import register_auth_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)

    jwt = JWTManager(app)

    with app.app_context():
        db.create_all()
    register_routes(app)
    register_auth_routes(app)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Resource not found"}), 404
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": "Bad Request"}), 400
    
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({"error": "Server error"}), 500
        
    return app