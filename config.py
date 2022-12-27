import os


class Config:
    WTF_CSRF_SECRET_KEY = os.getenv('WTF_CSRF_SECRET_KEY') or os.urandom(32)
    CSRF_ENABLE = os.getenv('CSRF_ENABLE') or False
    SECRET_KEY = os.getenv('SECRET_KEY') or os.urandom(32)
    DROPZONE_ENABLE_CSRF = bool(os.getenv('DROPZONE_ENABLE_CSRF')) or True
    DROPZONE_ALLOWED_FILE_CUSTOM = os.getenv('DROPZONE_ALLOWED_FILE_CUSTOM') or True
    DROPZONE_ALLOWED_FILE_TYPE = os.getenv('DROPZONE_ALLOWED_FILE_TYPE') or '.xls, .xlsx'
    DROPZONE_MAX_FILE_SIZE = os.getenv('DROPZONE_MAX_FILE_SIZE') or 10
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') or False
    MAIL_SERVER = os.getenv('MAIL_SERVER') or 'smtp.yandex.ru'
    MAIL_PORT = os.getenv('MAIL_PORT') or 465
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL') or True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME') or 'senderupd@yandex.ru'
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD') or 'flask135mail79'
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER') or 'senderupd@yandex.ru'
    SCHEDULER_API_ENABLED = os.getenv('SCHEDULER_API_ENABLED') or True
    FLASK_ADMIN_SWATCH = os.getenv('FLASK_ADMIN_SWATCH') or 'lumen'
    BABEL_DEFAULT_LOCALE = os.getenv('BABEL_DEFAULT_LOCALE') or 'ru'



class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/upd_manager'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///production.db'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}