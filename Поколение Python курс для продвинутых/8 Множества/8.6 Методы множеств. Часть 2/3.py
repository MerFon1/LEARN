"""
Числа первой строки
На вход программе подаются две строки текста, содержащие числа. Напишите программу, которая выводит все числа в порядке возрастания, которые есть в первой строке, но отсутствуют во второй.

Формат входных данных
На вход программе подаются две строки текста, содержащие числа, отделенные символом пробела.

Формат выходных данных
Программа должна вывести множество чисел, встречающихся только в первой строке.

Тестовые данные 🟢
Sample Input 1:

1 2 3 4
5 6 7 8
Sample Output 1:

1 2 3 4
Sample Input 2:

1 2 3 4 5
1 2 3 4 6
Sample Output 2:

5
"""

a = set([int(i) for i in input().split()])
b = set([int(i) for i in input().split()])
res = sorted(set(a - b))
print(*res)