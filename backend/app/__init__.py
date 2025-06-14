from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.config")

    db.init_app(app)

    from .routes import api_bp
    app.register_blueprint(api_bp, url_prefix="/api/v1")

    return app
