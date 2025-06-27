"""
Задание 1.
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""

class Person:

    def __init__(self, first_name: str, last_name: str, middle_name: str = None, age: int = 0):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self._age = age

    @property
    def age(self) -> int:
        #Только для чтения: возвращает текущий возраст
        return self._age

    def full_name(self) -> str:
        #Возвращает ФИО человека
        parts = [self.first_name]
        if self.middle_name:
            parts.append(self.middle_name)
        parts.append(self.last_name)
        return " ".join(parts)

    def birthday(self) -> None:
        #Увеличивает возраст на один год
        self._age += 1

    def __str__(self) -> str:
        return f"{self.full_name()}, возраст: {self.age}"

# Создаём объект человека
p = Person(first_name="Иван", middle_name="Сергеевич", last_name="Бунин", age=30)
print(p)

p.birthday()
print(f"После дня рождения: {p.age} лет")
print("ФИО:", p.full_name())