""""
Дополните приведенный код, используя цикл for и встроенную функцию max(), чтобы он выводил один общий максимальный элемент среди всех элементов вложенных списков list1."""

list1 = [[1,7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
print(max(max(list1, key=lambda item: item[1])))