"""
Задание 1

Напишите декоратор для замеров времени выполнения любой функции
Для реализации замеров воспользуйтесь модулем timeit

Реализуйте декоратор в виде функции и класса
"""

import timeit
from functools import wraps

# Функциональный декоратор для измерения времени выполнения функции
def timeit_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        end = timeit.default_timer()
        print(f"[timeit_decorator] Функция {func.__name__} выполнена за {end - start:.6f} секунд")
        return result
    return wrapper

# Класс-декоратор для измерения времени выполнения функции
class TimeitDecorator:
    def __init__(self, func):
        wraps(func)(self)  # сохраняем метаданные оригинальной функции
        self.func = func

    def __call__(self, *args, **kwargs):
        start = timeit.default_timer()
        result = self.func(*args, **kwargs)
        end = timeit.default_timer()
        print(f"[TimeitDecorator] Функция {self.func.__name__} выполнена за {end - start:.6f} секунд")
        return result

# Примеры использования
@timeit_decorator
def compute_sum(n):
    #Пример функции — суммирует числа от 0 до n-1."""
    return sum(range(n))
#
@TimeitDecorator
def compute_prod(n):
    #Пример функции — перемножает числа от 1 до n.
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

# Выполнение

compute_sum(1000000)
compute_prod(10000)
