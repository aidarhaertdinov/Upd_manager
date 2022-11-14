from app.main import main
from flask import render_template, request, flash, redirect, url_for
from app import login_manager
from flask_wtf.csrf import CSRFError
from app.model import ProductLine, db
from .form import ProductLineForm
import os
from .service import parsing_upd


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


@main.route('/uploads', methods=['GET', 'POST'])
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
                                       tax_rate=product_line.tax_rate, tax_amount=product_line.tax_amount,
                                       cost_with_tax=product_line.cost_with_tax))
        db.session.commit()
        os.remove(os.path.join('app/static/files', f.filename))
    return render_template("main/main.html", title="Main")


@main.route('/')
def index():
    return render_template("main/base.html")


@main.route('/product_line_browser')
def product_line_browser():
    product_lines = ProductLine.query.all()
    return render_template("main/product_line_browser.html", product_lines=product_lines, title="Экран №2")


@main.route('/product_line_editor/<id_product_line>', methods=['GET', 'POST'])
def product_line_editor(id_product_line):
    product_line = ProductLine.query.filter_by(id_product_line=id_product_line).first()
    if product_line:
        form = ProductLineForm(formdata=request.form, obj=product_line)
        if form.validate_on_submit():
            product_line.product_name = form.product_name.data
            product_line.unit_of_measurement = form.unit_of_measurement.data
            product_line.quantity = form.quantity.data
            product_line.price = form.price.data
            product_line.cost_without_tax = form.cost_without_tax.data
            product_line.tax_rate = form.tax_rate.data
            product_line.tax_amount = form.tax_amount.data
            product_line.cost_with_tax = form.cost_with_tax.data
            db.session.add(product_line)
            db.session.commit()
            return redirect(url_for("main.product_line_browser"))
        return render_template("main/product_line_editor.html", form=form)
    else:
        product_line_empty_editor()


@main.route('/product_line_editor', methods=['GET', 'POST'])
def product_line_empty_editor():
    form = ProductLineForm()
    if form.validate_on_submit():
        product_line = ProductLine(form.product_name.data, form.unit_of_measurement.data, form.quantity.data,
                                   form.price.data, form.cost_without_tax.data, form.tax_rate.data,
                                   form.tax_amount.data, form.cost_with_tax.data)
        db.session.add(product_line)
        db.session.commit()
        return redirect(url_for("main.product_line_browser"))
    return render_template("main/product_line_editor.html", form=form)


@main.route('/delete_product_line/<id_product_line>', methods=['GET', 'POST'])
def delete_product_line(id_product_line):
    product_line = ProductLine.query.filter_by(id_product_line=id_product_line).first()
    db.session.delete(product_line)
    db.session.commit()
    return redirect(url_for("main.product_line_browser"))







