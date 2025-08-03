"""
Задание 4
📌 Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
📌 возврат строки без изменений
📌 возврат строки с преобразованием регистра без потери
символов
📌 возврат строки с удалением знаков пунктуации
📌 возврат строки с удалением букв других алфавитов
📌 возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""

import pytest
from doctest_clean_text import clean_text

@ pytest.mark.parametrize("input_text, expected", [
    # 1. Возврат строки без изменений
    ("hello world", "hello world"),
    # 2. Преобразование регистра без потери символов
    ("HeLLo WoRLD", "hello world"),
    # 3. Удаление знаков пунктуации
    ("Hello, world!", "hello world"),
    # 4. Удаление букв других алфавитов
    ("Привет hello", " hello"),
    # 5. Сочетание всех пунктов (кроме чистой строки)
    ("Abc, Привет! XYZ123?!", "abc  xyz"),
])
def test_clean_text(input_text, expected):
    assert clean_text(input_text) == expected
