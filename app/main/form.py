from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired
from enum import Enum
from ..model import Permissions

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


class UserForm(FlaskForm):
    id = IntegerField("№", validators=[DataRequired()])
    user_name = StringField("Имя пользователя: ", validators=[DataRequired()])
    permission = SelectField("Разрешение: ", choices=[e.value for e in Permissions])
    submit = SubmitField("Отправить")