"""
Подвиг 9 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, x3,..., xN)
где x1, x2, x3,..., xN - координаты вектора (числа: целые или вещественные).

С каждым объектом класса Vector должны выполняться операторы:

v1 + v2 # суммирование соответствующих координат векторов
v1 - v2 # вычитание соответствующих координат векторов
v1 * v2 # умножение соответствующих координат векторов

v1 += 10 # прибавление ко всем координатам вектора числа 10
v1 -= 10 # вычитание из всех координат вектора числа 10
v1 += v2
v2 -= v1

v1 == v2 # True, если соответствующие координаты векторов равны
v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает
При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с новыми (вычисленными) координатами. При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.

Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -, * должно генерироваться исключение командой:

raise ArithmeticError('размерности векторов не совпадают')
P.S. В программе на экран выводить ничего не нужно, только объявить класс.
"""


class Vector:

    def __init__(self, *args):
        self.args = list(args)

    def test(self, other):
        if type(other) == Vector:
            return len(self.args) != len(other.args)
        else:
            return False

    def __eq__(self, other):
        if self.test(other):
            raise ArithmeticError('размерности векторов не совпадают')
        if type(other) == Vector:
            return self.args == other.args
        else:
            return self.args == other

    def __add__(self, other):
        if self.test(other):
            raise ArithmeticError('размерности векторов не совпадают')
        if type(other) == Vector:
            return Vector(*[self.args[i] + other.args[i] for i in range(len(self.args))])
        else:
            return Vector(*[self.args[i] + other for i in range(len(self.args))])

    def __sub__(self, other):
        if self.test(other):
            raise ArithmeticError('размерности векторов не совпадают')
        if type(other) == Vector:
            return Vector(*[self.args[i] - other.args[i] for i in range(len(self.args))])
        else:
            return Vector(*[self.args[i] - other for i in range(len(self.args))])

    def __mul__(self, other):
        if self.test(other):
            raise ArithmeticError('размерности векторов не совпадают')
        if type(other) == Vector:
            return Vector(*[self.args[i] * other.args[i] for i in range(len(self.args))])
        else:
            return Vector(*[self.args[i] * other for i in range(len(self.args))])

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).args)  # [5, 7, 9]
print((v1 - v2).args)  # [-3, -3, -3]
print((v1 * v2).args)  # [4, 10, 18]
v1 += 10
print(v1.args)  # [11, 12, 13]
v1 -= 10
print(v1.args)  # [1, 2, 3]
v1 += v2
print(v1.args)  # [5, 7, 9]
v2 -= v1
print(v2.args)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True
