"""
Симметричная матрица
Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести YES, если матрица симметрична относительно главной диагонали, и слово NO в противном случае.

Тестовые данные 🟢
Sample Input 1:

3
0 1 2
1 2 3
2 3 4
Sample Output 1:

YES
Sample Input 2:

3
0 1 2
1 2 7
2 3 4
Sample Output 2:

NO
Sample Input 3:

2
1 2
3 4
Sample Output 3:

NO
"""
n = int(input())
l = [[int(i) for i in input().split()] for i in range(n)]
r = []
chek = lambda i,j: r.append('YES') if l[i][j] == l[j][i] else r.append('NO')

for i in range(n):
    for j in range(n):
        chek(i,j)

result = lambda list: print('YES') if len(set(list)) == 1 else print('NO')
result(r)
