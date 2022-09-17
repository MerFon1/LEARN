"""

"""


class Dimensions:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if type(value) not in (int, float) or value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        return object.__setattr__(self, key, value)

    def __hash__(self):
        return hash((self.a, self.b, self.c))


lst_dims = [Dimensions(*list(map(float, i.split()))) for i in input().split('; ')]
lst_dims = sorted(lst_dims, key=lambda x: hash(x))
