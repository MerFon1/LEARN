"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/cHV-yuNFavg

Подвиг 3. Объявите класс Track (маршрут), объекты которого создаются командой:

track = Track(start_x, start_y)
где start_x, start_y - координаты начала маршрута (целые или вещественные числа).

Каждый линейный сегмент маршрута определяется классом TrackLine, объекты которого создаются командой:

line = TrackLine(to_x, to_y, max_speed)
где to_x, to_y - координаты следующей точки маршрута (целые или вещественные числа); max_speed - максимальная скорость на данном участке (целое число).

Для формирования и работы с маршрутом в классе Track должны быть объявлены следующие методы:

add_track(self, tr) - добавление линейного сегмента маршрута (следующей точки);
get_tracks(self) - получение кортежа из объектов класса TrackLine.

Также для объектов класса Track должны быть реализованные следующие операции сравнения:

track1 == track2  # маршруты равны, если равны их длины
track1 != track2  # маршруты не равны, если не равны их длины
track1 > track2  # True, если длина пути для track1 больше, чем для track2
track1 < track2  # True, если длина пути для track1 меньше, чем для track2
И функция:

n = len(track) # возвращает целочисленную длину маршрута (привести к типу int) для объекта track
Создайте два маршрута track1 и track2 с координатами:

1-й маршрут: (0; 0), (2; 4), (5; -4) и max_speed = 100
2-й маршрут: (0; 1), (3; 2), (10; 8) и max_speed = 90

Сравните их между собой на равенство. Результат сравнения сохраните в переменной res_eq.

P.S. На экран в программе ничего выводить не нужно.
"""


class Box:

    def __init__(self):
        self.__data = []

    def add_thing(self, obj):
        self.__data.append(obj)

    def get_things(self):
        return self.__data

    def __eq__(self, other):
        if len(self.__data) != len(other.__data):
            return False

        r = []
        for i in range(len(self.__data)):
            p = []
            for j in range(len(other.__data)):
                p.append(self.__data[i] == other.__data[j])
            r.append(True in p)
        return all(r)

class Thing:

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return all([self.name.lower() == other.name.lower(), self.mass == other.mass])


b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2

