"""
Шахматная доска
На вход программе подаются два натуральных числа nn и mm. Напишите программу для создания матрицы размером n \times mn×m, заполнив её символами . и * в шахматном порядке. В левом верхнем углу должна стоять точка. Выведите полученную матрицу на экран, разделяя элементы пробелами.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу, описанную в условии задачи.

Тестовые данные 🟢
Sample Input 1:

3 4
Sample Output 1:

. * . *
* . * .
. * . *
Sample Input 2:

2 2
Sample Output 2:

. *
* .
Sample Input 3:

1 8
Sample Output 3:

. * . * . * . *
"""
v,d = [int(i) for i in input().split()]
dsk = lambda i,j: print('.', end=' ') if  (i + j) % 2 == 0 else print('*', end=' ')
for i in range(v):
    for j in range(d):
        dsk(i,j)
    print('')
