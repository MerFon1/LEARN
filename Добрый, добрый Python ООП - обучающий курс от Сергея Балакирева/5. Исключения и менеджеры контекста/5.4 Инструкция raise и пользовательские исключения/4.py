"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/wLaOyNN8x7E

Значимый подвиг 7. Вам поручается разработать класс TupleData, элементами которого могут являются только объекты классов: CellInteger, CellFloat и CellString.



Вначале в программе нужно объявить класс CellInteger, CellFloat и CellString, объекты которых создаются командами:

cell_1 = CellInteger(min_value, max_value)
cell_2 = CellFloat(min_value, max_value)
cell_3 = CellString(min_length, max_length)
где min_value, max_value - минимальное и максимальное допустимое значение в ячейке; min_length, max_length - минимальная и максимальная допустимая длина строки в ячейке.

В каждом объекте этих классов должны формироваться локальные атрибуты с именами _min_value, _max_value или _min_length, _max_length и соответствующими значениями.

Запись и считывание текущего значения в ячейке должно выполняться через объект-свойство (property) с именем:

value - для записи и считывания значения в ячейке (изначально возвращает значение None).

Если в момент записи новое значение не соответствует диапазону [min_value; max_value] или [min_length; max_length], то генерируется исключения командами:

raise CellIntegerException('значение выходит за допустимый диапазон')  # для объектов класса CellInteger
raise CellFloatException('значение выходит за допустимый диапазон')    # для объектов класса CellFloat
raise CellStringException('длина строки выходит за допустимый диапазон')  # для объектов класса CellString
Все три класса исключений должны быть унаследованы от одного общего класса:

CellException

Далее, объявите класс TupleData, объекты которого создаются командой:

ld = TupleData(cell_1, ..., cell_N)
где cell_1, ..., cell_N - объекты классов CellInteger, CellFloat и CellString (в любом порядке и любом количестве).

Обращение к отдельной ячейке должно выполняться с помощью оператора:

value = ld[index] # считывание значения из ячейке с индексом index
ld[index] = value # запись нового значения в ячейку с индексом index
Индекс index отсчитывается с нуля (для первой ячейки) и является целым числом. Если значение index выходит за диапазон [0; число ячеек-1], то генерировать исключение IndexError.

Также с объектами класса TupleData должны выполняться следующие функции и операторы:

res = len(ld) # возвращает общее число элементов (ячеек) в объекте ld
for d in ld:  # перебирает значения ячеек объекта ld (значения, а не объекты ячеек)
    print(d)
Все эти классы в программе можно использовать следующим образом:

ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")
P.S. Данная программа должна быть выполнена штатно, без ошибок. На экран отображать ничего не нужно.
"""


class CellException(Exception):
    pass


class CellIntegerException(CellException):
    pass


class CellFloatException(CellException):
    pass


class CellStringException(CellException):
    pass


class Cell:

    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._value = None


class CellInteger(Cell):

    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if self._min_value > val or self._max_value < val:
            raise CellIntegerException('значение выходит за допустимый диапазон')
        self._value = val


class CellFloat(Cell):

    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if self._min_value > val or self._max_value < val:
            raise CellFloatException('значение выходит за допустимый диапазон')

        self._value = val


class CellString(Cell):

    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if self._min_value > len(val) or self._max_value < len(val):
            raise CellStringException('длина строки выходит за допустимый диапазон')

        self._value = val


class TupleData:

    def __init__(self, *args):
        self.data = args

    def __setitem__(self, key, value):
        if key < 0 or key >= len(self.data):
            raise IndexError()
        self.data[key].value = value

    def __getitem__(self, item):
        if item < 0 or item >= len(self.data):
            raise IndexError()
        return self.data[item].value

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        self.counter = -1
        return self

    def __next__(self):
        self.counter += 1
        if self.counter < len(self.data):
            return self.data[self.counter].value
        raise StopIteration()




t = TupleData(CellInteger(-10, 10), CellInteger(0, 2), CellString(5, 10))

d = (1, 0, 'sergey')
t[0] = d[0]
t[1] = d[1]
t[2] = d[2]
for i, x in enumerate(t):
    assert x == d[i], "объект класса TupleData хранит неверную информацию"

assert len(t) == 3, "неверное число элементов в объекте класса TupleData"

cell = CellFloat(-5, 5)
try:
    cell.value = -6.0
except CellFloatException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellFloatException"

cell = CellInteger(-1, 7)
try:
    cell.value = 8
except CellIntegerException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellIntegerException"

cell = CellString(5, 7)
try:
    cell.value = "hello world"
except CellStringException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellStringException"

assert issubclass(CellIntegerException, CellException) and issubclass(CellFloatException, CellException) and issubclass(
    CellStringException,
    CellException), "классы CellIntegerException, CellFloatException, CellStringException должны наследоваться от класса CellException"
