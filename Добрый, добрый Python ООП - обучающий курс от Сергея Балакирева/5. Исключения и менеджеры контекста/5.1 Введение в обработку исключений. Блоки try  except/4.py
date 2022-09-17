class Triangle:

    def __init__(self, a, b, c):
        if self.__check_side(a, b, c):
            raise TypeError('стороны треугольника должны быть положительными числами')
        if self.__check_is_true_thiangle(a, b, c):
            raise ValueError('из указанных длин сторон нельзя составить треугольник')

        self._a = a
        self._b = b
        self._c = c

    def __check_side(self, *args):
        for i in args:
            if type(i) not in (int, float) or i <= 0:
                return True

        return False

    def __check_is_true_thiangle(self, a, b, c):
        return a + b <= c or b + c <= a or a + c <= b


lst_tr = []
input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
for i in input_data:
    try:
        lst_tr.append(Triangle(*i))
    except Exception:
        pass
