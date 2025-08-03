"""
Задание 1.
Реализуйте логгирование в файл и в поток для любой из задач используя продвинутое логгирование
"""


import logging
import sys

# Настройка логгера
logger = logging.getLogger('advanced_logger')
logger.setLevel(logging.DEBUG)

# Форматтер для логов
formatter = logging.Formatter('%(asctime)s %(levelname)s [%(name)s] %(funcName)s: %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')

# Файловый обработчик (DEBUG и выше)
file_handler = logging.FileHandler('advanced.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Консольный обработчик (INFO и выше)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)

# Добавляем обработчики к логгеру
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def divide(a, b):
    """
    Делит a на b, логирует результат и ошибки.
    """
    try:
        result = a / b
        logger.info(f"divide({a}, {b}) = {result}")
        return result
    except ZeroDivisionError as e:
        logger.error(f"divide({a}, {b}) - ошибка: {e}")
        return None


def compute_factorial(n):
    """
    Вычисляет факториал n рекурсивно, логируя начало и конец функции.
    """
    logger.debug(f"Вход в compute_factorial: n={n}")
    if n < 0:
        logger.error(f"Неверный аргумент для factorial: {n}")
        raise ValueError("n must be >= 0")
    if n in (0, 1):
        logger.debug(f"Базовый случай factorial: n={n}")
        return 1
    result = n * compute_factorial(n - 1)
    logger.debug(f"compute_factorial({n}) = {result}")
    return result


if __name__ == '__main__':
    # Примеры использования
    divide(10, 2)
    divide(5, 0)
    logger.info(f"Factorial of 5: {compute_factorial(5)}")
    try:
        compute_factorial(-1)
    except ValueError:
        pass
