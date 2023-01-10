from ..model import User, db
from ..admin.user_view import UserView
# from ..admin.admin_view import AdminMainView
from flask_admin import Admin
from flask_admin.menu import MenuLink
from app.admin.file_admin_view  import FileAdminView
import os.path as op
# from app import admin
from flask import Blueprint

# admin_bp = Blueprint("admin_bp", __name__, template_folder="templates", static_folder="static")
# admin = Admin(name='UPD Manager', index_view=AdminMainView(), template_mode='bootstrap4')

# admin.add_view(UserView(User, db.session, name="Пользователи"))
# admin.add_link(MenuLink(name='Домашняя страница', url='/'))
#
# admin.add_view(FileAdminView(base_path=op.join(op.dirname(__file__)), name='Файловый менеджер'))

