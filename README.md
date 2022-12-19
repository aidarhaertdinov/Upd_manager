# 1.Как собрать и запустить проект

1. Создаем проект в PyCharm
2. Копируем ```https://github.com/aidarhaertdinov/Upd_manager.git``` 
2. Вставить в свой проект ```VCS -> Get from version control -> в поле URL -> clone``` 
3. Создать виртуальное окружение ```python -m venv venv```, активировать ```venv\Scripts\activate```
4. Из файла ```requirements.txt``` установить библиотеки

# 2. Что делает проект

Проект помогает автоматизировать ручное заполнение информации из УПД (универсальный передаточный документ)

# 3.Описание используемых Конфигураций (Config) и специфичных методов в проекте 

## 3.1 Используемые Конфигураций (Config)
__WTF_CSRF_SECRET_KEY = os.urandom(32)__ - для защиты веб-форм от атаки под названием Cross-Site Request Forgery 

__CSRF_ENABLE = True__ - активирует предотвращение поддельных межсайтовых запросов

__SECRET_KEY = os.urandom(32)__ - используют значение секретного ключа в качестве криптографического ключа, полезного для генерации подписей или токенов.

__DROPZONE_ENABLE_CSRF = True__ - включит защиту от CSRF - атак

__DROPZONE_ALLOWED_FILE_CUSTOM__ = True__ - если хотим самостоятель установить расширение файлов

__DROPZONE_ALLOWED_FILE_TYPE = '.xls, .xlsx'__ - установка типов расширения 

__DROPZONE_MAX_FILE_SIZE = 10__ - максимально допустимый размер файла. единица измерения: МБ

__SQLALCHEMY_TRACK_MODIFICATIONS = False__ - если установлен в True, то Flask-SQLAlchemy будет отслеживать изменения объектов и посылать сигналы.

__MAIL_SERVER = 'smtp.yandex.ru'__ - почтовый сервер

__MAIL_PORT = 465__ - почтовый порт

__MAIL_USE_SSL = True__ -  использовать протокол шифрования с SSL

__MAIL_USERNAME = 'senderupd@yandex.ru'__ - имя пользователя отправителя

__MAIL_PASSWORD = 'flask135mail79'__ - пароль пользователя отправителя

__MAIL_DEFAULT_SENDER = 'senderupd@yandex.ru'__ - устанавливает отправителя

__SCHEDULER_API_ENABLED = True__ - включение встроенного API

__FLASK_ADMIN_SWATCH = 'lumen'__ - задать тему для flask_admin

__BABEL_DEFAULT_LOCALE = 'ru'__ - перевод приложения на русский

## 3.2 Описание работы методов (функций)

* Метод **parsing_upd** (**app/main/service.py**) - на вход принимает путь excele файла, парсит и возвращает список product_lines (в нашем случае товары)

* Методы обработок ошибок сервера **page_not_found** - 404 и **unauthorized**- 401 (**app/main/service.py**) - возвращают пользователю более дружественную информацию с помощью написанных шаблонов



