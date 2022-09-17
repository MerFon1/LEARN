"""
class PathLines:

    def __init__(self, *args):
        self.data = list(args)

    def get_path(self):
        return self.data

    def get_length(cls):
        import math
        x0 = y0 = 0
        r = 0
        for point in cls.data:
            cls.point = point
            r += math.sqrt((cls.point.x - x0) ** 2 + (cls.point.y - y0) ** 2)
            x0 = cls.point.x
            y0 = cls.point.y
        return r

    def add_line(self, line):
        self.data.append(line)


class LineTo:

    def __init__(self, x, y):
        self.x = x
        self.y = y
"""


class PathLines:

    def __init__(self, *args):
        self.data = list(args)

    def get_path(self):
        return self.data

    def get_length(cls):
        import math
        x0 = y0 = 0
        r = 0
        for point in cls.data:
            cls.point = point
            r += math.sqrt((cls.point.x - x0) ** 2 + (cls.point.y - y0) ** 2)
            x0 = cls.point.x
            y0 = cls.point.y
        return r

    def add_line(self, line):
        self.data.append(line)


class LineTo:

    def __init__(self, x, y):
        self.x = x
        self.y = y
