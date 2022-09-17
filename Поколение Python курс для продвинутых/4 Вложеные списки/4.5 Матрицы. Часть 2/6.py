"""
Зеркальное отображение
Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно горизонтальной оси симметрии.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести матрицу в которой зеркально отображены элементы относительно горизонтальной оси симметрии.
"""
n =int(input())
ls = [[int(i) for i in input().split()] for i in range(n)]
ls.reverse()
for i in ls:
    print(*i)