"""
Задание 3. Напишите 2-4 unittest-теста
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""

import unittest
from check_triangle import check_triangle

class TestCheckTriangle(unittest.TestCase):
    """
    Юнит-тесты для функции check_triangle из модуля check_triangle.py
    Проверяются следующие сценарии:
    1. Разносторонний треугольник
    2. Равносторонний треугольник
    3. Равнобедренный треугольник
    4. Несуществующий треугольник
    5. Дополнительный несуществующий треугольник
    """

    def test_scalene_triangle(self):
        # Разносторонний
        result = check_triangle(3, 4, 5)
        self.assertEqual(result, 'Треугольник существует. Треугольник разносторонний')

    def test_equilateral_triangle(self):
        # Равносторонний
        result = check_triangle(5, 5, 5)
        self.assertEqual(result, 'Треугольник существует. Треугольник равносторонний')

    def test_isosceles_triangle(self):
        # Равнобедренный
        result = check_triangle(5, 5, 8)
        self.assertEqual(result, 'Треугольник существует. Треугольник равнобедренный')

    def test_nonexistent_triangle_border(self):
        # Граничный случай: сумма двух равна третьей -> не существует
        result = check_triangle(1, 2, 3)
        self.assertEqual(result, 'Треугольник не существует')

    def test_nonexistent_triangle_negative(self):
        # Несуществующий треугольник, одна сторона слишком велика
        result = check_triangle(10, 1, 2)
        self.assertEqual(result, 'Треугольник не существует')

if __name__ == '__main__':
    unittest.main()
