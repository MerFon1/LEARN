"""
Заполнение спиралью 😈😈
На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n \
times mn×m заполнив её "спиралью" в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии образцом.

Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 33 символа на каждый элемент.
Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇

Тестовые данные 🟢
Sample Input 1:

4 5
Sample Output 1:

1  2  3  4  5
14 15 16 17 6
13 20 19 18 7
12 11 10 9  8
Sample Input 2:

1 6
Sample Output 2:

1  2  3  4  5  6
Sample Input 3:

3 3
Sample Output 3:

1  2  3
8  9  4
7  6  5
"""

n, m = 4,5  #map(int, input().split())
data = [[0 for j in range(m)] for i in range(n)]

trend = 'r'  # r - right, l - left, u - up, d - down
counter = 0
i = 0
j = 0


while counter != n * m:
    counter += 1

    if trend == 'r':

        if data[i][j] != 0:
            trend = 'd'
            j -= 1
            i += 1
            counter -= 1
        elif j == m-1:
            trend = 'd'
            data[i][j] = counter
            i += 1
        elif j >= 0 and j < m and data[i][j] == 0:
            data[i][j] = counter
            j += 1
        continue

    if trend == 'l':

        if data[i][j] != 0:
            trend = 'u'
            j += 1
            i -= 1
            counter -= 1
        elif j == 0:
            trend = 'u'
            data[i][j] = counter
            i -= 1
        elif j >= 0 and j < m and data[i][j] == 0:
            data[i][j] = counter
            j -= 1
        continue

    if trend == 'u':

        if data[i][j] != 0:
            trend = 'r'
            i += 1
            j += 1
            counter -= 1
        elif i == 0:
            trend = 'r'
            data[i][j] = counter
            j += 1
        elif i >= 0 and i < n and data[i][j] == 0:
            data[i][j] = counter
            i -= 1
        continue

    if trend == 'd':

        if data[i][j] != 0:
            trend = 'l'
            i -= 1
            j -= 1
            counter -= 1
        elif i == n - 1:
            trend = 'l'
            data[i][j] = counter
            j -= 1
        elif i >= 0 and i < n and data[i][j] == 0:
            data[i][j] = counter
            i += 1
        continue

[print(*i,sep='\t') for i in data]


