from flask_admin import AdminIndexView, expose
from ..model import User, db, Permissions
from flask import flash, redirect, url_for
from flask_login import current_user


class AdminMainView(AdminIndexView):
    @expose('/')
    def admin_main_view(self):
        if current_user.permission == Permissions.ADMIN:
            return self.render('admin/admin_index.html')
        return redirect(url_for("auth.login"))

