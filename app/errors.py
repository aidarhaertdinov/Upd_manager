from . import create_app

app = create_app()

@app.error(401)
def unauthorized(error):
    return render_template('page401.html', title="Страница не доступна")
