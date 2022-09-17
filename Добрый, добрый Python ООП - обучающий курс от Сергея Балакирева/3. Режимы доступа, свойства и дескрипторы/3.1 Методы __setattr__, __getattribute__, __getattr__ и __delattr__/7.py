"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/2iS8qnEK9to

Подвиг 9. Объявите в программе класс Dimensions (габариты) с атрибутами:

MIN_DIMENSION = 10
MAX_DIMENSION = 1000

Каждый объект класса Dimensions должен создаваться командой:

d3 = Dimensions(a, b, c)   # a, b, c - габаритные размеры
и содержать локальные атрибуты:

__a, __b, __c - габаритные размеры (целые или вещественные числа).

Для работы с этими локальными атрибутами в классе Dimensions следует прописать следующие объекты-свойства:

a, b, c - для изменения и считывания соответствующих локальных атрибутов __a, __b, __c.

При изменении значений __a, __b, __c следует проверять, что присваиваемое значение число в диапазоне [MIN_DIMENSION; MAX_DIMENSION]. Если это не так, то новое значение не присваивается (игнорируется).

С помощью магических методов данного занятия запретить создание локальных атрибутов MIN_DIMENSION и MAX_DIMENSION в объектах класса Dimensions. При попытке это сделать генерировать исключение:

raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
Пример использования класса  (эти строчки в программе писать не нужно):

d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
d.MAX_DIMENSION = 10  # исключение AttributeError
P.S. На экран ничего выводить не нужно.
"""


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000
    ta = 0
    tb = 0
    tc = 0

    def __init__(self, a, b, c):
        self.ta = a
        self.tb = b
        self.tc = c

    @property
    def a(self):
        return self.ta

    @a.setter
    def a(self, value):
        self.ta = value

    @property
    def b(self):
        return self.tb

    @b.setter
    def b(self, value):
        self.tb = value

    @property
    def c(self):
        return self.tc

    @c.setter
    def c(self, value):
        self.tc = value

    def __setattr__(self, key, value):
        if key == 'MIN_DIMENSION' or key == 'MAX_DIMENSION':
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")

        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            return object.__setattr__(self, key, value)

d = Dimensions(10,20,30)
print(d.a == 10)
print(d.b == 20)
print(d.c == 30)
