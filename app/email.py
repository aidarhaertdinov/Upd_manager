from threading import Thread
from flask import current_app
from flask_mail import Message
from . import mail
import time


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(recipients):
    app = current_app._get_current_object()
    msg = Message('Привет', recipients=[recipients])
    msg.body = f'Пользователь с {recipients} почтой зарегистрирован!'
    thr = Thread(target=send_async_email, args=[app, msg])
    time.sleep(5)
    thr.start()
    return thr


def background_task():
    print("Hello")
    time.sleep(15)
    print("world!")