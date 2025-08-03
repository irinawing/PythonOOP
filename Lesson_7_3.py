"""
Задание 3
📌 Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
📌 возврат строки без изменений
📌 возврат строки с преобразованием регистра без потери
символов
📌 возврат строки с удалением знаков пунктуации
📌 возврат строки с удалением букв других алфавитов
📌 возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""

import unittest
from doctest_clean_text import clean_text

class TestCleanText(unittest.TestCase):
    """
    Юнит-тесты для функции clean_text из doctest_clean_text.py
    Проверяются сценарии:
    1. Возврат строки без изменений
    2. Преобразование регистра без потери символов
    3. Удаление знаков пунктуации
    4. Удаление букв других алфавитов
    5. Совмещение всех вышеперечисленных (кроме чистой строки)
    """

    def test_no_change(self):
        # 1. Возврат строки без изменений
        text = "hello world"
        self.assertEqual(clean_text(text), "hello world")

    def test_to_lowercase(self):
        # 2. Преобразование регистра без потери символов
        text = "HeLLo WoRLD"
        self.assertEqual(clean_text(text), "hello world")

    def test_remove_punctuation(self):
        # 3. Удаление знаков пунктуации
        text = "Hello, world!"
        self.assertEqual(clean_text(text), "hello world")

    def test_remove_non_latin(self):
        # 4. Удаление букв других алфавитов
        text = "Привет hello"
        self.assertEqual(clean_text(text), " hello")

    def test_combined(self):
        # 5. Комбинированный сценарий
        text = "Abc, Привет! XYZ123?!"
        expected = "abc  xyz"
        self.assertEqual(clean_text(text), expected)

if __name__ == '__main__':
    unittest.main()
