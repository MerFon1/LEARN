"""

"""

# здесь объявите класс TriangleChecker


a, b, c = map(int, input().split()) # эту строчку не менять

class TriangleChecker:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if type(self.a) not in (int, float) or type(self.b) not in (int, float) or type(self.c) not in (int, float) or self.a<=0 or self.b<=0 or self.c<=0:
            return 1
        elif self.a + self.b <= self.c or self.b + self.c <= self.a or self.a + self.c <= self.b:
            return 2
        elif self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b:
            return 3
        else:
            return 4

tr = TriangleChecker(a,b,c)
print(tr.is_triangle())

