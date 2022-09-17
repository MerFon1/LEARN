"""
Неповторимые цифры
На вход программе подается строка, состоящая из цифр. Необходимо определить, верно ли, что в ее записи ни одна из цифр не повторяется?

Формат входных данных
На вход программе подается строка, состоящая из цифр

Формат выходных данных
Программа должна вывести YES если ни одна из цифр в строке не повторяется и NO в противном случае.

Тестовые данные 🟢
Sample Input 1:

1093482
Sample Output 1:

YES
Sample Input 2:

10000000
Sample Output 2:

NO
Sample Input 3:

3445321290
Sample Output 3:

NO
"""

n = input()
f = lambda n: print('YES') if len(set(n)) == len(n) else print('NO')
f(n)
