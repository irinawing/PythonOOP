"""
Задание 1.
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.
"""

from functools import wraps

def repeat(times):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

# Пример использования
if __name__ == "__main__":
    @repeat(3)
    def greet(name):
        print(f"Привет, {name}!")
        return f"Приветствуем, {name}"

    # Вызов функции:
    outputs = greet("Светлана")  # функция запустится 3 раза
    print(outputs)
