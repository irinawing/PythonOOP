"""
Задание 92.
📌 Создайте функцию аналог get для словаря.
📌 Помимо самого словаря функция принимает ключ и
значение по умолчанию.
📌 При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
📌 Реализуйте работу через обработку исключений.
"""


def dict_get(dictionary, key, default=None):
    """
    Аналог метода get() для словаря.

    :param dictionary: Словарь, из которого получаем значение.
    :param key: Ключ, значение которого нужно получить.
    :param default: Значение по умолчанию, если ключ не существует (по умолчанию None).
    :return: Значение ключа или default, если ключа нет.
    """
    try:
        return dictionary[key]
    except KeyError:
        return default


# Пример использования
if __name__ == "__main__":
    my_dict = {"a": 1, "b": 2, "c": 3}

    # Ключ существует
    print(dict_get(my_dict, "a", "default_value"))  # Вывод: 1

    # Ключ не существует
    print(dict_get(my_dict, "x", "default_value"))  # Вывод: default_value

    # Без указания default (вернёт None)
    print(dict_get(my_dict, "y"))  # Вывод: None