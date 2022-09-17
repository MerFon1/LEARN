"""
Заполнение 5 🌶️
На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n \times mn×m заполнив её в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 33 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇

Тестовые данные 🟢
Sample Input 1:

5 5
Sample Output 1:

1 2 3 4 5
2 3 4 5 1
3 4 5 1 2
4 5 1 2 3
5 1 2 3 4
Sample Input 2:

6 6
Sample Output 2:

1 2 3 4 5 6
2 3 4 5 6 1
3 4 5 6 1 2
4 5 6 1 2 3
5 6 1 2 3 4
6 1 2 3 4 5
Sample Input 3:

3 7
Sample Output 3:

1 2 3 4 5 6 7
2 3 4 5 6 7 1
3 4 5 6 7 1 2
Sample Input 4:

7 3
Sample Output 4:

1 2 3
2 3 1
3 1 2
1 2 3
2 3 1
3 1 2
1 2 3
Sample Input 5:

4 2
Sample Output 5:

1 2
2 1
1 2
2 1
"""

n,m = [int(i) for i in input().split()]

res = [[i for i in range(1,m+1)]]
[print(*i) for i in res]

for i in range(n-1):
    npl = res[i]
    npl.extend([npl.pop(0)])
    res.append(npl)
    print(*npl)


