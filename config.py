import os


class Config:
    WTF_CSRF_SECRET_KEY = os.urandom(32)
    CSRF_ENABLE = True
    SECRET_KEY = os.urandom(32)
    DROPZONE_ENABLE_CSRF = True
    DROPZONE_ALLOWED_FILE_CUSTOM = True
    DROPZONE_ALLOWED_FILE_TYPE = '.xls, .xlsx'
    DROPZONE_MAX_FILE_SIZE = 10
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'senderupd@yandex.ru'
    MAIL_PASSWORD = 'flask135mail79'
    MAIL_DEFAULT_SENDER = 'senderupd@yandex.ru'

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