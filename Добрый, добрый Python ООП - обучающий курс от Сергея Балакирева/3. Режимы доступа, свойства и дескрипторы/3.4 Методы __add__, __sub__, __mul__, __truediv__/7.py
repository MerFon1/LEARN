"""

"""


class MaxPooling:

    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = list(step)
        self.size = list(size)

    @staticmethod
    def out_test(list: list):
        while [] in list:
            list.remove([])
        return list

    def __call__(self, matx: list):
        rows = len(matx)
        cols = len(matx[0]) if rows > 0 else 0

        if rows == 0:
            return [[]]

        if not all(map(lambda x: len(x) == cols, matx)) or not all(
                map(lambda row: all(map(lambda x: type(x) in (int, float), row)), matx)):
            raise ValueError("Неверный формат для первого параметра matrix.")

        counter = 0
        result = [[] for i in range(0, len(matx), self.step[0])]
        for i in range(0, len(matx), self.step[0]):
            p = []
            for j in range(0, len(matx[i]), self.step[1]):
                p = []
                if i <= len(matx) - self.step[0] and j <= len(matx[i]) - self.step[1]:
                    for c1 in range(0, self.size[0]):
                        for c2 in range(0, self.size[1]):
                            p.append(matx[i + c1][j + c2])
                    result[counter].append(max(p))
                else:
                    break
            counter += 1

        return self.out_test(result)


mp = MaxPooling(step=(2, 2), size=(2, 2))
print(mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]))  # [[6, 8], [9, 7]]
print(mp([[5, 0, 88, 2, 7, 65],
          [1, 33, 7, 45, 0, 1],
          [54, 8, 2, 38, 22, 7],
          [73, 23, 6, 1, 15, 0],
          [4, 12, 9, 1, 76, 6],
          [0, 15, 10, 8, 11, 78]]))  # [[33, 88, 65], [73, 38, 22], [15, 10, 78]]
print(mp([[1, 5, 2], [7, 0, 1], [4, 10, 3]]))  # [[7]]
