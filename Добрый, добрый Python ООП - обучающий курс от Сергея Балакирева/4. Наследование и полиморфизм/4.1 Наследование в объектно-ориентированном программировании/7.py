"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/I8upOO_ZjqQ

Большой подвиг 9. Используя механизм наследования, вам поручено разработать функционал по построению моделей нейронных сетей. Общая схема модели очень простая:



Базовый класс Layer имеет локальный атрибут next_layer, который ссылается на следующий объект слоя нейронной сети (объект класса Layer или любого объекта дочерних классов). У последнего слоя значение next_layer = None.

Создавать последовательность слоев предполагается командами:

first_layer = Layer()
next_layer = first_layer(Layer())
next_layer = next_layer(Layer())
...
То есть, сначала создается объект first_layer класса Layer, а затем он вызывается как функция для образования связки со следующим слоем. При этом возвращается ссылка на следующий слой и переменная next_layer ссылается уже на этот следующий слой нейронной сети. И так можно создавать столько слоев, сколько необходимо.

В каждом объекте класса Layer также должен формироваться локальный атрибут:

name = 'Layer'

Но сам по себе класс Layer образует только связи между слоями. Никакой другой функциональности он не несет. Чтобы это исправить, в программе нужно объявить еще два дочерних класса:

Input - формирование входного слоя нейронной сети;
Dense - формирование полносвязного слоя нейронной сети.



Конечно, создавать нейронную сеть мы не будем. Поэтому, в классе Input нужно лишь прописать инициализатор так, чтобы его объекты создавались следующим образом:

inp = Input(inputs)
где inputs - общее число входов (целое число). Также в объектах класса Input должен автоматически формироваться атрибут:

name = 'Input'

(Не забывайте при этом, вызывать инициализатор базового класса Layer).

Объекты второго дочернего класса Dense предполагается создавать командой:

dense = Dense(inputs, outputs, activation)
где inputs - число входов в слой; outputs - число выходов слоя (целые числа); activation - функция активации (строка, например: 'linear', 'relu', 'sigmoid'). И в каждом объекте класса Dense также должен автоматически формироваться атрибут:

name = 'Dense'

Все эти классы совместно можно использовать следующим образом (эти строчки пример, писать не нужно):

network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))
Здесь создается три слоя нейронной сети.

Наконец, для перебора всех слоев с помощью цикла for, необходимо объявить отдельный класс NetworkIterator для итерирования (перебора) слоев нейронной сети следующим образом:

for x in NetworkIterator(network):
    print(x.name)
Здесь создается объект класса NetworkIterator. На вход передается первый объект (слой) нейронной сети. Объект этого класса является итератором, который в цикле for последовательно возвращает объекты (слои) нейронной сети.

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""


class Vector:

    def __init__(self, *args):
        self.coords = list(args)

    def _check_len(self, list_coords1: list, list_coords2: list):
        if len(list_coords1) != len(list_coords2):
            raise TypeError('размерности векторов не совпадают')

    def get_coords(self):
        return tuple(self.coords)

    def __add__(self, other):
        self._check_len(self.coords, other.coords)

        new_list = [self.coords[index] + other.coords[index] for index in range(len(self.coords))]
        return Vector(*new_list)

    def __sub__(self, other):
        self._check_len(self.coords, other.coords)

        new_list = [self.coords[index] - other.coords[index] for index in range(len(self.coords))]
        return Vector(*new_list)


class VectorInt(Vector):

    def __init__(self, *args):
        if self._check_type(list(args)):
            raise ValueError('координаты должны быть целыми числами')
        else:
            self.coords = list(args)

    def _check_type(self, list):

        for i in list:
            if type(i) != int:
                return True
        return False

    def __add__(self, other):
        self._check_len(self.coords, other.coords)

        new_list = [self.coords[index] + other.coords[index] for index in range(len(self.coords))]

        if self._check_type(new_list):
            return Vector(*new_list)
        else:
            return VectorInt(*new_list)

    def __sub__(self, other):
        self._check_len(self.coords, other.coords)

        new_list = [self.coords[index] - other.coords[index] for index in range(len(self.coords))]

        if self._check_type(new_list):
            return Vector(*new_list)
        else:
            return VectorInt(*new_list)


v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)

assert (v1 + v2).get_coords() == (
    4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (
    -2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

v = VectorInt(1, 2, 3, 4)
assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"

try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"

v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1 + v2
assert type(
    v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1 + v3
assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"