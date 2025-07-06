"""
Задание 1
📌 Создайте прямоугольник с методами расчета периметра и площади
📌 Добавьте сравнение прямоугольников по площади
📌 Должны работать все шесть операций сравнения
"""

class Rectangle:
    """
    Класс прямоугольника с методами расчета периметра и площади,
    а также перегрузкой операторов сравнения по площади.
    """
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными")
        self.width = width
        self.height = height

    def perimeter(self) -> float:
        """Вычисляет периметр прямоугольника."""
        return 2 * (self.width + self.height)

    def area(self) -> float:
        """Вычисляет площадь прямоугольника."""
        return self.width * self.height

    # Операции сравнения по площади
    def __eq__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() == other.area()

    def __ne__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() != other.area()

    def __lt__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() <= other.area()

    def __gt__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() >= other.area()

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

# Пример использования
if __name__ == "__main__":
    r1 = Rectangle(3, 4)
    r2 = Rectangle(2, 6)
    r3 = Rectangle(3, 4)
    print(f"r1 area: {r1.area()}, perimeter: {r1.perimeter()}")
    print(f"r2 area: {r2.area()}, perimeter: {r2.perimeter()}")
    print("r1 == r2?", r1 == r2)
    print("r1 != r2?", r1 != r2)
    print("r1 < r2?", r1 < r2)
    print("r1 <= r3?", r1 <= r3)
    print("r2 > r1?", r2 > r1)
    print("r2 >= r1?", r2 >= r1)
