"""
Задание 1.

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivisionByZeroError(Exception):
    """Пользовательское исключение для деления на ноль."""

    def __init__(self, message="Деление на ноль недопустимо!"):
        self.message = message
        super().__init__(self.message)


def safe_divide(dividend, divisor):
    """
    Выполняет деление и обрабатывает деление на ноль.

    :param dividend: Делимое (число, которое делим).
    :param divisor: Делитель (число, на которое делим).
    :return: Результат деления.
    :raises DivisionByZeroError: Если делитель равен нулю.
    """
    if divisor == 0:
        raise DivisionByZeroError()
    return dividend / divisor


# Пример использования
if __name__ == "__main__":
    try:
        dividend = float(input("Введите делимое: "))
        divisor = float(input("Введите делитель: "))

        result = safe_divide(dividend, divisor)
        print(f"Результат деления: {result}")

    except DivisionByZeroError as e:
        print(f"Ошибка: {e}")
    except ValueError:
        print("Ошибка: Введены некорректные данные (требуется число).")