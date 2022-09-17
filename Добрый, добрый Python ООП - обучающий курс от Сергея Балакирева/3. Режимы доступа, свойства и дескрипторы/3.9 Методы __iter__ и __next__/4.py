"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/WrZ1TMwuvis

Подвиг 8. Вы несколько раз уже делали стек-подобную структуру, когда объекты последовательно связаны между собой:



Доведем ее функционал до конца. Для этого, по прежнему, нужно объявить классы:

Stack - для представления стека в целом;
StackObj - для представления отдельных объектов стека.

В классе Stack должны быть методы:

push_back(obj) - для добавления нового объекта obj в конец стека;
push_front(obj) - для добавления нового объекта obj в начало стека.

В каждом объекте класса Stack должен быть публичный атрибут:

top - ссылка на первый объект стека (при пустом стеке top = None).

Объекты класса StackObj создаются командой:

obj = StackObj(data)
где data - данные, хранящиеся в объекте стека (строка).

Также в каждом объекте класса StackObj должны быть публичные атрибуты:

data - ссылка на данные объекта;
next - ссылка на следующий объект стека (если его нет, то next = None).

Наконец, с объектами класса Stack должны выполняться следующие команды:

st = Stack()

st[indx] = value # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
data = st[indx]  # получение данных из объекта стека по индексу
n = len(st) # получение общего числа объектов стека

for obj in st: # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль
При работе с индексами (indx), нужно проверять их корректность. Должно быть целое число от 0 до N-1, где N - число объектов в стеке. Иначе, генерировать исключение командой:

raise IndexError('неверный индекс')
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""


class StackObj:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.list = []
        self.top = None

    def push_back(self, obj):
        if len(self.list) == 0:
            self.top = obj
            self.list.append(obj)
        else:
            self.list[-1].next = obj
            self.list.append(obj)

    def push_front(self, obj):
        if len(self.list) == 0:
            self.top = obj
            self.list.insert(0, obj)
        else:
            self.list.insert(0, obj)
            obj.next = self.list[1]

    def __iter__(self):
        self.index = -1
        self.iter_list = self.list
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.iter_list):
            return self.iter_list[self.index]
        else:
            raise StopIteration

    def __getitem__(self, item):
        if type(item) != int or item < 0 or item > len(self.list):
            raise IndexError('неверный индекс')

        return self.list[item].data

    def __setitem__(self, key, obj):
        if type(key) != int or key < 0 or key > len(self.list):
            raise IndexError('неверный индекс')
        if type(obj) != StackObj:
            obj = StackObj(obj)
        if key == 0:
            self.top = obj
            self.list[key] = obj
            try:
                self.list[key].next = self.list[1]
            except IndexError:
                pass
        else:
            self.list[key - 1].next = obj
            self.list[key] = obj
            try:
                self.list[key].next = self.list[key + 1]
            except IndexError:
                pass





st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))
assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

st[0] = "0"
assert st[
           0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

for obj in st:
    assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

try:
    a = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

