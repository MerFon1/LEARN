"""

"""


class SparseTable:

    def __init__(self):
        self.data = {}
        self.rows = 0
        self.cols = 0

    def __check_index(self, row, col):
        return (row, col) not in self.data.keys()

    def __update_index(self):
        self.rows = max([key[0] for key in self.data]) + 1
        self.cols = max([key[1] for key in self.data]) + 1

    def add_data(self, row, col, data):
        self.data[(row, col)] = data
        self.__update_index()

    def remove_data(self, row, col):
        if self.__check_index(row, col):
            raise IndexError('ячейка с указанными индексами не существует')

        self.data.pop((row, col))
        self.__update_index()

    def __getitem__(self, item):
        if self.__check_index(*item):
            raise ValueError('данные по указанным индексам отсутствуют')

        return self.data[item].value

    def __setitem__(self, key, value):
        if self.__check_index(*key):
            self.add_data(*key, Cell(value))
        else:
            self.data[key].value = value


class Cell:

    def __init__(self, value):
        self.value = value


st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100

assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"


st.remove_data(1, 1)

try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"