from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired


class ProductLineForm(FlaskForm):
    product_name = StringField("Наименование товара: ", validators=[DataRequired()])
    unit_of_measurement = StringField("Единица измерения: ", validators=[DataRequired()])
    quantity = FloatField("Количество: ", validators=[DataRequired()])
    price = FloatField("Цена: ", validators=[DataRequired()])
    cost_without_tax = FloatField("Стоимость товаров без налога: ", validators=[DataRequired()])
    tax_rate = StringField("Налоговая ставка: ", validators=[DataRequired()])
    tax_amount = FloatField("Сумма налога: ", validators=[DataRequired()])
    cost_with_tax = FloatField("Стоимость товаров c налогом: ", validators=[DataRequired()])
    submit = SubmitField("Отправить")
