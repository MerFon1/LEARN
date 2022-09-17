"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/kxCAnaAqdOk

Подвиг 7. Теперь, вам необходимо разработать итератор, который бы перебирал указанные столбцы двумерного списка. Список представляет собой двумерную таблицу из данных:

lst = [[x11, x12, ..., x1N],
       [x21, x22, ..., x2N],
       ...
       [xM1, xM2, ..., xMN]
      ]
Для этого в программе необходимо объявить класс с именем IterColumn, объекты которого создаются командой:

it = IterColumn(lst, column)
где lst - ссылка на двумерный список; column - индекс перебираемого столбца (отсчитывается от 0).

Затем, с объектами класса IterColumn должны быть доступны следующие операции:

it = IterColumn(lst, 1)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)

it_iter = iter(it)
x = next(it_iter)
P.S. В программе нужно объявить только класс итератора. Выводить на экран ничего не нужно.
"""


class IterColumn:

    def __init__(self, lst, column):
        self.lst = lst
        self.column = column

    def __iter__(self):
        self.index = -1
        self.list = [i[self.column] for i in self.lst]
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.list):
            return self.list[self.index]
        else:
            raise StopIteration


lst = [['x11', 'x12', 'x1N'],
       ['x21', 'x22', 'x2N'],
       ['xM1', 'xM2', 'xMN']
       ]
column = 0
it = IterColumn(lst, column)

it = IterColumn(lst, 1)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)

it_iter = iter(it)
x = next(it_iter)
