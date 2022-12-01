from flask import Flask
from flask_bootstrap import Bootstrap
from flask_dropzone import Dropzone
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import config
from flask_mail import Mail
from flask_apscheduler import APScheduler
from flask_errors_handler import ErrorHandler
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink



dropzone = Dropzone()
csrf = CSRFProtect()
db = SQLAlchemy()
bootstrap = Bootstrap()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()
scheduler = APScheduler()
error = ErrorHandler()


def create_app(config_name="development"):

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    dropzone.init_app(app)
    csrf.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    scheduler.init_app(app)
    from . import tasks
    scheduler.start(paused=True)

    from .main import main
    app.register_blueprint(main)

    from.auth import auth
    app.register_blueprint(auth)

    error.init_app(app)

    from .model import User
    from .admin.user_view import UserView
    admin = Admin(app, name='UPD Manager', template_mode='bootstrap4', endpoint='/admin')
    admin.add_view(UserView(User, db.session))
    from .main.view import url_for
    admin.add_link(MenuLink(name='Home Page', url='/', category='Links'))

    return app

