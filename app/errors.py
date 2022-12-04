from .main import app

@app.errorhandler(401)
def unauthorized(error):
    return render_template('page401.html', title="Страница не доступна")
