"""
Задание 93.
📌 Создайте класс с базовым исключением и дочерние классы-
исключения:
○ ошибка уровня,
○ ошибка доступа.
"""
class BaseCustomException(Exception):
    """Базовое пользовательское исключение."""
    pass


class LevelError(BaseCustomException):
    """Ошибка уровня (например, недостаточный уровень доступа)."""
    pass


class AccessError(BaseCustomException):
    """Ошибка доступа (например, отказ в доступе)."""
    pass


# Пример использования
if __name__ == "__main__":
    try:
        raise LevelError("Недостаточный уровень доступа!")
    except LevelError as e:
        print(f"Поймано исключение LevelError: {e}")

    try:
        raise AccessError("Доступ запрещён!")
    except AccessError as e:
        print(f"Поймано исключение AccessError: {e}")