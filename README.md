# UPD Manager

## Что делает проект

Проект помогает автоматизировать ручное заполнение информации из УПД (универсальный передаточный документ)

## Как собрать и запустить проект

1. Клонировать проект выполнив команду```git clone https://github.com/aidarhaertdinov/Upd_manager.git```
2. Создать виртуальное окружение выполнив команду ```python -m venv venv``` 
3. Активировать виртуальное окружение выполнив команду```venv\Scripts\activate```  команды актуальны для Windows
4. Установить пакеты выполнив команду ```pip freeze > requirements.txt```
5. Установить миграцию выполнив команду ```pip install flask-migrate``` 
6. Создать репозиторий миграции выполнив команду ```flask db init``` 

## Используемые Конфигураций (Config)
```WTF_CSRF_SECRET_KEY = os.urandom(32)``` - для защиты веб-форм от атаки под названием Cross-Site Request Forgery. [ссылка на документацию](https://flask-wtf.readthedocs.io/en/0.15.x/config/)

```CSRF_ENABLE = True``` - активирует предотвращение поддельных межсайтовых запросов. [ссылка на документацию](https://flask-wtf.readthedocs.io/en/0.15.x/config/)

```SECRET_KEY = os.urandom(32)``` - используют значение секретного ключа в качестве криптографического ключа, полезного для генерации подписей или токенов. [ссылка на документацию](https://explore-flask.readthedocs.io/en/latest/configuration.html)

```DROPZONE_ENABLE_CSRF = True``` - включит защиту от CSRF - атак. [ссылка на документацию](https://flask-dropzone.readthedocs.io/en/latest/index.html)

```DROPZONE_ALLOWED_FILE_CUSTOM__ = True``` - если хотим самостоятель установить расширение файлов. [ссылка на документацию](https://flask-dropzone.readthedocs.io/en/latest/index.html)

```DROPZONE_ALLOWED_FILE_TYPE = '.xls, .xlsx'``` - установка типов расширения . [ссылка на документацию](https://flask-dropzone.readthedocs.io/en/latest/index.html)

```DROPZONE_MAX_FILE_SIZE = 10``` - максимально допустимый размер файла. единица измерения: МБ. [ссылка на документацию](https://flask-dropzone.readthedocs.io/en/latest/index.html)

```SQLALCHEMY_TRACK_MODIFICATIONS = False``` - если установлен в True, то Flask-SQLAlchemy будет отслеживать изменения объектов и посылать сигналы. [ссылка на документацию](https://flask-sqlalchemy-russian.readthedocs.io/ru/latest/config.html)

```MAIL_SERVER = 'smtp.yandex.ru'``` -uri smtp сервера, который отвечает за рассылку писем. [ссылка на документацию](https://flask-mail.readthedocs.io/en/latest/?badge=latest)

```MAIL_PORT = 465``` - порт почтового сервера. [ссылка на документацию](https://flask-mail.readthedocs.io/en/latest/?badge=latest)

```MAIL_USE_SSL = True``` -  использовать протокол шифрования с SSL, при отправке сообщений. [ссылка на документацию](https://flask-mail.readthedocs.io/en/latest/?badge=latest)

```MAIL_USERNAME = 'senderupd@yandex.ru'``` - имя клиента рассылки, с которого будет отправленно письмо. [ссылка на документацию](https://flask-mail.readthedocs.io/en/latest/?badge=latest)

```MAIL_PASSWORD = 'flask135mail79'``` - пароль, который необходим для авторизации. [ссылка на документацию](https://flask-mail.readthedocs.io/en/latest/?badge=latest)

```MAIL_DEFAULT_SENDER = 'senderupd@yandex.ru'``` - устанавливает отправителя элетронных писем. [ссылка на документацию](https://flask-mail.readthedocs.io/en/latest/?badge=latest)

```SCHEDULER_API_ENABLED = True``` - включение встроенного API [ссылка на документацию](https://pypi.org/project/Flask-Scheduler/#description)

```FLASK_ADMIN_SWATCH = 'lumen'``` - задать тему для flask_admin [ссылка на документацию](https://flask-admin.readthedocs.io/en/latest/index.html)

```BABEL_DEFAULT_LOCALE = 'ru'``` - перевод приложения на русский [ссылка на документацию](https://python-babel.github.io/flask-babel/)




