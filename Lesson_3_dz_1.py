"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет)
и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

import time

class TrafficLight:

    def __init__(self):
        # Приватный атрибут текущего цвета
        self.__color = None

    def running(self):

        # Список режимов: (название, длительность в секундах)
        modes = [
            ("Красный", 7),
            ("Желтый", 2),
            ("Зеленый", 5)
        ]
        # Бесконечный цикл переключения
        while True:
            for color, delay in modes:
                self.__color = color
                print(f"Светофор: {self.__color}")
                time.sleep(delay)


tl = TrafficLight()
tl.running()
