"""
Разбиение на чанки 🌶️
На вход программе подаются две строки, на одной символы, на другой число nn. Из первой строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает список из чанков указанной длины.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число nn на отдельной строке.

Формат выходных данных
Программа должна вывести указанный вложенный список.

Примечание. Не забудьте вызвать функцию chunked(), чтобы вывести результат 😀.

Тестовые данные 🟢
Sample Input 1:

a b c d e f
2
Sample Output 1:

[['a', 'b'], ['c', 'd'], ['e', 'f']]
Sample Input 2:

a b c d e f
3
Sample Output 2:

[['a', 'b', 'c'], ['d', 'e', 'f']]
Sample Input 3:

a b c d e f
6
Sample Output 3:

[['a', 'b', 'c', 'd', 'e', 'f']]
Sample Input 4:

a b c d e f r g b
2
Sample Output 4:

[['a', 'b'], ['c', 'd'], ['e', 'f'], ['r', 'g'], ['b']]
Sample Input 5:

a b
3
Sample Output 5:

[['a', 'b']]"""

def chunked(s, n):
    p,r = [],[]
    c = 0
    if len(s) < n:
        r.append(s)
    else:
        for i in s:
            if c==n:
                r.append(p)
                c = 0
                p = []
                p.append(i)
                c += 1
            else:
                p.append(i)
                c += 1
    if len(p)>0:
        r.append(p)
    return r
print(chunked(input().split(),int(input())))