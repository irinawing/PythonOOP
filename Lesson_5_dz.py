"""
Задание 1.

Реализовать программу работы с органическими клетками, состоящими из ячеек.

Необходимо создать класс Клетка (Cell).

В его конструкторе инициализировать параметр (quantity),
соответствующий количеству ячеек клетки (целое число).

В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()),
вычитание (sub()),
умножение (mul()),
деление (truediv()).

Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток.
При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.


------------------------------------------------------------------------------
Пример клиентского кода:
print("Создаем объекты клеток")
cell1 = Cell(30)
cell2 = Cell(25)

cell3 = Cell(10)
cell4 = Cell(15)

print()

print("Складываем")
print(cell1 + cell2)

print()

print("Вычитаем")
print(cell2 - cell1)
print(cell4 - cell3)

print()

print("Умножаем")
print(cell2 * cell1)

print()

print("Делим")
print(cell1 / cell2)

print()


------------------------------------------------------------------------------
Результаты:
Создаем объекты клеток

Складываем
Сумма клеток = (55)

Вычитаем
Разность отрицательна, поэтому операция не выполняется
Разность клеток = (5)

Умножаем
Умножение клеток = (750)

Делим
Деление клеток = (1)

"""

class Cell:
    """
    Класс клетки с заданным количеством ячеек.
    Перегрузка арифметических операторов для работы только с Cell.
    Операции возвращают строку-результат в формате примера.
    """
    def __init__(self, quantity: int):
        if not isinstance(quantity, int) or quantity < 1:
            raise ValueError("Количество ячеек должно быть натуральным числом")
        self.quantity = quantity

    def __add__(self, other):
        if not isinstance(other, Cell):
            return NotImplemented
        total = self.quantity + other.quantity
        return f"Сумма клеток = ({total})"

    def __sub__(self, other):
        if not isinstance(other, Cell):
            return NotImplemented
        diff = self.quantity - other.quantity
        if diff > 0:
            return f"Разность клеток = ({diff})"
        return "Разность отрицательна, поэтому операция не выполняется"

    def __mul__(self, other):
        if not isinstance(other, Cell):
            return NotImplemented
        prod = self.quantity * other.quantity
        return f"Умножение клеток = ({prod})"

    def __truediv__(self, other):
        if not isinstance(other, Cell):
            return NotImplemented
        if other.quantity == 0:
            return "Деление на клетку с нулевым количеством ячеек невозможно"
        div = self.quantity // other.quantity
        return f"Деление клеток = ({div})"

    def __repr__(self):
        return f"Cell({self.quantity})"

# Пример клиентского кода
if __name__ == "__main__":
    print("Создаем объекты клеток")
    cell1 = Cell(30)
    cell2 = Cell(25)

    cell3 = Cell(10)
    cell4 = Cell(15)

    print()

    print("Складываем")
    print(cell1 + cell2)

    print()

    print("Вычитаем")
    print(cell2 - cell1)
    print(cell4 - cell3)

    print()

    print("Умножаем")
    print(cell2 * cell1)

    print()

    print("Делим")
    print(cell1 / cell2)

    print()
