"""
Задание 2
📌 Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
📌 возврат строки без изменений
📌 возврат строки с преобразованием регистра без потери
символов
📌 возврат строки с удалением знаков пунктуации
📌 возврат строки с удалением букв других алфавитов
📌 возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""
import re

def clean_text(text: str) -> str:
    """
    Удаляет из текста все символы, кроме букв латинского алфавита и пробелов,
    и возвращает результат в нижнем регистре.

    doctest examples:
    >>> clean_text("hello world")
    'hello world'
    >>> clean_text("Hello World")
    'hello world'
    >>> clean_text("Hello, world!")
    'hello world'
    >>> clean_text("Привет world")
    'world'
    >>> clean_text("Abc, Привет! XYZ")
    'abc  xyz'
    """
    cleaned = re.sub(r'[^A-Za-z ]+', '', text)
    return cleaned.lower()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
