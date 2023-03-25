from datetime import datetime
import logging


logging.basicConfig(level=logging.INFO, filename='mylog.log')


def function_execution_time(func):
    def wrapper(*args):
        start_time = datetime.utcnow()
        logging.info(f'Функция: {func.__name__}, с параметрами: {args} начала свою работу в {start_time} ')
        try:
            func(*args)
            stop_time = datetime.utcnow()
            logging.info(f'Функция: {func.__name__}, с параметрами: {args} закончила свою работу в {stop_time}'
                  f'\nВремя выполнения функции: {stop_time - start_time} ')

            return func(*args)

        except TypeError:
            logging.exception("Функция не выполнилась. Выпала ошибка: TypeError, ")

        except IndexError:
            logging.exception("Функция не выполнилась. Выпала ошибка: IndexError, ")

        except ValueError:
            logging.exception("Функция не выполнилась. Выпала ошибка: ValueError")

        except Exception:
            logging.exception("Функция не выполнилась. Выпала ошибка: Exception")

    return wrapper
