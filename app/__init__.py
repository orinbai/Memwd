from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    app.app_context().push()

#    from .auth import auth as auth_blueprints
#    app.register_blueprint(auth_blueprints, url_prefix='/auth')
    return app

