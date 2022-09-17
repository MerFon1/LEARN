"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/0EYz8-qG2iU

Подвиг 10 (на повторение). Объявите класс с именем Triangle, объекты которого создаются командой:

tr = Triangle(a, b, c)
где a, b, c - длины сторон треугольника (числа: целые или вещественные). В классе Triangle объявите следующие дескрипторы данных:

a, b, c - для записи и считывания длин сторон треугольника.

При записи нового значения нужно проверять, что присваивается положительное число (целое или вещественное). Иначе, генерируется исключение командой:

raise ValueError("длины сторон треугольника должны быть положительными числами")
Также нужно проверять, что все три стороны a, b, c могут образовывать стороны треугольника. То есть, должны выполняться условия:

a < b+c; b < a+c; c < a+b

Иначе генерируется исключение командой:

raise ValueError("с указанными длинами нельзя образовать треугольник")
Наконец, с объектами класса Triangle должны выполняться функции:

len(tr) - возвращает периметр треугольника, приведенный к целому значению с помощью функции int();
tr() - возвращает площадь треугольника (можно вычислить по формуле Герона: s = sqrt(p * (p-a) * (p-b) * (p-c)), где p - полупериметр треугольника).

P.S. На экран ничего выводить не нужно, только объявить класс Triangle.
"""
from math import sqrt

class Descriptor_data:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if type(value) not in (int, float) or value < 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        instance.__dict__[self.name] = value


class Triangle:
    a = Descriptor_data()
    b = Descriptor_data()
    c = Descriptor_data()

    def __init__(self, a, b, c):
        if a > b + c or b > a + c or c > a + b:
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        self.a = a
        self.b = b
        self.c = c
        self.perimeter = self.a + self.b + self.c
        self.p = self.perimeter/2

    def __len__(self):
        return int(self.perimeter)

    def __call__(self, *args, **kwargs):
        return sqrt(self.p * (self.p-self.a) * (self.p-self.b) * (self.p-self.c))


tr = Triangle(5, 4, 3)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"
