# UPD Manager

## Что делает проект

Проект помогает автоматизировать ручное заполнение информации из УПД (универсальный передаточный документ)

## Как собрать и запустить проект

1. Git clone ```https://github.com/aidarhaertdinov/Upd_manager.git```
2. Создать виртуальное окружение ```python -m venv venv```, активировать ```venv\Scripts\activate``` , команды актуальны для Windows
3. ```pip freeze > requirements.txt```
4. Установить миграцию ```pip install flask-migrate```, создать репозиторий миграции ```flask db init``` 

## Используемые Конфигураций (Config)
```WTF_CSRF_SECRET_KEY = os.urandom(32)``` - для защиты веб-форм от атаки под названием Cross-Site Request Forgery 

```CSRF_ENABLE = True``` - активирует предотвращение поддельных межсайтовых запросов

```SECRET_KEY = os.urandom(32)``` - используют значение секретного ключа в качестве криптографического ключа, полезного для генерации подписей или токенов.

```DROPZONE_ENABLE_CSRF = True``` - включит защиту от CSRF - атак (документация https://flask-dropzone.readthedocs.io/en/latest/index.html)

```DROPZONE_ALLOWED_FILE_CUSTOM__ = True``` - если хотим самостоятель установить расширение файлов

```DROPZONE_ALLOWED_FILE_TYPE = '.xls, .xlsx'``` - установка типов расширения 

```DROPZONE_MAX_FILE_SIZE = 10``` - максимально допустимый размер файла. единица измерения: МБ

```SQLALCHEMY_TRACK_MODIFICATIONS = False``` - если установлен в True, то Flask-SQLAlchemy будет отслеживать изменения объектов и посылать сигналы.

```MAIL_SERVER = 'smtp.yandex.ru'``` -uri smtp сервера, который отвечает за рассылку писем. [ссылка на документацию](https://flask-mail.readthedocs.io/en/latest/?badge=latest)

```MAIL_PORT = 465``` - порт почтового сервера

```MAIL_USE_SSL = True``` -  использовать протокол шифрования с SSL, при отправке сообщений

```MAIL_USERNAME = 'senderupd@yandex.ru'``` - имя клиента рассылки, с которого будет отправленно письмо

```MAIL_PASSWORD = 'flask135mail79'``` - пароль, который необходим для авторизации 

```MAIL_DEFAULT_SENDER = 'senderupd@yandex.ru'``` - устанавливает отправителя элетронных писем

```SCHEDULER_API_ENABLED = True``` - включение встроенного API (документация https://pypi.org/project/Flask-Scheduler/#description)

```FLASK_ADMIN_SWATCH = 'lumen'``` - задать тему для flask_admin (документация https://flask-admin.readthedocs.io/en/latest/index.html)

```BABEL_DEFAULT_LOCALE = 'ru'``` - перевод приложения на русский (документация https://python-babel.github.io/flask-babel/)




