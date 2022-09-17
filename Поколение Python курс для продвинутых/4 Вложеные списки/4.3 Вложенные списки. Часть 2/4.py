"""
Треугольник Паскаля 2
На вход программе подается натуральное число nn. Напишите программу, которая выводит первые nn строк треугольника Паскаля.

Формат входных данных
На вход программе подается число n \, (n \ge 1)n (n≥1).

Формат выходных данных
Программа должна вывести первые nn строк треугольника Паскаля, каждую на отдельной строке в соответствии с образцом.

Тестовые данные 🟢
Sample Input 1:

4
Sample Output 1:

1
1 1
1 2 1
1 3 3 1
Sample Input 2:

5
Sample Output 2:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
Sample Input 3:

2
Sample Output 3:

1
1 1
"""

def pascal2(n):
    l = [[1]]
    if n == 1:
        print(*l[0])
    else:
        while n!=len(l):
            cl1 = 0
            cl2 = 1
            pr = [1]
            while len(pr)!=len(l[-1]):
                prn = l[-1][cl1]+l[-1][cl2]
                pr.append(prn)
                cl1 +=1
                cl2 +=1
            pr.append(1)
            l.append(pr)
        for i in l:
            print(*i)
pascal2(int(input()))