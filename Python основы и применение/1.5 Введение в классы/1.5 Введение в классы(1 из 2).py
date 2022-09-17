#Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

#Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.

#Класс должен иметь следующий вид

#class MoneyBox:
#    def __init__(self, capacity):
    # конструктор с аргументом – вместимость копилки

#    def can_add(self, v):
        # True, если можно добавить v монет, False иначе

#    def add(self, v):
        # положить v монет в копилку
#При создании копилки, число монет в ней равно 0.
#Примечание:
#Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True﻿.

class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stk = 0
    def can_add(self, v):
        self.can_add_v = v
        if ((self.capacity - self.stk) - self.can_add_v) >= 0:
            return True
        else:
            return False
    def add(self, v):
        self.v = v
        self.stk = self.stk + self.v

x = MoneyBox(10)
print(x.capacity)
print(x.can_add(3))
x.add(3)
print(x.can_add(1))


