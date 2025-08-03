"""
Задание 2
Реализуйте декоратор для записи в файл
"""

from functools import wraps

def log_to_file(filepath):
    """
    Декоратор-фабрика, создающий декоратор, который записывает информацию о вызовах
    функции в указанный файл.

    В лог пишутся:
    - имя функции
    - переданные args и kwargs
    - возвращаемое значение или информация об исключении
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_line = (
                    f"Function '{func.__name__}' called with args={args}, kwargs={kwargs} -> returned {result}\n"
                )
            except Exception as e:
                log_line = (
                    f"Function '{func.__name__}' called with args={args}, kwargs={kwargs} -> raised {e.__class__.__name__}: {e}\n"
                )
                # Записать до повторного поднятия исключения
                with open(filepath, 'a', encoding='utf-8') as f:
                    f.write(log_line)
                raise
            # Запись успешного вызова в файл
            with open(filepath, 'a', encoding='utf-8') as f:
                f.write(log_line)
            return result
        return wrapper
    return decorator

# Пример использования
if __name__ == '__main__':
    @log_to_file('func_calls.log')
    def divide(a, b):
        return a / b

    @log_to_file('func_calls.log')
    def greet(name, greeting='Hello'):
        return f"{greeting}, {name}!"

    # Вызовы функций для демонстрации
    print(divide(10, 2))   # 5.0
    try:
        divide(5, 0)
    except ZeroDivisionError:
        pass
    print(greet('Alice'))  # Hello, Alice!
    print(greet('Bob', greeting='Hi'))  # Hi, Bob!
