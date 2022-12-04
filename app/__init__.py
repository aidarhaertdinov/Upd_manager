from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_dropzone import Dropzone
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import config
from flask_mail import Mail
from flask_apscheduler import APScheduler
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from flask_babelex import Babel
import os.path as op
from flask_admin.contrib.fileadmin import FileAdmin

dropzone = Dropzone()
csrf = CSRFProtect()
db = SQLAlchemy()
bootstrap = Bootstrap()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()
scheduler = APScheduler()
babel = Babel()


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

    from .auth import auth
    app.register_blueprint(auth)

    babel.init_app(app)

    from .model import User
    from .admin.user_view import UserView
    admin = Admin(app, name='UPD Manager', template_mode='bootstrap4', endpoint='/admin')
    admin.add_view(UserView(User, db.session))

    admin.add_link(MenuLink(name='Home Page', url='/', category='Links'))

    from .admin.file_admin_view import FileAdminView
    admin.add_view(FileAdminView(base_path=op.join(op.dirname(__file__), 'static/files'), name='File manager'))

    # @app.errorhandler(401)
    # def unauthorized(error):
    #     return render_template('page401.html', title="Страница не доступна")


    return app


