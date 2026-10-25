"""Задание 3.1. Методы класса Student.

Добавьте в класс Student два метода:
    is_excellent() — возвращает True, если балл не меньше 85;
    describe()     — возвращает строку вида «Анна (Б01-123): 92».

Проверьте оба метода на двух студентах с разными баллами.
"""


class Student:
    def __init__(self, name, group, score):
        self.name = name
        self.group = group
        self.score = score

    # TODO: добавьте метод is_excellent

    # TODO: добавьте метод describe


# TODO: создайте двух студентов и проверьте оба метода
