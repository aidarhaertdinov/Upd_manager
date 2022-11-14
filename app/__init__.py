from flask import Flask
from flask_bootstrap import Bootstrap
from flask_dropzone import Dropzone
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import config


dropzone = Dropzone()
csrf = CSRFProtect()
db = SQLAlchemy()
bootstrap = Bootstrap()
migrate = Migrate()
login_manager = LoginManager()


def create_app(config_name="development"):

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    dropzone.init_app(app)
    csrf.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from .main import main
    app.register_blueprint(main)

    return app
