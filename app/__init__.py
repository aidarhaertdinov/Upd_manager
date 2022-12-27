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
from flask_admin import Admin
from flask_admin.menu import MenuLink
from flask_babelex import Babel
import os.path as op
from flask_restful_swagger_3 import Api
from flasgger import Swagger
# from .admin.admin_view import AdminMainView

dropzone = Dropzone()
csrf = CSRFProtect()
db = SQLAlchemy()
bootstrap = Bootstrap()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()
scheduler = APScheduler()
babel = Babel()
api = Api()
swagger = Swagger()
# admin = Admin(name='UPD Manager', template_mode='bootstrap4')

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
    babel.init_app(app)
    api = Api(app, decorators=[csrf.exempt], swagger_prefix_url='/api_v2', swagger_url='swagger.json')
    # api.init_app(app)
    swagger.init_app(app)



    from app.main import tasks
    scheduler.start(paused=True)

    from .main import main
    app.register_blueprint(main)

    from .auth import auth
    app.register_blueprint(auth)

    # from .error import error
    # app.register_blueprint(error)

    from app.rest.v1 import rest_v1
    csrf.exempt(rest_v1)
    app.register_blueprint(rest_v1)

    # from .rest.v2.view import RestUser, RestUserList
    # api.add_resource(RestUser, "/rest/v2/users/<int:id>", methods=['GET', 'PUT', 'DELETE', 'POST', ])
    # api.add_resource(RestUserList, "/rest/v2/users")



    from .model import User
    from .admin.user_view import UserView
    from .admin.admin_view import AdminMainView
    admin = Admin(app, name='UPD Manager', index_view=AdminMainView(), template_mode='bootstrap4')

    admin.add_view(UserView(User, db.session, name="Пользователи"))
    admin.add_link(MenuLink(name='Домашняя страница', url='/'))

    from .admin.file_admin_view import FileAdminView
    admin.add_view(FileAdminView(base_path=op.join(op.dirname(__file__), 'static/files'), name='Файловый менеджер'))


    # from app.admin import admin_bp
    # app.register_blueprint(admin_bp)
    # # from app.admin import admin
    # # admin= Admin(app)


    # # admin.init_app(app)
    # from .admin.admin_view import AdminMainView
    # # from .admin import add_views
    # # admin = Admin(app, name='UPD Manager', index_view=AdminMainView(), template_mode='bootstrap4')
    # admin.init_app(app, index_view=AdminMainView())

    return app


