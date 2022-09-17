"""Упаковка дубликатов 🌶️
На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает последовательности одинаковых символов заданной строки в подсписки.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела.

Формат выходных данных
Программа должна вывести указанный вложенный список.

Тестовые данные 🟢
Sample Input 1:

a b c d
Sample Output 1:

[['a'], ['b'], ['c'], ['d']]
Sample Input 2:

w w w o r l d g g g g r e a t t e c c h e m g g p w w
Sample Output 2:

[['w', 'w', 'w'], ['o'], ['r'], ['l'], ['d'], ['g', 'g', 'g', 'g'], ['r'], ['e'], ['a'], ['t', 't'], ['e'], ['c', 'c'], ['h'], ['e'], ['m'], ['g', 'g'], ['p'], ['w', 'w']]
Sample Input 3:

g i v e t h h i i s m a a a n a g u u n
Sample Output 3:

[['g'], ['i'], ['v'], ['e'], ['t'], ['h', 'h'], ['i', 'i'], ['s'], ['m'], ['a', 'a', 'a'], ['n'], ['a'], ['g'], ['u', 'u'], ['n']]"""

s = input().split()
result = []
c = 0
pr = [s[c]]

for i in s[1:len(s)]:
    if i in pr:
        c += 1
        pr.append(i)
    elif i not in pr:
        c += 1
        result.append(pr)
        pr = [s[c]]

result.append(pr)
print(result)




