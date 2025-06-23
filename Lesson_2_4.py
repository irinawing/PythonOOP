"""
Задание 4.

Выведите строку по частям

Hello
Hell
Hel
He
H
"""

# data = "Hello"
#
#
# def func_1(data):
#     while len(data) != 0:
#         print(data)
#         data = data[:-1]
#
#
# func_1(data)

data = "Hello"

def func_1(data):
    """
    Рекурсивно печатает исходную строку и все её
    «срезы» без последнего символа до пустой строки.
    """
    if not data:
        return
    print(data)
    func_1(data[:-1])

func_1(data)