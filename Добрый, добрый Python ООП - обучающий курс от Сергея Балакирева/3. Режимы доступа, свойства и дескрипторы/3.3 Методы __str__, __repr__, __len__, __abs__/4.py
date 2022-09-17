"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/6-xKuQp9b7Y

Подвиг 5. Объявите класс LinkedList (связный список) для работы со следующей структурой данных:



Здесь создается список из связанных между собой объектов класса ObjList. Объекты этого класса создаются командой:

obj = ObjList(data)
где data - строка с некоторой информацией. Также в каждом объекте obj класса ObjList должны создаваться следующие локальные атрибуты:

__data - ссылка на строку с данными;
__prev - ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None);
__next - ссылка на следующий объект связного списка (если объекта нет, то __next = None).

В свою очередь, объекты класса LinkedList должны создаваться командой:

linked_lst = LinkedList()
и содержать локальные атрибуты:

head - ссылка на первый объект связного списка (если список пуст, то head = None);
tail - ссылка на последний объект связного списка (если список пуст, то tail = None).

А сам класс содержать следующие методы:

add_obj(obj) - добавление нового объекта obj класса ObjList в конец связного списка;
remove_obj(indx) - удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу); индекс отсчитывается с нуля.

Также с объектами класса LinkedList должны поддерживаться следующие операции:

len(linked_lst) - возвращает число объектов в связном списке;
linked_lst(indx) - возвращает строку __data, хранящуюся в объекте класса ObjList, расположенного под индексом indx (в связном списке).

Пример использования классов (эти строчки в программе писать не нужно):

linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1) # s = Balakirev
P.S. На экран в программе ничего выводить не нужно.
"""


class ObjList:

    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    @property
    def data(self):
        return self.__data


class LinkedList:

    def __init__(self):
        self.list = []
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if len(self.list) == 0:
            self.head = obj
            self.list.append(obj)
        else:
            self.list[-1].next = obj
            obj.prev = self.list[-1]
            self.list.append(obj)
        self.tail = obj

    def remove_obj(self, indx):
        if len(self.list) == 1:
            self.tail = None
            self.head = None
            self.list.pop(indx)
        elif len(self.list) == 2:
            self.list.pop(indx)
            self.head = self.list[0]
            self.tail = self.list[0]
            self.list[0].next = None
            self.list[0].prev = None
        elif indx == 0:
            self.list.pop(indx)
            self.head = self.list[0]
            self.list[indx].prev = None
        elif indx == len(self.list) - 1:
            self.list.pop(indx)
            self.tail = self.list[-1]
            self.list[-1].next = None
        else:
            self.list[indx - 1].next = self.list[indx + 1]
            self.list[indx + 1].prev = self.list[indx - 1]
            self.list.pop(indx)

    def __len__(self):
        return len(self.list)

    def __call__(self, indx, *args, **kwargs):
        return self.list[indx].data


ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(2)
assert len(
    ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("Python"))
assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"

n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"
