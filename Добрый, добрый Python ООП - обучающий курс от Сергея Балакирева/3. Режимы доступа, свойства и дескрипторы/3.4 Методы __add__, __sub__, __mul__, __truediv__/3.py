"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/PY-E4OSh1gM

Подвиг 6. Ранее, в одном из подвигов мы с вами создавали односвязный список с объектами класса StackObj (когда один объект ссылается на следующий и так далее):



Давайте снова создадим такую структуру данных. Для этого объявим два класса:

Stack - для управления односвязным списком в целом;
StackObj - для представления отдельных объектов в односвязным списком.

Объекты класса StackObj должны создаваться командой:

obj = StackObj(data)
где data - строка с некоторыми данными.

Каждый объект класса StackObj должен иметь локальные приватные атрибуты:

__data - ссылка на строку с переданными данными;
__next - ссылка на следующий объект односвязного списка (если следующего нет, то __next = None).

Объекты класса Stack создаются командой:

st = Stack()
и каждый из них должен содержать локальный атрибут:

top - ссылка на первый объект односвязного списка (если объектов нет, то top = None).

Также в классе Stack следует объявить следующие методы:

push_back(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
pop_back(self) - удаление последнего объекта из односвязного списка.

Дополнительно нужно реализовать следующий функционал (в этих операциях копии односвязного списка создавать не нужно):

# добавление нового объекта класса StackObj в конец односвязного списка st
st = st + obj
st += obj

# добавление нескольких объектов в конец односвязного списка
st = st * ['data_1', 'data_2', ..., 'data_N']
st *= ['data_1', 'data_2', ..., 'data_N']
В последних двух строчках должны автоматически создаваться N объектов класса StackObj с данными, взятыми из списка (каждый элемент списка для очередного добавляемого объекта).

P.S. В программе достаточно только объявить классы. На экран ничего выводить не нужно.
"""


class StackObj:

    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


class Stack:

    def __init__(self):
        self.top = None
        self.list = []

    def push_back(self, obj):
        if len(self.list) == 0:
            self.top = obj
            self.list.append(obj)
        else:
            self.list[-1].next = obj
            self.list.append(obj)

    def pop_back(self):
        if len(self.list) == 1:
            self.top = None
            self.list.pop()
        else:
            self.list[-1].next = None
            self.list.pop()

    def __add__(self, other):
        if type(other)==StackObj:
            self.push_back(other)
        else:
            self.push_back(StackObj(other))
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        for i in range(len(other)):
            if type(other) == StackObj:
                self.push_back(other[i])
            else:
                self.push_back(StackObj(other[i]))
        return self

    def __imul__(self, other):
        return self.__mul__(other)

assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"
st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[
        i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"