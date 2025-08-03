"""
Задание 3
 Доработаем задачу 2.
 Сохраняйте в лог файл раздельно:
○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат.
"""

import logging
from functools import wraps

# Декоратор-фабрика для записи логов в файл с указанием уровня, даты, имени функции, аргументов и результата

def log_to_file(filepath):
    """
    Декоратор, создающий логгер, который пишет в файл:
      - уровень логирования
      - дату события
      - имя функции
      - переданные args и kwargs
      - результат или информацию об ошибке
    :param filepath: путь до файла лога
    """
    # Создаем и настраиваем обработчик
    handler = logging.FileHandler(filepath, encoding='utf-8')
    formatter = logging.Formatter(
        '%(levelname)s %(asctime)s %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    handler.setFormatter(formatter)

    def decorator(func):
        logger = logging.getLogger(func.__name__)
        logger.setLevel(logging.INFO)
        # Избегаем дублирования добавляемых handler'ов
        if not logger.handlers:
            logger.addHandler(handler)
            logger.propagate = False

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                logger.info(f"args={args}, kwargs={kwargs}, result={result}")
                return result
            except Exception as e:
                logger.error(f"args={args}, kwargs={kwargs}, error={e}")
                raise

        return wrapper

    return decorator

# Пример использования
if __name__ == '__main__':
    @log_to_file('app.log')
    def divide(a, b):
        return a / b

    @log_to_file('app.log')
    def greet(name, greeting='Hello'):
        return f"{greeting}, {name}!"

    # Успешный вызов
    print(divide(10, 2))
    # Ошибка деления
    try:
        divide(5, 0)
    except ZeroDivisionError:
        pass
    # Другие вызовы
    print(greet('Alice'))
    print(greet('Bob', greeting='Hi'))
