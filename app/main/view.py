from app.main import main
from flask import render_template, request, flash, redirect, url_for
from app import login_manager
from flask_wtf.csrf import CSRFError
from app.model import ProductLine, db, User
from .form import ProductLineForm, UserForm
import os
from .service import parsing_upd, calculation_cost_without_tax, calculation_tax_amount, calculation_cost_with_tax
from app.auth.decorators import admin_required, user_required
from flask_login import login_required


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@main.route('/uploads', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join('app/static/files', f.filename))
        product_lines = parsing_upd(os.path.join('app/static/files', f.filename))
        for product_line in product_lines:
            db.session.add(ProductLine(product_name=product_line.product_name,
                                       unit_of_measurement=product_line.unit_of_measurement,
                                       quantity=product_line.quantity, price=product_line.price,
                                       cost_without_tax=product_line.cost_without_tax,
                                       tax_rate=product_line.tax_rate[:-1], tax_amount=product_line.tax_amount,
                                       cost_with_tax=product_line.cost_with_tax))
        db.session.commit()
        # закомментировал намеренно, чтобы можно было демонстрировать работу файлового менеджера в flask admin
        # os.remove(os.path.join('app/static/files', f.filename))
    return render_template("main/main.html", title="Main")


@main.route('/')
def index():
    return render_template("main/base.html")


# @main.route('/product_line_browser')
# @login_required
# def product_line_browser():
#     product_lines = ProductLine.query.all()
#     return render_template("main/product_line_browser.html", product_lines=product_lines, title="Экран №2")
@main.route("/product_line_browser", methods=['GET', 'POST'])
@login_required
def product_line_browser():
    page = request.args.get('page', 1, type=int)
    product_lines = ProductLine.query.paginate(page=page, per_page=7)
    return render_template("main/product_line_browser.html", product_lines=product_lines, title="Экран №2")


@main.route('/product_line_editor/<id_product_line>', methods=['GET', 'POST'])
@login_required

def product_line_editor(id_product_line):
    product_line = ProductLine.query.filter_by(id_product_line=id_product_line).first()
    if product_line:
        form = ProductLineForm(formdata=request.form, obj=product_line)
        if form.validate_on_submit():
            product_line.product_name = form.product_name.data
            product_line.unit_of_measurement = form.unit_of_measurement.data
            product_line.quantity = form.quantity.data
            product_line.price = form.price.data
            product_line.cost_without_tax = calculation_cost_without_tax(product_line.quantity, product_line.price)
            product_line.tax_rate = form.tax_rate.data
            product_line.tax_amount = calculation_tax_amount(product_line.cost_without_tax, product_line.tax_rate)
            product_line.cost_with_tax = calculation_cost_with_tax(product_line.cost_without_tax,
                                                                   product_line.tax_amount)
            db.session.add(product_line)
            db.session.commit()
            return redirect(url_for("main.product_line_browser"))
        return render_template("main/product_line_editor.html", form=form)
    else:
        product_line_empty_editor()


@main.route('/product_line_editor', methods=['GET', 'POST'])
@login_required
def product_line_empty_editor():
    form = ProductLineForm()
    if form.validate_on_submit():
        cost_without_tax = calculation_cost_without_tax(form.quantity.data, form.price.data)
        tax_amount = calculation_tax_amount(cost_without_tax, form.tax_rate.data)
        cost_with_tax = calculation_cost_with_tax(cost_without_tax, tax_amount)
        product_line = ProductLine(product_name=form.product_name.data,
                                   unit_of_measurement=form.unit_of_measurement.data,
                                   quantity=form.quantity.data,
                                   price=form.price.data,
                                   cost_without_tax=cost_without_tax,
                                   tax_rate=form.tax_rate.data,
                                   tax_amount=tax_amount,
                                   cost_with_tax=cost_with_tax)
        db.session.add(product_line)
        db.session.commit()
        return redirect(url_for("main.product_line_browser"))
    return render_template("main/product_line_editor.html", form=form)

@main.route('/delete_product_line/<id_product_line>', methods=['GET', 'POST'])
@login_required
def delete_product_line(id_product_line):
    product_line = ProductLine.query.filter_by(id_product_line=id_product_line).first()
    db.session.delete(product_line)
    db.session.commit()
    return redirect(url_for("main.product_line_browser"))


@main.route('/user_browser')
@login_required
@admin_required
def user_browser():
    users = User.query.all()
    return render_template("main/user_browser.html", users=users, title="Пользователи")


@main.route('/user_editor/<id>', methods=['GET', 'POST'])
@login_required
@admin_required
def user_editor(id):
    user = User.query.filter_by(id=id).first()
    if user:
        form = UserForm(formdata=request.form, obj=user)
        if form.validate_on_submit():
            user.id = form.id.data
            user.user_name = form.user_name.data
            user.permission = form.permission.data
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("main.user_browser"))
        return render_template("main/user_editor.html", form=form)


@main.route('/delete_user/<id>', methods=['GET', 'POST'])
@login_required
@admin_required
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("main.user_browser"))