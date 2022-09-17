"""
Дополнительная
Выведите таблицу размером n \times nn×n, заполненную числами от 11 до n^2n
2
  по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5n=5):
Sample Input:

5
Sample Output:

1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""

n = int(input())
data = [[0 for j in range(n)] for i in range(n)]

trend = 'r'  # r - right, l - left, u - up, d - down
counter = 0
i = 0
j = 0


while counter != n * n:
    counter += 1

    if trend == 'r':

        if data[i][j] != 0:
            trend = 'd'
            j -= 1
            i += 1
            counter -= 1
        elif j == n-1:
            trend = 'd'
            data[i][j] = counter
            i += 1
        elif j >= 0 and j < n and data[i][j] == 0:
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
        elif j >= 0 and j < n and data[i][j] == 0:
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

[print(*i,sep=' ') for i in data]