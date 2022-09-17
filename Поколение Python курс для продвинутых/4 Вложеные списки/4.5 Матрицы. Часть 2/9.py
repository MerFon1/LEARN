"""
Магический квадрат 🌶️
Магическим квадратом порядка nn называется квадратная таблица размера n \times nn×n, составленная из всех чисел 1, 2, 3, \ldots, n^21,2,3,…,n
2
  так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы: nn строк, по nn чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.

Тестовые данные 🟢
Sample Input 1:

3
8 1 6
3 5 7
4 9 2
Sample Output 1:

YES
Sample Input 2:

3
8 2 6
3 5 7
4 9 1
Sample Output 2:

NO
Sample Input 3:

3
4 9 2
3 5 7
8 1 6
Sample Output 3:

YES
"""
n =int(input())
ls = [[int(i) for i in input().split()] for i in range(n)]

def maxim(l):
    result = []
    for i in l:
        result.extend(i)
    return max(result)

def magic_square(list, n):

    for i in list:
        if len(set(i)) == 1:
            return 'NO'
    if maxim(list)!=n**2:
        return 'NO'

    lines = []
    columns = []
    diagonals = []

    for i in list:
        lines.extend([sum(i)])
    if len(set(lines)) != 1:
        return 'NO'

    for i in range(n):
        pr = []
        for j in range(n):
            pr.extend([list[j][i]])
        columns.extend([sum(pr)])
    if len(set(columns)) != 1:
        return 'NO'

    gd = []
    vd = []
    for i in range(n):
        for j in range(n):
            if i == j and j == n - i - 1:
                gd.extend([list[i][j]])
                vd.extend([list[i][j]])
            elif i == j:
                gd.extend([list[i][j]])
            elif j == n - i - 1:
                vd.extend([list[i][j]])
    diagonals.extend([sum(gd)])
    diagonals.extend([sum(vd)])
    if len(set(diagonals)) != 1:
        return 'NO'

    return 'YES'

print(magic_square(ls,n))









