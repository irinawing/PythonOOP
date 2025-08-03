"""
Задание 1
📌 Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
📌 Например отлавливаем ошибку деления на ноль.
"""

import logging

# Настройка логирования: ошибки будут записаны в файл error.log
logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def divide(a, b):
    """
    Делит a на b, при делении на ноль логгирует ошибку и возвращает None.
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error("Ошибка деления: попытка разделить %s на %s", a, b, exc_info=True)
        return None

if __name__ == "__main__":
    # Пример работы
    result = divide(10, 0)
    if result is None:
        print("Произошла ошибка деления — смотрите details в error.log")
    else:
        print("Результат:", result)
