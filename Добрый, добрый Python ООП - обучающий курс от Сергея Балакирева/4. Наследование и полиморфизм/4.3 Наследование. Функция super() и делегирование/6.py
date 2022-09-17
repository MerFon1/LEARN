"""
Подвиг 8 (на повторение). Объявите класс SoftList, который наследуется от стандартного класса list. В классе SoftList следует объявить необходимые магические методы так, чтобы при обращении к несуществующему элементу (по индексу) возвращалось значение False (а не исключение Out of Range). Например:

sl = SoftList("python")
sl[0] # 'p'
sl[-1] # 'n'
sl[6] # False
sl[-7] # False
P.S. В программе нужно объявить только класс. На экран выводить ничего не нужно.
"""


class SoftList:

    def __init__(self, data):
        self.data = [i for i in data]

    def __getitem__(self, item):
        if item >= len(self.data) or  item <= len(self.data)-len(self.data)*2:
            return False
        return self.data[item]


sl = SoftList("python")
print(sl[0])  # 'p'
print(sl[-1])  # 'n'
print(sl[6])  # False
print(sl[-7])  # False
