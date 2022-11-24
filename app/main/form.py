from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, SelectField
from wtforms.validators import DataRequired
from enum import Enum

class Dimension(Enum):
    PIECE = "шт"
    PACK = "упак"
    METRE = "м"
    TONNE = "т"

class ProductLineForm(FlaskForm):
    product_name = StringField("Наименование товара: ", validators=[DataRequired()])
    unit_of_measurement = SelectField("Единица измерения: ", choices=[e.value for e in Dimension])
    quantity = FloatField("Количество: ", validators=[DataRequired()])
    price = FloatField("Цена: ", validators=[DataRequired()])
    tax_rate = FloatField("Налоговая ставка %: ", validators=[DataRequired()])
    submit = SubmitField("Отправить")
