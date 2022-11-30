from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class LoginForm(FlaskForm):
    email = EmailField("Email: ", validators=[DataRequired(), Email("Email адрес введен не верно")])
    password = PasswordField("Password: ", validators=[DataRequired(), Length(1, 30)])
    submit = SubmitField("Log In")


class RegistrationForm(FlaskForm):
    email = EmailField("Email: ", validators=[DataRequired(), Email("Email адрес введен не верно")])
    password = PasswordField("Password: ", validators=[DataRequired(), Length(1, 30), EqualTo('check_password')])
    check_password = PasswordField("Password: ", validators=[DataRequired(), Length(1, 30)])
    submit = SubmitField("Log In")