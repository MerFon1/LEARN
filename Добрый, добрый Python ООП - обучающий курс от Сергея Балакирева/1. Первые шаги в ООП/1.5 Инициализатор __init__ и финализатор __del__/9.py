"""
С помощью класса Cell предполагается создавать отдельные клетки командой:

c1 = Cell(around_mines, mine)
Здесь around_mines - число мин вокруг данной клетки поля; mine - булева величина (True/False), означающая наличие мины в текущей клетке. При этом, в каждом объекте класса Cell должны создаваться локальные свойства:

around_mines - число мин вокруг клетки (начальное значение 0);
mine - наличие мины в текущей клетке (True/False);
fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False).



С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:

pole_game = GamePole(N, M)
Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка представляется объектом класса Cell и все объекты хранятся в двумерном списке N x N элементов - локальном свойстве pole объекта класса GamePole.

В классе GamePole должны быть также реализованы следующие методы:

init() - инициализация поля с новой расстановкой M мин (случайным образом по игровому полю, разумеется каждая мина должна находиться в отдельной клетке).
show() - отображение поля в консоли в виде таблицы чисел открытых клеток (если клетка не открыта, то отображается символ #).

При создании экземпляра класса GamePole в его инициализаторе следует вызывать метод init() для первоначальной инициализации игрового поля.

В классе GamePole могут быть и другие вспомогательные методы.

Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12.

P.S. На экран в программе ничего выводить не нужно.
"""
from random import choice

class Cell:

    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

class GamePole:

    def __init__(self, N, M):
        self.pole = [[Cell() for j in range(N)] for i in range(N)]
        self.M = M

    def init(self):
        counter = 0
        for i in range(len(self.pole)):
            for j in range(len(self.pole)):
                if counter<self.M+1:
                    val = choice([True, False])
                    if val:
                        counter += 1
                        self.pole[i][j].mine = val
                    else:
                        continue
                else:
                    break

        indx = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(len(self.pole)):
            for j in range(len(self.pole)):
                counter = 0
                for x in indx:
                    i2, j2 = x
                    if i + i2 < 0 or j + j2 < 0:
                        continue
                    try:
                        if self.pole[i + i2][j + j2].mine == True:
                            counter += 1
                    except:
                        pass
                self.pole[i][j].around_mines = counter

    def show(self):
        public_list = [['#' for j in range(len(self.pole))] for i in range(len(self.pole))]
        for i in range(len(self.pole)):
            for j in range(len(self.pole)):
                if self.pole[i][j].fl_open:
                    if self.pole[i][j].mine:
                        public_list[i][j] = '*'
                    else:
                        public_list[i][j] = self.pole[i][j].around_mines
        print(public_list)

pole_game = GamePole(10,12)
assert isinstance(pole_game, GamePole) and hasattr(GamePole, 'init') and hasattr(GamePole, 'show')

Cell.__doc__

N = 10
M = 10


def get_around_mines(i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k + i, l + j
            if ii < 0 or jj < 0 or ii >= N or jj >= N:
                continue
            if pole_game.pole[ii][jj].mine:
                n += 1
    return n


for i in range(N):
    for j in range(N):
        if not pole_game.pole[i][j].mine:
            assert pole_game.pole[i][j].around_mines == get_around_mines(i,
                                                                         j), f"неверное число мин вокруг клетки с индексами {i, j}"
