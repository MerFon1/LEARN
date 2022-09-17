"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/2lnbu3n7Y_w

Большой подвиг 8. Вы начинаете разрабатывать игру "Сапер". Для этого вам нужно уметь представлять и управлять игровым полем.
Будем полагать, что оно имеет размеры N x M клеток. Каждая клетка будет представлена объектом класса Cell и содержать либо число мин вокруг этой клетки, либо саму мину.


Для начала в программе объявите класс GamePole, который будет создавать и управлять игровым полем. Объект этого класса должен формироваться командой:

pole = GamePole(N, M, total_mines)
И, так как поле в игре одно, то нужно контролировать создание только одного объекта класса GamePole (используйте паттерн Singleton, о котором мы с вами говорили, когда рассматривали магический метод __new__()).

Объект pole должен иметь локальный приватный атрибут:

__pole_cells - двумерный (вложенный) кортеж, размерами N x M элементов (N строк и M столбцов), состоящий из объектов класса Cell.

Для доступа к этой коллекции объявите в классе GamePole объект-свойство (property):

pole - только для чтения (получения) ссылки на коллекцию __pole_cells.

Далее, в самом классе GamePole объявите следующие методы:

init_pole() - для инициализации начального состояния игрового поля (расставляет мины и делает все клетки закрытыми);
open_cell(i, j) - открывает ячейку с индексами (i, j); нумерация индексов начинается с нуля; метод меняет значение атрибута __is_open объекта Cell в ячейке (i, j) на True;
show_pole() - отображает игровое поле в консоли (как именно сделать - на ваше усмотрение, этот метод - домашнее задание).

Расстановку мин выполняйте случайным образом по игровому полю (для этого удобно воспользоваться функцией randint модуля random). После расстановки всех total_mines мин, вычислите их количество вокруг остальных клеток (где нет мин). Область охвата - соседние (прилегающие) клетки (8 штук).

В методе open_cell() необходимо проверять корректность индексов (i, j). Если индексы указаны некорректно, то генерируется исключение командой:

raise IndexError('некорректные индексы i, j клетки игрового поля')
Следующий класс Cell описывает состояние одной ячейки игрового поля. Объекты этого класса создаются командой:

cell = Cell()
При этом в самом объекте создаются следующие локальные приватные свойства:

__is_mine - булево значение True/False; True - в клетке находится мина, False - мина отсутствует;
__number - число мин вокруг клетки (целое число от 0 до 8);
__is_open - флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.

Для работы с этими приватными атрибутами объявите в классе Cell следующие объекты-свойства с именами:

is_mine - для записи и чтения информации из атрибута __is_mine;
number - для записи и чтения информации из атрибута __number;
is_open - для записи и чтения информации из атрибута __is_open.

В этих свойствах необходимо выполнять проверку на корректность переданных значений (либо булево значение True/False, либо целое число от 0 до 8). Если передаваемое значение некорректно, то генерировать исключение командой:

raise ValueError("недопустимое значение атрибута")
С объектами класса Cell должна работать функция:

bool(cell)
которая возвращает True, если клетка закрыта и False - если открыта.

Пример использования классов (эти строчки в программе писать не нужно):

pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.show_pole()
P.S. В программе на экран выводить ничего не нужно, только объявить классы.
"""
from random import choice


class Cell:

    def __init__(self):
        self.__is_mine = False  # булево значение True/False; True - в клетке находится мина, False - мина отсутствует;
        self.__number = 0  # число мин вокруг клетки (целое число от 0 до 8);
        self.__is_open = False  # флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if value not in (True, False):
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if value not in (0, 1, 2, 3, 4, 5, 6, 7, 8):
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if value not in (True, False):
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = value

    def __bool__(self):
        return self.__is_open == False


class GamePole:
    __ban = False
    __link = None

    def __new__(cls, *args, **kwargs):
        if cls.__ban:
            return cls.__link
        cls.__link = super().__new__(cls)
        cls.__ban = True
        return cls.__link

    @classmethod
    def __del__(cls):
        cls.__ban = False
        cls.__link = None

    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells = tuple(tuple(Cell() for i in range(M)) for j in range(N))

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        set_up_mines = 0
        for i in range(self.N):
            for j in range(self.M):
                self.__pole_cells[i][j].__is_open = False
                if set_up_mines != self.total_mines:
                    is_min = choice([True, False])
                    if is_min:
                        set_up_mines += 1
                        self.__pole_cells[i][j].is_mine = is_min
                    else:
                        self.__pole_cells[i][j].is_mine = is_min

        indx = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(self.N):
            for j in range(self.M):
                coun = 0
                for x in indx:
                    i2, j2 = x
                    if i + i2 < 0 or j + j2 < 0:
                        continue
                    try:
                        if self.__pole_cells[i + i2][j + j2].is_mine == True:
                            coun += 1
                    except:
                        pass
                self.__pole_cells[i][j].number = coun

    def open_cell(self, i, j):
        if i > self.N or i < 0 or j > self.M or j < 0:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.__pole_cells[i][j].is_open = True
        indx = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for x in indx:
            i2, j2 = x
            if i + i2 < 0 or j + j2 < 0:
                continue
            try:
                if self.__pole_cells[i + i2][j + j2].is_open:
                    continue

                self.__pole_cells[i + i2][j + j2].is_open = True

                if self.__pole_cells[i + i2][j + j2].is_mine:
                    self.open_cell(i + i2, j + j2)
            except IndexError:
                pass

    def show_pole(self):
        # ◉ - Close cell
        # ☆ - mine
        # ○ - Open cell, not mine around
        # (1, 2, 3, 4, 5, 6, 7, 8) - Open cell, there is a mine around
        public_pole = [['◉' for j in range(self.M)] for i in range(self.N)]
        for i in range(self.N):
            for j in range(self.M):
                if self.__pole_cells[i][j].is_open:
                    if self.__pole_cells[i][j].is_mine:
                        public_pole[i][j] = '☆'
                    else:
                        if self.__pole_cells[i][j].number > 0:
                            public_pole[i][j] = self.__pole_cells[i][j].number
                        else:
                            public_pole[i][j] = '○'
        [print(*i, sep=' ') for i in public_pole]
