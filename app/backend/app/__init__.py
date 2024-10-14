# app/__init__.py
from flask import Flask
from app.rest.system import system_bp
from app.rest.user_controller import user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Blueprintの登録
    app.register_blueprint(system_bp)
    app.register_blueprint(user_bp)

    return app
