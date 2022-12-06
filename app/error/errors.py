from flask import render_template
from app.error import error

@error.app_errorhandler(404)
def page_not_found(error):
    return render_template('error/page404.html', title="Страница не доступна")

@error.app_errorhandler(401)
def unauthorized(error):
    return render_template('error/page401.html', title="Вы не авторизованы")
