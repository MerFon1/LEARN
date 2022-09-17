"""

"""


class Tuple(tuple):

    def __add__(self, iter_obj):
        new = list(self)
        for i in iter_obj:
            new.extend(i)
        return Tuple(new)


t = Tuple([1, 2, 3])
t = t + "Python"
print(t)  # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"
print(t)
