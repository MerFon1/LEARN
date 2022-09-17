"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/jk9AOnvm65k

Подвиг 6. Ранее вы уже создавали стек-подобную структуру, когда один объект ссылается на следующий и так по цепочке до последнего:



Для этого в программе объявлялись два класса:

StackObj - для описания объектов стека;
Stack - для управления стек-подобной структурой.

И, далее, объекты класса StackObj следовало создавать командой:

obj = StackObj(data)
где data - это строка с некоторым содержимым объекта (данными). При этом каждый объект класса StackObj должен иметь следующие локальные атрибуты:

data - ссылка на строку с данными, указанными при создании объекта;
next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).

Класс Stack предполагается использовать следующим образом:

st = Stack() # создание объекта стек-подобной структуры
В каждом объекте класса Stack должен быть локальный публичный атрибут:

top - ссылка на первый объект стека (если стек пуст, то top = None).

А в самом классе Stack следующие методы:

push(self, obj) - добавление объекта класса StackObj в конец стека;
pop(self) - извлечение последнего объекта с его удалением из стека;

Дополнительно в классе Stack нужно объявить магические методы для обращения к объекту стека по его индексу, например:

obj_top = st[0] # получение первого объекта
obj = st[4] # получение 5-го объекта стека
st[2] = StackObj("obj3") # замена прежнего (3-го) объекта стека на новый
Если индекс не целое число или число меньше нуля или больше числа объектов в стеке, то должно генерироваться исключение командой:

raise IndexError('неверный индекс')
Пример использования классов Stack и StackObj (эти строчки в программе не писать):

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data) # obj3
print(st[1].data) # new obj2
res = st[3] # исключение IndexError
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

    def push(self, obj):
        if len(self.list) == 0:
            self.top = obj
            self.list.append(obj)
        else:
            self.list[-1].next = obj
            self.list.append(obj)

    def pop(self):
        if len(self.list) == 1:
            self.top = None
            l = self.list.pop()
            return l
        else:
            self.list[-2].next = None
            l = self.list.pop()
            return l

    def __getitem__(self, item):
        return self.list[item]

    def __setitem__(self, key, obj):
        if type(key) != int or key < 0 or key > len(self.list):
            raise IndexError('неверный индекс')

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
                self.list[key].next = self.list[key+1]
            except IndexError:
                pass


st = Stack()
st.push(StackObj("obj11"))
st.push(StackObj("obj12"))
st.push(StackObj("obj13"))
st[1] = StackObj("obj2-new")
assert st[0].data == "obj11" and st[
    1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

try:
    obj = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

obj = st.pop()
assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"

n = 0
h = st.top
while h:
    assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
    n += 1
    h = h.next

assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"
